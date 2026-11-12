# 單元 05：QIIME 2 腸道菌相分析 — 用自然語言在國網 HPC 上跑完整套分析

手上有一批 16S 定序資料，想做腸道菌相分析，但不熟 Linux、Slurm 和 QIIME 2 指令？這個單元示範：在國網 HPC 上打開 AI Agent，**用幾句中文**請它下載資料、選計畫帳號、派送作業、回報進度，最後交出一份 9 頁、附 8 張圖的分析報告。

> 📥 **本單元上課簡報**：[下載 05-qiime2-analysis.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/05-qiime2-analysis.pptx)（18 頁，含講者備註）

> 🎬 **本單元教學影片**：[單元 05｜QIIME 2 腸道菌相分析](https://github.com/gemini960114/ai-workshop-research/blob/main/movies/05-qiime2-analysis.mp4)（MP4，4 分 06 秒，附[繁體中文字幕](https://github.com/gemini960114/ai-workshop-research/blob/main/movies/05-qiime2-analysis.zh-TW.srt)）

**下載資料 → 確認帳號與佇列 → 派送作業 → 產出報告**

本單元的重點有兩個：前半段看「怎麼請 AI 在 HPC 上做事」，過程很短；後半段看「分析報告裡有什麼」，這是下一單元寫論文的材料。

> ⚠️ 本單元的資料來自 QIIME 2 官方教學（cancer microbiome intervention tutorial），用於練習。報告是 AI 產出的，數字已逐一核對，但部分用詞過強，引用前請看〈解讀時要注意〉。

| 步驟 | 內容 | 預估時間 |
| :--- | :--- | :---: |
| **準備** | [登入 HPC、開啟 AI Agent](#準備) | 5 分鐘 |
| **Step 1** | [下載資料](#step-1下載資料) | 2 分鐘 |
| **Step 2** | [確認計畫帳號與佇列](#step-2確認計畫帳號與佇列) | 3 分鐘 |
| **Step 3** | [派送作業、定時回報](#step-3派送作業定時回報) | 20 分鐘（等待） |
| **Step 4** | [產出分析報告](#step-4產出分析報告) | 20 分鐘（等待） |
| **導讀** | [分析報告逐節導讀](#分析報告逐節導讀) | 30 分鐘 |

```mermaid
flowchart LR
    A["Step 1<br>下載資料"] --> B["Step 2<br>帳號與佇列"]
    B --> C["Step 3<br>派送 + 回報"]
    C --> D["Step 4<br>PDF 報告"]
    D --> F["下一單元<br>寫論文"]
```

---

## 準備

1. 登入國網 HPC 的登入節點，打開終端機。
2. 進入自己的工作資料夾，啟動 AI Agent（本次用 Antigravity CLI；Claude Code、Gemini CLI 也可以）。HPC 登入節點沒有圖形介面，所以這裡用 CLI 版；單元 01 提醒「不要選 CLI」指的是在自己電腦上安裝的情況。
3. 把本資料夾的 [`AGENTS.md`](AGENTS.md) 放進工作資料夾。它寫好了 AI 要遵守的規則：用哪份腳本當範本、Slurm 預設值、報告格式、「數字一律從輸出檔讀」。
   - Antigravity / Gemini CLI 讀的是 `GEMINI.md`，Claude Code 讀 `CLAUDE.md`，內容相同，複製一份改名即可。

> 💡 不需要先學 Slurm 或 QIIME 2 指令。下面每一步都只是一句中文。

---

## Step 1：下載資料

### 📋 請複製以下指令貼給 AI Agent：

```text
下載 https://drive.usercontent.google.com/download?id=1JXGPT2bhLJvOnpTY9-oYBKxvZ45M0qPN&export=download&authuser=1 解壓縮
```

### 你應該會看到

AI 下載 `QIIME2.tar.gz`（約 60 MB），解壓縮成 `QIIME2/`：

| 資料夾 | 內容 |
|---|---|
| `Input_Data/` | 原始定序檔、檢體資料表、特徵表、SILVA 分類器（見[輸入資料](#輸入資料)） |
| `Qiime2_Pipeline.sh` | 整套分析的 Slurm 腳本（本資料夾的 [`pipeline/`](pipeline/) 有一份） |

---

## Step 2：確認計畫帳號與佇列

在 HPC 上跑作業要扣計畫點數，所以要先確認用哪個計畫、哪個佇列。直接問 AI：

### 📋 請複製以下指令貼給 AI Agent：

```text
我的帳號可以使用哪些計畫？應該是 MST109178？
```

```text
改為 MST109178，然後 ngscourse8g 這個夠用嗎？還是要用 ngs62g，CPU 數量也增加？
```

### 你應該會看到

AI 會自己查 Slurm 的帳號設定，告訴你哪些計畫能用（本次：MST109178 可以用），並把腳本改成這個帳號。

關於佇列，AI 的判斷是：

| 佇列 | 資源 | 適合 |
|---|---|---|
| **ngscourse8g** | 1 CPU / 8 GB | **本次就夠用**：最吃資源的 DADA2 去噪與分類器訓練已預先算好，約 20 分鐘跑完 |
| ngs62g | 最多 8 CPU / 62 GB | 自己重跑 DADA2、訓練分類器，或分析正式的大型資料 |

---

## Step 3：派送作業、定時回報

### 📋 請複製以下指令貼給 AI Agent：

```text
直接派送就可以了
```

```text
每五分回報一次進度
```

### 你應該會看到

| 時間 | AI 回報 |
|---|---|
| 0 分 | 已派送，作業編號 570915，狀態 Running |
| 8 分 | 資料匯入、五階段篩選、物種分類完成；正在畫物種組成圖、建演化樹 |
| 15 分 | 多樣性分析、組間檢定、LME、UMAP 完成；進入最後的縱向分析 |
| **18 分** | **COMPLETED**，總耗時 17 分 57 秒，自動停止回報 |

跑完會得到一堆 `.qza`（資料檔）與 `.qzv`（圖表檔）。`.qzv` 拖進 <https://view.qiime2.org> 就能看互動圖表，本資料夾的 [`results/qzv/`](results/qzv/) 有一份。

---

## Step 4：產出分析報告

一堆 `.qzv` 很難一次看懂，請 AI 整理成一份報告：

### 📋 請複製以下指令貼給 AI Agent：

```text
幫我產出一份 PDF 報告，裡面請針對每一個分析進行分段報告，並加上相對應的分析圖檔，你可以自己處理，然後最後做總結、結論
```

### 你應該會看到

AI 自己解壓縮、讀數字、畫圖、排版，約 17 分鐘後交出：

- [`report/QIIME2_Analysis_Report.pdf`](report/QIIME2_Analysis_Report.pdf)：9 頁繁體中文報告
- [`report/figures/`](report/figures/)：8 張 300 DPI 組合圖（fig01–fig08）

報告內容見下方〈[分析報告逐節導讀](#分析報告逐節導讀)〉。

---

## 附註：AI 寫的東西也會錯

整理教材時，我們把報告的數字逐一回到 `.qza / .qzv` 原始輸出檔核對：**PDF 的數字都對得上**，但 AI 交 PDF 時在對話裡另外寫的摘要，有好幾處寫錯：

| 項目 | AI 對話摘要 | 原始輸出檔 |
|---|---|---|
| LME 組別主效應 | β = −4.254 | **β = 2.962** |
| 移植前 vs 後的 q 值 | 6.95 × 10⁻¹⁴ | **1.33 × 10⁻¹⁶** |
| Unweighted UniFrac PC1 | 13.48% | **20.42%** |
| 門層級組成 | Firmicutes 76.33%、Bacteroidetes 11.27% | **Bacillota 84.0%、Bacteroidota 2.7%** |

要寫進論文的數字，一律回到原始輸出檔確認。關鍵數字已抽成表格放在 [`results/tables/`](results/tables/)，抽取程式是 [`tools/extract_tables.py`](tools/extract_tables.py)；完整對話見 [`history/analysis-conversation.md`](history/analysis-conversation.md)。

---

## 分析報告逐節導讀

### 研究背景

資料來自臨床試驗 **NCT02269150**：接受**異體造血幹細胞移植（allo-HSCT）**的病人，隨機分成兩組：

- **自體糞菌移植組（auto-FMT）**：化療前先保存自己的糞便菌叢，移植後 8–27 天（中位數 18 天）再放回去，希望重建被化療與抗生素破壞的腸道菌相。
- **對照組**：不介入。

**要回答的問題**：移植過程中腸道菌相怎麼變化？auto-FMT 組的菌相，隨時間的變化和對照組不同嗎？哪些菌跟著移植時間起落？

### 輸入資料

| 檔案 | 內容 | 用在 |
|---|---|---|
| `data_to_import/` | 82 個 `.fastq.gz` = **41 個檢體 × 雙端（R1/R2）**原始定序檔 | 上游：品質評估、DADA2 去噪示範 |
| `sample-metadata.tsv` | 12,546 個檢體 × 27 欄：病人、分組、距移植天數、糞便性狀、幹細胞來源… | 上下游共用（本資料夾 [`input/`](input/) 有一份） |
| `feature-table.qza` | **12,546 個檢體 × 17,865 個 ASV** 的計數表（FigShare 公開資料） | 下游所有分析的起點 |
| `rep-seqs.qza` | 17,865 條 ASV 的代表序列 | 物種分類、建演化樹 |
| `silva-138.2-ssu-nr99-515f-806r-classifier.qza` | 預先訓練好的 SILVA 138.2 分類器（V4 區段） | 物種分類 |

> ⚠️ **上游和下游的資料不承接。** 上游的 41 個檢體只是示範「原始定序檔怎麼處理」；下游直接用 FigShare 上整理好的大表，從 12,546 個檢體篩出本研究的 356 個。

### 分析流程

| 節 | 分析 | QIIME 2 指令（重點） | 產出 |
|---|---|---|---|
| 1 | 上游品質控管、DADA2 去噪 | `demux summarize`、`dada2` | `demultiplexed-sequences-summ.qzv` |
| 2 | 五階段篩選 | `feature-table filter-samples / filter-features`、`taxa filter-table` | `filtered-table-4-summ.qzv` |
| 3 | 物種組成 | `feature-classifier classify-sklearn`、`taxa barplot` | `taxa-bar-plots-1/2.qzv` |
| 4 | 演化樹、稀釋曲線 | `phylogeny align-to-tree-mafft-fasttree`、`diversity alpha-/beta-rarefaction` | `shannon- / braycurtis-rarefaction-plot.qzv` |
| 5 | Alpha 多樣性組間比較 | `diversity core-metrics-phylogenetic`、`alpha-group-significance` | `alpha-group-sig-obs-feats.qzv` |
| 6 | Beta 多樣性排序 | PCoA、`diversity umap`、`emperor plot` | `*_emperor.qzv`、`uu-umap-emperor-w-time.qzv` |
| 7 | 縱向模型（LME）與隨機森林 | `longitudinal linear-mixed-effects`、`feature-volatility` | `lme-…qzv`、`rf-accuracy-results.qzv` |

---

### 1. 上游：定序品質與 DADA2 去噪

![上游品質控管與 DADA2](report/figures/fig01_upstream_qc_dada2.png)

**做什麼**：檢查 41 個檢體原始讀序的品質，決定從第幾個鹼基截斷，再用 DADA2 去除定序錯誤、合併雙端、移除嵌合體，得到 ASV（精確到單一鹼基的序列變異）。

**結果**

| DADA2 階段 | 總讀序數 | 保留率 |
|---|---:|---:|
| 原始輸入 | 1,832,285 | 100% |
| 品質過濾 | 1,662,429 | 90.7% |
| 去噪 | 1,654,313 | 90.3% |
| 雙端合併 | 1,608,758 | 87.8% |
| **移除嵌合體** | **1,535,600** | **83.8%** |

- R1、R2 前 200 bp 的品質中位數都在 Q37–Q38，之後快速下滑，所以截在 **204 bp（R1）/ 205 bp（R2）**。
- 最後得到 **660 個 ASV**，每個檢體中位數 37,899 條讀序。

**白話**：定序品質很好，八成以上的讀序都留下來了。

---

### 2. 下游：從 12,546 個檢體篩出 356 個

![下游五階段篩選](report/figures/fig02_downstream_filtering.png)

**做什麼**：公開大表裡有很多其他研究的檢體，要依條件一步步篩出本試驗、本時間窗、品質夠的檢體。

| 階段 | 條件 | 檢體 | ASV | 總讀序 |
|---|---|---:|---:|---:|
| 起點 | FigShare 全部檢體 | 12,546 | 17,865 | 550,243,459 |
| 1 | 屬於本試驗（有隨機分組） | 556 | 4,256 | 27,997,124 |
| 2 | 移植前 10 天到移植後 70 天 | 406 | 3,680 | 23,069,077 |
| 3 | 剔除只出現在 1 個檢體的 ASV | 406 | 2,458 | 22,972,681 |
| 4 | 剔除葉綠體、粒線體、無門級分類 | 406 | 2,425 | 22,909,139 |
| 5 | 剔除讀序 < 10,000 的檢體 | **356** | **2,422** | 22,692,526 |

- 最終 **24 位病人、356 個檢體**：對照組 10 人 150 個、auto-FMT 組 14 人 206 個；每人採檢 2–34 次（平均 14.8 次）。
- 第 3 步一口氣刪掉 1,222 個 ASV（少 33%），但讀序只少 0.42%：被刪的幾乎都是極稀有的序列。

**白話**：同一個病人被採了很多次，這點是後面所有統計方法選擇的關鍵。

---

### 3. 物種組成：移植後腸球菌暴增

![物種組成堆疊圖](report/figures/fig03_taxonomy_barplots.png)

**做什麼**：用 SILVA 分類器把每個 ASV 對到菌名，畫出各時期、各組的菌相組成。

**結果**

- 門層級：所有檢體平均以 **Bacillota（舊稱 Firmicutes）為主，約 84%**，其次是 Actinomycetota（5.7%）、Pseudomonadota（4.8%）。
- 科層級：**Enterococcaceae（腸球菌科）**在移植前平均只占 0.9%，移植期間 2.5%，**移植後升到 22.0%**；移植後的 225 個檢體中，有 48 個超過一半都是它。這是移植後常見的「單一菌種霸占」現象。
- 圖 3B：移植後，對照組的 Enterococcaceae 比例偏高；auto-FMT 組則有較多 Lachnospiraceae 等厭氧共生菌。

---

### 4. 稀釋曲線：10,000 條讀序夠不夠？

![稀釋曲線](report/figures/fig04_rarefaction_curves.png)

**做什麼**：多樣性指標會受定序深度影響，所以每個檢體要隨機抽到同樣深度（本次 10,000 條）再比較。稀釋曲線用來確認這個深度夠不夠。

**結果**

- Shannon 指數在第一個取樣深度（3,667 條）就已接近平台，10,000 條足夠。
- 在 10,000 條深度重複抽樣 10 次，Bray-Curtis 距離矩陣彼此的相關係數約 0.999，抽樣結果很穩定。
- 移植前的 Shannon 指數最高（中位數 4.56），移植期間（2.90）和移植後（2.49）明顯較低（取自稀釋曲線上的 11,000 條取樣點；曲線的取樣點是 3,667、7,333、11,000…，沒有剛好 10,000）。

---

### 5. Alpha 多樣性：哪些因素和菌相豐富度有關？

![Alpha 多樣性組間比較](report/figures/fig05_alpha_group_significance.png)

**做什麼**：以「觀察到的 ASV 數」（observed features）代表菌相豐富度，用 Kruskal-Wallis 檢定比較各分組。

| 比較 | 組別（檢體數） | H | q 值 |
|---|---|---:|---:|
| 移植時期 | 移植前（78）vs 移植後（225） | 70.58 | 1.3 × 10⁻¹⁶ |
| 移植時期 | 移植前（78）vs 移植期間（53） | 20.38 | 9.5 × 10⁻⁶ |
| 移植時期 | 移植期間（53）vs 移植後（225） | 8.51 | 0.0035 |
| 幹細胞來源 | 未處理骨髓（67）vs 未處理周邊血（128） | 21.20 | 2.5 × 10⁻⁵ |
| 幹細胞來源 | T 細胞去除（129）vs 未處理周邊血（128） | 18.86 | 4.2 × 10⁻⁵ |
| 糞便性狀 | 成形（97）vs 半成形（115） | 8.26 | 0.012 |
| 糞便性狀 | 成形（97）vs 水便（143） | 5.55 | 0.028 |
| FMT 時期 | FMT 期間（27）vs FMT 後（41） | 10.42 | 0.0037 |
| **治療分組** | **對照組（150）vs auto-FMT 組（206）** | **1.29** | **0.256** |

**白話**：移植後菌相豐富度大幅下降；但**把所有時間點混在一起比，兩組看不出差別**（最後一列）。這是下一節要用縱向模型的原因。

---

### 6. Beta 多樣性：菌相組成隨時間移動

![Beta 多樣性 PCoA 與 UMAP](report/figures/fig06_beta_pcoa_umap.png)

**做什麼**：計算檢體之間「菌相有多不像」，再壓到二維平面上看分群。

| 距離 | 考慮什麼 | PC1 | PC2 |
|---|---|---:|---:|
| Unweighted UniFrac | 有沒有這種菌＋親緣關係 | 20.4% | 6.3% |
| Weighted UniFrac | 菌的比例＋親緣關係 | 31.6% | 11.6% |
| Bray-Curtis | 菌的比例 | 13.9% | 10.7% |

**結果**：移植前的檢體集中在同一區；移植期間與移植後，群落中心明顯移開、散得更開。UMAP 依「移植後第幾週」著色，可以看到菌相隨時間連續移動。

---

### 7. 縱向分析：LME 與隨機森林

![LME 縱向模型](report/figures/fig07_lme_longitudinal.png)

**為什麼要縱向模型**：同一位病人有多個檢體，彼此不是獨立的；而且兩組的差別可能在「變化的速度」，而不是某個時間點的平均。線性混合效應模型（LME）以病人為隨機效應，檢定兩組豐富度隨時間的斜率。

| 參數 | 估計值 | 95% 信賴區間 | p 值 | 白話 |
|---|---:|---|---:|---|
| 截距（對照組在 FMT 當天） | 65.69 | 52.56–78.81 | < 0.001 | 對照組 Day 0 約 66 個 ASV |
| 組別（auto-FMT − 對照） | 2.96 | −14.38–20.31 | 0.738 | Day 0 兩組差不多 |
| 時間（對照組每天） | **−0.859** | −1.196 – −0.523 | < 0.001 | 對照組每天少約 0.86 個 ASV |
| **時間 × 組別** | **+0.560** | 0.104–1.015 | **0.016** | **auto-FMT 組下降得比較慢** |

24 位病人、356 個檢體；模型輸出註記 **未收斂（Converged: No）**，見〈解讀時要注意〉。

![隨機森林與菌群消長](report/figures/fig08_volatility_and_importance.png)

**隨機森林**：把屬層級的菌群比例聚合成 22 個核心菌屬，預測「移植後第幾週」。

- 預測效果：**R² = 0.319**（r = 0.565，p = 2.4 × 10⁻⁷）。
- 最重要的菌：

| 排名 | 菌群 | 重要性 |
|---:|---|---:|
| 1 | Enterococcaceae（腸球菌科，未分類屬） | 12.4% |
| 2 | *Clostridium* | 10.9% |
| 3 | Enterococcaceae *Incertae Sedis* | 8.9% |
| 4 | Lachnospiraceae（毛螺菌科，未分類屬） | 8.7% |
| 5 | Actinobacteria（未分類） | 7.7% |

- 圖 8C：Enterococcaceae 在 auto-FMT 組於移植後 1–3 週急升（多半還在回輸糞菌之前），對照組則到第 6 週才上升。
- 圖 8D：Lachnospiraceae 在兩組都於移植時跌到 5% 以下，之後逐漸回升。

> 注意：隨機森林預測的是**時間**，不是治療組別。這些菌代表「跟著移植時間起落的菌」，不是「auto-FMT 有效的指標」。

---

### 解讀時要注意

AI 報告的數字正確，但結論的用詞比證據強。下一單元寫論文時要改成合適的說法：

| 報告寫法 | 問題 | 比較恰當的說法 |
|---|---|---|
| 「auto-FMT 療效驗證」「證實顯著扭轉菌相崩跌」 | 只有 24 位病人；時間範圍跨過 FMT 前後，斜率差不等於 FMT 後回升；模型未收斂 | 「auto-FMT 組的豐富度下降斜率較緩（p = 0.016），需進一步驗證」 |
| 幹細胞來源、糞便性狀「顯著相關」 | 同一位病人的多個檢體被當成獨立樣本 | 註明檢體非獨立，屬探索性結果 |
| 隨機森林「辨識出核心指標菌群」 | 預測的是時間，不是組別 | 「與移植後時間相關的菌群」 |
| 「堅實的微生物組學實證」 | 單一資料集、單次稀釋抽樣 | 刪除 |

---

## 資料夾內容

```
05-ai-workshop-qiime2-analysis/
├── README.md                      本手冊
├── AGENTS.md                      AI 要遵守的規則（改名 GEMINI.md / CLAUDE.md 即可用）
├── input/sample-metadata.tsv      檢體資料表（12,546 個檢體 × 27 欄）
├── pipeline/
│   ├── Qiime2_Pipeline.sh         整套分析的 Slurm 腳本
│   └── job-570915.out / .err      本次執行紀錄
├── results/
│   ├── qzv/upstream/              上游圖表（拖進 view.qiime2.org 檢視）
│   ├── qzv/downstream/            下游圖表：篩選、物種組成、多樣性、LME、隨機森林
│   └── tables/                    從輸出檔抽出的關鍵數字（所有數字以這裡為準）
├── report/
│   ├── QIIME2_Analysis_Report.pdf AI 產出的 9 頁分析報告
│   └── figures/fig01–fig08.png    報告用的 8 張 300 DPI 圖
├── history/analysis-conversation.md   本次分析的對話紀錄（去識別化）＋數字核對
└── tools/extract_tables.py        從 .qza / .qzv 抽數字的程式
```

原始 FASTQ 與大型中間檔（.qza，共約 860 MB）沒有放進來，可用 Step 1 的連結重新下載。

---

## 下一步

分析做完了、報告也有了，但**一份分析報告還不是論文**。下一單元〈研究論文處理〉會帶著這些結果，和 AI 一起找文獻、做筆記、寫出一篇有引用的英文論文。
