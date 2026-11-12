# herman2024assessing

- **標題**：Assessing microbiome engraftment extent following fecal microbiota transplant with q2-fmt
- **作者**：Chloe Herman, Evan Bolyen, Anthony Simard, Liz Gehret, J. Gregory Caporaso (2024)
- **檔案**：`papers/Herman_2024_Assessing-microbiome-engraftment-extent-following.pdf`
- **對應我們的研究**：前言（FMT 背景）、限制 6（本研究隨機森林僅預測時間，未直接量化供體菌叢植入程度［engraftment］，未來可在 QIIME 2 中使用 `q2-fmt` 評估社區聚合、供體指標特徵與時間穩定性）。

## 核心重點（別人做了什麼）
- 開發 QIIME 2 外掛 `q2-fmt`，將評估糞菌移植（FMT）菌叢植入程度（engraftment extent）的三大準則標準化為可重現的分析流程：
  1. **嵌合非對稱群落聚合（Chimeric Asymmetric Community Coalescence）**：利用 `qiime fmt cc` 追蹤受體菌相與供體（或自體移植前基線）的距離變化。
  2. **供體菌相指標特徵（Donated Microbiome Indicator Features）**：利用 `qiime fmt pedf`（供體特徵植入比例，PEDF）搭配置換檢定（`pedf-permutation-test`）以及 `detect-donor-indicators`（ANCOM-BC）找出真正從供體轉移並留存的特徵。
  3. **時間穩定性（Temporal Stability）**：透過縱向多個時間點追蹤上述指標是否穩定維持。
- 文中甚至直接以 Taur et al. (2018) 的 auto-FMT 癌症病人資料作為實例展示（Figure 1, p. 6）。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 1 (Abstract)**:
  > "We present q2-fmt, a QIIME 2 plugin that provides diverse methods for assessing the extent of microbiome engraftment following fecal microbiota transplant. The methods implemented here were informed by a recent literature review on approaches for assessing FMT engraftment, and cover aspects of engraftment including Chimeric Asymmetric Community Coalescence, Donated Microbiome Indicator Features, and Temporal Stability."

- **p. 1 (Introduction)**:
  > "Quantifying engraftment extent after FMTs is pivotal to interpreting the results of an FMT study. For example, if no positive clinical outcome is achieved, is it because FMT is not a relevant treatment option for the condition, or because the microbiome didn’t successfully engraft?"

- **p. 2 (Proportional Engraftment of Donor Features)**:
  > "qiime fmt pedf uses microbiome feature tables (QIIME 2 semantic type: FeatureTable) as input and calculates the number of donor features observed in each recipient sample divided by the total number of donor features."

- **p. 6 (Figure 1 caption, applying q2-fmt to Taur et al. 2018 auto-FMT data)**:
  > "Since this is an autoFMT study, the ‘donor’ is the recipient before cancer treatment. This figure shows that spontaneous recovery from cancer treatment leads to some individuals recovering quickly while others do not. The FMT intervention decreases the variability in distance to donor of all recipients."
