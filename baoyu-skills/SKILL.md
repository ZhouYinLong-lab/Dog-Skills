---
name: baoyu-skills
description: >
  A comprehensive collection of 22 Claude Code skills for content creation,
  AI-powered generation, and productivity utilities. Includes skills for image
  generation (11 backends), slide deck creation (17 styles), SVG diagram
  generation (9 types), educational comic creation, article illustration,
  social media posting (X/WeChat/Weibo), translation (3 modes), image
  compression, YouTube transcript extraction, URL-to-markdown conversion,
  markdown formatting, and more. Use when the user needs content creation,
  image generation, slide decks, diagrams, comics, social media publishing,
  translation, or any of the 22 specialized workflows. Trigger keywords:
  生成图片, 幻灯片, PPT, 图表, diagram, 漫画, comic, 配图, 发帖, post to X,
  翻译, translate, 压缩图片, compress image, YouTube transcript, markdown
  formatting, 小红书, infographic, 封面图, cover image, 微信公众号, 微博,
  Electron extract, format markdown, url to markdown.
metadata:
  category: content
---

# baoyu-skills — 暴鱼技能合集

A collection of 22 Claude Code skills by JimLiu for AI-assisted content creation,
publishing, and productivity automation. Version 2.0.0. MIT-0 License.

---

## Installation

```bash
# Via Claude Code Plugin Marketplace
claude plugin marketplace add JimLiu/baoyu-skills
claude plugin install baoyu@baoyu-skills-plugin

# Via npx skills
npx skills add JimLiu/baoyu-skills -g --all
```

**Prerequisites**: Bun runtime, Chrome (for CDP-based skills), various API keys for image generation skills.

---

## Skills Overview

### Content Skills (内容技能)

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `baoyu-slide-deck` | 创建幻灯片, PPT | Generate professional slide images with 17 preset styles, auto-merge to PPTX/PDF |
| `baoyu-diagram` | 画图, diagram, flowchart | Create SVG diagrams (9 types) — architecture, sequence, mindmap, timeline, etc. |
| `baoyu-comic` | 知识漫画, comic | Educational comic creation with 6 art styles, 7 moods, 7 layouts |
| `baoyu-article-illustrator` | 为文章配图, illustrate | Smart article illustration using type × style × palette dimensions |
| `baoyu-xhs-images` | 小红书图片 | Xiaohongshu-style image cards: 10 styles × 6 layouts |
| `baoyu-infographic` | infographic, 信息图 | Professional infographics: 21 layouts × 17 visual styles |
| `baoyu-cover-image` | 封面图, cover image | Article cover images with 5 dimensions (type, palette, render, text, mood) |
| `baoyu-post-to-x` | post to X, tweet | Post to X/Twitter — text, images, video, quote tweets, and X Articles |
| `baoyu-post-to-wechat` | 发布到微信公众号 | Publish to WeChat Official Accounts via API or browser |
| `baoyu-post-to-weibo` | 发布到微博 | Post to Weibo — text posts and headline articles |

### AI Generation Skills (AI 生成技能)

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `baoyu-image-gen` | 生成图片, generate image | AI image generation via 11 backends (OpenAI, Google, Replicate, etc.) |
| `baoyu-danger-gemini-web` | — | Interact with Gemini Web via reverse-engineered web API |

### Utility Skills (实用技能)

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `baoyu-translate` | 翻译, translate | Three-mode translation (fast/normal/refined) with glossary support |
| `baoyu-compress-image` | 压缩图片, compress | Image compression to WebP/PNG/JPEG with auto tool selection |
| `baoyu-youtube-transcript` | YouTube transcript | Download YouTube transcripts/subtitles and cover images |
| `baoyu-url-to-markdown` | url to markdown | Fetch URLs via Chrome CDP and convert to Markdown |
| `baoyu-danger-x-to-markdown` | — | Convert X/Twitter content (tweets, articles) to Markdown |
| `baoyu-format-markdown` | format markdown | Add YAML headers, titles, and formatting to raw text/Markdown |
| `baoyu-markdown-to-html` | markdown to html | Convert Markdown to styled HTML (WeChat compatible) |
| `baoyu-wechat-summary` | 微信群聊总结 | Summarize WeChat group chat highlights into structured digests |
| `baoyu-electron-extract` | Electron extract | Extract resources and source code from Electron app.asar |

---

## Configuration

Skills use `EXTEND.md` files for per-project or per-user configuration:
- Project: `.baoyu-skills/<skill-name>/EXTEND.md`
- User: `~/.baoyu-skills/<skill-name>/EXTEND.md`
- API keys: `.env` files

---

## Architecture

- **Runtime**: TypeScript via Bun (preferred) or `npx -y bun` (fallback)
- **Browser automation**: Chrome CDP for web scraping and social media posting
- **Self-contained**: Each skill can be extracted and used independently

---

## License

MIT-0
