# zhou2021linda

- **標題**：LinDA: linear models for differential abundance analysis of microbiome compositional data
- **作者**：Huijuan Zhou, Kejun He, Jun Chen, Xianyang Zhang (2021)
- **檔案**：`papers/Zhou_2021_LinDA-linear-models-differential-abundance.pdf`
- **對應我們的研究**：限制 5（將重複測量當成獨立樣本會造成嚴重的偽陽性 FDR 膨脹，而引入隨機截距的線性混合效應模型能控制 FDR 並提升檢定力）、限制 6 & 討論章節（菌相定序資料本質為組成資料［compositional data］，使用無偏差校正的相對豐度或機器學習特徵重要性無法直接等同於絕對豐度變化）。

## 核心重點（別人做了什麼）
- 指出定序實驗只能測量相對豐度（組成資料，compositional data），總讀數（library size）不反映真實微生物總量；某個菌種絕對豐度增加會連帶改變所有其他菌種的相對豐度（compositional effects），直接套用 t 檢定、Wilcoxon/Kruskal-Wallis 或一般線性迴歸會導致大量偽陽性。
- 提出 `LinDA`（Linear models for Differential Abundance analysis）：先對豐度資料進行中心對數比轉換（CLR transformation），再透過線性迴歸或**線性混合效應模型（LMM，針對縱向/重複測量資料）**配適，最後利用各菌種迴歸係數的眾數（mode）校正組成偏差（bias correction）。
- 在重複採樣模擬與真實資料中證明：若把同一受試者的重複檢體當成獨立樣本（OLS），會造成嚴重的 FDR 膨脹；而納入受試者隨機截距的 `LinDA-LMM` 能有效控制 FDR 並藉由利用受試者內相關性大幅提升檢定力（呼應我們 Q2 從 Kruskal-Wallis 到 LME 的核心論點）。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 1 (Abstract)**:
  > "Differential abundance analysis is at the core of statistical analysis of microbiome data. The compositional nature of microbiome sequencing data makes false positive control challenging. Here, we show that the compositional effects can be addressed by a simple, yet highly flexible and scalable, approach. The proposed method, LinDA, only requires fitting linear regression models on the centered log-ratio transformed data, and correcting the bias due to compositional effects. We show that LinDA enjoys asymptotic FDR control and can be extended to mixed-effect models for correlated microbiome data."

- **p. 2–3 (Background, compositional effects)**:
  > "However, the data from a sequencing experiment only captures the relative abundance (compositional) information since the total sequence read count, also known as sequencing depth or library size, does not reflect the total microbial load in the specimen due to the complex chemistry involved in sequencing [6, 7]."
  > "The increase or decrease in the abundance of some taxa with respect to a covariate of interest automatically results in changes in the relative abundances of all other taxa, a statistical phenomenon known as compositional effects. Therefore, using the standard statistical techniques such as two-sample t-test, Wilcoxon rank sum test, and linear regression analysis ignoring the compositional nature of the data could lead to a large number of false discoveries."

- **p. 11 (Results, correlated/repeated-measurement microbiome data)**:
  > "In addition, LinDA-LMM is more powerful than LinDA-OLS due to its ability to exploit the correlation between pre- and post-treatment samples. Under the replicate sampling setting (S8.2, Additional file 2: Fig. S14), we see that the LinDA-OLS has significant FDR inflation by treating the replicate samples as independent ones. In contrast, LinDA-LMM controls the FDR at the target level."

- **p. 15 (Discussion, rarefaction trade-off)**:
  > "Although rarefaction controls the effect of uneven library sizes, it discards a significant portion of the reads and thus loses much information in the data. When there are many samples with small library sizes, the users have to decide whether to retain more reads or more samples."
