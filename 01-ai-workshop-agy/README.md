# Unit 01: Getting Started with Antigravity — Installation, Setup & Your First Web Page

> 🌐 **Language**: English | [繁體中文](README.zh-TW.md)

Use **Google Antigravity IDE** with its built-in AI Agent to install tools, create a web page, and build a playable mini-game through natural language conversation. No programming experience is required, and it takes about 30 minutes.

> 📥 **Unit Slides**: [Download 01-antigravity.en.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/01-antigravity.en.pptx) (19 slides, with speaker notes; [Chinese version](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/01-antigravity.pptx))

> 🎬 **Tutorial Video**: [Unit 01 | Getting Started with Antigravity](https://youtu.be/72oCyg8MDLg) (YouTube, 3 min 59 sec, English narration with [English subtitles](https://github.com/gemini960114/ai-workshop-research/blob/main/movies/01-antigravity.en.srt); [Chinese version on YouTube](https://youtu.be/PQEkjWiNC5o))

| Step | Content | Est. Time |
| :--- | :--- | :---: |
| **Step 1** | [Download and Install Antigravity IDE](#step-1-download-and-install-antigravity-ide) | 3 min |
| **Step 2** | [Open Antigravity and Sign In](#step-2-open-antigravity-and-sign-in) | 2 min |
| **Step 3** | [Open a Project Folder and Adjust Layout](#step-3-open-a-project-folder-and-adjust-layout) | 3 min |
| **Step 4** | [Ask AI to Install and Verify Tools](#step-4-ask-ai-to-install-and-verify-tools) | 5 min |
| **Step 5** | [Quick Warm-Up: Confirm AI Works Properly](#step-5-quick-warm-up-confirm-ai-works-properly) | 3 min |
| **Step 6** | [Game Example: Memory Match](#step-6-game-example-memory-match) | 10 min |

> [!NOTE]
> Classroom computers already have Antigravity and all required tools installed: **skip Step 1**, and in Step 4 only run the final "Verify Tools" prompt. The installation steps below are for your reference when setting up your own computer.

---

## Step 1: Download and Install Antigravity IDE

Open the official download page: **<https://antigravity.google/download>**

> [!WARNING]
> **Do NOT select "Antigravity app" or "Antigravity CLI" at the top of the page.**
> Scroll down to the **"Antigravity IDE (Standalone)"** section and download the version matching your operating system:

| Your Operating System | Version to Choose | How to Check System Specs |
| :--- | :--- | :--- |
| **Windows 10 / 11** | Mostly **x64**<br>*(Choose ARM64 for ARM laptops)* | Go to "Settings → System → About" and check "System type" |
| **macOS (Apple Silicon)** | **Apple Silicon** (M1 / M2 / M3 / M4) | Click the Apple menu in the top-left → "About This Mac" and check the chip model |

- **Windows**: Run the downloaded `.exe` installer and click Next with default settings.
- **macOS**: Open the downloaded file and drag **Antigravity IDE** into your `Applications` folder.

## Step 2: Open Antigravity and Sign In

Launch **Antigravity** and sign in with your **Google account**. Once signed in, you can immediately use the built-in AI Agent in the right-hand chat panel without installing any extra extensions or setting up API keys.

> [!NOTE]
> Work or school Google Workspace accounts may be restricted by administrators from using the built-in Agent; if you cannot sign in, please use a **personal Gmail account** instead.

## Step 3: Open a Project Folder and Adjust Layout

### Open a Project Folder

The AI Agent only reads and writes files **inside the folder you open**, so we recommend creating a new folder for each project.

1. Click the blue **Open Folder** button in the center of the window (or use the menu **"File → Open Folder"**).
2. In your `Documents` directory, create a new empty folder such as `my-first-project`, select it, and click **Select folder**.
3. Previously opened folders are listed under **Workspaces**, so you can reopen them with a single click next time.

### Understand the Layout

| Location | Name | Purpose |
| :--- | :--- | :--- |
| Left | **Explorer** | All files and folders inside your project |
| Center | **Editor / Preview Area** | Click any file on the left to view or edit its contents here |
| Right | **Agent Chat Panel** | Chat with the AI; choose models and Low / Medium / High thinking effort at the bottom |
| Far Right | **Agent Activity Bar** | Switch between different Agents (e.g., built-in Agent, Claude Code; see "Optional: Install Additional AI Agents" below) |

### Place the AI Chat Panel on the Right

1. Click the top menu **"View → Appearance"** and check **Secondary Side Bar**.
2. If you also want to move the **Terminal** to the right side, right-click the Terminal tab header → **Move → Secondary Side Bar**.

### (Optional) Install Additional AI Agents: Claude Code, Codex

Demos in Units 00, 04, and 06 switch to **Claude Code** inside the same IDE so that AI Agents from different providers can cross-check each other's work. If you want to follow along with that setup:

1. Click **Extensions** on the left sidebar, search for **Claude Code** (or **Codex**), and click **Install**.
2. Go to **"View → Appearance"** and set **Secondary Activity Bar Position** to **Default**. Icons for each Agent will appear on the far right, allowing you to switch with a single click.
3. Claude Code and Codex require signing in to their respective accounts.

> [!NOTE]
> It is completely fine if you do not have those accounts: all core steps in every unit can be completed using the built-in Antigravity Agent, and when a step calls for "cross-checking with another AI," you can simply switch to a different model within the built-in Agent.

## Step 4: Ask AI to Install and Verify Tools

Instead of looking up installation guides yourself, just ask the AI in a single sentence. The AI will detect your operating system (Windows / macOS) and pick the right installation method automatically.

Before running commands, the AI will ask for permission—click **Accept / Run** (this is a normal security confirmation, not a freeze). If an OS dialog pops up (Windows User Account Control or macOS Command Line Developer Tools), click **Yes / Install**. On macOS, if `Password:` appears in the **Terminal panel**, type your Mac login password and press Enter; **no characters or asterisks will appear on screen** as you type, which is normal.

| Tool | Purpose | Category |
| :--- | :--- | :---: |
| **Git** | Track version history of your projects | Essential |
| **GitHub CLI (gh)** | Sign in to GitHub, create repos, and publish work (not required for this workshop) | Optional |
| **Node.js** (with npm) | Run web apps and install Skills | Essential |
| **uv** | Run Python scripts and manage environments | Essential |
| **LibreOffice** | Process Word, Excel, and PowerPoint files, and convert slides to images so AI can inspect layouts | Recommended |
| **ffmpeg** | Process video and audio files | Recommended |

**Prompt 1: Install Essential Tools**

```text
Please help me install Git, uv, and Node.js. Skip any that are already installed, tell me the reason if any fail, and finally list the version of each tool.
```

> [!IMPORTANT]
> After installation completes, **close Antigravity completely and reopen it**. Newly installed tools require a restart to be detected in `PATH`; otherwise you may see errors like "npm not found" or "git not found."

**Prompt 2: Install Recommended Tools** (LibreOffice is ~300–400 MB, so downloading takes a moment)

```text
Please help me install GitHub CLI, LibreOffice, and ffmpeg. Skip any that are already installed, tell me the reason if any fail, and finally list the version of each tool.
```

**On computers where tools are already installed**, simply verify them:

```text
Please tell me the installed versions of git, gh, uv, node, npm, ffmpeg, and LibreOffice (soffice) on this computer.
List any that cannot be found, and do not install them yet.
```

Once every tool reports a version number, you are ready to go!

> [!TIP]
> Project-specific libraries like React, Vite, or `python-docx`—as well as Python itself—**do not need to be installed manually**: when building a project, the AI will automatically install them inside the project folder using `npm` or `uv` (Python packages are placed in `.venv`).

## Step 5: Quick Warm-Up: Confirm AI Works Properly

This step simply confirms that the AI can create files and run commands; you do not need to keep the `my-first-project` folder afterward. Paste the following into the right-hand chat panel:

**Prompt 3: First Web Page**

```text
Create a hello.html in this folder that displays "Hello Antigravity" and today's date in large text, then open it in the browser for me.
```

When `hello.html` appears in the Explorer on the left and opens in your browser, it means the AI can create files and execute commands on your computer. Your environment setup is complete!

## Step 6: Game Example: Memory Match

Now let's build a playable mini-game. Create a new empty folder named `my-second-project` in `Documents`, open it with **Open Folder**, and paste this prompt into the chat panel:

**Prompt 4: Memory Match Game**

```text
In this folder, help me build a "Memory Match" card game using the simplest Vite + JS setup:
16 cards arranged randomly; flip two matching cards to clear them, and show move count and timer at the top.
When all cards are cleared, display "Congratulations!" and a "Play Again" button.
Once finished, start the web server directly and give me the URL so I can click and play.
```

The AI will scaffold the project, install packages, and start a **development server**. Click the URL it provides (typically `http://localhost:5173`) and play a round: once card flipping, matching, move counter, and timer all work and "Congratulations!" appears upon clearing the board, you're done!

> [!NOTE]
> On Windows, if a "Windows Defender Firewall" dialog pops up, click **"Allow"**. Keep the dev server running in the terminal while playing; when finished, simply tell the AI "Stop the dev server."

> [!TIP]
> Keep this game project around! In Unit 02, we will install the `frontend-design` skill and run nearly the exact same prompt again so you can compare the visual difference side by side.

If you want to customize the game further, just ask the AI in one sentence—for example: "Change the card faces to fruit icons," "Add a best score record," or "Change it to 20 cards"—and refresh the browser to see the changes.

---

## What You Learned

- The AI Agent only works inside **the folder you open**; create a dedicated folder for each project.
- You don't need to look up how to install developer tools—**just ask the AI to install them**, then restart Antigravity.
- Describe your desired outcome in **one clear sentence** (what to build, where to put it, and what to do when finished), and the AI can build a working application from scratch.
- To modify your project, simply tell the AI what you want changed and how it should look.

## Next Step

In Unit 02, you will learn what a Skill is, install the `frontend-design` skill, and build the Memory Match game again with nearly the same prompt to compare the results.

---

## Appendix: Optional Tools

You can skip these if you don't need them right now, and ask the AI to install them later whenever needed:

| Package | Purpose |
| :--- | :--- |
| **pandoc** | Convert Markdown documents into Word files |
| **ripgrep, jq** | Search file contents rapidly and process JSON data |
| **ImageMagick** | Image manipulation and conversion |
| **yt-dlp** | Download videos |

```text
Please help me install pandoc, ripgrep, jq, and ImageMagick, and then install yt-dlp using uv.
Skip any that are already installed, tell me the reason if any fail, and finally list the version of each tool.
```

---

## Glossary

| Term | Meaning |
| :--- | :--- |
| **Prompt** | The text instruction you give to the AI |
| **Accept / Run** | Before modifying files or running shell commands, the AI asks for your approval; click to proceed |
| **Terminal** | A text-based command window; all commands executed by the AI are displayed here |
| **Dev Server** | A program that temporarily hosts your web app on your computer so you can view it in a browser |
| **localhost:5173** | "Port 5173 on this computer"—the local address of the dev server, accessible only on your machine |

## Troubleshooting

Most issues can be solved by **copying the entire error message, pasting it to the AI, and asking it to fix the problem**. Here are several common situations:

| Situation | Solution |
| :--- | :--- |
| Error saying `node / npm / git / gh / uv not found` | Close Antigravity completely and reopen it |
| Windows Firewall popup when AI starts a server | Click **"Allow"** |
| Windows PowerShell error `"running scripts is disabled on this system"` | Paste the error message to the AI and ask it to fix the execution policy |
| Local URL won't open or says the port is already in use | Ask the AI to "restart the server on a different port" |
| AI keeps waiting for permission | Review the command and click **Accept / Run** |
| macOS Terminal prompts for `Password:` | Type your Mac login password and press Enter (characters won't be shown) |
| Unable to sign in to Antigravity with a work/school Google account | Use a personal Gmail account instead |
