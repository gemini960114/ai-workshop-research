import { defineConfig } from 'vitepress'
import { githubSlugify } from '../../scripts/slugify.mjs'

const units = [
  { text: '00. 雲端 vs 地端', link: '/guide/00_cloud_vs_local' },
  { text: '01. Antigravity 入門', link: '/guide/01_antigravity' },
  { text: '02. 前端設計 skill', link: '/guide/02_frontend_design' },
  { text: '03. Office 文件處理', link: '/guide/03_office_skills' },
  { text: '04. 核銷憑證：建立自己的 Skill', link: '/guide/04_voucher_ocr' },
  { text: '05. QIIME 2 腸道菌相分析', link: '/guide/05_qiime2_analysis' },
  { text: '06. 研究論文處理', link: '/guide/06_research_papers' },
]

export default defineConfig({
  title: 'AI 研究工作坊',
  description: '讓 AI Agent 和你一起做研究：從文獻整理、論文撰寫，到建立自己的 Skill',
  head: [['meta', { name: 'theme-color', content: '#7c3aed' }]],
  base: '/ai-workshop-research/',
  ignoreDeadLinks: true,
  markdown: { anchor: { slugify: githubSlugify } },
  themeConfig: {
    nav: [
      { text: '首頁', link: '/' },
      { text: '課程總覽', link: '/guide/overview' },
      { text: '七個單元', items: units },
      { text: '06 參考答案', link: '/guide/06_research_papers_answer' },
      { text: '附錄：提示詞速查表', link: '/guide/prompts' },
    ],
    sidebar: [
      { text: '課程介紹', items: [{ text: '課程總覽與單元列表', link: '/guide/overview' }] },
      { text: '單元', items: units },
      { text: '參考答案', items: [{ text: '06 研究論文處理（試跑結果）', link: '/guide/06_research_papers_answer' }] },
      { text: '附錄', items: [{ text: '提示詞速查表（各單元 prompt）', link: '/guide/prompts' }] },
    ],
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/gemini960114/ai-workshop-research' }],
    footer: {
      message: '讓 AI Agent 和你一起做研究',
      copyright: 'Copyright © 2026 AI 研究工作坊',
    },
  },
})
