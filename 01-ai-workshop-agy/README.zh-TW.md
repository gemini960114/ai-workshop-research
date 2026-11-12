# 單元 01：Antigravity 入門 — 安裝設定與第一個網頁

> 🌐 **語言**：[English](README.md) | 繁體中文

用 **Google Antigravity IDE** 搭配內建的 AI Agent，用中文對話完成安裝、建立網頁，最後做出一個能玩的小遊戲。不需要寫程式經驗，約 30 分鐘。

> 📥 **本單元上課簡報**：[下載 01-antigravity.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/01-antigravity.pptx)（19 頁，含講者備註）

> 🎬 **本單元教學影片**：[單元 01｜Antigravity 入門](https://youtu.be/PQEkjWiNC5o)（YouTube）

| 步驟 | 內容 | 預估時間 |
| :--- | :--- | :---: |
| **Step 1** | [下載並安裝 Antigravity IDE](#step-1下載並安裝-antigravity-ide) | 3 分鐘 |
| **Step 2** | [開啟 Antigravity 並登入](#step-2開啟-antigravity-並登入) | 2 分鐘 |
| **Step 3** | [開啟專案資料夾、調整版面](#step-3開啟專案資料夾調整版面) | 3 分鐘 |
| **Step 4** | [請 AI 安裝與確認工具](#step-4請-ai-安裝與確認工具) | 5 分鐘 |
| **Step 5** | [小暖身：確認 AI 能正常工作](#step-5小暖身確認-ai-能正常工作) | 3 分鐘 |
| **Step 6** | [遊戲範例：記憶翻牌](#step-6遊戲範例記憶翻牌) | 10 分鐘 |

> [!NOTE]
> 課堂電腦已經裝好 Antigravity 和所有工具：**跳過 Step 1**，Step 4 只做最後的「確認工具」。以下安裝步驟是給你在自己的電腦上使用時參考。

---

## Step 1：下載並安裝 Antigravity IDE

開啟官方下載頁：**<https://antigravity.google/download>**

> [!WARNING]
> **請勿選擇頁面上方的「Antigravity app」或「Antigravity CLI」。**
> 請向下捲動至 **「Antigravity IDE (Standalone)」** 區塊，依你的作業系統下載：

| 你的作業系統 | 選擇下載版本 | 如何確認系統規格？ |
| :--- | :--- | :--- |
| **Windows 10 / 11** | 大多數選 **x64**<br>*(ARM 筆電選 ARM64)* | 「設定 → 系統 → 關於」查看「系統類型」 |
| **macOS (Apple Silicon)** | **Apple Silicon**（M1 / M2 / M3 / M4） | 左上角蘋果選單  →「關於這台 Mac」查看晶片型號 |

- **Windows**：執行下載的 `.exe` 安裝檔，照預設一路按下一步。
- **macOS**：打開下載檔案，將 **Antigravity IDE** 拖曳至「應用程式 (Applications)」資料夾。

## Step 2：開啟 Antigravity 並登入

開啟 **Antigravity**，以 **Google 帳號**登入。登入後就能在右側對話面板使用內建的 AI Agent，不需要另外安裝，也不需要 API 金鑰。

> [!NOTE]
> 公司或學校的 Google 帳號可能被管理者限制，無法使用內建 Agent；若無法登入，請改用**個人 Gmail 帳號**。

## Step 3：開啟專案資料夾、調整版面

### 開啟專案資料夾

AI Agent 只會在**你打開的資料夾**裡讀檔、寫檔，建議每個專案開一個新資料夾。

1. 按畫面中間藍色的 **Open Folder**（或選單「**檔案 → 開啟資料夾**」）。
2. 在「文件」（Documents）裡新建一個空資料夾，例如 `my-first-project`，選取後按 **Select folder**。
3. 開過的資料夾會列在 **Workspaces**，下次點一下就能再打開。

### 認識版面

| 位置 | 名稱 | 用途 |
| :--- | :--- | :--- |
| 左邊 | **檔案總管** | 專案裡所有檔案和資料夾 |
| 中間 | **檔案預覽／編輯區** | 點一下左邊的檔案，內容顯示在這裡 |
| 右邊 | **Agent 對話面板** | 跟 AI 對話；下方可選模型，以及 Low／Medium／High 思考程度 |
| 最右邊 | **Agent 圖示列** | 切換不同的 Agent（例如內建 Agent、Claude Code，見下方「加裝其他 AI Agent」） |

### 把 AI 對話面板放在右側

1. 點選上方選單「**檢視 → 外觀**」（`View → Appearance`），勾選 **Secondary Side Bar**。
2. 想把「**終端機 (Terminal)**」也移到右邊的話，在終端機分頁標題按右鍵 → **Move → Secondary Side Bar**。

### （選用）加裝其他 AI Agent：Claude Code、Codex

單元 00、04、06 的示範會在同一個編輯器裡切換到 **Claude Code**，讓不同家的 AI 互相檢核。想照著做的話：

1. 點左側的 **Extensions**（擴充功能），搜尋 **Claude Code**（或 **Codex**），按 **Install**。
2. 選單「**檢視 → 外觀**」，把 **Secondary Activity Bar Position** 設成 **Default**。右側會出現每個 Agent 的圖示，點一下就能切換。
3. Claude Code、Codex 要**登入各自的帳號**才能使用。

> [!NOTE]
> 沒有這些帳號也沒關係：各單元的主要步驟用內建的 Antigravity Agent 就能完成，需要「換一家 AI 檢核」時，改用內建 Agent 換另一個模型即可。

## Step 4：請 AI 安裝與確認工具

不用自己查安裝方法，直接用一句話請 AI 處理。AI 會自己判斷你的作業系統（Windows / macOS）並選擇安裝方式。

AI 要執行指令時會先詢問權限，請點 **Accept / Run**（這是正常的安全確認，不是卡住）。若跳出系統視窗（Windows 的「使用者帳戶控制」、macOS 的「命令列開發者工具」），請點 **是 / 安裝**。macOS 若在**終端機面板**出現 `Password:`，請輸入電腦的登入密碼後按 Enter；輸入時畫面**不會顯示任何字元**，這是正常的。

| 工具 | 用途 | 類別 |
| :--- | :--- | :---: |
| **Git** | 記錄作品的每一個版本 | 必要 |
| **GitHub CLI（gh）** | 登入 GitHub、建立 repo、保存作品（本課程用不到） | 選用 |
| **Node.js**（含 npm） | 執行網頁 App、安裝 Skill | 必要 |
| **uv** | 執行 Python 程式 | 必要 |
| **LibreOffice** | 處理 Word、Excel、簡報檔，把簡報轉成圖片讓 AI 檢查版面 | 建議 |
| **ffmpeg** | 影片、聲音處理 | 建議 |

**Prompt 1：安裝必要工具**

```text
請幫我安裝 Git、uv 和 Node.js。已經裝好的就跳過，有失敗的告訴我原因，最後列出每個工具的版本。
```

> [!IMPORTANT]
> 裝完後請**關掉 Antigravity 再重新打開**。剛裝好的工具要重開才抓得到，否則之後可能出現「找不到 npm」或「找不到 git」。

**Prompt 2：安裝建議工具**（LibreOffice 安裝檔約 300～400 MB，下載需要一點時間）

```text
請幫我安裝 GitHub CLI、LibreOffice 和 ffmpeg。已經裝好的就跳過，有失敗的告訴我原因，最後列出每個工具的版本。
```

**已經裝好工具的電腦**，只要確認就好：

```text
請告訴我這台電腦上 git、gh、uv、node、npm、ffmpeg 和 LibreOffice（soffice）的版本。
找不到的請列出來，先不要安裝。
```

全部都有版本號就完成了。

> [!TIP]
> React、Vite、python-docx 這類專案用的套件，以及 Python 本身，都**不用自己裝**：AI 做專案時會用 npm 或 uv 自動裝在專案資料夾裡（Python 套件放在 `.venv`）。

## Step 5：小暖身：確認 AI 能正常工作

這一步只是確認 AI 能動，做完 `my-first-project` 資料夾不用保存。在右側對話面板貼上：

**Prompt 3：第一個網頁**

```text
在這個資料夾建立一個 hello.html，用大字顯示「Hello Antigravity」和今天的日期，然後幫我用瀏覽器打開。
```

左邊檔案總管出現 `hello.html`，瀏覽器也打開了這個網頁，就代表 AI 可以在你的電腦上建立檔案、執行指令。環境準備完成！

## Step 6：遊戲範例：記憶翻牌

這次做一個能玩的小遊戲。請在「文件」（Documents）裡新建一個空資料夾 `my-second-project`，用 **Open Folder** 打開，在右側對話面板貼上：

**Prompt 4：記憶翻牌遊戲**

```text
在這個資料夾幫我用最簡單的 Vite + JS 做一個「記憶翻牌」遊戲：
總共 16 張牌隨機排列，翻到相同的兩張就消除，上方顯示步數和計時。
全部消除後顯示「恭喜完成」和「重新開始」按鈕，介面用繁體中文。
做完後直接幫我把網頁跑起來，給我網址讓我可以點開玩。
```

AI 會建立專案、安裝套件，再啟動**開發伺服器**。點開它給的網址（通常是 `http://localhost:5173`），玩一局看看：翻牌、配對、步數和計時都正常，全部消除後出現「恭喜完成」，就完成了！

> [!NOTE]
> Windows 若跳出「防火牆」視窗，請按「**允許**」。網頁開著時，終端機裡的開發伺服器要保持執行；不玩了，對 AI 說「停止開發伺服器」即可。

> [!TIP]
> 先把這個遊戲留著。單元 02 會裝上 frontend-design skill，用幾乎一樣的 prompt 再做一次，可以比較兩者的差別。

想多玩一點，可以直接用一句話請 AI 修改，例如「牌面改成水果圖案」「加一個最佳紀錄」「改成 20 張牌」，改完重新整理網頁就看得到。

---

## 學到的事

- AI Agent 只在**你打開的資料夾**裡工作；每個專案開一個資料夾。
- 工具不用自己查怎麼裝，**請 AI 安裝**，裝完重開 Antigravity。
- 用**一句清楚的中文**描述想要的結果（做什麼、放哪裡、做完要做什麼），AI 就能從零做出能跑的作品。
- 想改作品時，直接告訴 AI 哪裡要改、改成什麼樣子。

## 下一步

單元 02 認識 skill，裝上 frontend-design skill，用幾乎一樣的 prompt 再做一次記憶翻牌，比較兩者的差別。

---

## 附錄：其他工具（選用）

用不到可以不裝，之後需要再請 AI 安裝：

| 套件 | 用途 |
| :--- | :--- |
| **pandoc** | 把 Markdown 轉成 Word 檔 |
| **ripgrep、jq** | 搜尋檔案內容、處理 JSON |
| **ImageMagick** | 圖片處理 |
| **yt-dlp** | 下載影片 |

```text
請幫我安裝 pandoc、ripgrep、jq、ImageMagick，再用 uv 安裝 yt-dlp。
已經裝好的就跳過，有失敗的告訴我原因，最後列出每個工具的版本。
```

---

## 名詞小辭典

| 名詞 | 意思 |
| :--- | :--- |
| **Prompt** | 你貼給 AI 的指令文字 |
| **Accept／Run** | AI 要修改檔案或執行指令前，會先請你同意；按下才會執行 |
| **終端機（Terminal）** | 用文字輸入指令的視窗；AI 執行的指令都會顯示在這裡 |
| **開發伺服器** | 在你的電腦上暫時執行網頁 App 的程式；開著它，瀏覽器才看得到你的作品 |
| **localhost:5173** | 「這台電腦上的第 5173 號門（port）」，開發伺服器的網址；只有你的電腦看得到 |

## 遇到問題怎麼辦

大部分問題，**把錯誤訊息整段貼給 AI，請它處理**就能解決。以下是幾個常見狀況：

| 狀況 | 處理方式 |
| :--- | :--- |
| 出現「找不到 node／npm／git／gh／uv」 | 關掉 Antigravity 再重新打開 |
| Windows 跳出「防火牆」視窗（AI 啟動伺服器時） | 按「**允許**」 |
| Windows 出現「已停用指令碼執行」（PowerShell 執行原則） | 把錯誤訊息貼給 AI，請它處理 |
| 網址打不開，或顯示 port 已被使用 | 請 AI「換一個 port 重新啟動伺服器」 |
| AI 一直詢問權限 | 確認指令內容後按 **Accept / Run** |
| macOS 終端機要求 `Password:` | 輸入電腦登入密碼後按 Enter（不會顯示字元） |
| 無法用公司或學校的 Google 帳號登入 Antigravity | 改用個人 Gmail 帳號 |
