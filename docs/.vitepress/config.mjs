import { defineConfig } from 'vitepress'
import { githubSlugify } from '../../scripts/slugify.mjs'

const enUnits = [
  { text: '00. Cloud vs. Local', link: '/guide/00_cloud_vs_local' },
  { text: '01. Getting Started with Antigravity', link: '/guide/01_antigravity' },
  { text: '02. Frontend Design Skill', link: '/guide/02_frontend_design' },
  { text: '03. Office Document Processing', link: '/guide/03_office_skills' },
  { text: '04. Voucher OCR: Build Your Own Skill', link: '/guide/04_voucher_ocr' },
  { text: '05. QIIME 2 Gut Microbiome Analysis', link: '/guide/05_qiime2_analysis' },
  { text: '06. Research Paper Workflow', link: '/guide/06_research_papers' },
]

const zhUnits = [
  { text: '00. 雲端 vs 地端', link: '/zh-TW/guide/00_cloud_vs_local' },
  { text: '01. Antigravity 入門', link: '/zh-TW/guide/01_antigravity' },
  { text: '02. 前端設計 skill', link: '/zh-TW/guide/02_frontend_design' },
  { text: '03. Office 文件處理', link: '/zh-TW/guide/03_office_skills' },
  { text: '04. 核銷憑證：建立自己的 Skill', link: '/zh-TW/guide/04_voucher_ocr' },
  { text: '05. QIIME 2 腸道菌相分析', link: '/zh-TW/guide/05_qiime2_analysis' },
  { text: '06. 研究論文處理', link: '/zh-TW/guide/06_research_papers' },
]

export default defineConfig({
  title: 'AI Research Workshop',
  description: 'Do Research with AI Agents: From Literature Review & Paper Writing to Building Your Own Skills',
  head: [['meta', { name: 'theme-color', content: '#7c3aed' }]],
  base: '/ai-workshop-research/',
  ignoreDeadLinks: true,
  markdown: { anchor: { slugify: githubSlugify } },
  themeConfig: {
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/gemini960114/ai-workshop-research' }],
  },
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'AI Research Workshop',
      description: 'Do Research with AI Agents: From Literature Review & Paper Writing to Building Your Own Skills',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Overview', link: '/guide/overview' },
          { text: '7 Units', items: enUnits },
          { text: '06 Reference Answer', link: '/guide/06_research_papers_answer' },
          { text: 'Appendix: Prompt Cheat Sheet', link: '/guide/prompts' },
        ],
        sidebar: [
          { text: 'Introduction', items: [{ text: 'Course Overview & Units', link: '/guide/overview' }] },
          { text: 'Units', items: enUnits },
          { text: 'Reference Answer', items: [{ text: '06 Research Paper Workflow (Test Run)', link: '/guide/06_research_papers_answer' }] },
          { text: 'Appendix', items: [{ text: 'Prompt Cheat Sheet (All Units)', link: '/guide/prompts' }] },
        ],
        footer: {
          message: 'Do Research with AI Agents',
          copyright: 'Copyright © 2026 AI Research Workshop',
        },
      },
    },
    'zh-TW': {
      label: '繁體中文',
      lang: 'zh-TW',
      link: '/zh-TW/',
      title: 'AI 研究工作坊',
      description: '讓 AI Agent 和你一起做研究：從文獻整理、論文撰寫，到建立自己的 Skill',
      themeConfig: {
        nav: [
          { text: '首頁', link: '/zh-TW/' },
          { text: '課程總覽', link: '/zh-TW/guide/overview' },
          { text: '七個單元', items: zhUnits },
          { text: '06 參考答案', link: '/zh-TW/guide/06_research_papers_answer' },
          { text: '附錄：提示詞速查表', link: '/zh-TW/guide/prompts' },
        ],
        sidebar: [
          { text: '課程介紹', items: [{ text: '課程總覽與單元列表', link: '/zh-TW/guide/overview' }] },
          { text: '單元', items: zhUnits },
          { text: '參考答案', items: [{ text: '06 研究論文處理（試跑結果）', link: '/zh-TW/guide/06_research_papers_answer' }] },
          { text: '附錄', items: [{ text: '提示詞速查表（各單元 prompt）', link: '/zh-TW/guide/prompts' }] },
        ],
        footer: {
          message: '讓 AI Agent 和你一起做研究',
          copyright: 'Copyright © 2026 AI 研究工作坊',
        },
      },
    },
  },
})
