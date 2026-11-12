# 單元 02：前端設計 — frontend-design skill

認識 skill 是什麼、怎麼安裝，再用 Anthropic 官方的 frontend-design skill 做一個品牌網頁和記憶翻牌遊戲，比較有沒有 skill 的差別。

> 📥 **本單元上課簡報**：[下載 02-frontend-design.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/02-frontend-design.pptx)（12 頁，含講者備註）

> 🎬 **本單元教學影片**：[單元 02｜前端設計](https://youtu.be/qVPdYf5CD2A)（YouTube）

| 步驟 | 內容 | 預估時間 |
| :--- | :--- | :---: |
| **Step 1** | [認識 Skill 是什麼、怎麼安裝](#先備知識) | 3 分鐘 |
| **Step 2** | [安裝 frontend-design skill](#安裝-frontend-design) | 3 分鐘 |
| **Step 3** | [範例 1：從零做一個有個性的產品頁](#範例-1從零做一個有個性的產品頁) | 10 分鐘 |
| **Step 4** | [範例 2：記憶翻牌，和單元 01 比一比](#範例-2記憶翻牌和單元-01-比一比) | 10 分鐘 |

> [!IMPORTANT]
> 請用 Antigravity 的 **Open Folder** 開啟 `02-ai-workshop-frontend-design` 這個資料夾，不要開外層的 `ai-workshop-research`。

## 先備知識

### 什麼是 Skill？
Skill 是寫給 AI Agent 的工作說明書：告訴它某一類任務該怎麼做、要遵守哪些規範、可以用哪些工具或腳本。有了 skill，AI Agent 就不必每次從頭摸索，而是照你（或別人）整理好的經驗做事。

Skill 是一個資料夾，內含 `SKILL.md`（以及可選的腳本、資料、參考文件）。AI Agent 會依據 `SKILL.md` 開頭的 `description` 判斷什麼時候該自動載入它；載入後就照裡面的流程與規範做事。

你通常不需要點名 skill，只要描述任務，符合條件的 skill 就會被觸發。若想強制使用，也可以直接寫 `/skill名稱` 或「請使用 xxx skill」。

### Skill 的安裝位置

| 位置 | 範圍 |
| :--- | :--- |
| **專案目錄**（例如 `.claude/skills/`、`.agents/skills/`） | 只在這個專案生效，本單元的 skill 會裝在這裡 |
| **使用者目錄**（例如 `~/.claude/skills/`） | 全域 skill，所有專案都會生效 |

> [!NOTE]
> 如果你的電腦上另外裝了全域 skill，它們也會在本課程的專案裡出現，可能和本單元的 skill 搶著被觸發。

---

### 安裝指令說明

> [!IMPORTANT]
> **本單元的 skill 需要自己安裝。** 請在 Antigravity 開啟終端機（確認目前位置是本資料夾），執行〈安裝 frontend-design〉的指令，裝好後**重新開啟 AI Agent 的對話**再開始做範例。

#### 安裝語法
```bash
npx skills add <GitHub擁有者>/<repo>[@skill名稱] -a antigravity -a claude-code --copy -y
```

| 參數 | 意義 |
| :--- | :--- |
| `owner/repo` | 安裝該 repo 內所有 skills |
| `owner/repo@name` | 只安裝 repo 中的某一個 skill |
| `-a antigravity -a claude-code` | 同時安裝給兩個 AI Agent（寫入 `.agents/skills/` 與 `.claude/skills/`） |
| `--copy` | 複製檔案而非建立連結（Windows 上較穩定） |
| `-y` | 略過確認提示 |

#### 常用管理指令
```bash
npx skills find <關鍵字>   # 搜尋 skill
npx skills update          # 更新所有已安裝 skill
```

> [!TIP]
> 安裝完成後，專案根目錄會出現 `skills-lock.json` 記錄版本。**重新開啟 AI Agent 的對話後 skill 才會生效**。

---

## 安裝 frontend-design

```bash
npx skills add anthropics/skills@frontend-design -a antigravity -a claude-code --copy -y
```

- **用途**：Anthropic 官方 skill。讓 AI 做前端時像「設計工作室的設計總監」，從主題本身找出配色、字體與版面方向，避免千篇一律的「紫色漸層 + 大數字 + 卡片」AI 模板感。

## 重點觀念
1. **先釐清主題、受眾、頁面的主要任務**，再決定美學方向。
2. **Hero 區要放「這個主題最有代表性的東西」**。
3. **字體刻意挑選，建立明確的字級系統**；字體本身就是設計的一部分。

---

## 範例 1：從零做一個有個性的產品頁

### 任務 Prompt
```text
在目錄 output/case01/ 中，幫我做一個台灣手工茶葉品牌「山嵐茶研所」的單頁官網（HTML + CSS），主頁面存成 output/case01/index.html。
受眾是 30–50 歲重視產地與職人精神的消費者。
需要：品牌故事、三款茶品介紹、產地地圖區、訂購按鈕。
不要用常見的 SaaS 模板風格，請先提出 2 個美學方向讓我選。
```

- **預期行為**：AI Agent 先提出例如「宣紙水墨 + 襯線字」與「高山晨霧 + 大留白」兩種方向，確認後再實作，配色與字體都會呼應茶與山的主題。
- **驗證觸發**：完成後追問下面這句，確認 AI Agent 確實載入了 skill：
  ```text
  在這個 Case 你使用了哪些 Skills
  ```

---

## 範例 2：記憶翻牌，和單元 01 比一比

這段 prompt 和單元 01 Step 6 幾乎一樣，差別只在這次裝了 frontend-design skill。做完後把兩個遊戲並排打開，比較配色、字體和版面。

### 任務 Prompt
```text
在目錄 output/case02/ 幫我用最簡單的 Vite + JS 做一個「記憶翻牌」遊戲：
總共 16 張牌隨機排列，翻到相同的兩張就消除，上方顯示步數和計時。
全部消除後顯示「恭喜完成」和「重新開始」按鈕，介面用繁體中文。
做完後直接幫我把網頁跑起來，給我網址讓我可以點開玩。
```

- **預期行為**：AI Agent 會自動建立輕量的 Vite + JS 專案、撰寫洗牌與翻牌配對邏輯，完成後在背景啟動伺服器並提供本地網址（如 `http://localhost:5173`），讓學員能直接點擊在瀏覽器試玩。
- **驗證觸發**：完成後追問下面這句，確認 AI Agent 確實載入了 skill：
  ```text
  在這個 Case 你使用了哪些 Skills
  ```

---

## 學到的事

- Skill 是一個資料夾＋`SKILL.md`，裝在專案層級只在這個資料夾生效；裝在使用者層級則所有專案都會用到。
- 不用點名 skill，AI 會依任務內容自動判斷要不要載入；不確定有沒有生效，直接問「這個 Case 你使用了哪些 Skills」。
- 同樣的 prompt，裝了 frontend-design 之後，AI 會先想清楚主題、受眾和視覺方向，而不是套用制式模板——這就是 skill 帶來的差別。
- 裝好 skill 後要**重新開啟 AI Agent 的對話**，才會生效。
