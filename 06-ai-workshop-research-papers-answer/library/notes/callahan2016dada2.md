# callahan2016dada2：DADA2: High-resolution sample inference from Illumina amplicon data

- **書目**：Callahan BJ et al., 2016, Nature Methods, 13(7):581–583, DOI 10.1038/nmeth.3869, PMID 27214047
- **檔案**：無 PDF（期刊論文，需自行從圖書館取得）
- **閱讀程度**：僅讀摘要

## 一句話摘要
DADA2 是開源軟體，能模擬並校正 Illumina amplicon 定序錯誤，精確推斷樣本中的序列，解析度可以到只差 1 個核苷酸。

## 研究問題
如何從 Illumina amplicon 定序資料中校正定序錯誤，精確推斷真實的樣本序列？

## 方法（摘要所述）
- 開發開源 R 套件 DADA2（https://github.com/benjjneb/dada2），用來模擬並校正 Illumina amplicon 定序錯誤。
- 用多個 mock community 和其他方法比較。
- 應用在一群孕婦的陰道樣本上。

## 主要發現（摘要所述）
- DADA2 能精確推斷樣本序列，分辨只差 1 個核苷酸的序列。
- 在多個 mock community 中，DADA2 找到的真實 variant 比其他方法多，產生的假序列比其他方法少。
- 在陰道樣本中發現多種先前沒偵測到的 Lactobacillus crispatus variant。

## 和我們研究的關係
- **Methods**：上游 41 個示範檢體以 DADA2 去噪（截斷 204 / 205 bp，`data/Qiime2_Pipeline.sh`；1,832,285 → 1,535,600 條讀序，`01_dada2_stats.tsv`）。可引用 DADA2 說明 ASV 的產生方式，以及它能分辨只差 1 個核苷酸的序列。
- 注意：本次流程的 DADA2 結果是預先算好再載入的，且上游 41 檢體與下游分析不承接；下游的特徵表來自公開資料，Methods 要寫清楚。

## 可引用的原文（摘要）
- > "We present the open-source software package DADA2 for modeling and correcting Illumina-sequenced amplicon errors (https://github.com/benjjneb/dada2)." (abstract)
- > "DADA2 infers sample sequences exactly and resolves differences of as little as 1 nucleotide." (abstract)
- > "In several mock communities, DADA2 identified more real variants and output fewer spurious sequences than other methods." (abstract)
