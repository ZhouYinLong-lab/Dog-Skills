# Dog-Skills

> A collection of Claude skills for AI-assisted development workflows.

Skills are installable prompt bundles for [Claude](https://claude.ai) (Cowork / Claude Code). Each skill teaches Claude a specialized workflow so you don't have to re-explain it every time.

---

## Installation

### Method 1: Install from `.skill` file

Download the `.skill` file from `dist/` and drag it into Claude Code's chat window — it auto-installs to `~/.claude/skills/`.

### Method 2: Manual copy

```bash
mkdir -p ~/.claude/skills

# 🧠 Thinking & Research
cp -r first-principles ~/.claude/skills/first-principles
cp -r feynman-learning ~/.claude/skills/feynman-learning
cp -r nuwa-skill ~/.claude/skills/nuwa
cp -r last30days-skill ~/.claude/skills/last30days
cp -r storm-research ~/.claude/skills/storm-research
cp -r thinking-toolkit ~/.claude/skills/thinking-toolkit

# 💻 Development
cp -r cc-dispatch ~/.claude/skills/cc-dispatch
cp -r code-review ~/.claude/skills/code-review
cp -r website-cloner ~/.claude/skills/website-cloner
cp -r claude-to-im-skill ~/.claude/skills/claude-to-im
cp -r superpowers ~/.claude/skills/superpowers
cp -r planning-with-files ~/.claude/skills/planning-with-files
cp -r code-simplifier ~/.claude/skills/code-simplifier
cp -r webapp-testing ~/.claude/skills/webapp-testing
cp -r ralph-loop ~/.claude/skills/ralph-loop
cp -r mcp-builder ~/.claude/skills/mcp-builder
cp -r repo-evaluator ~/.claude/skills/repo-evaluator

# 🎨 Design & Frontend
cp -r ui-ux-pro-max-skill ~/.claude/skills/ui-ux-pro-max
cp -r dog-frontier ~/.claude/skills/dog-frontier
cp -r html_video ~/.claude/skills/html-video
cp -r lottie-animation ~/.claude/skills/lottie-animation
cp -r brand-workshop ~/.claude/skills/brand-workshop
cp -r pixel-art ~/.claude/skills/pixel-art
cp -r presentation-design ~/.claude/skills/presentation-design
cp -r article-poster ~/.claude/skills/article-poster
cp -r canvas-design ~/.claude/skills/canvas-design
cp -r algorithmic-art ~/.claude/skills/algorithmic-art
cp -r slack-gif-creator ~/.claude/skills/slack-gif-creator
cp -r theme-factory ~/.claude/skills/theme-factory
cp -r soviet-storybook-grotesque ~/.claude/skills/soviet-storybook-grotesque
cp -r torn-paper-collage-poster ~/.claude/skills/torn-paper-collage-poster
cp -r dog-poster ~/.claude/skills/dog-poster

# 📝 Content & Writing
cp -r humanizer-zh ~/.claude/skills/humanizer-zh
cp -r baoyu-skills ~/.claude/skills/baoyu-skills
cp -r humanize-ppt ~/.claude/skills/humanize-ppt
cp -r writing-assistant ~/.claude/skills/writing-assistant
cp -r scientific-writing-editor ~/.claude/skills/scientific-writing-editor
cp -r ghostwriter ~/.claude/skills/ghostwriter

# 📚 Learning & Teaching
cp -r tutor ~/.claude/skills/exam-tutor
cp -r dog-tutor ~/.claude/skills/dog-tutor
cp -r learning-studio ~/.claude/skills/learning-studio

# 💼 Business & Strategy
cp -r dbskill ~/.claude/skills/dbskill

# 🔍 Tools & Discovery
cp -r vercel-labs-skills ~/.claude/skills/find-skills
cp -r weread-skill ~/.claude/skills/weread-skill
cp -r token-optimizer ~/.claude/skills/token-optimizer
cp -r handshake ~/.claude/skills/handshake
cp -r vibe-sing ~/.claude/skills/vibe-sing
cp -r family-doctor ~/.claude/skills/family-doctor
```

### Verification

```bash
ls ~/.claude/skills/
# 🧠: feynman-learning/  first-principles/  last30days/  nuwa/  storm-research/  thinking-toolkit/
# 📚: dog-tutor/  exam-tutor/  learning-studio/
# 💻: cc-dispatch/  claude-to-im/  code-review/  code-simplifier/  mcp-builder/  planning-with-files/  ralph-loop/  repo-evaluator/  superpowers/  webapp-testing/  website-cloner/
# 🎨: algorithmic-art/  article-poster/  brand-workshop/  canvas-design/  dog-frontier/  html-video/  lottie-animation/  pixel-art/  dog-poster/  presentation-design/  slack-gif-creator/  soviet-storybook-grotesque/  theme-factory/  torn-paper-collage-poster/  ui-ux-pro-max/
# 📝: baoyu-skills/  ghostwriter/  humanize-ppt/  humanizer-zh/  scientific-writing-editor/  writing-assistant/
# 💼: dbskill/
# 🔍: family-doctor/  find-skills/  handshake/  token-optimizer/  vibe-sing/  weread-skill/
```

Once installed, skills trigger automatically when Claude detects a matching task — no special command needed.

---

## Trigger examples

### 🧠 Thinking & Research

| Skill | Try saying... |
|-------|---------------|
| `first-principles` | "从第一性原理出发" / "从本质出发重新思考" / "think from first principles" |
| `storm-research` | "用 STORM 方法做技术调研" / "做一份深度研究简报" / "Stanford STORM research" |
| `feynman-learning` | "用费曼学习法帮我理解" / "用费曼技巧深度学习" / "Feynman technique" |
| `nuwa` | "蒸馏 Paul Graham 的思维方式" / "分析张一鸣的决策框架" / "造一个 skill" |
| `last30days` | "/last30days Cursor vs Copilot" / "research what people think about..." |
| `thinking-toolkit` | "帮我做校准预测" / "对这三个方案做决策矩阵" / "用贝叶斯更新我的判断" / "沙盘推演未来走向" |

### 💻 Development

| Skill | Try saying... |
|-------|---------------|
| `cc-dispatch` | "拆一个 Task Package 给 Claude Code" / "验收这份完成报告" |
| `code-review` | "帮我审查代码" / "/code-review"→工程质量 / "做对抗式审查" / "adversarial review"→攻击视角 |
| `website-cloner` | "克隆这个网站" / "帮我复刻这个页面" / "/clone-website https://..." |
| `claude-to-im` | "帮我把 Claude 连到 Telegram" / "setup claude-to-im" / "在手机上跟 Claude 聊天" |
| `superpowers` | "开始一个新功能开发" / "帮我按 Superpowers 流程来" / "brainstorm this feature" |
| `planning-with-files` | "plan this feature" / "帮我做开发规划" / "记录这个设计决策" |
| `code-simplifier` | "简化刚才生成的代码" / "优化这个模块的可读性" / "/simplify" |
| `webapp-testing` | "测一下登录流程" / "部署前跑截图对比" / "帮我写 e2e 测试" |
| `ralph-loop` | "自动迭代完成这些 story" / "启动循环开发" / "批量实现 PRD 任务" |
| `repo-evaluator` | "评估这个 GitHub 仓库" / "这个开源项目靠谱吗" / "对比这三个类似项目" |
| `mcp-builder` | "帮我创建一个 MCP Server" / "把这个 API 包装成 MCP 工具" / "build an MCP server" |

### 🎨 Design & Frontend

| Skill | Try saying... |
|-------|---------------|
| `ui-ux-pro-max` | "推荐一个 SaaS landing page 的配色" / "生成 design system" / "dashboard 用什么字体" |
| `dog-frontier` | "帮我设计一个 AI SaaS 落地页" / "审查这个仪表盘的 UX" / "生成设计系统" / "反AI味审查" |
| `html-video` | "把这篇文章做成视频" / "用这个 GitHub 仓库生成一个介绍视频" / "做一个产品宣传动画" |
| `lottie-animation` | "帮我做一个心跳动效" / "生成 Lottie 动画" / "create a Lottie animation" |
| `brand-workshop` | "帮我做品牌全案设计" / "run brand workshop for my startup" / "设计Logo和标语" |
| `pixel-art` | "画一幅像素画" / "做一个等距像素场景" / "create pixel art" |
| `presentation-design` | "设计演示方案板" / "做一套投资人Pitch视觉方案" / "design presentation board" |
| `article-poster` | "把这篇文章做成信息图海报" / "生成知识卡片"→数据可视化风 |
| `canvas-design` | "帮我设计活动海报" / "生成宣传单页"→通用设计风 |
| `torn-paper-collage-poster` | "做一张撕纸拼贴海报" / "Zine 风格展览海报"→手工拼贴艺术风 |
| `dog-poster` | "帮我做海报"【先问风格再路由】 / "同主题三种风格各来一张" / "poster studio" |
| `algorithmic-art` | "生成一幅流场艺术画" / "用 p5.js 画分形" / "create generative art" |
| `slack-gif-creator` | "做一张 Slack 动图" / "把录屏转 GIF 发 Slack" / "create animated emoji" |
| `theme-factory` | "给幻灯片换一个科技风主题" / "生成一套品牌配色" / "apply a dark theme" |
| `soviet-storybook-grotesque` | "把这张照片变成苏联童书风" / "东欧绘本风格插画" |
### 📝 Content & Writing

| Skill | Try saying... |
|-------|---------------|
| `humanizer-zh` | "帮我把这段文字去AI味"【改已有文本】 / "改写得更像人写的" |
| `baoyu-skills` | "帮我生成幻灯片" / "画一个架构图" / "翻译这篇文章" / "压缩图片" |
| `humanize-ppt` | "帮我把这份资料做成PPT" / "给我的deck做演讲体检" / "PPT渲染质检" |
| `writing-assistant` | "帮我写一篇博客" / "写一份项目报告" / "draft a memo" |
| `scientific-writing-editor` | "润色这篇论文" / "写基金申请书" / "回复审稿意见" |
| `ghostwriter` | "帮我回这封邮件（用我的语气）"【从零创作】 / "draft a reply in my voice" |

### 📚 Learning & Teaching

| Skill | Try saying... |
|-------|---------------|
| `exam-tutor` | "帮我生成第5章复习资料" / "分析往年卷的高频考点" / "为这道题写一份习题讲解" |
| `dog-tutor` | "帮我生成 Linux 入门教程" / "编制一份 R 语言学习材料" / "设计课程大纲" |
| `learning-studio` | "把机器学习做成一套课程" / "compare 三本书的观点" / "苏格拉底阅读模式" |

### 💼 Business & Strategy

| Skill | Try saying... |
|-------|---------------|
| `dbskill` | "/问诊 我的商业模式有问题吗" / "/好问题" / "/决策系统" / "/对标" |

### 🔍 Tools & Discovery

| Skill | Try saying... |
|-------|---------------|
| `find-skills` | "有没有能做 PR 描述的 skill" / "find a skill for code review" |
| `weread-skill` | "帮我查查我的书架" / "分析我的阅读统计" / "搜索某本书的评分" |
| `token-optimizer` | "优化项目 token 消耗" / "cto audit" / "帮我清理上下文" / "检查 token 用量" |
| `handshake` | "/handshake 校准协作风格" / "帮我做 whoami 画像" / "calibrate how we work" |
| `vibe-sing` | "/vibe-sing 给我来一首" / "/vibe-sing pro 完整版" / "写完了唱首歌" |
| `family-doctor` | "分析我最近一周的健康数据" / "血压高帮我查原因" / "解读体检报告" / "制定减脂计划" |

---

## Skills

### 🧠 Thinking & Research

---

#### `first-principles` — 第一性原理思考 — First Principles Thinking

**Purpose**: 强制 AI 从第一性原理出发思考问题——打断类比推理，剥离所有假设，从最基本的事实和约束重新推导方案。

**Workflow**:

```
1. Break Down — Decompose the problem, surfacing every assumption, convention, and analogy
2. Strip Away — Remove layers of received wisdom, precedent, and existing solutions
3. Identify Fundamentals — Find the irreducible facts, constraints, and first principles
4. Rebuild — Derive a fresh solution from fundamentals without copying prior approaches
5. Validate — Test the new solution against reality and stated constraints
```

**Key features**:
- Strips away all assumptions, analogies, and received wisdom before reasoning
- Starts from irreducible facts and fundamental constraints
- Applicable to any domain: bug fixing, architecture design, business decisions, writing
- Forces rigorous bottom-up reasoning instead of pattern matching
- Single universal prompt that works across all complex problem types

**Install**: Download `dist/first-principles.skill` and drag it into Claude Code.

---

#### `storm-research` — 斯坦福 STORM 深度研究方法

**Purpose**: 4 个提示让 Claude 像博士一样做研究。STORM = Systematic + Thorough + Organized + Rigorous + Methodical。5 分钟产出博士 48 小时级别的研究简报。

**Workflow**:

```
1. 研究框架构建 → 拆解核心问题，定义研究边界
2. 多源信息收集 → 学术/工业界/社区多角度，标注可信度和偏见
3. 深度分析与综合 → 主张-证据-推理结构，标注置信度
4. 研究简报生成 → 一页纸摘要 + 框架概览 + 关键发现 + 开放问题
```

**Key features**:
- 4 个结构化提示覆盖完整研究流程
- 多源交叉验证，区分事实/观点/推测
- 标注知识缺口（不知道比错误更诚实）
- 5 分钟可读完核心内容的研究简报

**Install**: Download `dist/storm-research.skill` and drag it into Claude Code.

---

#### `feynman-learning` — 费曼学习法 AI 助手

**Purpose**: 把费曼四步学习法装进 AI，通过「教给别人→发现缺口→回归原始→简化类比」的循环，在 20 分钟内完成对任意概念的深度理解和长期记忆。

**Workflow**:

```
概念输入 → 模拟教学（第一轮）→ 缺口诊断 → 回归原始材料 → 简化输出（第二轮教学）→ 长期记忆固化
```

**Key features**:
- 费曼四步法：选择概念 → 教给别人 → 发现缺口 → 简化类比
- AI 扮演学生追问，暴露理解盲点
- 自动生成生活化类比
- 间隔复习时间表和自测题

**Install**: Download `dist/feynman-learning.skill` and drag it into Claude Code.

---

#### `nuwa` — 女娲 · Distill Anyone's Thinking into an AI Skill

**Purpose**: A meta-skill that distills any person's way of thinking into a runnable AI skill. Launches 6 parallel research agents to scour public sources (writings, interviews, decisions, criticism, timeline), triple-verifies extracted mental models, and generates a complete SKILL.md that acts as a cognitive advisor in that person's voice.

**What it distills**: Expression DNA, 3-7 mental models, 5-10 decision heuristics, anti-patterns, values, intellectual genealogy, and honest limits.

**Workflow**: 6-agent parallel research → triple-verification framework extraction → SKILL.md construction → quality validation → dual-agent refinement.

**Already distilled figures**: Paul Graham, Zhang Yiming, Karpathy, Steve Jobs, Elon Musk, Munger, Feynman, Naval, Taleb, and more (13 person skills + 1 topic skill).

**Install**: Download `dist/nuwa-skill.skill` and drag it into Claude Code. Or: `npx skills add alchaincyf/nuwa-skill`

---

#### `last30days` — AI-Powered Topic Research

**Purpose**: AI agent-led search engine researching any topic across Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, and more — scored by real engagement signals (upvotes, likes, comment counts, real-money odds), not SEO. Produces HTML briefs with Best Takes, cross-source clusters, ELI5 mode, comparison mode, and competitor auto-discovery.

**Usage**: `/last30days <topic> [--mode research|compare|hiring|agent|eli5] [--save]`

**Sources (15+)**: Reddit, X, YouTube, TikTok, Instagram, HN, Polymarket, GitHub, Threads, Pinterest, Bluesky, Perplexity, general web.

**Install**: Download `dist/last30days-skill.skill` and drag it into Claude Code. Or: `npx skills add mvanhorn/last30days-skill -g`

---

#### `thinking-toolkit` — 思考决策工具箱 · Thinking Toolkit

**Purpose**: 元技能整合 6 大思考框架——superforecaster（校准预测）、decision-matrix（决策矩阵）、bayesian-reasoning（贝叶斯推理）、systems-thinking（系统思维）、scout-mindset（偏见审查）、doctor-strange（平行宇宙沙盘推演）。覆盖预测→决策→推理→系统分析→偏见审查→情景模拟的完整深度思考链路。

**6 大子技能**:
- **superforecaster** — 五阶段校准预测（基准率→证据更新→置信区间→复盘）
- **decision-matrix** — 多维度量化权衡，含敏感度分析
- **bayesian-reasoning** — 基于新证据持续更新信念
- **systems-thinking** — 识别反馈回路、杠杆点和涌现行为
- **scout-mindset** — 认知偏见审查（确认偏误/锚定/过度自信等）
- **doctor-strange** — 多Agent并行模拟不同未来走向

**Install**: `git clone https://github.com/lyndonkl/claude.git` (子技能来源) + `npx skills add MagicCube/agentara --skill doctor-strange -y -g`

---

### 💻 Development

---

#### `cc-dispatch` — Codex × Claude Code Collaboration Protocol

**Purpose**: Saves Codex quota by turning the Codex ↔ Claude Code relationship into a structured ticket system rather than a back-and-forth conversation.

**Workflow**:

```
Codex (PM)  ──[Task Package]──▶  Claude Code (Executor)
                                        │
Codex (QA)  ◀──[Completion Report]──────┘
```

Codex acts as product manager: it decomposes requirements into a structured **Task Package** with explicit acceptance criteria and hands it off to Claude Code. Claude Code executes and returns a structured **Completion Report** with per-criterion PASS/FAIL status. Codex reviews the report and either accepts or generates an incremental Change Request.

**Why it saves quota**: Precise task packages mean Claude Code executes correctly on the first attempt — no clarification loops. Structured reports mean Codex verifies acceptance without re-reading all diffs — no unnecessary back-and-forth.

**Key components**:

- **Task Package template** — Task ID, context (file paths, not pasted code), numbered requirements, constraints, verifiable acceptance criteria, test commands
- **Completion Report format** — Status (DONE / PARTIAL / BLOCKED), modified files table, AC checklist with PASS/FAIL, test output, deviations
- **Acceptance framework** — 4-step review checklist, ACCEPT declaration format, Change Request format (incremental, references original Task ID)
- **Quality checklist** — Pre-flight self-check before handing off a task package

**Install**: Download `dist/cc-dispatch.skill` and drag it into Claude Code.

---

#### `code-review` — 双模式代码审查元技能

**Purpose**: 元技能整合两种互补审查模式。（1）Standard：5 Agent 并行五维审查（安全/性能/可维护/规范/边界）+ 置信度过滤；（2）Adversarial：恶意用户视角破坏性测试，逻辑漏洞·隐藏 Bug·思维盲点。覆盖从日常 PR 到安全审计的完整审查链路。

**两种模式**:

| 模式 | 视角 | 触发 |
|------|------|------|
| Standard | 工程质量把关 | "帮我审查代码" / `/code-review` |
| Adversarial | 攻击者视角 | "做对抗式审查" / "以攻击者视角审查" |

**推荐流水线**: Code Simplifier → Code Review standard → Code Review adversarial → 人工 Review

**Install**: 本仓库 skill 目录直接使用

---

#### `website-cloner` — AI 网站复刻器

**Purpose**: Reverse-engineer and clone any website into a clean Next.js + shadcn/ui + Tailwind v4 codebase using AI coding agents. A multi-phase pipeline that extracts design tokens, assets, and component specs from live websites, then dispatches parallel builder agents in git worktrees to reconstruct every section with pixel-perfect fidelity.

**Author**: [JCodesMore](https://github.com/JCodesMore) · Original repo: [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) (22.4K ⭐, MIT License)

**How it works**:

```
Phase 1: Reconnaissance     Phase 2: Foundation      Phase 3: Spec & Build      Phase 4: Assembly    Phase 5: QA
┌──────────────┐          ┌──────────────┐          ┌──────────────────┐      ┌──────────────┐     ┌──────────────┐
│ Screenshots  │          │ Fonts, colors│          │ Extract CSS      │      │ Wire all     │     │ Side-by-side │
│ Design tokens│──────────▶│ Types, icons │─────────▶│ Write spec file  │─────▶│ sections     │────▶│ visual diff  │
│ Behaviors    │          │ Asset dl    │          │ Dispatch builder │      │ Page-level   │     │ Fix issues   │
│ Topology     │          │ npm build   │          │ Merge worktree   │      │ behaviors    │     │ Test interact│
└──────────────┘          └──────────────┘          └──────────────────┘      └──────────────┘     └──────────────┘
```

**Key features**:

- **Pixel-perfect emulation** — exact CSS values via `getComputedStyle()`, not approximate Tailwind classes
- **Multi-agent parallel build** — one builder agent per section/component, working in isolated git worktrees
- **Comprehensive extraction** — design tokens, fonts, all image/video assets, inline SVGs, real text content, favicons
- **Behavior-aware cloning** — extracts not just static appearance but scroll-driven changes, hover states, click interactions, multi-state components (tabs, accordions, carousels)
- **Component spec files** — every component gets a detailed specification with exact CSS values, interaction model, responsive behavior, and per-state content before any builder is dispatched
- **Visual QA pass** — side-by-side comparison, section by section, at multiple viewport widths
- **12-agent platform support** — Claude Code (recommended), Codex CLI, OpenCode, Copilot, Cursor, Windsurf, Gemini CLI, Cline, Roo Code, Continue, Amazon Q, Augment Code, Aider
- **Guided by 9 core principles** — completeness beats speed, small tasks perfect results, real content real assets, foundation first, extract behavior not just appearance, identify interaction model first, extract every state, spec files are source of truth, build must always compile

**Tech stack of generated clones**: Next.js 16 (App Router) · React 19 · TypeScript strict · shadcn/ui · Tailwind CSS v4 · oklch design tokens

**Use cases**:

- **Platform migration** — rebuild a site from WordPress/Webflow/Squarespace into modern Next.js
- **Lost source code** — recover the codebase when the repo is gone, developer left, or stack is legacy
- **Learning** — deconstruct how production sites achieve specific layouts, animations, and behaviors

**Not intended for**: phishing/impersonation, passing off someone's design as your own, violating terms of service.

**Trigger examples**:
- "克隆这个网站 https://example.com" / "帮我复刻这个页面"
- "Copy this website" / "Make a pixel-perfect clone of..." / "Rebuild this site in Next.js"
- "/clone-website https://example.com"
- "帮我用 Next.js 重建这个网站"

**Install**: `npx skills add website-cloner -g -y` (from local). Or download from `website-cloner/` directory.

---

#### `claude-to-im` — Claude to IM Bridge

**Purpose**: Bridges Claude Code or Codex sessions to instant messaging platforms (Telegram, Discord, Feishu/Lark, QQ, WeChat) so you can chat with your AI coding agent from your phone. Bidirectional message forwarding with streaming preview, inline permission approval buttons, and session persistence.

**Supported IMs**: Telegram, Discord, Feishu/Lark, QQ, WeChat

**Subcommands**: `setup`, `start`, `stop`, `status`, `logs`, `reconfigure`, `doctor`

**Prerequisites**: Node.js ≥ 20, Claude Code CLI or Codex CLI.

**Install**: Download `dist/claude-to-im-skill.skill` and drag it into Claude Code. Or: `npx skills add op7418/Claude-to-IM-skill`

---

#### `superpowers` — AI 软件开发方法论 · Superpowers

**Purpose**: 一套完整的 AI 软件开发方法论，包含 20+ 可自由组合的 Skill。核心五步流程：头脑风暴（苏格拉底式追问）→ Git Worktree 隔离 → 任务规划（拆成 2-5 分钟小任务）→ 子 Agent 驱动开发（两级审查）→ 分支收尾。

**Workflow**:

```
brainstorming → using-git-worktrees → writing-plans → subagent-driven-development → finishing-a-development-branch
```

**Key features**:
- **苏格拉底式追问** — 写完代码前把所有需求问清楚，杜绝"先斩后奏"
- **子Agent驱动开发** — 每完成一个任务，全新子Agent做两级审查（Spec审查+代码质量审查）
- **Critical 阻断机制** — 查出 Critical 问题直接阻断后续流程，不修好别想往下走
- **Git Worktree 隔离** — 每个功能在独立分支开发，互不干扰
- **GitHub 22 万 Star** — 社区验证的方法论

**Install**: `/plugin install superpowers@claude-plugins-official`（Claude Code 插件）

---

#### `planning-with-files` — 开发规划持久化

**Purpose**: 把所有开发规划、设计决策、进度追踪强制写入项目 Markdown 文件里，解决上下文压缩导致的状态丢失问题。下次开新对话，Claude Code 读文件即可恢复全部上下文。

**Key features**:
- **强制持久化** — 每次设计讨论后自动更新对应 plan 文件，不是"建议"而是"必须"
- **状态恢复** — 新对话中自动读取 plan 文件，无需重复解释之前的设计决策
- **与 Superpowers 互补** — Superpowers 管流程约束，Planning with Files 管状态持久化

**Install**: `/plugin install planning-with-files@claude-plugin-directory`（Claude Code 插件）

**Usage**: 对 Claude Code 说 `plan this feature` 即可启动。

---

#### `code-simplifier` — AI 代码二次优化

**Purpose**: 在代码生成后自动做二次优化——不改代码行为，只优化结构和可读性。消除重复代码、减少嵌套层级、简化复杂逻辑、提取公共可复用函数。代码行数通常减少 30-40%。

**Key features**:
- **不改行为** — 功能逻辑原封不动，只优化结构和可读性
- **消除重复** — 合并相同逻辑块，提取重复模式
- **减少嵌套** — if 嵌套从 4-5 层降到 1-2 层
- **行数减少 30-40%** — 实测数据

**Install**: `/plugin install code-simplifier@claude-plugin-directory`（Claude Code 插件）

**Usage**: `/simplify` 或对 Claude Code 说 "简化刚才生成的代码"

---

#### `webapp-testing` — 基于 Playwright 的自动化前端测试

**Purpose**: Anthropic 官方出品，底层基于 Playwright。一句话驱动全流程：自动写测试脚本 → 启动浏览器 → 执行测试 → 截屏输出结果。

**Key features**:
- **一句话测试** — "测一下登录流程"，自动完成所有步骤
- **真实浏览器环境** — Playwright Chromium，不是模拟
- **自动截图** — 每一步都有截图佐证，适合部署前回归对比
- **Anthropic 官方出品** — 质量有保证

**Install**: `/plugin install webapp-testing@claude-plugin-directory`（Claude Code 插件）+ `npx playwright install chromium`

---

#### `ralph-loop` — 循环开发机制

**Purpose**: 防止 AI 提前结束未完成任务的 bash 循环脚本。每次迭代启动全新 AI 实例（干净上下文），从 PRD 挑未完成任务 → 实现 → 测试 → 提交 → 标记完成 → 写入 progress.txt → 下一轮。直到所有任务完成。

**Key features**:
- **上下文隔离** — 每轮全新上下文，没有历史包袱，质量一致
- **自动化循环** — 无人值守下持续开发，直到所有 story 完成
- **progress.txt 状态追踪** — 每轮只读关键信息，不加载冗余历史

**前置条件**：PRD story 必须小到一个上下文窗口完成；项目必须配 typecheck 和测试。

**Install**: `git clone https://github.com/snarktank/ralph.git && cp -r ralph/scripts ./ && ./scripts/ralph/ralph.sh`

---

#### `repo-evaluator` — GitHub 仓库评估器

**Purpose**: 多 Agent 并行评估任意开源项目的 6 类 30 项指标：社区健康、维护性、安全性、文档质量、采纳度、代码质量。每项指标附源 URL + 时间戳，输出结构化评分报告。

**6 维评估**: 社区健康度 · 维护性 · 安全性 · 文档质量 · 采纳度 · 代码质量（等权重）

**Key features**:
- 6 Agent 并行评估，证据驱动可追溯
- 适合开源选型、依赖审查、自评改进、投资尽调
- "对比这三个类似的开源项目"→ 3×6 Agent 并行

**Install**: `npx skills add maxamillion/skill-oss-project-kpi-evaluation`

---

#### `mcp-builder` — MCP Server 开发引导

**Purpose**: Anthropic 官方出品的 MCP Server 四阶段开发引导工具。定义工具接口 → 实现业务逻辑 → 处理错误和边界情况 → 测试和部署，每一步都带着你做。

**Key features**:
- **四阶段引导** — 不是丢一个模板，是每一步带着做
- **边界情况覆盖** — 认证配置、超时处理、并发限制等常见坑都有提示
- **官方示例** — Anthropic 维护了十几个高质量 MCP Server 示例

**Install**: `/plugin install mcp-builder@claude-plugin-directory`（Claude Code 插件）

---

### 🎨 Design & Frontend

---

#### `ui-ux-pro-max` — Design Intelligence for AI Coding Agents

**Purpose**: AI-powered design toolkit with 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, and 99 UX guidelines across 16 tech stacks. v2.0 Design System Generator: describe your project → get a complete design system with pattern, colors, typography, effects, and anti-patterns.

**Tech stacks (16)**: HTML+Tailwind, React, Next.js, shadcn/ui, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Jetpack Compose, Angular, Laravel, JavaFX.

**Install**: `npx uipro-cli init --ai <platform>`. Or download `dist/ui-ux-pro-max-skill.skill` and drag into Claude Code.

---

#### `dog-frontier` — 前端设计综合技能系统

**Purpose**: A comprehensive frontend design meta-skill that integrates 19 specialized skills through structured multi-turn dialogue. Covers the full chain: UI/UX design systems → Tailwind/shadcn components → Vue/React framework patterns → CSS expertise → landing pages → animation/video → brand design → design tokens (3-layer architecture) → anti-AI-taste design review.

**Integrated skills (19)**: ui-ux-pro-max, frontend-design, shadcn-ui (18.5K installs), tailwind-design-system (1.6K), shadcn-vue (727), vue-component-patterns, css-styling-expert, vanilla-web, brand, design-system, ui-styling, landing-page-generator (1.2K), liquid-theme-standards (1.9K), html-video, sprite-animation, humanizer-zh, taste-skill (反AI味审查), shadcn-tailwind — all with full attribution.

**5-phase workflow**:
```
Discovery → Design System → Implementation → Handoff → Quality Review
   │            │               │            │              │
   └─Gate 1─────┘─Gate 2────────┘─Gate 3─────┘─Gate 4──────┘─Gate 5
```

**Key features**:
- Structured multi-turn dialogue to precisely understand requirements
- Auto-generates complete design system (style + colors + fonts + effects + anti-patterns)
- Routes to optimal skill combination based on tech stack and task type
- 6-dimension quality review (30-item checklist, ≥22/30 pass threshold)
- Structured handoff formats between phases
- All integrated skills fully attributed in ATTRIBUTIONS.md

**Trigger examples**:
- "帮我设计一个 AI SaaS 落地页" → Full 5-phase workflow
- "审查这个仪表盘的 UX" → Phase 5 review only
- "生成设计系统,产品是健康养生App" → Phase 2 design system
- "写一个 Vue 3 数据表格组件" → Phase 3 component generation
- "帮我把这段文案去 AI 味" → Phase 5 copy review

**Install**: `npx skills add dog-frontier -g -y` (from local). Or download `dist/dog-frontier.skill`.

---

#### `html-video` — HTML→Video Meta-Layer for Coding Agents

**Purpose**: Turn prompts, article links, or GitHub repos into multi-frame animated MP4 videos by letting coding agents pick rendering engines, fill curated templates, and render locally via headless Chromium + ffmpeg.

**How it works**:

```
  prompt / link / repo
        │
        ▼
  ① source fetch        studio pulls the URL or repo server-side
        │
        ▼
  ② agent loop          agent reads the material + template style, emits a
        │               content-graph (storyboard) + one HTML block per frame
        ▼
  ③ engine render       headless Chromium records animated HTML → webm
        │
        ▼
  ④ ffmpeg              each webm → mp4 (libx264), concat into one video
        │
        ▼
      your.mp4
```

**Key features**:

- **14 coding agent backends** — Open Design (Vela), Windsurf CLI, Trae CLI, Claude Code, Cursor, Codex, Gemini, Grok, Qwen, OpenCode, Copilot, Aider, Hermes, Anthropic API — auto-detected and switchable
- **21 curated templates** — data viz (NYT-style charts), title cards & VFX, heroes & cinematics, product promos, outros, explainer scaffolds — all license-clean with provenance trail
- **Article / repo → video** — paste a URL or GitHub repo; studio fetches content server-side (WeChat 公众号 supported) and builds the video from real content
- **Multi-frame storyboards** — content-graph drives multi-scene videos; edit per-frame text inline, reorder, re-render
- **AI soundtrack** — optional background music + narration via MiniMax, mixed into the exported MP4
- **Pluggable engines** — Hyperframes (shipped), Remotion (native support), with Motion Canvas/Revideo and Manim on the roadmap
- **Real MP4 render** — headless Chromium + ffmpeg (libx264), locally — no cloud render, no per-clip fee
- **Apache-2.0** — no per-render fees, no seat caps

**Quick start**:

```bash
cd html_video
pnpm install && pnpm -r build
node packages/cli/dist/bin.js studio    # opens at http://127.0.0.1:3071
```

**Studio workflow**: pick a template → chat with your agent → edit per-frame text → add soundtrack → export MP4.

**CLI utilities**:

```bash
node packages/cli/dist/bin.js doctor
node packages/cli/dist/bin.js search-templates --intent "data chart" --top 3
node packages/cli/dist/bin.js project-create --name "my-video" --template frame-glitch-title
```

**Prerequisites**: Node.js 20+, pnpm 9+, ffmpeg, Chromium (Playwright).

**Install**: Download `dist/html-video.skill` and drag it into Claude Code.

---

#### `lottie-animation` — Lottie 动画生成 + Prompt 优化层

**Purpose**: 一句话让 Claude Code 生成轻量 Lottie 动画动效。

**Workflow**:

```
1. User Input — Receive natural language animation request
2. Prompt Optimization — Auto-optimize prompt using five principles: FPS/frame count, controls, materials, easing, camera movement
3. User Review — Show optimized prompt; allow user to modify and confirm
4. Animation Generation — Call text-to-lottie to generate Lottie JSON
5. Output — Return the Lottie animation file
```

**Key features**:
- **Prompt optimization layer** — Automatically enhances your prompt based on five animation principles (FPS/frame count, controls, materials, easing, camera movement) before generation
- **User review cycle** — Displays the optimized prompt for your approval or modification before committing to generation
- **Lightweight Lottie output** — Generates vector-based Lottie JSON animations suitable for web, mobile, and UI micro-interactions
- **Natural language input** — Describe what you want in plain Chinese or English; no animation expertise required

**Install**: `npx skills add diffusionstudio/lottie` (upstream) + Download `dist/lottie-animation.skill` for the prompt optimization layer.

---

#### `brand-workshop` — 品牌全案设计工作坊

**Purpose**: 三阶段品牌设计（Discovery→Concept→Creation），输出完整品牌标识包：Logo 多方案、品牌标语、品牌简介、DESIGN.md 设计令牌。

**Key features**:
- Logo 多方案比选，每种方案有设计理念说明
- 3-5 个品牌标语候选，附适用场景
- DESIGN.md 设计令牌（颜色/字体/间距体系）

**Install**: `/plugin marketplace add sorawit-w/agent-skills` + `/plugin install agent-skills@sorawit-w`

---

#### `pixel-art` — 像素画工作室

**Purpose**: 内置设计系统的像素画工具，输出真正的网格对齐像素 PNG/SVG。支持复古游戏、等距视角、角色精灵等风格。

**Key features**:
- 复古游戏风格 (8-bit / 16-bit)
- 等距视角像素建筑和场景
- 角色精灵含行走帧动画
- 输出 PNG/SVG，可直接用于游戏和网站

**Install**: `/plugin marketplace add sorawit-w/agent-skills` + `/plugin install agent-skills@sorawit-w`

---

#### `dog-poster` — 海报设计工作室 · Dog-Poster

**Purpose**: 元技能——上游风格询问 + 下游路由到三个海报子技能。先通过三连问确定你的需求（内容来源/视觉风格/使用平台），然后自动路由：信息图风→article-poster，通用设计风→canvas-design，手工拼贴风→torn-paper-collage-poster。

**路由逻辑**:

| 你的需求 | 路由到 |
|----------|--------|
| 文章/链接→信息图 | article-poster |
| 活动/产品→宣传海报 | canvas-design |
| 艺术感→手工质感 | torn-paper-collage-poster |
| 不确定 → "三种风格各来一张" | 三子技能并行生成 |

**Install**: 三个子技能各自安装（article-poster / canvas-design / torn-paper-collage-poster）

---

#### `presentation-design` — 演示设计板生成器

**Purpose**: 生成 6 页高级演示设计板（亮/暗双模式），合成为一张复合预览图，适合向客户或投资人展示设计方案。

**Key features**:
- 6 页设计板：封面 + 4 页内容 + 封底
- 亮色/暗色一键切换
- 命名布局库统一视觉语言

**Install**: `npx skills add MagicCube/agentara --skill presentation-design -y -g`

---

#### `article-poster` — 文章→信息图海报

**Purpose**: 从文章 URL 或文本自动生成精美信息图海报，适合社交媒体传播（小红书、公众号、Twitter）。

**Key features**:
- 自动提取文章关键信息
- 信息图布局：数据可视化 + 要点提炼 + 金句高亮
- 多平台尺寸适配

**Install**: `npx skills add MagicCube/agentara --skill article-poster -y -g`

---

#### `canvas-design` — 程序化画布设计

**Purpose**: Anthropic 官方出品。代码生成高分辨率 PNG/PDF 图形，适合海报、传单、社交媒体图、活动物料，可直接印刷。

**Key features**:
- 程序化生成，像素级精确控制
- 高分辨率 PNG/PDF 输出
- 任意尺寸、灵活布局

**Install**: `/plugin install example-skills@anthropic-agent-skills`

---

#### `algorithmic-art` — p5.js 算法艺术

**Purpose**: Anthropic 官方出品。用 p5.js 创作生成艺术——流场、粒子系统、分形、Perlin 噪声。每段代码都是独一无二的艺术品。

**Key features**:
- 流场 (Flow Fields)、粒子系统、递归分形
- 种子随机——同一种子永远生成同一幅画
- 多种调色板：复古、赛博朋克、自然

**Install**: `/plugin install example-skills@anthropic-agent-skills`

---

#### `slack-gif-creator` — Slack GIF 动图

**Purpose**: Anthropic 官方出品。创建 Slack 优化的动画 GIF——Emoji 128×128、消息 480×480，自动适配限制。

**Key features**:
- Emoji / 消息 GIF / 演示 GIF 三种规格
- 自动优化帧率和文件大小
- 从截图、录屏、代码动画生成

**Install**: `/plugin install example-skills@anthropic-agent-skills`

---

#### `theme-factory` — 主题工厂

**Purpose**: Anthropic 官方出品。10 套预设主题 + 自定义即时生成，一键应用到幻灯片/文档/HTML，含亮暗双模式。

**Key features**:
- 10 套预设主题（字体+颜色+间距+圆角+阴影）
- 亮色/暗色双模式
- 输出 CSS 变量 / Tailwind 配置 / DESIGN.md

**Install**: `/plugin install example-skills@anthropic-agent-skills`

---

#### `soviet-storybook-grotesque` — 苏联童书怪诞风

**Purpose**: 把照片变成粗糙褪色的东欧儿童书籍插图，配荒诞手写押韵诗。一种独特而有趣的艺术风格转换。

**Key features**:
- 苏联童书印刷质感——灰绿、棕黄、褪色红
- 怪诞人物比例 + 手写押韵诗
- 泛黄纸底 + 粗糙边缘

**Install**: `npx skills add MagicCube/agentara --skill soviet-storybook-grotesque -y -g`

---

#### `torn-paper-collage-poster` — 撕纸拼贴海报

**Purpose**: 手工感极强的编辑式拼贴海报——撕纸层叠 + 粗糙排版 + 邮票 + 胶带 + 贴纸 + 复印机纹理。适合独立杂志、音乐演出、艺术展览。

**Key features**:
- 撕纸层叠（不规则边缘、纤维毛边）
- 粗糙排版 + 邮票邮戳 + 胶带贴纸
- 复印机噪点纹理 + 手写注释

**Install**: `npx skills add MagicCube/agentara --skill torn-paper-collage-poster -y -g`

---

### 📝 Content & Writing

---

#### `humanizer-zh` — AI 写作去痕工具

**Purpose**: Removes AI-generated writing traces from text, making it sound more natural and human-like. Based on Wikipedia's "Signs of AI writing" guide maintained by WikiProject AI Cleanup. Detects and fixes: exaggerated symbolism, promotional language, shallow analysis, vague attributions, dash overuse, rule-of-three patterns, AI vocabulary, negative parallelism, excessive connective phrases.

**What it detects (9 patterns)**:
- 夸大的象征意义 (exaggerated symbolism)
- 宣传性语言 (promotional language)
- 肤浅分析 (shallow -ing analysis)
- 模糊归因 (vague attributions)
- 破折号过度使用 (dash overuse)
- 三段式法则 (rule-of-three)
- AI 词汇 (AI vocabulary)
- 否定式排比 (negative parallelism)
- 过多连接性短语 (excessive connective phrases)

**Workflow**: Identify patterns → rewrite problematic passages → preserve meaning → maintain tone → inject authentic personality.

**Install**: Download `dist/humanizer-zh.skill` and drag it into Claude Code. Or: `npx skills add https://github.com/op7418/Humanizer-zh.git`

---

#### `baoyu-skills` — 宝玉技能合集 · 22 Content & Productivity Skills

**Purpose**: A comprehensive collection of 22 Claude Code skills for content creation, AI-powered generation, and productivity. Created by JimLiu. Version 2.0.0, MIT-0.

**Key skills**:
- **Content**: slide decks (17 styles), SVG diagrams (9 types), educational comics (6 art styles), article illustration, infographics (21 layouts), cover images, Xiaohongshu cards, social posting (X/WeChat/Weibo)
- **AI Generation**: image gen via 11 backends, Gemini Web interaction
- **Utilities**: translation (3 modes), image compression, YouTube transcripts, URL→markdown, markdown formatting, WeChat summary, Electron extraction

**Install**: `npx skills add JimLiu/baoyu-skills -g --all`. Or download `dist/baoyu-skills.skill`.

---

#### `humanize-ppt` — 为演讲而生的PPT系统

**Purpose**: An agent-facing PPT presentation orchestrator that turns raw material into an AST (audience-state-transfer) outline — every page turn moves the audience forward. It decides per-page visual enhancement (images, SVG diagrams, Remotion video), orchestrates downstream template skills to render beautiful HTML slides, then runs a 3-round presentation checkup (演讲体检) comparing rendered pages against the outline to flag slides that "can only be looked at, not presented."

**Author**: 卡尔的AI沃兹 (微信公众号) · [LearnPrompt](https://github.com/LearnPrompt)

**How it works**:
```
Raw Material → Style Gallery (≥4 cover candidates) → AST Outline
   → Per-slide Plan (content + visual decisions)
   → Downstream Skill renders HTML (guizang-ppt / frontend-slides / etc.)
   → Presentation Checkup (3 rounds max) → Ready to Present
```

**Key features**:
- **AST outline**: Audience-state-transfer model — each slide advances understanding, not just information display
- **Style gallery**: Generates ≥4 cover candidates before committing to the full outline
- **Visual enhancement**: Decides when to use real images (via baoyu-image-gen), SVG diagrams, or Remotion video
- **Presentation checkup**: Post-render QA comparing rendered pages against outline specs — catches "eye candy only" slides
- **Downstream agnostic**: Compatible with any HTML-PPT skill (Chinese: guizang-ppt-skill, English: frontend-slides / beautiful-html-templates)

**Install**: `npx skills add LearnPrompt/humanize-ppt -g`. Or download from `humanize-ppt/` directory.

---

#### `writing-assistant` — 结构化写作助手

**Purpose**: 从大纲到草稿到润色到发表前审查，覆盖完整写作流程。适用于博客、备忘录、论文、报告、Newsletter 等各类文体。

**Key features**:
- 四阶段写作流程：Outline → Draft → Revise → Pre-publish Gate
- 多文体支持：博客/备忘录/论文/报告/Newsletter
- 风格适配：正式/半正式/随性，按场景调整

**Install**: `git clone https://github.com/lyndonkl/claude.git` (来自 lyndonkl 仓库)

---

#### `scientific-writing-editor` — 科学写作编辑

**Purpose**: 专为学术场景设计的写作助手。覆盖论文手稿、基金申请书、推荐信、审稿回复等学术文体，确保符合学术规范和期刊要求。

**Key features**:
- 论文手稿结构化编辑
- 基金申请书说服力增强
- 审稿回复（逐条回应，礼貌而坚定）
- 期刊格式适配

**Install**: `git clone https://github.com/lyndonkl/claude.git` (来自 lyndonkl 仓库)

---

#### `ghostwriter` — AI 代笔专家

**Purpose**: 用你自己的语气写消息，零 AI 痕迹。分析你的写作风格后，帮你写邮件、Slack、微信回复，读起来像你本人在打字。

**Key features**:
- 语气克隆——分析历史消息，提取语气特征
- 零 AI 痕迹——不啰嗦、不官方、不模板化
- 多平台适配——邮件/微信/Slack 自动切换正式度

**Install**: `/plugin marketplace add sorawit-w/agent-skills` + `/plugin install agent-skills@sorawit-w`

---

### 📚 Learning & Teaching

---

#### `exam-tutor` — 期末复习资料生成器

**Purpose**: Generates structured exam review materials — chapter-by-chapter tutorials and exercise class handouts — by analyzing textbook PDFs, past exam papers, and answer keys. Identifies high-frequency topics, classifies content (keep / compress / remove) with evidence, and produces quality-audited markdown output.

**Two operating modes**:

| Mode | Trigger | Output |
|------|---------|--------|
| **Lightweight** | Single knowledge point, one exercise, pure topic analysis | Single `.md` file |
| **Complete** | Full chapter or multi-chapter generation | Tutorials + exercise classes + audit files + images |

**Complete mode workflow** (6 phases):

```
Phase 0: Inventory       →  List source materials, confirm scope
Phase 1: Topic Analysis  →  Map past paper questions to chapters/knowledge points
                            Classify: keep / compress-keep / remove (with evidence)
Phase 2: Tutorial Gen    →  Per-chapter tutorials with structured template
                            (exam summary → knowledge structure → deep dives → 
                             question types → self-check checklist)
Phase 3: Exercise Class  →  Group past paper questions by topic, detailed walkthroughs
Phase 4: Quality Gates   →  12-item checklist (format, images, coverage, evidence,
                            explanations, audit files) — no report until all pass
Phase 5: Report          →  Structured completion report with open issues
```

**Output structure per chapter**:

```
output/
├── tutorials/chXX.md              # Structured tutorial with exam relevance analysis
├── exercise_classes/chXX.md       # Exercise class with detailed walkthroughs
├── assets/chXX/                   # Locally cropped images (no full-page screenshots)
└── audit/
    ├── past_paper_topic_map.csv   # Every past question → chapter/knowledge point
    ├── chXX_coverage.csv          # Per-section keep/compress/remove decisions
    ├── chXX_md_check.txt          # Markdown format self-check
    ├── chXX_text_quality_check.txt # Content quality self-check
    └── chXX_image_audit.csv       # Per-image quality audit (if images used)
```

**Subject adaptation**: Defaults to math (calculus, linear algebra). References guide for circuits/electronics, physics, CS, and chemistry/biology with subject-specific writing requirements.

**Key design principles**:
- Evidence-driven: every keep/remove decision backed by past paper question numbers
- Student-centric: every formula explained in plain language with "why", "when", and "common mistakes"
- Image quality enforced: local crops only, full-page screenshots rejected
- Strict gating: 12-item quality checklist must pass before chapter is declared complete

**Install**: Download `dist/exam-tutor.skill` and drag it into Claude Code.

---

#### `dog-tutor` — 智能教程编制系统

**Purpose**: A comprehensive tutorial generation meta-skill based on SmartTutor Generator (莫弈, 2026). Transforms any subject's learning materials into high-quality MkDocs Material format tutorials through a 6-phase guided dialogue. Topic-agnostic, audience-adaptive, with 4 analogy styles.

**Integrated from**: SmartTutor Generator v1.1 by 莫弈 — original author of the 6-phase workflow, 4-level audience model, 4-style analogy system, 5-domain configurations, and MkDocs formatting standards.

**6-phase workflow**:
```
Ingestion → Domain Analysis → Outline → Content Writing → Quality Review → Publishing
   │            │              │            │               │              │
   └─Gate 1─────┘─Gate 2───────┘─Gate 3─────┘─Gate 4────────┘─Gate 5───────┘
```

**Key features**:
- **Topic-agnostic**: Supports technology, business, academic, life, and art domains
- **4-level audience model**: absolute_beginner / beginner / intermediate / expert with auto-detection
- **4 analogy styles**: daily_life / professional / humorous / rigorous with auto-matching
- **5-dimension quality review**: format (15%) + completeness (25%) + pedagogy (25%) + practicality (20%) + analogy (15%)
- **MkDocs Material compliance**: strict formatting rules (blank-line isolation, bold-space isolation, Admonition usage)
- **3-layer classification**: domain → direction → topic with auto-categorization
- **Archive & reuse**: incremental updates, style migration, audience adjustment, multi-language

**Trigger examples**:
- "帮我生成一个 Linux 新手入门教程,4-5小时,零基础"
- "编制一份 R 语言学习材料,面向有 Python 基础的人"
- "设计一个摄影入门课程大纲"
- "写一份 LLM API 开发的入门指南"

**Install**: `npx skills add dog-tutor -g -y` (from local). Or download `dist/dog-tutor.skill`.

---

#### `learning-studio` — 学习工作室 · Learning Studio

**Purpose**: 元技能整合 4 大学习工具——studyws（任意主题→完整课程+播客）、The Knowledge Guy（PDF/EPUB→可查询书架+跨书对比）、ljg-read（中英双语苏格拉底式阅读）、Aibrary Skills（9 技能：书籍发现+3 种播客+成长计划）。覆盖课程生成→书籍消化→深度阅读→知识输出的完整学习闭环。

**4 大子技能**:
- **studyws** — 8 阶段流水线：`/sws:start→scope→research→write→diagrams→guide→slides→podcast`
- **The Knowledge Guy** — PDF/EPUB→结构化 skill，`compare <主题>` 跨书对比
- **ljg-read** — 三段标注（骨/肉/筋）+ 苏格拉底追问 + 三速阅读
- **Aibrary Skills** — 3 种播客形式（单人/对话/AI 分身辩论）+ 成长计划

**Install**: `npx studyws init` + `git clone https://github.com/vitalysim/the-knowledge-guy.git`

---

### 💼 Business & Strategy

---

#### `dbskill` — 商业诊断工具箱 · 21 Business Diagnostic Skills

**Purpose**: Business diagnostic toolbox with 21 Claude Code skills extracted from 12,307 tweets and refined into 4,176 knowledge atoms. Created by dontbesilent. Version 2.14.2, CC BY-NC 4.0.

**Key skills**:
- **Core diagnostics**: business model diagnosis (6 axioms), benchmark analysis, content quality testing, hook optimization, Xiaohongshu titles, AI writing detection
- **Methodology**: "Slow is fast", Adlerian execution diagnosis, Wittgenstein-style concept deconstruction, goal clarification, good question generation
- **State management**: save/restore/report diagnostic sessions across conversations
- **Learning & chatrooms**: interactive learning, Austrian Economics chatroom (Hayek×Mises), directed multi-role chatrooms

**Install**: `npx skills add dontbesilent2025/dbskill -g --all`. Or download `dist/dbskill.skill`.

---

### 🔍 Tools & Discovery

---

#### `family-doctor` — AI 家庭健康管理套件

**Purpose**: 26 个技能覆盖 17 个健康领域。核心差异：跨维度关联分析——血压升高自动检查钠摄入+睡眠+运动+压力。慢性病管理、营养分析、睡眠质量、ACSM 训练计划、心理健康筛查 (PHQ-9/GAD-7)、药物相互作用。

**17 大领域**: 慢性病·营养·睡眠·运动·心理·药物·生命体征·体检解读·妇儿·老年·疼痛·过敏·皮肤·消化·心血管·呼吸·中医体质

**Key features**:
- 跨维度关联分析（非孤立分析每个指标）
- 26 个专业技能模块化调用
- 本地存储，零数据泄露
- ⚠️ 辅助工具，不替代医生诊断

---

#### `find-skills` — Discover and Install Agent Skills

**Purpose**: Helps users discover, evaluate, and install agent skills from the open skills ecosystem. Searches skills.sh leaderboard and `npx skills find <query>`, verifies quality (install count, reputation, stars), and offers one-click install. Part of the vercel-labs/skills project — the `npx skills` CLI ecosystem supporting 70+ agents.

**Workflow**: Understand need → check leaderboard → search → verify quality → present → install.

**Skill categories**: Web Development, Testing, DevOps, Documentation, Code Quality, Design, Productivity.

**Install**: `npx skills add vercel-labs/agent-skills`. Or download `dist/vercel-labs-skills.skill`.

---

#### `handshake` — 协作风格校准

**Purpose**: 开工前与 Claude 的简短校准仪式。通过 6 个维度刻度（详细程度/技术深度/幽默感/质疑程度/创意自由度/简洁度）和 RPG 职业分类，让 Claude 了解你的协作偏好，从此不再给千篇一律的回答。

**Key features**:
- 6 维度协作偏好刻度
- RPG 职业分类（架构师/黑客/探险家/外交官……）
- 生成便携工作手册，跨会话生效

**Install**: `/plugin marketplace add sorawit-w/agent-skills` + `/plugin install agent-skills@sorawit-w`

---

#### `token-optimizer` — 上下文 Token 优化工具

**Purpose**: 重新组织项目文档结构，只保留 4 个核心文件在启动时自动加载（约 800 token），其他内容按需加载。实测省 90% token（11000 → 1300），一条命令 30 秒搞定。

**Key features**:
- **90% token 节省** — 实测从 11000 token 降到 1300 token
- **自动检测技术栈** — 从 package.json / requirements.txt / go.mod 读取，匹配 13 种框架模板
- **维护工具链** — `cto measure`（查看消耗）/ `cto audit`（健康检查）/ `cto compress`（压缩）/ `cto prune`（清理）
- **.claudeignore 机制** — 明确告诉 Claude Code 哪些文件别碰
- **CI 集成** — `cto audit --json` 输出机器可读结果

**Install**: `npx claude-token-optimizer init`（npm 包，30 秒完成）

**Usage**: 每周跑一次 `cto audit`，token 涨了就做一轮清理。

---

#### `vibe-sing` — 让 Claude Code 为你唱歌

**Purpose**: 读取当前会话记录 → Gemini 分析情绪 → Google Lyria 3 作曲并演唱 → 自动播放。支持 30 秒片段 (`/vibe-sing`) 和 2 分钟完整版 (`/vibe-sing pro`)。

**Key features**:
- 分析会话情绪和氛围生成对应风格的歌曲
- Google Lyria 3 作曲+人声演唱
- 约 4-8 美分一首歌
- macOS/Linux 支持

**Install**: `git clone https://github.com/harajlim/vibe-sing.git ~/.claude/skills/vibe-sing`（需 Google API Key）

---

#### `weread-skill` — 微信读书 AI 助手

**Purpose**: 连接你的微信读书账号，用 AI 搜书、查笔记、看书评、分析阅读数据。支持查阅书架、阅读统计、笔记和划线、书籍搜索、书籍详情、个性化推荐。

**Key features**:
- 查阅书架 — 快速了解藏书全貌
- 阅读统计 — 时长、天数、偏好深度分析
- 笔记和划线 — 查看和导出个人阅读笔记
- 书籍搜索 — 搜索书城，获取评分等关键信息
- 个性化推荐 — 基于阅读偏好的智能推荐

**Install**: `npx skills add Tencent/WeChatReading -g` (upstream). Or download `dist/weread-skill.skill`.

---

## Skill Categories

| Category | Skills |
|----------|--------|
| 🧠 **Thinking & Research** | first-principles, storm-research, feynman-learning, nuwa, last30days, thinking-toolkit |
| 💻 **Development** | cc-dispatch, code-review, website-cloner, claude-to-im, superpowers, planning-with-files, code-simplifier, webapp-testing, ralph-loop, mcp-builder, repo-evaluator |
| 🎨 **Design & Frontend** | ui-ux-pro-max, dog-frontier, html-video, lottie-animation, brand-workshop, pixel-art, dog-poster, presentation-design, article-poster, canvas-design, algorithmic-art, slack-gif-creator, theme-factory, soviet-storybook-grotesque, torn-paper-collage-poster |
| 📝 **Content & Writing** | humanizer-zh, baoyu-skills, humanize-ppt, writing-assistant, scientific-writing-editor, ghostwriter |
| 📚 **Learning & Teaching** | exam-tutor, dog-tutor, learning-studio |
| 💼 **Business & Strategy** | dbskill |
| 🔍 **Tools & Discovery** | find-skills, family-doctor, handshake, token-optimizer, vibe-sing, weread-skill |

---

## Adding Skills

Each skill lives in its own directory with a `SKILL.md` file. To contribute:

1. Create `your-skill-name/SKILL.md` with YAML frontmatter (`name`, `description`) and `metadata.category`
2. Package with `python scripts/package_skill.py your-skill-name/`
3. Submit a PR with the directory and the `.skill` file in `dist/`

---

## Usage Workflow

### 新项目上手流程

```
① token-optimizer     ← 第一时间运行，优化项目文档结构，省 90% token
        │
② Superpowers         ← 启用开发方法论，让 Claude Code "先问再做"
        │
③ Planning with Files ← 启用规划持久化，防止上下文丢失
        │
④ 开始开发！
```

```bash
# Step 1: 优化 token（30 秒）
npx claude-token-optimizer init

# Step 2-3: 安装插件（Claude Code 内执行）
/plugin install superpowers@claude-plugins-official
/plugin install planning-with-files@claude-plugin-directory

# Step 4: 开始开发
"帮我开发一个 XXX 功能"
# Claude Code 会走完整的 Superpowers 五步流程
```

### 日常开发流水线

```
需求讨论           代码编写          质量把关           部署验证
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│Superpowers│   │Superpowers│   │Code      │   │Webapp    │
│追问需求   │──▶│子Agent开发│──▶│Simplifier│──▶│Testing   │
│Plan记录   │   │逐个实现   │   │Code      │   │截图对比   │
│          │    │          │    │Review    │    │          │
└──────────┘    └──────────┘    └──────────┘    └──────────┘
                                                     │
                                                     ▼
                                                ✅ 部署上线
```

**在每个阶段对 Claude Code 说什么：**

| 阶段 | 你说 |
|------|------|
| 需求讨论 | "帮我 brainstorm 这个功能" |
| 规划记录 | "plan this feature" |
| 开发实现 | "开始实现第 3 个 task" |
| 代码优化 | "简化刚才生成的代码" 或 `/simplify` |
| 代码审查 | "帮我审查代码" 或 `/code-review` |
| 部署测试 | "跑一下所有页面的截图测试" |

### 项目维护周期

```
每周:
  cto audit                    ← 检查 token 消耗是否健康
  /code-review                 ← 对本周改动做一次全面审查

每月:
  cto prune                    ← 清理过期文档
  检查 Planning files 是否过时 ← 确保规划文件和实际代码一致

大版本前:
  Webapp Testing 全页面截图    ← 防止回归
  Code Review --effort high    ← 高强度全面审查
```

---

## Skill Combination Recommendations

### 🥇 必装四件套（所有项目）

```
token-optimizer → Superpowers → Planning with Files → Code Review
```

**为什么是这四个：**
- `token-optimizer`：ROI 最高的 30 秒，省 90% token，不装就亏
- `Superpowers`：改变 Claude Code 行为模式，从"先斩后奏"变成"先问再做"
- `Planning with Files`：解决上下文丢失这个 AI 编程最大的痛点
- `Code Review`：第一道自动化质量防线，5 个 Agent 并行审查

### 🥈 完整开发流水线（推荐）

```
token-optimizer → Superpowers → Planning with Files
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
              写代码（子Agent）                   需求变更
                    │                               │
                    ▼                               ▼
            Code Simplifier                  更新 Plan 文件
                    │
                    ▼
              Code Review
                    │
                    ▼
           Webapp Testing（部署前）
                    │
                    ▼
              ✅ 合并 / 部署
```

**适用场景**：中大型项目，有正式的上线流程。

### 🎨 前端项目增强包

在必装四件套基础上追加：

```
UI UX Pro Max  →  设计系统自动生成，解决"AI slop"问题
Webapp Testing →  部署前全页面截图对比
```

### 🏗️ 大项目自动化包

在完整流水线基础上追加：

```
Ralph Loop   →  PRD 驱动自动迭代，适合几十个 story 的大项目
MCP Builder  →  把内部 API 包装成 MCP 工具，让 AI 直接调用
```

### 📋 组合速查表

| 项目类型 | 推荐组合 | 安装命令 |
|----------|----------|----------|
| **小工具/脚本** | token-optimizer + Superpowers | `npx claude-token-optimizer init` + `/plugin install superpowers@...` |
| **中型 Web 应用** | 必装四件套 + Code Simplifier + Webapp Testing | 4 个 plugin + 1 个 npx + 1 个 plugin |
| **大型项目** | 完整流水线 + Ralph Loop + MCP Builder | 全部安装 |
| **前端项目** | 必装四件套 + UI UX Pro Max + Webapp Testing | 追加 2 个 |
| **后端/API 项目** | 必装四件套 + MCP Builder | 追加 MCP Builder |
| **技术文档/教程** | token-optimizer + dog-tutor + exam-tutor | 按需组合 |

---

*Built with the Claude skill-creator workflow.*
