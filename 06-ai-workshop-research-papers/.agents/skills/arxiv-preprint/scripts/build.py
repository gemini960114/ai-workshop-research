#!/usr/bin/env python3
"""arXiv preprint 一鍵工具：建立 → 檢查 → 編譯 → 打包。只用 Python 標準函式庫。

用法（在專案根目錄執行）：
  python build.py manuscript --init                         # 第一次：複製範本與版型檔
  python build.py manuscript --bib library/references.bib   # 檢查 + 編譯 + 打包

產出（都在論文資料夾內）：
  main.pdf                 編譯結果（本機有 pdflatex 時）
  arxiv-submission.tar.gz  上傳 arXiv 用：main.tex、main.bbl、.sty、用到的圖
  overleaf.zip             沒有 LaTeX 時上傳到 Overleaf 編譯用
  check-report.md          投稿前檢查結果
"""
import argparse
import re
import shutil
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ASSETS = Path(__file__).resolve().parents[1] / "assets"
STY_FILES = ["arxiv.sty", "fancyhdr.sty"]
LICENSES = ["LICENSE-arxiv-style.txt", "LICENSE-fancyhdr.txt"]
ABSTRACT_LIMIT = 1920  # arXiv metadata 摘要上限（字元）


def init(paper):
    paper.mkdir(parents=True, exist_ok=True)
    (paper / "figures").mkdir(exist_ok=True)
    main = paper / "main.tex"
    if main.exists():
        print("main.tex 已存在，不覆蓋。")
    else:
        shutil.copy(ASSETS / "template.tex", main)
        print("已建立 main.tex（由範本複製）")
    copy_style(paper)


def copy_style(paper):
    for f in STY_FILES + LICENSES:
        shutil.copy(ASSETS / f, paper / f)


def strip_comments(tex):
    return re.sub(r"(?<!\\)%.*", "", tex)


def tex_sources(paper):
    """main.tex 與它用 \\input / \\include 引入的所有 .tex（遞迴），回傳相對路徑清單。"""
    found, queue = [], ["main.tex"]
    while queue:
        rel = queue.pop(0)
        if rel in found or not (paper / rel).exists():
            continue
        found.append(rel)
        body = strip_comments((paper / rel).read_text(encoding="utf-8"))
        for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", body):
            queue.append(name if name.endswith(".tex") else name + ".tex")
    return found


def check(paper, bib_path):
    sources = tex_sources(paper)
    tex = "\n".join(strip_comments((paper / f).read_text(encoding="utf-8")) for f in sources)
    problems, notes = [], []

    for name in re.findall(r"\\(?:input|include)\{([^}]+)\}", tex):
        rel = name if name.endswith(".tex") else name + ".tex"
        if not (paper / rel).exists():
            problems.append("找不到 \\input 的檔案：" + rel)
    notes.append("LaTeX 原始檔 {} 個".format(len(sources)))

    # 1. 引用都在 bib 裡
    cited = set()
    for group in re.findall(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", tex):
        cited.update(k.strip() for k in group.split(",") if k.strip())
    bib_keys = set()
    if bib_path.exists():
        bib_keys = set(re.findall(r"@\w+\{([^,\s]+),", bib_path.read_text(encoding="utf-8")))
    missing = sorted(cited - bib_keys)
    unused = sorted(bib_keys - cited)
    if missing:
        problems.append("引用了但不在 references.bib：" + ", ".join(missing))
    notes.append("引用文獻 {} 篇；bib 中未引用 {} 篇{}".format(
        len(cited), len(unused), "（" + ", ".join(unused) + "）" if unused else ""))

    # 2. 圖檔存在
    figs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", tex)
    used_figs = []
    for f in figs:
        cands = [paper / f, paper / "figures" / f]
        hit = next((c for c in cands if c.exists()), None)
        if hit is None:
            problems.append("找不到圖檔：" + f)
        else:
            used_figs.append(hit)
    notes.append("圖 {} 張".format(len(used_figs)))

    # 3. 摘要長度
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, flags=re.S)
    if m:
        plain = re.sub(r"\\[a-zA-Z]+\*?(\{([^}]*)\})?", r"\2", m.group(1))
        plain = re.sub(r"[{}~$\\]", "", re.sub(r"\s+", " ", plain)).strip()
        n = len(plain)
        (problems if n > ABSTRACT_LIMIT else notes).append(
            "摘要約 {} 字元（arXiv 上限 {}）".format(n, ABSTRACT_LIMIT))

    # 4. 範本佔位文字是否還在
    for placeholder in ["FULL TITLE OF THE PAPER", "SHORT TITLE FOR RUNNING HEAD", "First Author", "email@example.org", "[To be completed", "[To be confirmed"]:
        if placeholder in tex:
            problems.append("範本佔位文字尚未替換：" + placeholder)
    return problems, notes, used_figs, sources


def compile_pdf(paper):
    exe = {k: shutil.which(k) for k in ("pdflatex", "bibtex")}
    if not all(exe.values()):
        return None, "本機沒有 pdflatex/bibtex，略過編譯；請把 overleaf.zip 上傳到 Overleaf 編譯。"
    cmds = [["pdflatex", "-interaction=nonstopmode", "main.tex"], ["bibtex", "main"],
            ["pdflatex", "-interaction=nonstopmode", "main.tex"], ["pdflatex", "-interaction=nonstopmode", "main.tex"]]
    for c in cmds:
        r = subprocess.run(c, cwd=paper, capture_output=True, text=True, errors="replace")
        if c[0] == "pdflatex" and not (paper / "main.pdf").exists():
            return None, "pdflatex 失敗，請看 main.log 最後幾行：\n" + "\n".join(r.stdout.splitlines()[-15:])
    log = (paper / "main.log").read_text(encoding="utf-8", errors="replace")
    warns = []
    undef = sorted(set(re.findall(r"(?:Citation|Reference) `([^']+)' .*undefined", log)))
    if undef:
        warns.append("未定義的引用或參照：" + ", ".join(undef))
    over = len(re.findall(r"Overfull \\hbox", log))
    if over:
        warns.append("Overfull hbox {} 處（文字超出邊界，可檢查長網址或表格）".format(over))
    pages = re.search(r"Output written on main\.pdf \((\d+) page", log)
    return warns, "已編譯 main.pdf（{} 頁）".format(pages.group(1) if pages else "?")


def package(paper, figs, has_bbl, sources):
    files = list(sources) + STY_FILES + LICENSES + (["main.bbl"] if has_bbl else [])
    rel_figs = [f.relative_to(paper).as_posix() for f in figs]
    with tarfile.open(paper / "arxiv-submission.tar.gz", "w:gz") as t:
        for f in files + rel_figs:
            t.add(paper / f, arcname=f)
    with zipfile.ZipFile(paper / "overleaf.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in files + rel_figs + ["references.bib"]:
            if (paper / f).exists():
                z.write(paper / f, arcname=f)
    return files + rel_figs


def main():
    p = argparse.ArgumentParser(description="arXiv preprint：建立、檢查、編譯、打包")
    p.add_argument("paper_dir", help="論文資料夾，例如 manuscript")
    p.add_argument("--init", action="store_true", help="建立資料夾並複製範本與版型檔")
    p.add_argument("--bib", help="要同步的 references.bib（例如 library/references.bib）")
    args = p.parse_args()
    paper = Path(args.paper_dir).resolve()

    if args.init:
        init(paper)
        return
    if not (paper / "main.tex").exists():
        sys.exit("找不到 main.tex，請先執行 --init")
    copy_style(paper)
    if args.bib:
        shutil.copy(args.bib, paper / "references.bib")

    problems, notes, figs, sources = check(paper, paper / "references.bib")
    warns, status = compile_pdf(paper)
    has_bbl = (paper / "main.bbl").exists()
    if not has_bbl:
        warns = (warns or []) + ["沒有 main.bbl：arXiv 不會執行 bibtex，上傳前請在 Overleaf 編譯後下載 main.bbl 放進資料夾，再重跑本程式打包"]
    packed = package(paper, figs, has_bbl, sources)

    lines = ["# 投稿前檢查", "", "## 狀態", "", "- " + status]
    lines += ["- " + n for n in notes]
    lines += ["", "## 需要修正", ""] + (["- ❌ " + x for x in problems] or ["- 無"])
    lines += ["", "## 編譯警告", ""] + (["- ⚠️ " + x for x in (warns or [])] or ["- 無"])
    lines += ["", "## arxiv-submission.tar.gz 內容", ""] + ["- " + f for f in packed]
    lines += ["", "## 上傳 arXiv 前請人工確認", "",
              "- [ ] 作者、單位、通訊作者 email 正確；所有作者同意上傳",
              "- [ ] 分類（例如 q-bio.QM、stat.AP）；第一次投該分類需要 endorsement",
              "- [ ] 授權選擇（例如 CC BY 4.0）",
              "- [ ] metadata 表單的標題、摘要與 PDF 一致",
              "- [ ] 已揭露 AI 工具的使用（Use of AI tools 段落）",
              "- [ ] 所有數字與引用已由作者本人核對"]
    (paper / "check-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:lines.index("## arxiv-submission.tar.gz 內容")]))
    print("\n完整報告：" + str(paper / "check-report.md"))
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
