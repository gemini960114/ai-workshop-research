# Unit 02: Frontend Design — `frontend-design` Skill

> 🌐 **Language**: English | [繁體中文](README.zh-TW.md)

Learn what a Skill is and how to install it, then use Anthropic's official `frontend-design` skill to build a brand landing page and a Memory Match card game—and compare the result with and without the skill.

> 📥 **Unit Slides**: [Download 02-frontend-design.en.pptx](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/02-frontend-design.en.pptx) (12 slides, with speaker notes; [Chinese version](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/02-frontend-design.pptx))

> 🎬 **Tutorial Video**: [Unit 02 | Frontend Design](https://youtu.be/86bsVsh2tXw) (YouTube, 3 min 02 sec, English narration with [English subtitles](https://github.com/gemini960114/ai-workshop-research/blob/main/movies/02-frontend-design.en.srt); [Chinese version on YouTube](https://youtu.be/qVPdYf5CD2A))

| Step | Content | Est. Time |
| :--- | :--- | :---: |
| **Step 1** | [Learn What a Skill Is and How to Install It](#background) | 3 min |
| **Step 2** | [Install the `frontend-design` Skill](#install-frontend-design) | 3 min |
| **Step 3** | [Example 1: Build a Distinctive Product Landing Page from Scratch](#example-1-build-a-distinctive-product-landing-page-from-scratch) | 10 min |
| **Step 4** | [Example 2: Memory Match — Compare with Unit 01](#example-2-memory-match--compare-with-unit-01) | 10 min |

> [!IMPORTANT]
> Use Antigravity's **Open Folder** to open the `02-ai-workshop-frontend-design` folder directly—do not open the outer `ai-workshop-research` folder.

## Background

### What Is a Skill?
A Skill is an operating manual written for an AI Agent: it tells the agent how to handle a specific category of tasks, what design or quality rules to follow, and what helper scripts or tools it can use. With a skill installed, the AI Agent doesn't have to guess from scratch every time—it follows curated best practices compiled by you or domain experts.

Technically, a Skill is a directory containing a `SKILL.md` file (along with optional scripts, templates, or reference documents). The AI Agent reads the `description` in the frontmatter of `SKILL.md` to decide when to load it automatically; once loaded, it follows the workflow and guidelines inside.

You usually don't need to mention a skill by name—simply describe your task and any matching skill will trigger automatically. To force a specific skill, you can also type `/skill-name` or say "Please use the xxx skill."

### Where Skills Are Installed

| Location | Scope |
| :--- | :--- |
| **Project directory** (e.g., `.claude/skills/`, `.agents/skills/`) | Active only within this project folder; skills in this unit are installed here |
| **User home directory** (e.g., `~/.claude/skills/`) | Global skills active across all projects on your machine |

> [!NOTE]
> If you have global skills installed in your user home directory, they will also be visible inside workshop projects and may compete to trigger alongside the unit's project-level skills.

---

### Installation Command Reference

> [!IMPORTANT]
> **You need to install the skill for this unit yourself.** Open the Terminal inside Antigravity (make sure your current working directory is this unit's folder), run the command under *Install frontend-design*, and **start a new AI Agent chat session** before running the examples.

#### Installation Syntax
```bash
npx skills add <github-owner>/<repo>[@skill-name] -a antigravity -a claude-code --copy -y
```

| Flag | Meaning |
| :--- | :--- |
| `owner/repo` | Install all skills inside that repository |
| `owner/repo@name` | Install only a specific named skill from that repository |
| `-a antigravity -a claude-code` | Install for both AI Agents simultaneously (writes to `.agents/skills/` and `.claude/skills/`) |
| `--copy` | Copy files instead of creating symlinks (more reliable on Windows) |
| `-y` | Skip interactive confirmation prompts |

#### Common Management Commands
```bash
npx skills find <keyword>   # Search for skills
npx skills update           # Update all installed skills
```

> [!TIP]
> After installation finishes, a `skills-lock.json` file will appear in the project root recording the installed version. **Remember to start a fresh AI Agent chat session so the newly installed skill takes effect.**

---

## Install frontend-design

```bash
npx skills add anthropics/skills@frontend-design -a antigravity -a claude-code --copy -y
```

- **Purpose**: Official Anthropic skill that guides the AI to approach frontend work like a creative director at a design studio—deriving color palettes, typography, and layout structure from the subject matter itself rather than defaulting to generic AI templates ("purple gradient + big numbers + 3 cards").

## Key Concepts
1. **Clarify the subject, audience, and primary goal of the page first** before deciding on an aesthetic direction.
2. **Put the most iconic representation of the subject in the Hero section**.
3. **Choose typography deliberately and establish a clear type scale**—typography itself is a core part of the design.

---

## Example 1: Build a Distinctive Product Landing Page from Scratch

### Task Prompt
```text
In the directory output/case01/, build a single-page official website (HTML + CSS) for a Taiwanese artisanal tea brand called "Shanlan Tea Research Institute (山嵐茶研所)", saving the main page as output/case01/index.html.
The target audience is 30–50 year-old consumers who value origin and craftsmanship.
Required sections: Brand Story, Introduction to Three Teas, Tea Origin Map, and Order Button.
Do not use a generic SaaS template style—please propose 2 aesthetic directions for me to choose from first.
```

- **Expected Behavior**: The AI Agent first proposes two distinct aesthetic directions—for example, *"Xuan Paper & Ink Wash with Serif Typography"* vs. *"High-Mountain Morning Mist with Generous Whitespace"*—and waits for your choice before implementing a layout whose colors and fonts echo the theme of tea and mountains.
- **Verify Skill Trigger**: After completion, ask the follow-up question below to confirm the AI Agent loaded the skill:
  ```text
  Which Skills did you use in this case?
  ```

---

## Example 2: Memory Match — Compare with Unit 01

This prompt is nearly identical to Unit 01 Step 6; the only difference is that the `frontend-design` skill is now installed. Once completed, open both games side by side in your browser and compare their color palettes, typography, and layout polish.

### Task Prompt
```text
In the directory output/case02/, help me build a "Memory Match" card game using the simplest Vite + JS setup:
16 cards arranged randomly; flip two matching cards to clear them, and show move count and timer at the top.
When all cards are cleared, display "Congratulations!" and a "Play Again" button.
Once finished, start the web server directly and give me the URL so I can click and play.
```

- **Expected Behavior**: The AI Agent scaffolds a lightweight Vite + JS project, writes the card shuffling and matching logic, starts the background dev server, and provides a local URL (such as `http://localhost:5173`) so you can click and play immediately.
- **Verify Skill Trigger**: After completion, ask the follow-up question below to confirm the AI Agent loaded the skill:
  ```text
  Which Skills did you use in this case?
  ```

---

## What You Learned

- A Skill is a folder containing `SKILL.md`; installing it at the project level scopes it to that folder, while installing it at the user level makes it available across all projects.
- You don't need to call out a skill by name—the AI automatically decides whether to load it based on your task description. If you aren't sure whether it triggered, just ask: *"Which Skills did you use in this case?"*
- Given the exact same prompt, having `frontend-design` installed prompts the AI to think through theme, audience, and visual direction instead of falling back on generic boilerplate—demonstrating the impact of a well-crafted skill.
- Always **start a new AI Agent chat session** after installing a skill so it takes effect.

## Next Step

In Unit 03, you will install four official skills—`docx`, `pdf`, `pptx`, and `xlsx`—to transform a single CSV dataset into an Excel workbook, an animated presentation, a Word report, and a PDF handout.
