# barrera2025stochastic

- **標題**：A stochastic method to estimate a zero-inflated two-part mixed model for human microbiome data
- **作者**：John Barrera, Cristian Meza, Ana Arribas-Gil (2025)
- **檔案**：`papers/Barrera_2025_stochastic-method-estimate-zero-inflated.pdf`
- **對應我們的研究**：限制 1（樣本不平衡與缺失）、限制 2（複雜混合效應模型在高度偏態/不平衡縱向菌相資料中容易發生數值最佳化不收斂或估計偏差，本研究 LME 出現 `Converged: No`）。

## 核心重點（別人做了什麼）
- 針對縱向人類菌相相對豐度資料中的零膨脹兩部分混合效應模型（Zero-Inflated Beta Regression, ZIBR），指出傳統最大概似估計（依賴數值優化與對數概似近似）常面臨**收斂不穩定（unstable convergence）**、參數估計偏差，以及無法直接處理不平衡資料（unbalanced data，即每位病人採樣次數不同）的問題。
- 提出基於隨機近似期望最大化演算法（Stochastic Approximation Expectation Maximization, SAEM）的精確最大概似估計框架，保證收斂性，並能直接處理臨床試驗常見的不平衡縱向採樣（如我們的 24 位病人每人有 2–34 個檢體）。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 1 (Abstract)**:
  > "However, as for other complex random effects models, maximum likelihood estimation suffers from the intractability of likelihood integrals. Available estimation methods rely on log-likelihood approximation, prone to limitations such as biased estimates or unstable convergence. In this work we develop an alternative maximum likelihood estimation approach for the ZIBR model, via the Stochastic Approximation Expectation Maximization (SAEM) algorithm. The proposed methodology can accommodate unbalanced data, not always possible in existing approaches."

- **p. 2 (Introduction)**:
  > "Moreover, the proposed ML implementation is suited only for balanced data, whereas clinical studies frequently yield unbalanced or missing observations, potentially leading to biased conclusions (Myers, 2000; Powney et al., 2014)."

- **p. 13 (Conclusions and discussion)**:
  > "A key advantage of the SAEM-based method is its ability to handle unbalanced data. This is essential in clinical studies, where dropout or irregular follow-up is frequent; yet the original ZIBR estimation method cannot accommodate such designs without prior interpolation."
