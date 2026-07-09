---
name: last30days
description: >
  AI agent-led search engine that researches any topic across Reddit, X (Twitter),
  YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, and more — scored
  by real engagement signals (upvotes, likes, comments) rather than SEO. Produces
  rich HTML briefs with Best Takes, cross-source cluster merging, ELI5 mode,
  comparison mode, hiring signals, and competitor auto-discovery. Use when the
  user wants to research what people are saying about a topic, product, person,
  or trend in the last 30 days.
  Trigger keywords: /last30days, research, what are people saying, trending,
  sentiment, compare, ELI5, hiring signals, best takes, 调研, 最近30天,
  大家都在说什么, 海外调研, AI新概念学习, 海外资讯, 社交媒体调研,
  热门话题, 深度搜索, Reddit搜索, X搜索, 跨平台调研.
metadata:
  category: thinking
  source: https://github.com/mvanhorn/last30days-skill
  references:
    - https://mp.weixin.qq.com/s/VDlBdkspV0SQNFJYLxOogQ
  author:
    original: mvanhorn
    chinese_intro: 卡兹克
---

# last30days — AI-Powered Topic Research

An AI agent-led search engine that researches any topic across 15+ platforms
scored by real engagement signals, not SEO or editorial curation.

---

## Installation

```bash
# Claude Code (recommended — auto-updates via marketplace)
claude plugin marketplace add mvanhorn/last30days-skill
claude plugin install last30days@last30days-skill

# Other agents (Codex, Cursor, Copilot, Gemini CLI, etc.)
npx skills add mvanhorn/last30days-skill -g
```

---

## Usage

```
/last30days <topic> [--mode <mode>] [--save]
```

**Modes**: `research` (default), `compare`, `hiring`, `agent`, `eli5`

---

## What it searches

| Source | What it captures |
|--------|-----------------|
| **Reddit** | Thread scores, comment counts, subreddit communities |
| **X (Twitter)** | Tweet engagement, verified signals |
| **YouTube** | Video metadata, view counts |
| **TikTok** | Trending short-form content |
| **Instagram** | Visual trend signals |
| **Hacker News** | Tech community discussion scores |
| **Polymarket** | Real-money prediction market odds |
| **GitHub** | Repo stars, issue activity, person/org mode |
| **Threads, Pinterest, Bluesky** | Emerging platform signals |
| **Perplexity** | AI-powered web research |
| **General Web** | Brave/Exa/Serper search backends |

---

## Key features

- **Real engagement signals** — upvotes, likes, comment counts, Polymarket odds
- **Best Takes** — extracts the most insightful comments/threads
- **Cross-source cluster merging** — deduplicates the same story across platforms
- **ELI5 mode** — simple explanations for complex topics
- **Comparison mode** — side-by-side analysis (e.g., "Cursor vs Copilot")
- **Hiring signals** — candidate/business evaluation patterns
- **GitHub person-mode** — research a developer's activity profile
- **Shareable HTML briefs** — self-contained reports with embedded media

---

## Configuration

Config file at `~/.config/last30days/.env` or `.claude/last30days.env`:

```
REDDIT_CLIENT_ID=...
REDDIT_CLIENT_SECRET=...
X_BEARER_TOKEN=...
SCRAPECREATORS_API_KEY=...
BLUESKY_APP_PASSWORD=...
PERPLEXITY_API_KEY=...
BRAVE_API_KEY=...
```

Output saved to `~/Documents/Last30Days/` (configurable via `LAST30DAYS_MEMORY_DIR`).

---

## Architecture

```
skills/last30days/
├── SKILL.md              # Canonical skill definition (10 LAWs + step-by-step)
└── scripts/
    ├── last30days.py     # Main engine
    └── lib/              # Source modules, search backends, scoring
```

---

## 中文介绍

> 以下内容整理自卡兹克的介绍文章：[《开源项目简介：last30days》](https://mp.weixin.qq.com/s/VDlBdkspV0SQNFJYLxOogQ)

### 这是什么？

给 last30days 一个话题，它让 AI agent 帮你扒一遍最近 30 天国外各大社交媒体上的真实讨论，然后综合成一份带引用的报告。

开源地址：https://github.com/mvanhorn/last30days-skill

### 和普通搜索的核心差异

**第一，深度爬取，不只是看帖子标题。**

Reddit 上一个帖子，它把评论带点赞数一起扒下来。X 上的推文，高赞回复也会纳入进去。就像你看小红书不会只看正文肯定要翻评论区一样，这个 Skill 把类似的考虑了进去，而且跨十几个平台一起翻。优质信息经常就埋在评论里，有时候评论比正文还值钱。

**第二，按真实热度排序，不按 SEO。**

Reddit 几千 upvote 的讨论，权重高于一篇没人看的博客。一个 3.6M 播放的 TikTok，权重高于一篇新闻稿。看到的排名是真人投出来的，不是哪篇博客做了 SEO 排上来的。

### 覆盖源

Reddit、X、YouTube、TikTok、Hacker News、GitHub、Polymarket 等十几个国外平台。

### 免费 vs 付费

- **零配置免费可用**：Reddit、Hacker News、Polymarket、GitHub
- **简单配置后可用**：X（登录浏览器账号或用 API key）、YouTube（装 yt-dlp）
- 免费源对日常学习新概念来说已经够用

### 适用场景

学习 AI 新概念新知识特别好用——国内很多信息是对海外资讯的搬运和二次咀嚼，直接用这个 Skill 从源头获取，信息更一手、更及时。

---

MIT License.
