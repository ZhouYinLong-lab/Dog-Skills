---
name: topic-collector
description: >
  AI 热点自动采集器——多源并行搜索 AI 领域最新动态，生成结构化选题清单。
  覆盖 AI 博主/KOL·Product Hunt 新产品·Hacker News·学术论文·模型厂商官方·
  Reddit 社区热议。聚焦 Vibe Coding·Claude 生态·AI Agent·AI 知识管理·
  模型更新·新产品·海外热点 7 大领域。
  与 last30days（海外实时信号）和 creator-buddy（中文平台运营）互补。
  Trigger keywords: 今日选题, AI热点, 采集热点, 今天有什么新闻,
  今日AI热点, 热点采集, 选题清单, AI动态, 每日热点,
  AI news today, topic collector, 开始今日选题,
  看看今天有什么, 最近AI圈有什么, daily AI briefing.
allowed-tools:
  - Read
  - Write
  - WebFetch
  - WebSearch
metadata:
  category: tools
  source: https://github.com/SpaceZephyr/read-buddy (MIT)
  upstream: read-topic-collector
  version: "1.0.0"
  license: MIT
---

# Topic Collector — AI 热点自动采集

> 不是让 AI 凭感觉编选题。是多源并行采集真实动态，生成带原文链接的结构化选题清单。
> 上游来源: [SpaceZephyr/read-buddy](https://github.com/SpaceZephyr/read-buddy) (MIT)

---

## 采集流程

```
多源并行搜索 → 分类整理 → 提取原文链接 → 输出结构化清单
```

---

## 五大数据源

### 一、AI 博主/KOL 实践分享

**重点追踪账号**: @AnthropicAI, @OpenAI, @kaborsk1 (Claude Code创作者), @swyx, @simonw, @levelsio

**搜索关键词**:
```
"Claude Code" tips OR tricks OR workflow
"Cursor" vibe coding best practices
AI agent automation n8n
Claude MCP server
```

### 二、创业公司/新产品

| 来源 | 搜索内容 |
|------|---------|
| Product Hunt | AI / Developer Tools / Productivity 当日上榜 |
| Hacker News | Show HN / Launch HN 中的 AI 项目 |

提取: 产品名 + 描述 + upvotes + 产品页链接

### 三、AI 研究/学术动态

**来源**: arXiv 热门论文、Google DeepMind 博客、Meta AI 博客、Microsoft Research

```
site:arxiv.org AI agent OR LLM 2026
site:deepmind.google AI research
site:ai.meta.com new paper
```

### 四、模型厂商官方动态

| 厂商 | 搜索 |
|------|------|
| Anthropic | `site:anthropic.com OR "Claude" new feature` |
| OpenAI | `site:openai.com OR "ChatGPT" update` |
| Google | `"Gemini" update OR site:blog.google AI` |
| xAI | `"Grok" update` |
| Mistral | `site:mistral.ai` |

### 五、技术社区讨论

**Reddit**: r/ClaudeAI, r/ChatGPT, r/LocalLLaMA, r/artificial, r/MachineLearning
**Hacker News**: AI 相关热门讨论

---

## 七大聚焦领域（优先级排序）

1. **Vibe Coding** — 自然语言编程、Cursor、Claude Code 新玩法
2. **Claude 生态** — Claude Skill、MCP Server、Claude Code 技巧
3. **AI Agent** — 自动化工作流、n8n、Make、Multi-Agent
4. **AI 知识管理** — 第二大脑、PKM、Obsidian + AI
5. **模型更新** — GPT、Claude、Gemini 版本发布
6. **AI 新产品** — Product Hunt 上榜、独立开发者作品
7. **海外热点** — 行业大事件、收购、融资

---

## 采集执行步骤

依次用 WebSearch 执行以下搜索：

```
# 1. AI 博主动态
"Claude Code" OR "Cursor" tips tricks 2026

# 2. Product Hunt AI 产品
Product Hunt AI tools trending 2026

# 3. 模型厂商更新
Anthropic Claude OR OpenAI ChatGPT update 2026

# 4. AI Agent 工作流
AI agent automation workflow n8n 2026

# 5. 社区讨论
Reddit ClaudeAI OR ChatGPT hot discussion 2026

# 6. 研究动态
AI research breakthrough 2026 DeepMind OR Google OR Meta
```

---

## 输出格式

```markdown
## 🤖 今日 AI 热点 — MM/DD

---

### 🧑‍💻 AI 博主实践分享

1. **[标题/内容摘要]**
   - 作者: @用户名
   - 原文: [URL]
   - 要点: 一句话总结
   - 热度: ❤️ likes | 🔁 shares

---

### 🚀 创业公司/新产品

1. **[产品名]** — 一句话描述
   - 链接: [Product Hunt](https://...)
   - 热度: ⬆️ N upvotes
   - 分类: AI / DevTools / Productivity

---

### 🔬 AI 研究/学术动态

1. **[论文/博客标题]**
   - 来源: DeepMind / Meta AI / arXiv
   - 原文: [URL]
   - 核心发现: 一句话

---

### 🏢 模型厂商动态

| 厂商 | 动态 | 原文 | 要点 |
|------|------|------|------|
| Anthropic | ... | [URL] | ... |
| OpenAI | ... | [URL] | ... |

---

### 💬 社区热议

1. **[讨论标题]**
   - 来源: r/ClaudeAI / HN
   - 链接: [URL]
   - 热度: ⬆️ upvotes | 💬 comments
   - 核心观点: 一句话

---

## 🎯 选题建议

基于今日热点，推荐以下选题方向：
1. **[选题方向]** — 来源: [热点#] — 角度: ...
2. ...
```

---

## 核心原则

- **必须带原文链接**：每条热点都要有可点击的具体 URL
- 不采集纯学术论文（除非引发广泛讨论）
- 合并同类内容，去重
- 标注内容语言（中/英）
- 优先有实操价值的（教程/技巧/工具）
- 时效性优先：24 小时内的内容

---

## 与 Dog-Skills 协作

```
topic-collector        →  每日 AI 热点自动采集（本技能）
last30days             →  按需深度研究特定话题（跨 Reddit/HN/X/YouTube）
creator-buddy          →  中文平台运营情报（小红书/公众号/B站/抖音）
baokuan-title-generator →  基于热点产出爆款标题
```

---

## 安装方式

```bash
cp -r topic-collector/ ~/.claude/skills/topic-collector/
```

上游: `npx skills add SpaceZephyr/read-buddy`（获取 read-buddy 全部 18 个技能）

---

## 上游致谢

基于 [SpaceZephyr/read-buddy](https://github.com/SpaceZephyr/read-buddy) 中的 `read-topic-collector` (MIT License)，作者：空格的键盘。
