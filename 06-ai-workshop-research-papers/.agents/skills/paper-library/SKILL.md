---
name: paper-library
description: >-
  本地文獻庫管理：把論文下載到 papers/，依「作者_年份_標題」重新命名，並同步追加 library/references.bib
  與 library/download-log.md。當使用者要下載、收錄、登錄論文，要把 arXiv ID 或 DOI 加入文獻庫、
  建立或更新 references.bib、查詢文獻庫裡有哪些論文，或在 arxiv skill 搜尋後要「把這幾篇存下來」時，
  必須使用此 Skill。可搭配 arxiv skill（負責搜尋）使用。
---

# 本地文獻庫 Skill（`paper-library`）

arxiv skill 只會搜尋；這個 skill 負責「收進文獻庫」。所有寫入都透過 `scripts/add_paper.py`，
**不要手動編輯 references.bib 或 download-log.md 來新增論文**，以免檔名、citekey 與紀錄對不上。

## 文獻庫結構（相對於專案根目錄）

| 路徑 | 內容 |
|---|---|
| `papers/` | PDF，檔名 `第一作者姓氏_年份_標題前幾個實詞.pdf` |
| `library/references.bib` | 書目清單；寫論文時只能引用這裡有的 citekey |
| `library/download-log.md` | 每收錄一篇新增一列：日期、來源、ID、標題、搜尋關鍵字、檔名、citekey |

citekey 規則：第一作者姓氏 + 年份 + 標題第一個實詞，全小寫，例如 `taur2018reconstitution`。

## 工作流程

### 1. 搜尋（用 arxiv skill）

依使用者的主題，用 arxiv skill 搜尋。把候選論文整理成表格給使用者看：
編號、arXiv ID、標題、第一作者、年份、一句話說明「和我們的研究有什麼關係」。

**先停下來，請使用者選要收錄哪幾篇**，不要自己決定全部下載。

### 2. 收錄

在專案根目錄執行（Windows 用 `python`，macOS / Linux 可能是 `python3`）：

```bash
# arXiv：一次可給多個 ID，會下載 PDF
python .agents/skills/paper-library/scripts/add_paper.py arxiv 2610.21224 2401.01234 --query "microbiome longitudinal"

# 期刊論文（不在 arXiv）：用 DOI 登錄書目，不會下載 PDF
python .agents/skills/paper-library/scripts/add_paper.py doi 10.1126/scitranslmed.aap9489 --query "auto-FMT allo-HSCT"

# 使用者已手動下載期刊 PDF：用 --pdf 改名並搬進 papers/
python .agents/skills/paper-library/scripts/add_paper.py doi 10.1126/scitranslmed.aap9489 --pdf "下載/某檔案.pdf"
```

- `--query` 一定要填當初搜尋用的關鍵字，之後才查得到每篇論文是怎麼找到的。
- 不確定時先加 `--dry-run` 預覽，不會寫入任何檔案。
- `--no-pdf`：只登錄書目、不下載。
- 已收錄過的 ID 或 DOI 會自動略過，重複執行不會產生重複資料。
- Claude Code 環境的路徑是 `.claude/skills/paper-library/scripts/add_paper.py`。

### 3. 回報

收錄完成後，用表格列出：citekey、PDF 檔名（或「未下載」）、標題。
有「查無此 ID」、「PDF 下載失敗」或「Crossref 查不到 DOI」的訊息時，要明確告訴使用者，不要略過。

## 規則

1. **不可捏造文獻。** 每一筆都必須來自 arXiv API 或 Crossref 的查詢結果；查不到就回報查不到。
2. **寫論文時只能引用 `references.bib` 裡的 citekey。** 需要的文獻還沒收錄，先用本 skill 收錄再引用。
3. **引用前要讀過內容。** 有 PDF 的，引用時要能指出原文出處（頁碼或段落）；只有書目、沒有 PDF 的，最多只能根據摘要引用，並在筆記中標示「僅讀摘要」。
4. arXiv 要求連續請求間隔 3 秒，腳本已處理；不要用迴圈一篇一篇快速呼叫腳本。
5. 期刊論文多半有版權，不要嘗試從非官方來源下載 PDF；請使用者自行從圖書館或期刊網站取得後用 `--pdf` 收錄。
