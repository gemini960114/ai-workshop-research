# 讓 AI Agent 和你一起做研究

> 🌐 **語言**：[English](README.md) | 繁體中文

**從文獻整理、論文撰寫，到建立自己的 Skill。**

把 AI Agent 請進你的電腦和你的資料夾：用中文對話，請它讀論文、整理報告、在國網 HPC 上跑分析、找文獻寫成英文論文，最後把做對的流程存成自己的 Skill，下次一句話就能重複使用。

> 📖 **線上課程網站**：<https://gemini960114.github.io/ai-workshop-research/zh-TW/>（含各單元簡報下載與教學影片）

## 下載課程

```bash
git clone https://github.com/gemini960114/ai-workshop-research.git
```

> [!IMPORTANT]
> **每個單元都要用 Antigravity 的 Open Folder 打開「該單元的資料夾」**，例如 `06-ai-workshop-research-papers`，**不要打開外層的 `ai-workshop-research`**。
> AI Agent 只會讀取打開的那個資料夾裡的 skill 和設定，打開外層會找不到。

## 單元

| 單元 | 內容 | 你會學到 |
| --- | --- | --- |
| [00 雲端 vs 地端](00-ai-workshop-openai/README.zh-TW.md) | 同一篇論文、同樣三個問題，交給 ChatGPT 網頁和地端 AI 編輯器，再換 Gemini 檢核 | 地端 AI Agent 能直接讀寫你的檔案、換模型互相檢核 |
| [01 Antigravity 入門](01-ai-workshop-agy/README.zh-TW.md) | 安裝 Antigravity 與工具，做第一個網頁和記憶翻牌遊戲 | 跟 AI Agent 對話、請 AI 安裝工具 |
| [02 前端設計](02-ai-workshop-frontend-design/README.zh-TW.md) | 安裝 frontend-design skill，做品牌網頁，再做一次記憶翻牌 | 什麼是 skill、怎麼安裝；比較有無 skill 的差別 |
| [03 Office 文件處理](03-ai-workshop-office-skills/README.zh-TW.md) | CSV → Excel → 簡報、Word 報告 → PDF 講義 | 用 docx、pdf、pptx、xlsx skill 產出可用的文件 |
| [04 核銷憑證登錄 Excel](04-ai-workshop-voucher-ocr/README.zh-TW.md) | 看懂掃描發票 PDF → 填進 Excel → 把做法存成 skill | **建立自己的 Skill**，一句話重複使用；換另一家 AI 互相覆核 |
| [05 QIIME 2 腸道菌相分析](05-ai-workshop-qiime2-analysis/README.zh-TW.md) | 在國網 HPC 上用中文請 AI 下載資料、派送作業、產出 9 頁分析報告 | 在 HPC 上用自然語言做分析；回到原始輸出檔核對數字 |
| [06 研究論文處理](06-ai-workshop-research-papers/README.zh-TW.md) | 從分析結果出發：找文獻 → 做筆記 → 寫論文 → 核對引用 → 輸出 PDF | 用 4 個 skill 寫出有引用、追得到出處的英文論文 |

- **05 → 06 是一條研究流程**：05 的分析結果，就是 06 寫論文的材料；06 的資料夾已經附上 05 整理好的研究摘要卡和數字表格。
- **06 有兩個資料夾**：[`06-ai-workshop-research-papers/`](06-ai-workshop-research-papers/README.zh-TW.md) 是乾淨的練習版；[`06-ai-workshop-research-papers-answer/`](06-ai-workshop-research-papers-answer/README.zh-TW.md) 是照手冊試跑一次的參考答案（12 頁英文論文、12 篇參考文獻）。

> 📋 **提示詞速查表**：七個單元會用到的 prompt 都整理在 [`tutorial.zh-TW.md`](tutorial.zh-TW.md)，上課時照順序複製貼上即可。

## 上課簡報與影片

各單元 README 開頭有簡報下載與教學影片連結；簡報檔在 [`PPTX/`](PPTX/)，影片放在 YouTube（附繁體中文字幕）：

| 單元 | 簡報 | 影片 |
| --- | --- | --- |
| 00 | [00-cloud-vs-local.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/00-cloud-vs-local.pptx) | [YouTube](https://youtu.be/QkUmEnTtMl4) |
| 01 | [01-antigravity.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/01-antigravity.pptx) | [YouTube](https://youtu.be/PQEkjWiNC5o) |
| 02 | [02-frontend-design.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/02-frontend-design.pptx) | [YouTube](https://youtu.be/qVPdYf5CD2A) |
| 03 | [03-office-skills.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/03-office-skills.pptx) | [YouTube](https://youtu.be/FwIpKAJ2-vk) |
| 04 | [04-voucher-ocr.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/04-voucher-ocr.pptx) | [YouTube](https://youtu.be/XOs_Pf7QyjA) |
| 05 | [05-qiime2-analysis.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/05-qiime2-analysis.pptx) | [YouTube](https://youtu.be/r1-ngUd3RKg) |
| 06 | [06-research-papers.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/06-research-papers.pptx) | [YouTube](https://youtu.be/fyyZEMmqQjY) |


## 事前準備

- 課堂電腦已經裝好 Antigravity 和需要的工具（Git、Node.js、uv、LibreOffice、ffmpeg）。在自己的電腦上使用時，可以照 01 的步驟安裝。
- **05** 需要國網中心 HPC 帳號與計畫代號；課堂上會說明。
- **06** 需要 LaTeX（例如 TinyTeX）或免費的 Overleaf 帳號，二選一。

## 注意事項

- AI 每次產生的內容可能略有不同，和教材的範例結果不完全一樣是正常的。
- **AI 寫的東西也會出錯。** 寫進報告或論文的數字，一律回到原始輸出檔確認（見 05、06）。
- 06 產出的是寫作練習用的論文草稿，不能直接投稿；真的要投稿時，所有數字和引用都要由作者本人核對。
- 04 的公開版只附去識別化的練習憑證；真實憑證與帳務資料不放在 GitHub。
