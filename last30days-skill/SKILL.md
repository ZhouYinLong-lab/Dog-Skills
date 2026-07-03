---
name: last30days
description: >
  AI agent-led search engine that researches any topic across Reddit, X (Twitter),
  YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, and more — scored
  by real engagement signals (upvotes, likes, comments) rather than SEO. Produces
  rich HTML briefs with Best Takes, cross-source cluster merging, ELI5 mode,
  comparison mode, hiring signals, and competitor auto-discovery. Use when the
  user wants to research what people are saying about a topic, product, person,
  or trend in the last 30 days. Trigger keywords: /last30days, research,
  what are people saying, trending, sentiment, compare, ELI5, hiring signals,
  best takes, 调研, 最近30天, 大家都在说什么.
metadata:
  category: thinking
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

MIT License.
