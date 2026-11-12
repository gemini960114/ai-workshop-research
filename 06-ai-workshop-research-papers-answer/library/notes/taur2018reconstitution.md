# taur2018reconstitution：Reconstitution of the gut microbiota of antibiotic-treated patients by autologous fecal microbiota transplant

- **書目**：Taur Y et al., 2018, Science Translational Medicine, 10(460):eaap9489, DOI 10.1126/scitranslmed.aap9489, PMID 30257956
- **檔案**：無 PDF（期刊論文，需自行從圖書館取得）
- **閱讀程度**：僅讀摘要

## 一句話摘要
在 allo-HSCT 病人身上進行 auto-FMT 對照無介入的隨機對照試驗，摘要指出 auto-FMT 提升了腸道菌相 diversity，並讓菌相組成回到病人在抗生素治療與移植之前的狀態。

## 研究問題
allo-HSCT 期間必要的抗生素會破壞腸道菌相 diversity，而 diversity 流失與死亡率上升有關。能否用病人自己先前保存的糞便（autologous FMT）把流失的共生菌補回來？

## 方法（摘要所述）
- 隨機對照臨床試驗：auto-FMT 對照無介入（摘要沒寫試驗編號；NCT02269150 來自我們自己的資料，不是摘要內容）。
- 分析 25 位 allo-HSCT 病人的腸道菌相 profile：14 位接受 auto-FMT，11 位為 control。
- 比較腸道菌相 diversity 與組成的變化。（摘要沒有交代定序方法與統計方法。）

## 主要發現（摘要所述）
- auto-FMT 提升了 microbial diversity。
- auto-FMT 讓腸道菌相組成回到病人在抗生素治療與 allo-HSCT 之前的狀態。
- 作者據此認為糞便檢體預存（fecal sample banking）、治療後再回輸是可行方向。

## 和我們研究的關係
- **Introduction**：allo-HSCT 期間的抗生素破壞腸道菌相 diversity，diversity 流失與死亡率上升有關；auto-FMT 是重建菌相的介入方式。
- **Methods**：我們重新分析的資料來自這個 auto-FMT 對照無介入的隨機對照試驗（資料經 QIIME 2 官方教學公開；試驗編號 NCT02269150 來自我們的資料說明，不是摘要內容）。
- **Discussion**：原研究摘要指出 auto-FMT 提升 diversity；我們的全期 Kruskal-Wallis 沒有組間差異（p = 0.256，`02_kruskal_autoFmtGroup.tsv`），縱向 LME 的 day × group 交互作用為 +0.560/天（p = 0.016，`03_lme_model_results.tsv`），方向一致，但差異表現在斜率而非單一時間點。比較時要註明原研究分析 25 位病人，我們是篩選後的 24 位、356 個檢體。
- 不能用摘要支持的說法：特定 diversity 指標、效果量、p 值、取樣時間點、臨床結果。

## 可引用的原文（摘要）
- > "We have initiated a randomized, controlled clinical trial of autologous fecal microbiota transplantation (auto-FMT) versus no intervention and have analyzed the intestinal microbiota profiles of 25 allo-HSCT patients (14 who received auto-FMT treatment and 11 control patients who did not)." (abstract)
- > "Changes in gut microbiota diversity and composition revealed that the auto-FMT intervention boosted microbial diversity and reestablished the intestinal microbiota composition that the patient had before antibiotic treatment and allo-HSCT." (abstract)
- > "Although gut microbiota diversity loss during allo-HSCT is associated with increased mortality, approaches to reestablish depleted commensal bacteria have yet to be developed." (abstract)
