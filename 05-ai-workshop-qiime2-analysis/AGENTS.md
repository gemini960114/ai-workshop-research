# 16S rRNA QIIME 2 分析：AI Agent 工作規則

這份規則讓 AI Agent 在國網 HPC 上分析 16S 資料時，不必每次重新詢問基本設定。
（Antigravity / Gemini CLI 讀 `GEMINI.md`，Claude Code 讀 `CLAUDE.md`；內容相同，複製一份改名即可。）

## 1. 參考範本與環境
- **分析腳本範本**：`QIIME2/Qiime2_Pipeline.sh`（下載資料解壓縮後就有）
- **報告格式**：繁體中文 PDF、圖 300 DPI；若工作資料夾有 `report/QIIME2_Analysis_Report.pdf` 範例，可參考它的版面
- **Slurm 預設**：
  - `#SBATCH --account=<計畫代號>`（本次為 `mst109178`）
  - `#SBATCH --partition=ngscourse8g`（上課用，1 CPU / 8 GB 上限）；正式資料可改 `ngs16g`、`ngs32g`、`ngs62g`
- **軟體**：`module load biology/qiime2/2026.7`

## 2. 拿到新資料時
1. **檢查資料**：壓縮檔先解壓縮；檢查 `manifest.tsv`（沒有就依 `.fastq.gz` 自動建立）與 `metadata.tsv` 的實際欄位（分組、時間點、臨床欄位）。
2. **調整參數**：依 Phred 品質分布調整 DADA2 的 `--p-trunc-len-f / -r`，依各檢體讀數調整稀釋深度 `--p-sampling-depth`，避免剔除太多檢體；依 metadata 欄位替換下游的分組、LME、隨機森林欄位名稱。
3. **派送與回報**：用 `sbatch` 派送，每 5 分鐘回報一次進度，直到 `COMPLETED`。
4. **報告**：完成後解析所有 `.qza / .qzv`，畫 300 DPI 圖（`report/figures/`），產出繁體中文 PDF 報告，每個分析一段，最後寫總結。

## 3. 寫報告的規則
- **數字一律從輸出檔讀**（`.qza / .qzv` 解壓縮後的 tsv/csv），不要憑印象或從對話摘要抄。
- **用詞要符合證據強度**：24 位病人的觀察性分析，不寫「證實療效」「證明有效」。
- 同一位病人有多個檢體時，把所有檢體混在一起做的檢定要註明「檢體不是獨立樣本」。
- 模型有警告（例如 LME `Converged: No`）要寫進報告。
