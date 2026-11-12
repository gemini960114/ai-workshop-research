# 研究摘要卡：從分析結果到論文

> 來源：上一單元〈QIIME 2 腸道菌相分析〉的輸出。**所有數字以 `data/tables/` 為準**；`data/QIIME2_Analysis_Report.pdf` 是 AI 產生的報告，數字正確但用詞過強，只作參考。

## 研究背景

- 異體造血幹細胞移植（allo-HSCT）前的化療與抗生素會嚴重破壞腸道菌相；菌相多樣性下降的病人，移植相關死亡率較高。
- 自體糞菌移植（auto-FMT）：化療前先保存病人自己的糞便菌叢，移植後再放回去，希望重建菌相。
- 資料：QIIME 2 官方教學使用的臨床試驗 NCT02269150 公開資料（隨機分為 auto-FMT 組與對照組）。

## 三個問題與答案

| 問題 | 答案 | 關鍵數字 | 來源 |
|---|---|---|---|
| **Q1** 移植過程中，腸道菌相怎麼變化？ | 豐富度大幅下降，腸球菌趁機霸占 | 移植前 vs 後 Kruskal-Wallis H = 70.58，q = 1.3 × 10⁻¹⁶；腸球菌科平均占比 移植前 0.9% → 移植後 22.0%；移植後 225 個檢體中 48 個超過一半是腸球菌 | `02_kruskal_categorical-time-relative-to-hct.tsv`；`taxa-bar-plots-1.qzv`（上一單元 `results/qzv/`） |
| **Q2** auto-FMT 組和對照組不同嗎？ | 混在一起比沒有差別；縱向模型中 auto-FMT 組下降得比較慢 | 全期 Kruskal-Wallis H = 1.29，p = 0.256；LME 對照組 −0.859 / 天（95% CI −1.196 至 −0.523，p < 0.001）；交互作用 +0.560 / 天（95% CI 0.104 至 1.015，p = 0.016）；組別主效應 +2.96（p = 0.738） | `02_kruskal_autoFmtGroup.tsv`；`03_lme_model_results.tsv` |
| **Q3** 哪些菌跟著移植時間起落？ | 主要是腸球菌科和毛螺菌科 | 隨機森林預測移植後週數 R² = 0.319（r = 0.565，p = 2.4 × 10⁻⁷）；重要性 Enterococcaceae 0.124、*Clostridium* 0.109、Enterococcaceae *Incertae Sedis* 0.089、Lachnospiraceae 0.087 | `04_rf_accuracy.tsv`；`04_rf_feature_importance.tsv` |

## 樣本與方法（寫 Methods 用）

| 項目 | 內容 | 來源 |
|---|---|---|
| 篩選 | 12,546 → 556（本試驗）→ 406（移植前 10 天至後 70 天）→ 406（ASV ≥ 2 檢體）→ 406（排除葉綠體、粒線體）→ **356 個檢體、2,422 個 ASV** | `00_filtering_funnel.tsv` |
| 病人 | 24 位（對照 10 人 150 檢體；auto-FMT 14 人 206 檢體）；每人 2–34 個檢體，平均 14.8 | `03_lme_model_summary.tsv`、`02_kruskal_autoFmtGroup.tsv` |
| 上游示範 | 41 個檢體 DADA2 去噪：1,832,285 → 1,535,600 條讀序（83.8%），660 個 ASV；**與下游資料不承接** | `01_dada2_stats.tsv`、`00_filtering_funnel.tsv` |
| 軟體與參數 | QIIME 2 2026.7；SILVA 138.2（515F/806R）分類器；稀釋深度 10,000；LME：observed_features ~ day-relative-to-fmt × autoFmtGroup，病人為隨機截距 | `data/Qiime2_Pipeline.sh` |
| Beta 多樣性 | PC1 解釋變異：Unweighted UniFrac 20.4%、Weighted UniFrac 31.6%、Bray-Curtis 13.9% | `05_pcoa_proportion_explained.tsv` |

## 論文定位

**同一份資料，混在一起比看不出差別（Q2 前半），縱向模型才看得到斜率差（Q2 後半）。**
論文定位為「縱向分析方法的示範與再分析」，不是新的療效結論。

## 研究限制（要去文獻找對應的討論與更好的做法）

1. **樣本小**：只有 24 位病人，信賴區間寬（交互作用 0.104 至 1.015）。
2. **LME 未收斂**：模型輸出註記 `Converged: No`（`03_lme_model_summary.tsv`），結果需謹慎解讀。
3. **時間跨過 FMT 前後**：交互作用是整段觀察期的斜率差，不等於「FMT 後回升」；分段（piecewise）或時變係數模型更貼近問題。
4. **單次稀釋抽樣**：豐富度來自稀釋到 10,000 條讀序的一次抽樣；稀釋的適當性有爭議。
5. **檢體不獨立**：Kruskal-Wallis 把同一病人的多個檢體當成獨立樣本。
6. **隨機森林預測的是時間**：重要特徵代表「跟著時間變化的菌」，不是療效標記；且未評估菌相移植（engraftment）。

## 搜尋關鍵字（給 arxiv skill）

| 面向 | 搜尋式 | 用在 |
|---|---|---|
| FMT 與菌相移植評估 | `abs:microbiome AND abs:transplant` | 前言、限制 6 |
| 縱向菌相模型 | `abs:microbiome AND abs:longitudinal AND abs:mixed` | 方法依據、限制 2、3 |
| 重複測量 | `abs:microbiome AND abs:"repeated measures"` | 限制 5 |
| 稀釋爭議 | `abs:microbiome AND abs:rarefying` | 限制 4 |
| 組成資料、零膨脹 | `abs:microbiome AND abs:compositional` | 討論 |

arXiv 上沒有的期刊論文，改用 DOI 登錄：原始試驗（Taur et al. 2018，Sci Transl Med）、QIIME 2（Bolyen et al. 2019）、DADA2、SILVA。
