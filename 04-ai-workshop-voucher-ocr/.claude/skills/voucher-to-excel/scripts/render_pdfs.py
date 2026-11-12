# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf"]
# ///
"""把掃描的 PDF 發票／黏存單每一頁轉成 PNG，供 AI 看圖辨識。

用法：
  uv run --script render_pdfs.py --out <輸出資料夾> [--dpi 150] a.pdf b.pdf ...
"""
import argparse
import pathlib

import pymupdf

ap = argparse.ArgumentParser()
ap.add_argument("pdfs", nargs="+")
ap.add_argument("--out", required=True)
ap.add_argument("--dpi", type=int, default=150)
args = ap.parse_args()

out = pathlib.Path(args.out)
out.mkdir(parents=True, exist_ok=True)
for p in map(pathlib.Path, args.pdfs):
    doc = pymupdf.open(p)
    text_len = sum(len(pg.get_text().strip()) for pg in doc)
    for i, pg in enumerate(doc):
        png = out / f"{p.stem}_p{i + 1}.png"
        pg.get_pixmap(dpi=args.dpi).save(png)
        print(f"{p.name}\tpage {i + 1}/{len(doc)}\ttext_layer={text_len}\t{png}")
