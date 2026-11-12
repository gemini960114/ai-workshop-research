// Generate docs/guide/*.md from each unit's README, so the unit README stays the
// single source of truth. Run automatically by `npm run docs:dev|docs:build`.
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

function rewriteLinks(markdown, rewrite) {
  return markdown.replace(/\]\(([^)\s]+)\)/g, (match, target) => {
    const next = rewrite(target)
    return next === undefined ? match : `](${next})`
  })
}

function chapterPage(target, prefix) {
  const m = target.match(new RegExp(`^${prefix}(\\d\\d-[a-z0-9-]+)(?:/README\\.md|/)?(#.*)?$`))
  if (m && CHAPTERS[m[1]]) return `./${CHAPTERS[m[1]]}${m[2] ?? ''}`
  return undefined
}

// Links inside a chapter README: keep http(s)/mailto/#anchor as-is; anything
// that points at a file inside this chapter's own folder (AGENTS.md, example/,
// .agents/skills/..., scripts/, models.md, *.toml, ...) becomes a GitHub
// blob/tree link, since those files are not part of the built docs site.
function fromChapter(dir, target) {
  if (/^(https?:|mailto:|#)/.test(target)) return undefined
  if (target === '../README.md' || target === '../') return './overview'
  const page = chapterPage(target, '\\.\\./')
  if (page) return page
  const clean = target.replace(/^\.\//, '')
  const kind = clean.endsWith('/') || clean === '' ? 'tree' : 'blob'
  return `${REPO}/${kind}/main/${dir}/${clean.replace(/\/$/, '')}`
}

// Links inside the root README: unit folders become internal docs pages,
// everything else (if any) becomes a GitHub blob/tree link.
function fromRoot(target) {
  if (/^(https?:|mailto:|#)/.test(target)) return undefined
  if (/^(\.\/)?tutorial\.md$/.test(target)) return './prompts'
  const page = chapterPage(target, '(?:\\./)?')
  if (page) return page
  const clean = target.replace(/^\.\//, '')
  const kind = clean.endsWith('/') || clean === '' ? 'tree' : 'blob'
  return `${REPO}/${kind}/main/${clean.replace(/\/$/, '')}`
}

const write = (page, content) => {
  writeFileSync(join(ROOT, 'docs', 'guide', `${page}.md`), content)
  console.log(`synced docs/guide/${page}.md`)
}

for (const [dir, page] of Object.entries(CHAPTERS)) {
  const source = readFileSync(join(ROOT, dir, 'README.md'), 'utf8')
  write(page, rewriteLinks(source, (t) => fromChapter(dir, t)))
}

write('overview', rewriteLinks(readFileSync(join(ROOT, 'README.md'), 'utf8'), fromRoot))
write('prompts', rewriteLinks(readFileSync(join(ROOT, 'tutorial.md'), 'utf8'), fromRoot))
