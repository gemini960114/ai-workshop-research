---
name: arxiv-preprint
description: >-
  把論文排版成英文 arXiv preprint（LaTeX，arxiv-style 版型），並完成投稿前檢查與打包。
  當使用者要「寫成 arXiv 格式」、「做成 preprint」、「轉成 LaTeX 論文」、「準備上傳 arXiv / Overleaf」、
  「把中文論文改寫成英文投稿版」，或要檢查 LaTeX 論文的引用、圖檔、摘要長度時，必須使用此 Skill。
  版型檔（arxiv.sty、fancyhdr.sty）已隨 skill 附上，不需安裝額外 LaTeX 套件；本機沒有 LaTeX 時改用 Overleaf。
---

# arXiv preprint Skill（`arxiv-preprint`）

以 [kourgeorge/arxiv-style](https://github.com/kourgeorge/arxiv-style)（MIT）為版型，改成適合生醫與計算生物論文的
IMRaD 結構，並加上期刊常要求的聲明段落。所有操作都透過 `scripts/build.py`（只用 Python 標準函式庫）。

## 附帶檔案

| 檔案 | 用途 |
|---|---|
| `assets/template.tex` | 範本：Abstract（結構化）、IMRaD、Data/Code availability、Ethics、Author contributions、Competing interests、Funding、Use of AI tools |
| `assets/arxiv.sty` | 版型（MIT，見 `LICENSE-arxiv-style.txt`） |
| `assets/fancyhdr.sty` | 版型唯一缺少的依賴，由 CTAN 原始碼產生、未修改（LPPL，見 `LICENSE-fancyhdr.txt`） |

`.sty` 放在論文資料夾內即可被 LaTeX 讀到，就像專案自己的 `.venv`，不會動到系統的 TeX 安裝。

## 工作流程

### 1. 建立論文資料夾

```bash
python .agents/skills/arxiv-preprint/scripts/build.py <論文資料夾> --init
```

會複製 `main.tex`（範本）、兩個 `.sty`、授權檔，並建立 `figures/`。已存在的 `main.tex` 不會被覆蓋。

### 2. 撰寫 `main.tex`

- **分節撰寫**：章節可拆成 `sections/*.tex`，由 `main.tex` 以 `\input{sections/...}` 依閱讀順序引入；`build.py` 會一併檢查與打包所有被 `\input` 的檔案。
- **建議寫作順序**：方法 → 結果（只描述事實）→ 前言 → 討論（含結論）→ 摘要 → 標題。
- **內容來源**：數字一律回到原始結果表核對；若由既有稿件改寫，不得新增原稿沒有的主張或數字。
- **引用**：用 `\citep{key}`（括號）或 `\citet{key}`（作者當主詞），key 必須存在於 `references.bib`。
- **圖**：放進 `figures/`，用 `\includegraphics[width=...]{檔名}`；表格用 `booktabs`（`\toprule` 等），不要用直線。
- **頁首**：修改 `\shorttitle`（短標題，約 60 字元內，避免與右側字樣重疊）與 `\headeright`。
- **摘要**：結構化（Background / Methods / Results / Conclusions），arXiv 表單上限 1,920 字元。
- **Use of AI tools**：如實寫出 AI 協助了哪些步驟、作者核對了什麼。AI 不得列為作者。

### 3. 檢查、編譯、打包

```bash
python .agents/skills/arxiv-preprint/scripts/build.py <論文資料夾> --bib library/references.bib
```

1. 把 `--bib` 指定的書目複製成 `references.bib`
2. 檢查：引用是否都在 bib、圖檔是否存在、摘要長度、範本佔位文字與 `[To be completed …]` 是否已替換（會跟著 `\input` 檢查所有章節檔）
3. 有 `pdflatex` 與 `bibtex` 時編譯 `main.pdf`（pdflatex → bibtex → pdflatex ×2），並回報未定義引用與 Overfull 警告
4. 打包：
   - `arxiv-submission.tar.gz`：上傳 arXiv 用（`main.tex`、`main.bbl`、`.sty`、授權檔、用到的圖）
   - `overleaf.zip`：上傳 Overleaf 用（另含 `references.bib`）
5. 寫出 `check-report.md`（含上傳前人工確認清單）

有 ❌ 項目時程式以非零狀態結束，請修正後重跑。

### 4. 本機沒有 LaTeX 時

`build.py` 仍會做檢查並產生 `overleaf.zip`。到 <https://www.overleaf.com> → New Project → Upload Project → 選 `overleaf.zip`，
Compiler 選 **pdfLaTeX** 即可編譯。

## 規則

1. **不得上傳到 arXiv**，除非使用者明確要求且所有作者同意；arXiv 文章無法刪除，只能撤回。
2. 不得新增 `references.bib` 以外的引用；需要新文獻時先用 `paper-library` skill 收錄。
3. 不得修改 `arxiv.sty`、`fancyhdr.sty`；版面調整寫在 `main.tex`。
4. 回報時列出 `check-report.md` 的狀態、需要修正與警告三段，不要只說「完成」。
