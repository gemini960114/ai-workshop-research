# 單元 00：雲端 vs 地端 — 同一篇論文，兩種 AI 用法

> 🌐 **語言**：[English](README.md) | 繁體中文

同一篇論文、同樣三個問題，分別交給**雲端的 ChatGPT 網頁**和**地端的 AI 編輯器**，看看兩種做法差在哪裡。這個單元是整個工作坊的開場：先看效果，後面的單元再一步步教你怎麼做。

> 📥 **本單元上課簡報**：[下載 00-cloud-vs-local.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/00-cloud-vs-local.pptx)（13 頁，含講者備註）

> 🎬 **本單元教學影片**：[單元 00｜雲端 vs 地端](https://github.com/gemini960114/ai-workshop-research/blob/main/movies/00-cloud-vs-local.mp4)（MP4，1 分 57 秒，附[繁體中文字幕](https://github.com/gemini960114/ai-workshop-research/blob/main/movies/00-cloud-vs-local.zh-TW.srt)）

| 步驟 | 內容 | 預估時間 |
| :--- | :--- | :---: |
| **示範 1** | [雲端做法：ChatGPT 網頁](#示範-1雲端做法chatgpt-網頁) | 5 分鐘 |
| **示範 2** | [地端做法：在編輯器裡用 Claude Code](#示範-2地端做法在編輯器裡用-claude-code) | 10 分鐘 |
| **示範 3** | [換另一個模型檢核：Gemini](#示範-3換另一個模型檢核gemini) | 5 分鐘 |
| **比較** | [雲端 vs 地端](#雲端-vs-地端) | 3 分鐘 |

---

## 示範用的論文

| 檔案 | 內容 |
|---|---|
| [`measuring-how-ai-agents-handle-wet-lab-science.pdf`](measuring-how-ai-agents-handle-wet-lab-science.pdf) | OpenAI〈Measuring how AI agents handle everyday wet-lab science〉（2026 年 11 月 6 日），排版成論文格式的 PDF |
| [`measuring-how-ai-agents-handle-wet-lab-science.tex`](measuring-how-ai-agents-handle-wet-lab-science.tex) | 上面那份 PDF 的 LaTeX 原始檔 |

論文重點：OpenAI 和生技公司 Ligo 合作建立 **BioBasicsBench**，用 **100 道**日常濕實驗室題目考 AI Agent。題目來自科學家自己的實驗資料，例如膠片、墨點、顯微鏡影像、儀器匯出檔，涵蓋五個領域：蛋白質方法、影像與流式細胞術、定量與檢測、核酸方法、分子選殖。

---

## 示範用的提示詞

三個問題，加上一句存成 Word 報告；檢核時，再對 Gemini 說兩句話。

### 📋 三個問題（雲端、地端都用同樣的問題）

```text
這篇論文標題寫的『wet-lab science（濕式實驗室科學）』是什麼意思？AI 為什麼要去處理實驗室的事？
```

```text
裡面說考了 AI 100 道實驗室題目，都是考些什麼？是考選擇題還是看圖題？請做成簡單的表格給我看。
```

```text
我是一個剛進生物實驗室的研究生，我應該怎麼安全地用 AI 幫我檢查實驗數據，才不會被它誤導？
```

### 📋 存成 Word 報告

```text
幫我整理上述的討論問題與回覆內容, 存成一份word 報告 report.docx
```

（雲端示範時實際輸入的是「幫我這結果存成一份word 報告」。）

### 📋 換 Gemini 檢核

```text
report.docx是 ai agent 根據 measuring-how-ai-agents-handle-wet-lab-science.pdf 的問題與回覆內容, 請確認是否正確
```

```text
根據您的建議進行修改 另儲存為新檔名
```

---

## 示範 1：雲端做法：ChatGPT 網頁

1. 打開 ChatGPT 網頁，**上傳 PDF**。
2. 三個問題**一題一題問**。回答很完整，還附上論文出處。
3. 最後請它做成 Word 報告：等了一分多鐘，還要**自己下載**，再用 Word 打開。

---

## 示範 2：地端做法：在編輯器裡用 Claude Code

1. 論文就放在**自己電腦的資料夾**。在編輯器（Antigravity）裡叫出 Claude Code（安裝方式見單元 01 Step 3），問同樣的三個問題。
2. 它會**自己找到資料夾裡的 PDF**，讀完再回答。例如第二題，就把 100 道題目整理成表格。
3. 接著一句話「存成 Word 報告」：它載入 **docx skill**，自己寫程式產生檔案，還轉成 PDF 檢查排版。
4. [`report.docx`](report.docx) 直接出現在同一個資料夾，在編輯器裡就能打開核對。

### 你應該會看到

`report.docx`〈AI 與濕式實驗室科學：論文閱讀與討論整理報告〉，依問題分節，例如：

- **問題一**：Wet lab 與 Dry lab 的對照表，以及 AI 為什麼要處理實驗室的事。
- **問題二**：BioBasicsBench 五大領域的題數表（蛋白質方法 25、影像與流式細胞術 23、定量與檢測 19、核酸方法 17、分子選殖 16），以及給 AI 看的資料類型（膠片與墨點、實驗流程與筆記、表格與儀器匯出檔…）。
- **問題三**：研究生安全使用 AI 檢查實驗數據的建議。

> 💡 docx skill 的安裝與用法在單元 03〈Office 文件處理〉。

---

## 示範 3：換另一個模型檢核：Gemini

1. 在同一個編輯器裡換成 **Gemini**，請它對照 PDF 檢查 `report.docx`。
2. Gemini 逐項對照原文：基本資訊、各領域題數、成功與失誤案例，**全部正確**。
3. 它也指出哪些段落是**背景延伸、不在論文裡**（例如 self-driving lab 這類廣義說明）。
4. 照建議修改後，這些段落被標成「背景補充」，另存成 [`report_revised.docx`](report_revised.docx)。

### 你應該會看到

比較兩份報告的「2.2 AI 為什麼要處理實驗室的事」：修改後分成**【論文指出的核心原因】**和**【廣義背景補充】**兩段，讀者分得出哪些是論文說的、哪些是 AI 補充的。

---

## 雲端 vs 地端

| | 雲端（ChatGPT 網頁） | 地端（編輯器 + AI Agent） |
|---|---|---|
| 檔案 | 要上傳 PDF、下載報告 | AI 直接讀寫你資料夾裡的檔案 |
| 產出 | 自己下載、再打開 | `report.docx` 就出現在同一個資料夾 |
| 檢核 | 同一個模型 | 可以換另一個模型（Gemini）互相檢核 |
| 上手 | 打開網頁就能用 | 要先安裝編輯器與 skill（單元 01–03） |

地端的做法，就像把 AI Agent 的大腦搬進你的筆電：它就在你的資料夾裡讀論文、寫報告、互相檢核，成為和你一起做研究的夥伴。

---

## 資料夾內容

```
00-ai-workshop-openai/
├── README.md                                          本說明
├── measuring-how-ai-agents-handle-wet-lab-science.pdf 示範用的論文
├── measuring-how-ai-agents-handle-wet-lab-science.tex 論文的 LaTeX 原始檔
├── report.docx                                        地端示範：Claude Code 產出的報告
└── report_revised.docx                                Gemini 檢核後修改、另存的報告
```

想自己試一次：用編輯器開啟這個資料夾，依序貼上上面的提示詞即可。

## 下一步

單元 01 從安裝 Antigravity 開始，一步步把這套地端的 AI 工作環境建起來。
