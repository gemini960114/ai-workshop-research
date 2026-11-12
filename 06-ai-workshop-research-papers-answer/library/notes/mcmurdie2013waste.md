# mcmurdie2013waste

- **標題**：Waste Not, Want Not: Why Rarefying Microbiome Data Is Inadmissible
- **作者**：Paul J. McMurdie, Susan Holmes (2013)
- **檔案**：`papers/McMurdie_2013_Waste-Not-Want-Not-Why.pdf`
- **對應我們的研究**：限制 4（本研究使用單次稀釋抽樣至 10,000 條讀序，不僅剔除了 50 個低於 10,000 讀序的檢體［406 → 356］，也丟棄了高深度檢體的大量讀序，並引入隨機抽樣誤差）。

## 核心重點（別人做了什麼）
- 從統計決策理論與模擬實驗證明，將菌相計數資料「稀釋抽樣至相同深度（rarefying）」在統計上是不可取的（inadmissible），因為它：（1）丟棄低於門檻的完整檢體、（2）丟棄高深度檢體中的大量有效讀序，導致型二錯誤率上升（失去統計檢定力）、（3）單次隨機不放回抽樣額外引入人工隨機變異、（4）需要主觀選擇最小讀數門檻 $N_{L,\min}$。
- 建議改用階層混合模型（如負二項分布 Gamma-Poisson 模型，DESeq2 / edgeR）或變異穩定轉換（variance-stabilizing transformation）來處理定序深度差異與過度離散。

## 可引用的原文（逐字抄錄並附頁碼）

- **p. 1 (Abstract)**:
  > "Regarding microbiome sample-wise clustering, we also show that the rarefying procedure often discards samples that can be accurately clustered by alternative methods."

- **p. 3 (Statistical motivation)**:
  > "Despite its current popularity in microbiome analyses rarefying biological count data is statistically inadmissible because it requires the omission of available valid data. This holds even if repeated rarefying trials are compared for stability as previously suggested [17]."

- **p. 11 (Results and Discussion, enumerated costs of rarefying)**:
  > "1. Rarefied counts represent only a small fraction of the original data, implying an increase in Type-II error – often referred to as a loss of power or decreased sensitivity (Table 1). In sample-wise comparisons, this lost power is evident through two separate phenomena, (1) samples that cannot be classified because they were discarded, (2) samples that are poorly distinguishable because of the discarded fraction of the original library (Figure 4)."
  > "3. Rarefying counts requires an arbitrary selection of a library size minimum threshold that affects downstream inference (Figure 4), but for which an optimal value cannot be known for new empirical data [17]."
  > "4. The random aspect of subsampling is unnecessary and adds artificial uncertainty (Protocol S2, minimal example, bottom)."
