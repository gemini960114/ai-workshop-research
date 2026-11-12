// Generate docs/guide/*.md and docs/zh-TW/guide/*.md from each unit's README
// and README.zh-TW.md, so the unit READMEs stay the single source of truth.
// Run automatically by `npm run docs:dev|docs:build`.
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const REPO = 'https://github.com/gemini960114/ai-workshop-research'

const CHAPTERS = {
  '00-ai-workshop-openai': '00_cloud_vs_local',
  '01-ai-workshop-agy': '01_antigravity',
  '02-ai-workshop-frontend-design': '02_frontend_design',
  '03-ai-workshop-office-skills': '03_office_skills',
  '04-ai-workshop-voucher-ocr': '04_voucher_ocr',
  '05-ai-workshop-qiime2-analysis': '05_qiime2_analysis',
  '06-ai-workshop-research-papers': '06_research_papers',
  '06-ai-workshop-research-papers-answer': '06_research_papers_answer',
}

mkdirSync(join(ROOT, 'docs', 'guide'), { recursive: true })
mkdirSync(join(ROOT, 'docs', 'zh-TW', 'guide'), { recursive: true })

function rewriteLinks(markdown, rewrite) {
  return markdown.replace(/\]\(([^)\s]+)\)/g, (match, target) => {
    const next = rewrite(target)
    return next === undefined ? match : `](${next})`
  })
}

function chapterPage(target, prefix) {
  const m = target.match(new RegExp(`^${prefix}(\\d\\d-[a-z0-9-]+)(?:/README(?:\\.zh-TW)?\\.md|/)?(#.*)?$`))
  if (m && CHAPTERS[m[1]]) return `./${CHAPTERS[m[1]]}${m[2] ?? ''}`
  return undefined
}

function langSwitch(target, page, locale) {
  if (locale === 'en' && /^(\.\/)?(README|tutorial)\.zh-TW\.md$/.test(target)) {
    return `/zh-TW/guide/${page}`
  }
  if (locale === 'zh-TW' && /^(\.\/)?(README|tutorial)\.md$/.test(target)) {
    return `/guide/${page}`
  }
  return undefined
}

// Links inside a chapter README: keep http(s)/mailto/#anchor as-is; anything
// that points at a file inside this chapter's own folder (AGENTS.md, example/,
// .agents/skills/..., scripts/, models.md, *.toml, ...) becomes a GitHub
// blob/tree link, since those files are not part of the built docs site.
function fromChapter(dir, page, locale, target) {
  if (/^(https?:|mailto:|#)/.test(target)) return undefined
  const sw = langSwitch(target, page, locale)
  if (sw) return sw
  if (target === '../README.md' || target === '../README.zh-TW.md' || target === '../') return './overview'
  const cp = chapterPage(target, '\\.\\./')
  if (cp) return cp
  const clean = target.replace(/^\.\//, '')
  const kind = clean.endsWith('/') || clean === '' ? 'tree' : 'blob'
  return `${REPO}/${kind}/main/${dir}/${clean.replace(/\/$/, '')}`
}

// Links inside the root README: unit folders become internal docs pages,
// everything else (if any) becomes a GitHub blob/tree link.
function fromRoot(page, locale, target) {
  if (/^(https?:|mailto:|#)/.test(target)) return undefined
  const sw = langSwitch(target, page, locale)
  if (sw) return sw
  if (/^(\.\/)?tutorial(?:\.zh-TW)?\.md$/.test(target)) return './prompts'
  const cp = chapterPage(target, '(?:\\./)?')
  if (cp) return cp
  const clean = target.replace(/^\.\//, '')
  const kind = clean.endsWith('/') || clean === '' ? 'tree' : 'blob'
  return `${REPO}/${kind}/main/${clean.replace(/\/$/, '')}`
}

const write = (relDir, page, content) => {
  writeFileSync(join(ROOT, relDir, `${page}.md`), content)
  console.log(`synced ${relDir}/${page}.md`)
}

for (const [dir, page] of Object.entries(CHAPTERS)) {
  const sourceEn = readFileSync(join(ROOT, dir, 'README.md'), 'utf8')
  write('docs/guide', page, rewriteLinks(sourceEn, (t) => fromChapter(dir, page, 'en', t)))

  const sourceZh = readFileSync(join(ROOT, dir, 'README.zh-TW.md'), 'utf8')
  write('docs/zh-TW/guide', page, rewriteLinks(sourceZh, (t) => fromChapter(dir, page, 'zh-TW', t)))
}

write('docs/guide', 'overview', rewriteLinks(readFileSync(join(ROOT, 'README.md'), 'utf8'), (t) => fromRoot('overview', 'en', t)))
write('docs/guide', 'prompts', rewriteLinks(readFileSync(join(ROOT, 'tutorial.md'), 'utf8'), (t) => fromRoot('prompts', 'en', t)))

write('docs/zh-TW/guide', 'overview', rewriteLinks(readFileSync(join(ROOT, 'README.zh-TW.md'), 'utf8'), (t) => fromRoot('overview', 'zh-TW', t)))
write('docs/zh-TW/guide', 'prompts', rewriteLinks(readFileSync(join(ROOT, 'tutorial.zh-TW.md'), 'utf8'), (t) => fromRoot('prompts', 'zh-TW', t)))
