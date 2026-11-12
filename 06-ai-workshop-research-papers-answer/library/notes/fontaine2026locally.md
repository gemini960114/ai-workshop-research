# fontaine2026locally

- **標題**：Locally sparse varying coefficient mixed model with application to longitudinal microbiome differential abundance
- **作者**：Simon Fontaine, Nisha J. D'Silva, Marcell Costa de Medeiros, Grace Y. Chen, Ji Zhu, Gen Li (2026)
- **檔案**：`papers/Fontaine_2026_Locally-sparse-varying-coefficient-mixed.pdf`
- **對應我們的研究**：方法依據、限制 3（我們的 LME 將整個跨越 FMT 前後的觀察期假設為單一固定斜率，無法區分哪個時間區間真正發生組間差異；改用局部稀疏時變係數混合模型［LSVCMM］可自動找出有顯著差異的特定時間區間，並處理不規則採樣與序列相關）。

## 核心重點（別人做了什麼）
- 提出局部稀疏時變係數混合效應模型（Locally Sparse Varying Coefficient Mixed Model, LSVCMM），結合核平滑（kernel smoothing）、自适应稀疏群組 Lasso（adaptive sparse group Lasso）與參數化工作共變異數矩陣（parametric working covariance，如隨機截距或 AR(1)）。
- 解決縱向菌相分析的五大需求：（1）效應隨時間平滑變化（時變係數 $\beta(t)$，而非固定斜率）、（2）考慮受試者內的時間序列相關、（3）直接容許不規則採樣時間點與缺失資料（無須插補）、（4）同時具備全域稀疏性（哪個特徵有差）與局部稀疏性（在哪個時間區間有差）、（5）支援交互作用與共變數調整。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 1 (Summary)**:
  > "To study DA in longitudinal microbial studies, we introduce a novel varying coefficient mixed-effects model with local sparsity. The proposed method can identify time intervals of significant group differences while accounting for temporal dependence. Specifically, we exploit a penalized kernel smoothing approach for parameter estimation and include a random effect to account for serial correlation. In particular, our method operates effectively regardless of whether sampling times are shared across subjects, accommodating irregular sampling and missing observations."

- **p. 2–3 (Introduction, desirable properties of longitudinal microbiome models)**:
  > "Second, the longitudinal nature of the data implies serial correlation within subjects, and failure to account for it may hinder the statistical properties of the method. Third, accomodating irregular designs demands a methodology that does not require all subjects to be measured at a common set of time points. Indeed, many studies have missing data, or samples may be collected irregularly in observational studies. Fourth, the methodology must be able not only to identify if there is a difference between conditions (global differences), but it must also determine the time interval(s) where the difference occurs (local differences)."

- **p. 15–16 (Discussion)**:
  > "LSVCMM addresses two main deficiencies in existing sparse VCM methodologies. First, it includes longitudinal effects in the form of a parametric working covariance model, whereas many methods cannot account for within-subject dependencies (Wang and Kai, 2015; Kong et al., 2015; Tu et al., 2020; Zhong et al., 2022). Simulation experiments in Section 3 have shown that omitting the dependency leads to worse estimation accuracy and worse support recovery in the densely sampled regime."
