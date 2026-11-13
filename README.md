# Do Research with AI Agents

> 🌐 **Language**: English | [繁體中文](README.zh-TW.md)

**From literature review and paper writing to building your own Skills.**

Bring an AI Agent into your computer and project folders: chat in natural language to ask it to read papers, organize reports, run analyses on NCHC HPC, search literature and write an English manuscript, and finally save your verified workflow as a custom Skill you can reuse with a single sentence.

> 📖 **Online Course Website**: <https://gemini960114.github.io/ai-workshop-research/> (includes slide downloads and tutorial videos for each unit)

## Clone the Repository

```bash
git clone https://github.com/gemini960114/ai-workshop-research.git
```

> [!IMPORTANT]
> **For every unit, use Antigravity's `Open Folder` to open that specific unit's folder** (e.g., `06-ai-workshop-research-papers`). **Do NOT open the outer `ai-workshop-research` folder.**
> The AI Agent only reads the skills and configuration inside the folder currently opened as the workspace; opening the root folder will prevent it from finding unit-specific skills.

## Units

| Unit | Content | What You Will Learn |
| --- | --- | --- |
| [00 Cloud vs. Local](00-ai-workshop-openai/) | Give the same paper and the same three questions to ChatGPT Web and a local AI IDE, then cross-check with Gemini | Local AI Agents can read/write files directly in your folder and cross-check across models |
| [01 Getting Started with Antigravity](01-ai-workshop-agy/) | Install Antigravity and tools, build your first web page and a Memory Match card game | Chat with an AI Agent and ask AI to install development tools |
| [02 Frontend Design](02-ai-workshop-frontend-design/) | Install the `frontend-design` skill, build a brand landing page, and remake the Memory Match game | What a skill is, how to install it, and the difference with vs. without a skill |
| [03 Office Document Processing](03-ai-workshop-office-skills/) | CSV → Excel → Animated Slides, Word Report → PDF Handout | Produce polished documents using `docx`, `pdf`, `pptx`, and `xlsx` skills |
| [04 Voucher OCR to Excel](04-ai-workshop-voucher-ocr/) | Read scanned invoice PDFs → fill in Excel → save the workflow as a skill | **Build your own Skill** for one-sentence reuse; cross-check with a second AI Agent |
| [05 QIIME 2 Gut Microbiome Analysis](05-ai-workshop-qiime2-analysis/) | Use natural language on NCHC HPC to download data, submit Slurm jobs, and generate a 9-page report | Run HPC analyses in natural language; verify numbers against raw output files |
| [06 Research Paper Workflow](06-ai-workshop-research-papers/) | From analysis results: search literature → take notes → write paper → verify citations → compile PDF | Use 4 skills to write a cited, traceable English manuscript |

- **05 → 06 is a continuous research pipeline**: The analysis output from Unit 05 becomes the material for writing the paper in Unit 06; the Unit 06 folder already includes the research brief and summary tables extracted from Unit 05.
- **Unit 06 has two folders**: [`06-ai-workshop-research-papers/`](06-ai-workshop-research-papers/) is the clean practice folder; [`06-ai-workshop-research-papers-answer/`](06-ai-workshop-research-papers-answer/) is a complete reference answer from a full test run (12-page English manuscript with 12 references).

> 📋 **Prompt Cheat Sheet**: All prompts used across the seven units are collected in [`tutorial.md`](tutorial.md) so you can copy and paste them in order during the workshop.

## Slides & Tutorial Videos

Every unit has **English and Traditional Chinese versions** of its slide deck (with speaker notes) and its narrated tutorial video. Each unit's README links to the English versions first; decks are in [`PPTX/`](PPTX/) and videos are on YouTube.

| Unit | Slides | Video |
| --- | --- | --- |
| 00 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/00-cloud-vs-local.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/00-cloud-vs-local.pptx) | [English](https://youtu.be/sLCBtmZAz2c) (2:00, English subtitles) · [中文](https://youtu.be/QkUmEnTtMl4) |
| 01 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/01-antigravity.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/01-antigravity.pptx) | [English](https://youtu.be/72oCyg8MDLg) (3:59, English subtitles) · [中文](https://youtu.be/PQEkjWiNC5o) |
| 02 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/02-frontend-design.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/02-frontend-design.pptx) | [English](https://youtu.be/86bsVsh2tXw) (3:02, English subtitles) · [中文](https://youtu.be/qVPdYf5CD2A) |
| 03 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/03-office-skills.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/03-office-skills.pptx) | [English](https://youtu.be/sOIg3osiPU4) (3:34, English subtitles) · [中文](https://youtu.be/FwIpKAJ2-vk) |
| 04 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/04-voucher-ocr.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/04-voucher-ocr.pptx) | [English](https://youtu.be/Kq0HLK2kIQg) (4:45, English subtitles) · [中文](https://youtu.be/XOs_Pf7QyjA) |
| 05 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/05-qiime2-analysis.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/05-qiime2-analysis.pptx) | [English](https://youtu.be/IP08MIu5TCk) (4:51, English subtitles) · [中文](https://youtu.be/r1-ngUd3RKg) |
| 06 | [English](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/06-research-papers.en.pptx) · [中文](https://github.com/gemini960114/ai-workshop-research/raw/main/PPTX/06-research-papers.pptx) | [English](https://youtu.be/o253sy87788) (6:57, English subtitles) · [中文](https://youtu.be/fyyZEMmqQjY) |

English videos have English narration and English subtitles. Screen recordings and screenshots in them show the original Chinese demo, with English captions. Chinese videos have Traditional Chinese subtitles.

## Prerequisites

- Classroom computers already have Antigravity and required tools installed (Git, Node.js, uv, LibreOffice, ffmpeg). On your own computer, follow the steps in Unit 01 to install them.
- **Unit 05** requires an NCHC HPC account and project ID; instructions will be provided in class.
- **Unit 06** requires either a local LaTeX installation (e.g., TinyTeX) or a free Overleaf account.

## Notes

- AI-generated output varies slightly between runs; it is normal if your results differ slightly from the examples.
- **AI can make mistakes.** Always verify any numbers written into reports or manuscripts against the raw output files (see Units 05 and 06).
- Unit 06 produces a draft manuscript for writing practice and must not be submitted as-is; before any real submission, all numbers and citations must be verified by the authors.
- Unit 04's public repository only includes de-identified sample vouchers; real vouchers and accounting records are never stored on GitHub.
