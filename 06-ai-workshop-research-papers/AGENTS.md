# Agent Rules

## 專案目的

用上一單元的 QIIME 2 分析結果（`data/`）加上文獻庫（`papers/`、`library/`），撰寫一篇**英文**研究論文（LaTeX，arXiv preprint 格式），放在 `manuscript/`。研究問題、答案與限制已整理在 `manuscript/00-research-brief.md`，動筆前先讀。

## 數字與資料

- 論文中所有數字一律取自 `data/tables/`。寫入前先讀檔確認，禁止憑記憶或從 `data/QIIME2_Analysis_Report.pdf` 抄數字。
- Methods 的軟體版本與參數取自 `data/Qiime2_Pipeline.sh`。
- 論文的圖依 `data/tables/` 重畫，放在 `manuscript/figures/`；`data/figures/` 只作參考。
- 新算出的數字，要把算法或來源檔案寫進 `manuscript/citation-check.md` 的「數字核對」表。

## 文獻

- 搜尋用 `arxiv` skill；收錄一律用 `paper-library` skill（`scripts/add_paper.py`），禁止手動編造或改寫 `library/references.bib`。
- 搜尋後先列候選清單給使用者挑選，不要自己決定全部下載。
- 寫論文時只能引用 `library/references.bib` 裡的 citekey，格式為 `\citep{citekey}` 或 `\citet{citekey}`。
- 每個引用都要能對應到 `library/notes/<citekey>.md` 的「可引用的原文」（逐字抄錄並附頁碼）；只有書目、沒有 PDF 的文獻，只能根據摘要引用，筆記標示「僅讀摘要」。

## 寫作

- 論文使用英文；與使用者溝通、筆記與核對文件使用繁體中文。
- 寫作順序（檔名編號）：01 方法 → 02 結果 → 03 前言 → 04 討論（含結論）→ 05 摘要 → 06 標題；聲明放在 07。`main.tex` 依閱讀順序 `\input` 各節。
- 各節檔案：`manuscript/sections/01-methods.tex`、`02-results.tex`、`03-introduction.tex`、`04-discussion.tex`、`05-abstract.tex`、`06-title.tex`、`07-declarations.tex`。使用者說「寫 Methods」等，就寫到對應檔案。
- 段落與章節結構參考 `research-paper-writing` skill；版型、檢查、編譯、打包用 `arxiv-preprint` skill。
- 結果只描述數據，不解釋；解釋放在討論。
- 主張的強度要和證據相符：24 位病人的再分析、LME 未收斂，避免 "prove"、"demonstrate efficacy"、"confirm" 等用詞；相關不等於因果。研究限制要寫進討論。
- 作者貢獻、利益衝突、經費只能由作者提供，不得代寫，保留 `[To be completed by the authors.]`。
- 不得把論文上傳到 arXiv、Overleaf 或任何外部網站，除非使用者明確要求。

## 環境

- Python 腳本只用標準函式庫為原則；畫圖需要 matplotlib。
- 編譯與檢查：在專案根目錄執行 `python .agents/skills/arxiv-preprint/scripts/build.py manuscript --bib library/references.bib`（Claude Code 用 `.claude/skills/...`；有 pdflatex 就編譯，沒有就只檢查並產生 `overleaf.zip`）。
