# zhang2026bayesian

- **標題**：Bayesian Nonparametric Longitudinal Factor Model for Microbiome Counts
- **作者**：Shuangjie Zhang, Seoyeon Ok, Arul Jayaraman, Kirsten Landrock, Ivan Ivanov, Robert S. Chapkin, Yang Ni (2026)
- **檔案**：`papers/Zhang_2026_Bayesian-Nonparametric-Longitudinal-Factor-Model.pdf`
- **對應我們的研究**：限制 5（Kruskal-Wallis 等橫斷面方法把同一病人的重複採樣當成獨立樣本，違反時間相依性；且將所有時間點混在一起會掩蓋動態變化）、討論章節（零膨脹計數與跨特徵動態共變異）。

## 核心重點（別人做了什麼）
- 指出縱向菌相計數資料的統計挑戰：定序深度差異大、零值過多（excess zeros）、過度離散（overdispersed），且同一受試者的重複採樣具有受試者內時間相依性（within-subject temporal dependence），違反橫斷面分析的獨立性假設。
- 開發貝氏無母數縱向因子模型（LODI），結合取整對數常態潛在變數（處理離散計數與零值，不需依賴稀釋）、Dirichlet 過程混合（DPM）基線先驗，以及群組特定的自我迴歸 AR(1) 過程，分離受試者特定軌跡與跨菌種動態共變異。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 1 (Abstract)**:
  > "Modeling longitudinal microbiome data is challenging because microbiome counts are highly heterogeneous and zero-inflated, and, moreover, repeated measurements induce within-subject temporal dependence and possibly time-varying cross-feature covariance."

- **p. 2 (Introduction)**:
  > "Generally, microbiome count data present several well-known statistical difficulties. Sequencing depth varies substantially across samples, excess zeros arise from both biological absence and limited detection, nonzero counts are highly overdispersed, and the number of taxa may be comparable to or larger than the number of subjects (Paulson et al., 2013; Li, 2015). Longitudinal sampling introduces two additional challenges. First, repeated samples from the same subject are temporally dependent, violating the independence assumption used by many cross-sectional procedures."

- **p. 3 (Introduction)**:
  > "These methods provide useful cross-sectional estimates, but for longitudinal microbiome data, fitting them independently at each time point ignores temporal dependence, whereas pooling all time points together ignores changes in covariance over time."
