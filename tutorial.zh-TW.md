# 提示詞速查表

> 🌐 **語言**：[English](tutorial.md) | 繁體中文

七個單元會用到的自然語言 prompt，照上課順序排好，直接複製貼給 AI Agent 即可。
詳細說明與預期結果請看各單元的 README。

> 每個單元都要用 **Open Folder** 打開「該單元的資料夾」，不要打開外層的 `ai-workshop-research`。

---

## 00 雲端 vs 地端

資料夾：`00-ai-workshop-openai/`

**三個問題**（雲端、地端都問同樣的問題）

```text
這篇論文標題寫的『wet-lab science（濕式實驗室科學）』是什麼意思？AI 為什麼要去處理實驗室的事？
```

```text
裡面說考了 AI 100 道實驗室題目，都是考些什麼？是考選擇題還是看圖題？請做成簡單的表格給我看。
```

```text
我是一個剛進生物實驗室的研究生，我應該怎麼安全地用 AI 幫我檢查實驗數據，才不會被它誤導？
```

**存成 Word 報告**

```text
幫我整理上述的討論問題與回覆內容, 存成一份word 報告 report.docx
```

**換 Gemini 檢核**

```text
report.docx是 ai agent 根據 measuring-how-ai-agents-handle-wet-lab-science.pdf 的問題與回覆內容, 請確認是否正確
```

```text
根據您的建議進行修改 另儲存為新檔名
```

---

## 01 Antigravity 入門

資料夾：自己新建的空資料夾，例如 `my-first-project`

**安裝必要工具**（裝完要關掉 Antigravity 再重開）

```text
請幫我安裝 Git、uv 和 Node.js。已經裝好的就跳過，有失敗的告訴我原因，最後列出每個工具的版本。
```

**安裝建議工具**

```text
請幫我安裝 GitHub CLI、LibreOffice 和 ffmpeg。已經裝好的就跳過，有失敗的告訴我原因，最後列出每個工具的版本。
```

**課堂電腦：只確認、不安裝**

```text
請告訴我這台電腦上 git、gh、uv、node、npm、ffmpeg 和 LibreOffice（soffice）的版本。
找不到的請列出來，先不要安裝。
```

**第一個網頁**

```text
在這個資料夾建立一個 hello.html，用大字顯示「Hello Antigravity」和今天的日期，然後幫我用瀏覽器打開。
```

**記憶翻牌遊戲**（另開資料夾 `my-second-project`）

```text
在這個資料夾幫我用最簡單的 Vite + JS 做一個「記憶翻牌」遊戲：
總共 16 張牌隨機排列，翻到相同的兩張就消除，上方顯示步數和計時。
全部消除後顯示「恭喜完成」和「重新開始」按鈕，介面用繁體中文。
做完後直接幫我把網頁跑起來，給我網址讓我可以點開玩。
```

**想多玩一點**：「牌面改成水果圖案」「加一個最佳紀錄」「改成 20 張牌」；不玩了就說「停止開發伺服器」。

**附錄：其他工具（選用）**

```text
請幫我安裝 pandoc、ripgrep、jq、ImageMagick，再用 uv 安裝 yt-dlp。
已經裝好的就跳過，有失敗的告訴我原因，最後列出每個工具的版本。
```

---

## 02 前端設計

資料夾：`02-ai-workshop-frontend-design/`
開始前先在終端機安裝 skill，裝好後重新開啟 AI 對話（指令見單元 README）。

**範例 1：品牌產品頁**

```text
在目錄 output/case01/ 中，幫我做一個台灣手工茶葉品牌「山嵐茶研所」的單頁官網（HTML + CSS），主頁面存成 output/case01/index.html。
受眾是 30–50 歲重視產地與職人精神的消費者。
需要：品牌故事、三款茶品介紹、產地地圖區、訂購按鈕。
不要用常見的 SaaS 模板風格，請先提出 2 個美學方向讓我選。
```

**範例 2：記憶翻牌，和單元 01 比一比**

```text
在目錄 output/case02/ 幫我用最簡單的 Vite + JS 做一個「記憶翻牌」遊戲：
總共 16 張牌隨機排列，翻到相同的兩張就消除，上方顯示步數和計時。
全部消除後顯示「恭喜完成」和「重新開始」按鈕，介面用繁體中文。
做完後直接幫我把網頁跑起來，給我網址讓我可以點開玩。
```

**確認有沒有用到 skill**（每個範例做完都可以問）

```text
在這個 Case 你使用了哪些 Skills
```

---

## 03 Office 文件處理

資料夾：`03-ai-workshop-office-skills/`
開始前先在終端機安裝 docx、pdf、pptx、xlsx 四個 skill（指令見單元 README）。四個範例要依序做，前一個的產出是下一個的輸入。

**範例 1（xlsx）：CSV → Excel**

```text
把 example/臺灣採購經理人指數(pmi及nmi).csv 做成 Excel，存成 output/pmi.xlsx：
第一個工作表放原始資料，第二個工作表算出每年的 PMI、NMI 平均，並加上歷年走勢的折線圖。
```

**範例 2（pptx）：Excel → 動畫簡報**

```text
根據 output/pmi.xlsx 做一份 5 頁的簡報，存成 output/pmi.pptx，說明臺灣採購經理人指數的意義、近年走勢與重點觀察，要有圖表。

文字都要能在 PowerPoint 裡編輯（不要做成圖片）。

每頁內容用卡片（圓角方塊）排版，標題直接顯示。卡片依序逐一出現。每按一下，只讓下一張卡片以淡入效果出現；播放開始時卡片先隱藏。背景與裝飾元素不需動畫。

換頁用淡入效果，慢一點。要講者備註。
```

**範例 3（docx）：Excel → Word 報告**

```text
根據 output/pmi.xlsx 寫一份 Word 分析報告，存成 output/pmi-report.docx：
要有封面、自動目錄，章節分成「指標說明」「歷年走勢」「近一年觀察」「結論」，
「歷年走勢」放年度平均的表格與折線圖。
```

**範例 4（pdf）：Word → 上課講義 PDF**

```text
把 output/pmi-report.docx 用 LibreOffice 轉成 PDF，存成 output/pmi-report.pdf：
每頁下方加上頁碼，並加上淡灰色「課堂講義」浮水印。
```

（沒有 LibreOffice 時，把「用 LibreOffice」改成「用 Word」。）

---

## 04 核銷憑證登錄 Excel：建立自己的 Skill

資料夾：`04-ai-workshop-voucher-ocr/`
想從頭體驗 Step 1–5，先把 `.claude/skills/voucher-to-excel` 移到別處，或在每句話前加「先不要使用任何 skill」。

**Step 1：先讓 AI 看懂要做什麼**

```text
先把 record.example.xlsx 複製成 record.xlsx。example_deid 資料夾有五份發票的 PDF，你先看一下 Excel 要填哪些東西，PDF 裡面找得到嗎？
```

**Step 2：先約定標示規則**

```text
缺少的資料還是要保留欄位，找不到的請用黃色螢光標示，你不確定的請用藍色螢光背景，並在儲存格加註解說明原因。也請在 Excel 最上方找個合適的地方，註解這兩種顏色代表的意義。
```

**Step 3：先做一筆**

```text
先做第一張 example_deid/SKM_650i25101515330_deid.pdf 就好，我要確認是否正確。
```

**Step 4：填入其餘四張**

```text
第一筆我核對過沒問題，請把剩下的四張 PDF 也照同樣的規則填入 record.xlsx，填完後列出結果，並說明每個黃色、藍色格子的原因。
```

**Step 5：把流程做成 skill**

```text
之後我會再上傳新的 PDF 發票和收據，希望我只要說「請幫我把這幾筆資料填入 excel」，你就能照今天的流程自動處理。請把今天確認過的做法整理成一個 skill，包括每個欄位要從 PDF 哪裡讀、黃色和藍色的標示規則、怎麼核對金額。也請幫這個 skill 取個名字，並給我幾個平常可以怎麼跟你說的使用範例。
```

**Step 6：開新對話，一句話搞定**（先刪掉 `record.xlsx`）

```text
example_deid 裡有五張新的發票 PDF，幫我把這幾筆資料填入 excel
```

其他說法：

- 「新的收據來了，先做一筆讓我確認，沒問題再做剩下的」
- 「把 example_deid 裡還沒登錄的 PDF 都填進去」
- 直接輸入 `/voucher-to-excel`

**用對話校正規則**

```text
為什麼發票抬頭都標藍？這批練習資料的買受人是財團法人未來科技研究院智慧雲端運算中心，統編 81924865，請把它也加進 skill 的規則，之後不用再標藍。
```

```text
藍色的區塊我看都是正確的，你為何沒有把握？
```

**加碼：一個做、一個審**（先刪掉 `record.xlsx`）

Gemini 負責做：

```text
先複製 record.example.xlsx 為 record.xlsx
幫我辨識 example_deid/SKM_650i25101515330_deid.pdf example_deid/SKM_650i25101515331_deid.pdf example_deid/SKM_650i25101515340_deid.pdf example_deid/SKM_650i25101515341_deid.pdf example_deid/SKM_650i25101515350_deid.pdf 填入 record.xlsx
```

Claude 負責審：

```text
我已將 example_deid/ 裡的 SKM_650i25101515330_deid.pdf、SKM_650i25101515331_deid.pdf、SKM_650i25101515340_deid.pdf、SKM_650i25101515341_deid.pdf、SKM_650i25101515350_deid.pdf 的發票內容擷取到 record.xlsx，請幫我比對 PDF 與 Excel，確認是否正確。
```

---

## 05 QIIME 2 腸道菌相分析（國網 HPC）

位置：HPC 上自己的工作資料夾，先放入 `AGENTS.md`（改名為 `GEMINI.md` 或 `CLAUDE.md`）。
計畫代號 `MST109178` 是示範用的，請換成自己的計畫代號。

**Step 1：下載資料**

```text
下載 https://drive.usercontent.google.com/download?id=1JXGPT2bhLJvOnpTY9-oYBKxvZ45M0qPN&export=download&authuser=1 解壓縮
```

**Step 2：確認計畫帳號與佇列**

```text
我的帳號可以使用哪些計畫？應該是 MST109178？
```

```text
改為 MST109178，然後 ngscourse8g 這個夠用嗎？還是要用 ngs62g，CPU 數量也增加？
```

**Step 3：派送作業、定時回報**

```text
直接派送就可以了
```

```text
每五分回報一次進度
```

**Step 4：產出分析報告**

```text
幫我產出一份 PDF 報告，裡面請針對每一個分析進行分段報告，並加上相對應的分析圖檔，你可以自己處理，然後最後做總結、結論
```

---

## 06 研究論文處理

資料夾：`06-ai-workshop-research-papers/`（參考答案在 `06-ai-workshop-research-papers-answer/`）

**Step 1：讀研究摘要卡**

```text
請閱讀 manuscript/00-research-brief.md，並對照 data/tables/ 確認數字，用白話告訴我：這篇論文要回答什麼問題、答案是什麼、有哪些限制、要去找哪些文獻。
```

**Step 2：找文獻，建立文獻庫**

```text
請用 arxiv skill，依照 manuscript/00-research-brief.md 的搜尋關鍵字找相關論文，列出候選清單給我挑選，並用 ★ 標出最推薦的幾篇，先不要下載。
```

```text
請用 paper-library skill 收錄所有標註 ★ 推薦的 arXiv 論文。
```

（也可以說「收錄第 1、3、5 篇」；結果混進不相關的論文時，請 AI「改用 `abs:microbiome AND abs:longitudinal` 這種語法重新搜尋」。）

```text
請用 paper-library skill，用 DOI 登錄 Taur 2018 原始試驗、QIIME 2、DADA2、SILVA 這 4 篇論文。
```

**Step 3：做筆記、文獻比較表**

```text
請讀 papers/ 的每篇論文，在 library/notes/ 幫每篇寫一份筆記，要附上可以引用的原文和頁碼。只有 DOI、沒有 PDF 的論文，改讀摘要並在筆記標註「僅讀摘要」。
```

```text
請根據 library/notes/ 的筆記和 manuscript/00-research-brief.md 的研究限制，整理一份文獻比較表：別人做了什麼、我們缺什麼，存成 library/literature-matrix.md。
```

**Step 4：依序寫論文**（每寫完一節，先看過再寫下一節）

```text
請用 arxiv-preprint skill 在 manuscript/ 建立英文論文架構，每一節一個檔案放在 sections/。
```

```text
請參考 research-paper-writing skill，用英文寫 Methods。
```

```text
請寫 Results，只描述數據，不要解釋。需要的圖請依 data/tables/ 重畫。
```

```text
請寫 Introduction。
```

```text
請依照文獻比較表寫 Discussion，包含研究限制和結論。
```

```text
請寫結構化摘要。
```

```text
請提出 3 個候選標題，說明你推薦哪一個。
```

```text
採用候選標題 1。請補上論文最後的聲明段落，作者貢獻、利益衝突、經費先留空，由作者填寫。
```

**Step 5：核對引用、輸出 PDF**

```text
請用 arxiv-preprint skill 檢查並編譯論文，告訴我檢查結果。
```

本機有 LaTeX 時也可以：

```text
請先用 which pdflatex 確認本機的 LaTeX，再用本機的 pdflatex + bibtex 直接編譯 manuscript/main.tex 產出 main.pdf，有錯誤就修正後重新編譯，並告訴我 PDF 有幾頁、有沒有警告。
```

```text
請逐句核對論文中的每一個引用，原文有沒有支持這句話；再把論文裡的每一個數字對回 data/tables/。整理成 manuscript/citation-check.md。
```

**換成自己的研究資料時**

```text
請根據 data/tables/ 的結果，整理一份研究摘要卡，包含問題、答案、數字來源、研究限制和搜尋關鍵字，存成 manuscript/00-research-brief.md。
```

```text
把這個數字對回 data/tables/ 的原始檔
```
