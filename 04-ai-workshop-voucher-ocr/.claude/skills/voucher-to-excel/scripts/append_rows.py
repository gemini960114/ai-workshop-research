# /// script
# requires-python = ">=3.11"
# dependencies = ["openpyxl"]
# ///
"""把辨識好的憑證資料寫進 record.xlsx，並依旗標上色、加註解。

用法：
  uv run --script append_rows.py --xlsx record.xlsx --template record.example.xlsx \
      --data records.json --backup-dir <備份資料夾>

- record.xlsx 不存在時，會從範本複製一份並清掉範例資料列。
- 新資料列接在現有資料後面，合計列自動往下移，並改成 SUM 公式。
- 控帳編號已存在的資料會跳過（不重複寫入）。
- 寫入前會先把 record.xlsx 備份到 --backup-dir。

records.json 格式：
{
  "records": [
    {
      "source": "SKM_xxx.pdf",
      "會計科目": "03-1111-03114Z1200-0000-51330607-00-00",
      "控帳編號": "203114005433",
      "發票號碼": "RT10707602",          # 找不到就給 null，並在 flags 標 missing
      "發票金額": 262688,
      "總計金額": 262688,
      "發票統編": "30170570",
      "發票抬頭": "財團法人國家實驗研究院國家高速網路與計算中心",
      "負債科目": null,                  # 省略或 null → 用範本值
      "flags": {
        "發票號碼": {"type": "missing",   "note": "免用發票收據，沒有發票號碼"},
        "發票金額": {"type": "uncertain", "note": "手寫數字模糊"}
      }
    }
  ]
}
"""
import argparse
import json
import pathlib
import re
import shutil
import sys
from copy import copy
from datetime import datetime

import openpyxl
from openpyxl.comments import Comment
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter

YELLOW = PatternFill("solid", fgColor="FFFF00")
BLUE = PatternFill("solid", fgColor="00B0F0")
AUTHOR = "Claude"
FIELDS = ["項次", "會計科目", "控帳編號", "發票號碼", "發票金額", "總計金額",
          "發票統編", "發票抬頭", "負債科目", "計畫代號"]
FORMATS = {
    "會計科目": r"^\d{2}-\d{4}-[0-9A-Z]{10}-\d{4}-\d{8}-\d{2}-\d{2}$",
    "控帳編號": r"^\d{12}$",
    "發票號碼": r"^[A-Z]{2}\d{8}$",
    "發票統編": r"^\d{8}$",
}
LEGEND = [
    ("FFFF00", "黃底", "找不到：PDF 中沒有此資料，欄位留空"),
    ("00B0F0", "藍底", "不確定：已填入推測值，請人工確認（見儲存格註解）"),
]


def find_layout(ws):
    header = next(r for r in range(1, ws.max_row + 1) if ws.cell(r, 1).value == "項次")
    cols = {ws.cell(header, c).value: c for c in range(1, ws.max_column + 1)}
    missing = [f for f in FIELDS if f not in cols]
    if missing:
        sys.exit(f"表頭缺少欄位：{missing}")
    total = next(r for r in range(header + 1, ws.max_row + 1)
                 if any(ws.cell(r, c).value == "合計" for c in range(1, ws.max_column + 1)))
    return header, cols, total


def to_cell_value(field, v):
    if v is None or v == "":
        return None
    if field in ("發票金額", "總計金額"):
        return int(v) if float(v).is_integer() else float(v)
    if field in ("控帳編號", "發票統編"):
        s = str(v).strip()
        # 開頭是 0 的統編存文字，避免 Excel 吃掉前導 0
        return s if s.startswith("0") or not s.isdigit() else int(s)
    return str(v).strip()


def ensure_legend(ws, font):
    for r, (color, label, text) in enumerate(LEGEND, start=1):
        k, l = ws.cell(r, 11), ws.cell(r, 12)
        if k.value not in (None, label):
            print(f"警告：K{r} 已有其他內容，未寫入圖例", file=sys.stderr)
            continue
        k.value, k.fill, k.font = label, PatternFill("solid", fgColor=color), copy(font)
        l.value, l.font = text, copy(font)
    ws.column_dimensions["K"].width = 8
    ws.column_dimensions["L"].width = 46


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xlsx", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--backup-dir", required=True)
    args = ap.parse_args()

    xlsx, template = pathlib.Path(args.xlsx), pathlib.Path(args.template)
    records = json.loads(pathlib.Path(args.data).read_text(encoding="utf-8"))["records"]

    # 範本：取第一筆資料列的乾淨樣式與預設負債科目
    tws = openpyxl.load_workbook(template).active
    t_header, t_cols, _ = find_layout(tws)
    t_row = t_header + 1
    row_styles = {f: copy(tws.cell(t_row, t_cols[f])._style) for f in FIELDS}
    default_liab = tws.cell(t_row, t_cols["負債科目"]).value
    header_font = tws.cell(t_header, 1).font

    fresh = not xlsx.exists()
    if fresh:
        print(f"從範本建立 {xlsx}")  # 成功寫完才存檔，失敗不留半成品
    else:
        bdir = pathlib.Path(args.backup_dir)
        bdir.mkdir(parents=True, exist_ok=True)
        bak = bdir / f"{xlsx.stem}.{datetime.now():%Y%m%d-%H%M%S}.bak.xlsx"
        shutil.copy(xlsx, bak)
        print(f"已備份：{bak}")

    wb = openpyxl.load_workbook(template if fresh else xlsx)
    ws = wb.active
    header, cols, total_row = find_layout(ws)
    first = header + 1

    if fresh:  # 清掉範本的範例資料列
        for r in range(first, total_row):
            for f in FIELDS:
                c = ws.cell(r, cols[f])
                c.value, c.comment = None, None
        existing_rows = []
    else:
        existing_rows = [r for r in range(first, total_row)
                         if ws.cell(r, cols["控帳編號"]).value not in (None, "")]
    existing_ids = {str(ws.cell(r, cols["控帳編號"]).value) for r in existing_rows}

    new = []
    for rec in records:
        cid = str(rec.get("控帳編號") or "").strip()
        if cid and cid in existing_ids:
            print(f"跳過（控帳編號 {cid} 已存在）：{rec.get('source')}")
            continue
        existing_ids.add(cid)
        new.append(rec)

    # 合計列往下移
    next_row = first + len(existing_rows)
    new_total = next_row + len(new)
    saved_total = [(c.column, c.value, copy(c._style)) for c in ws[total_row]]
    for c in ws[total_row]:
        c.value = None
    for col, v, st in saved_total:
        ws.cell(new_total, col).value = v
        ws.cell(new_total, col)._style = st

    report = []
    for i, rec in enumerate(new):
        r = next_row + i
        flags = dict(rec.get("flags") or {})
        vals = {f: rec.get(f) for f in FIELDS}
        if not vals["負債科目"]:
            vals["負債科目"] = default_liab  # 使用者已確認：固定沿用範本值
        vals["項次"] = r - first + 1
        vals["計畫代號"] = f"=MID({get_column_letter(cols['會計科目'])}{r},9,10)"
        for f, pat in FORMATS.items():
            v = vals.get(f)
            if v not in (None, "") and not re.match(pat, str(v)) and f not in flags:
                flags[f] = {"type": "uncertain", "note": f"格式不符預期（{pat}），請確認。"}
        for f in FIELDS:
            if vals.get(f) in (None, "") and f not in flags:
                flags[f] = {"type": "missing", "note": "PDF 中找不到此資料。"}

        for f in FIELDS:
            c = ws.cell(r, cols[f])
            c._style = copy(row_styles[f])
            c.value = vals[f] if f in ("項次", "計畫代號") else to_cell_value(f, vals[f])
            c.comment = None
            fl = flags.get(f)
            if fl:
                kind = fl["type"]
                c.fill = YELLOW if kind == "missing" else BLUE
                prefix = "找不到：" if kind == "missing" else "不確定："
                c.comment = Comment(prefix + fl.get("note", ""), AUTHOR, width=260, height=90)
        report.append((r, rec.get("source"), {f: fl["type"] for f, fl in flags.items()}))

    last = new_total - 1
    for f in ("發票金額", "總計金額"):
        L = get_column_letter(cols[f])
        ws.cell(new_total, cols[f]).value = f"=SUM({L}{first}:{L}{last})"

    ensure_legend(ws, header_font)
    wb.save(xlsx)

    for r, src, fl in report:
        marks = ", ".join(f"{k}={'黃' if v == 'missing' else '藍'}" for k, v in fl.items()) or "無"
        print(f"第 {r} 列 ← {src}　標示：{marks}")
    print(f"新增 {len(new)} 筆；合計列在第 {new_total} 列")


if __name__ == "__main__":
    main()
