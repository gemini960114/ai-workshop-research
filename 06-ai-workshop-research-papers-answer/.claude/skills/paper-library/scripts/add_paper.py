#!/usr/bin/env python3
"""把論文加入本地文獻庫：下載 PDF、重新命名、追加 BibTeX 與下載紀錄。

用法（在專案根目錄執行）：
  python add_paper.py arxiv 2610.21224 2401.01234 --query "microbiome longitudinal"
  python add_paper.py doi 10.1126/scitranslmed.aap9489 --query "auto-FMT allo-HSCT"
  python add_paper.py doi 10.xxxx/yyyy --pdf papers/已手動下載的檔案.pdf

只用 Python 標準函式庫，Windows / macOS / Linux 皆可執行。
"""
import argparse
import datetime
import json
import re
import shutil
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

UA = "paper-library-skill/1.0 (local research workshop)"
ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
STOPWORDS = {"a", "an", "the", "of", "on", "in", "for", "and", "to", "with", "from",
             "by", "at", "as", "is", "are", "via", "toward", "towards", "using"}

# Windows 的 cp950 主控台印中文會出錯，統一改成 UTF-8
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass


def http_get(url, accept=None):
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def ascii_slug(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "", text)


def last_name(author):
    """'Shuangjie Zhang' -> 'Zhang'；'Zhang, Shuangjie' -> 'Zhang'。"""
    author = author.strip()
    if "," in author:
        return author.split(",")[0].strip()
    return author.split()[-1] if author.split() else "Unknown"


def title_words(title):
    return [w for w in re.findall(r"[A-Za-z0-9]+", title)]


def make_citekey(meta, existing_keys):
    first_word = next((w for w in title_words(meta["title"]) if w.lower() not in STOPWORDS), "paper")
    base = (ascii_slug(last_name(meta["authors"][0])) + meta["year"] + first_word).lower()
    key, n = base, 0
    while key in existing_keys:
        n += 1
        key = base + chr(ord("a") + n)  # 重複時加 b、c…
    return key


def make_filename(meta):
    words = [w for w in title_words(meta["title"]) if w.lower() not in STOPWORDS][:5]
    return "{}_{}_{}.pdf".format(ascii_slug(last_name(meta["authors"][0])) or "Unknown",
                                 meta["year"], "-".join(words) or "paper")


def bib_escape(text):
    return re.sub(r"\s+", " ", text).replace("{", "\\{").replace("}", "\\}").strip()


# ---------- 取得書目資料 ----------

def fetch_arxiv(ids):
    clean = [re.sub(r"^(arxiv:|https?://arxiv\.org/(abs|pdf)/)", "", i, flags=re.I).replace(".pdf", "") for i in ids]
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"id_list": ",".join(clean), "max_results": len(clean)})
    root = ET.fromstring(http_get(url))
    out = []
    for e in root.findall("a:entry", ATOM):
        abs_id = e.find("a:id", ATOM).text.strip().split("/abs/")[-1]
        if e.find("a:title", ATOM) is None or abs_id.startswith("api/"):
            continue  # 查無此 ID 時 arXiv 會回傳錯誤 entry
        doi = e.find("arxiv:doi", ATOM)
        journal = e.find("arxiv:journal_ref", ATOM)
        out.append({
            "source": "arXiv",
            "id": re.sub(r"v\d+$", "", abs_id),
            "title": " ".join(e.find("a:title", ATOM).text.split()),
            "authors": [a.find("a:name", ATOM).text.strip() for a in e.findall("a:author", ATOM)],
            "year": e.find("a:published", ATOM).text[:4],
            "primary": e.find("arxiv:primary_category", ATOM).get("term"),
            "doi": doi.text.strip() if doi is not None else "",
            "journal_ref": journal.text.strip() if journal is not None else "",
            "url": "https://arxiv.org/abs/" + re.sub(r"v\d+$", "", abs_id),
            "pdf_url": "https://arxiv.org/pdf/" + abs_id,
        })
    found = {m["id"] for m in out}
    for i in clean:
        if re.sub(r"v\d+$", "", i) not in found:
            print("⚠ arXiv 查無此 ID：" + i)
    return out


def fetch_doi(doi):
    doi = re.sub(r"^(doi:|https?://(dx\.)?doi\.org/)", "", doi.strip(), flags=re.I)
    data = json.loads(http_get("https://api.crossref.org/works/" + urllib.parse.quote(doi)))["message"]
    # 期刊卷期的出版年優先（例如線上先行 2012、正式卷期 2013 時取 2013）
    parts = ((data.get("journal-issue") or {}).get("published-print") or data.get("published-print")
             or data.get("published-online") or data.get("issued") or {}).get("date-parts", [[None]])
    authors = ["{} {}".format(a.get("given", ""), a.get("family", "")).strip()
               for a in data.get("author", []) if a.get("family")]
    return {
        "source": "DOI",
        "id": doi,
        "title": " ".join((data.get("title") or ["Untitled"])[0].split()),
        "authors": authors or ["Unknown"],
        "year": str(parts[0][0] or "nd"),
        "journal": (data.get("container-title") or [""])[0],
        "volume": data.get("volume", ""),
        "issue": data.get("issue", ""),
        "pages": data.get("page", "") or ("" if str(data.get("article-number", "")).startswith("10.") else data.get("article-number", "")),
        "doi": doi,
        "url": "https://doi.org/" + doi,
        "pdf_url": "",
    }


# ---------- 寫入文獻庫 ----------

def to_bibtex(meta, key, pdf_rel, query):
    fields = [("title", "{" + bib_escape(meta["title"]) + "}"),
              ("author", " and ".join(bib_escape(a) for a in meta["authors"])),
              ("year", meta["year"])]
    if meta["source"] == "arXiv":
        entry_type = "misc"
        fields += [("eprint", meta["id"]), ("archivePrefix", "arXiv"), ("primaryClass", meta["primary"])]
        if meta["journal_ref"]:
            fields.append(("note", "Published in " + bib_escape(meta["journal_ref"])))
    else:
        entry_type = "article"
        for bib_k, meta_k in (("journal", "journal"), ("volume", "volume"), ("number", "issue"), ("pages", "pages")):
            if meta.get(meta_k):
                fields.append((bib_k, bib_escape(meta[meta_k])))
    if meta.get("doi"):
        fields.append(("doi", meta["doi"]))
    fields.append(("url", meta["url"]))
    if pdf_rel:
        fields.append(("file", pdf_rel))
    if query:
        fields.append(("keywords", bib_escape(query)))
    body = ",\n".join("  {} = {{{}}}".format(k, v) for k, v in fields)
    return "@{}{{{},\n{}\n}}\n".format(entry_type, key, body)


def main():
    p = argparse.ArgumentParser(description="把論文加入本地文獻庫（papers/ + library/）")
    p.add_argument("source", choices=["arxiv", "doi"], help="arxiv：用 arXiv ID；doi：用 DOI（Crossref）")
    p.add_argument("ids", nargs="+", help="一個或多個 arXiv ID / DOI")
    p.add_argument("--query", default="", help="找到這篇論文時用的搜尋關鍵字，會寫進紀錄")
    p.add_argument("--root", default=".", help="專案根目錄（含 papers/ 與 library/），預設為目前目錄")
    p.add_argument("--pdf", help="（只限單篇 DOI）已手動下載的 PDF 路徑，會改名後搬進 papers/")
    p.add_argument("--no-pdf", action="store_true", help="只登錄書目，不下載 PDF")
    p.add_argument("--dry-run", action="store_true", help="只顯示會做什麼，不寫入任何檔案")
    args = p.parse_args()

    root = Path(args.root).resolve()
    papers, bib_path, log_path = root / "papers", root / "library" / "references.bib", root / "library" / "download-log.md"
    if not bib_path.exists() or not log_path.exists():
        sys.exit("找不到 library/references.bib 或 library/download-log.md，請確認 --root 指向專案根目錄：" + str(root))
    papers.mkdir(exist_ok=True)

    bib_text = bib_path.read_text(encoding="utf-8")
    existing_keys = set(re.findall(r"@\w+\{([^,\s]+),", bib_text))
    existing_ids = {i.lower() for i in re.findall(r"(?:eprint|doi)\s*=\s*\{([^}]+)\}", bib_text)}

    if args.source == "arxiv":
        metas = fetch_arxiv(args.ids)
    else:
        metas = []
        for i, d in enumerate(args.ids):
            if i:
                time.sleep(1)
            try:
                metas.append(fetch_doi(d))
            except Exception as exc:
                print("⚠ Crossref 查不到 DOI {}：{}".format(d, exc))
    if args.pdf and (args.source != "doi" or len(metas) != 1):
        sys.exit("--pdf 只能搭配單篇 DOI 使用")

    today = datetime.date.today().isoformat()
    added = []
    for meta in metas:
        if meta["id"].lower() in existing_ids or (meta.get("doi") and meta["doi"].lower() in existing_ids):
            print("↷ 已在文獻庫中，略過：{}（{}）".format(meta["title"], meta["id"]))
            continue
        key = make_citekey(meta, existing_keys)
        existing_keys.add(key)
        fname = make_filename(meta)
        pdf_rel = ""
        if args.dry_run:
            pdf_rel = "papers/" + fname if (meta["pdf_url"] or args.pdf) and not args.no_pdf else ""
        elif args.pdf:
            shutil.move(args.pdf, papers / fname)
            pdf_rel = "papers/" + fname
        elif meta["pdf_url"] and not args.no_pdf:
            if added:
                time.sleep(3)  # arXiv 要求連續請求間隔 3 秒
            try:
                (papers / fname).write_bytes(http_get(meta["pdf_url"]))
                pdf_rel = "papers/" + fname
            except Exception as exc:
                print("⚠ PDF 下載失敗（仍會登錄書目）：{}".format(exc))

        entry = to_bibtex(meta, key, pdf_rel, args.query)
        row = "| {} | {} | {} | {} | {} | {} | {} |\n".format(
            today, meta["source"], meta["id"], meta["title"].replace("|", "/"),
            args.query or "—", fname if pdf_rel else "（未下載）", key)
        if args.dry_run:
            print("[dry-run] 將新增：\n" + entry + row)
        else:
            with bib_path.open("a", encoding="utf-8") as f:
                f.write("\n" + entry)
            with log_path.open("a", encoding="utf-8") as f:
                f.write(row)
        added.append(key)
        print("✓ {}  {}  {}".format(key, pdf_rel or "（無 PDF）", meta["title"]))

    print("\n完成：新增 {} 筆{}。".format(len(added), "（dry-run，未寫入）" if args.dry_run else ""))


if __name__ == "__main__":
    main()
