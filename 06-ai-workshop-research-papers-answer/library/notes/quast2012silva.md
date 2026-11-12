# quast2012silva：The SILVA ribosomal RNA gene database project: improved data processing and web-based tools

- **書目**：Quast C et al., 2013（2012 年 11 月線上先行發表，所以 citekey 是 2012；PubMed 記錄的期別年份是 2013），Nucleic Acids Research, 41(Database issue / D1):D590–D596, DOI 10.1093/nar/gks1219, PMID 23193283
- **檔案**：無 PDF（期刊論文，需自行從圖書館取得）
- **閱讀程度**：僅讀摘要

## 一句話摘要
SILVA 是提供經過品質控管、已比對（aligned）的 Bacteria、Archaea、Eukaryota rRNA 基因序列資料庫的網路資源；這篇描述 release 111 的新功能，以及它作為次世代定序資料分類參考的用途。

## 研究問題
如何提供最新、經品質控管的 rRNA 基因序列資料庫與 taxonomy，作為高通量定序資料分類的參考？

## 方法（摘要所述）
- 維護 Bacteria、Archaea、Eukaryota 三域的 aligned rRNA gene sequence 資料庫與線上服務。
- 新功能包括：進階品質控管流程、改良的 rRNA gene aligner、評估 probe 與 primer 的線上工具，以及更好用的網站瀏覽、搜尋與下載。
- 經大量人工整理的 SILVA taxonomy，以及新的 non-redundant 資料集。

## 主要發現（摘要所述）
- Release 111（2012 年 7 月）收錄 3,194,778 條 small subunit 與 288,717 條 large subunit rRNA 基因序列。
- 作者表示，SILVA taxonomy 與 non-redundant 資料集很適合作為次世代定序資料高通量分類的參考。

## 和我們研究的關係
- **Methods**：我們用 SILVA 138.2（515F/806R 區段）預訓練分類器做物種分類（`data/Qiime2_Pipeline.sh`），這篇是 SILVA 資料庫的標準引用文獻。
- 注意：摘要描述的是 release 111，我們用的是 138.2；摘要裡的序列數量不能套到我們用的版本。

## 可引用的原文（摘要）
- > "SILVA (from Latin silva, forest, http://www.arb-silva.de) is a comprehensive web resource for up to date, quality-controlled databases of aligned ribosomal RNA (rRNA) gene sequences from the Bacteria, Archaea and Eukaryota domains and supplementary online services." (abstract)
- > "Furthermore, the extensively curated SILVA taxonomy and the new non-redundant SILVA datasets provide an ideal reference for high-throughput classification of data from next-generation sequencing approaches." (abstract)
