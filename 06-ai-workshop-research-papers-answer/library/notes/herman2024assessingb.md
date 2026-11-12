# herman2024assessingb

- **標題**：Assessing Engraftment Following Fecal Microbiota Transplant
- **作者**：Chloe Herman, Bridget M. Barker, Thais F. Bartelli, Vidhi Chandra, Rosa Krajmalnik-Brown, Mary Jewell, Le Li, Chen Liao, Florencia McAllister, Khemlal Nirmalkar, Joao B. Xavier, J. Gregory Caporaso (2024)
- **檔案**：`papers/Herman_2024_Assessing-Engraftment-Following-Fecal-Microbiota.pdf`
- **對應我們的研究**：前言（FMT 在 allo-HSCT 的應用）、限制 1 & 5（縱向重複測量與獨立性假設錯誤）、限制 6（Alpha 多樣性與時間預測不等於菌相植入評估）。

## 核心重點（別人做了什麼）
- 回顧 46 篇人類與模式生物的 FMT 研究，提出評估菌相植入（engraftment）的三大互補準則：（1）Chimeric Asymmetric Community Coalescence、（2）Donated Microbiome Indicator Features、（3）Temporal Stability。
- 明確指出：**僅靠 Alpha 多樣性（如豐富度 Observed Features）無法確認植入成功**，因為兩個樣本可以擁有完全相同的特徵數量卻沒有任何共同菌種（p. 7, p. 9）。
- 在「縱向統計（Longitudinal Statistics）」一節（p. 16）明確指出：同一受試者的重複測量違反獨立性假設，使用假設獨立的檢定是常見錯誤，且未配對同一受試者的檢體會降低統計檢定力（呼應我們 Q2 中混在一起做 Kruskal-Wallis 看不出差異，改用 LME 才看出斜率差）。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 2 (Abstract)**:
  > "Here we review 46 studies of FMT in humans and model organisms and group their approaches for assessing the extent to which an FMT engrafts into three criteria: 1) Chimeric Asymmetric Community Coalescence investigates microbiome shifts following FMT engraftment using methods such as alpha diversity comparisons, beta diversity comparisons, and microbiome source tracking. 2) Donated Microbiome Indicator Features tracks donated microbiome features (e.g., amplicon sequence variants or species of interest) as a signal of engraftment with methods such as differential abundance testing based on the current sample collection, or tracking changes in feature abundances that have been previously identified (e.g., from FMT or disease-relevant literature). 3) Temporal Stability examines how resistant post-FMT recipient’s microbiomes are to reverting back to their baseline microbiome."

- **p. 7 (Alpha Diversity limitations)**:
  > "Alpha diversity metrics generally do not capture what features are shared between the donated microbiome and the recipient. For example, two individuals can have the same alpha diversity metric value, but have no features in common."

- **p. 9 (Alpha Diversity vs Engraftment)**:
  > "Alpha diversity metrics are able to track a shift in microbiome richness and/or evenness, but similar metric values do not indicate that the same features are present. Thus, they can relate microbiome changes to treatment, but they do not provide specific information about the extent to which a microbiome has engrafted."

- **p. 16 (Longitudinal Statistics / Repeated Measures)**:
  > "Dependence of data is one of the biggest issues when it comes to analyzing longitudinal data. Many statistical tests assume that the data points are independent, and repeat measures from the same subject violate this assumption. This limits the statistical tests that can be applied, and using tests that assume independence is a common error. Further, comparing timepoints to each other without pairing samples from the same subject can reduce statistical power for assessing the impact of an FMT or other microbiome intervention."
