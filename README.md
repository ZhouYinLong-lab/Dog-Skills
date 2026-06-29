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
cp -r adversarial-review ~/.claude/skills/adversarial-review
cp -r cc-dispatch ~/.claude/skills/cc-dispatch
cp -r tutor ~/.claude/skills/exam-tutor
cp -r html_video ~/.claude/skills/html-video
cp -r nuwa-skill ~/.claude/skills/nuwa
cp -r claude-to-im-skill ~/.claude/skills/claude-to-im
cp -r last30days-skill ~/.claude/skills/last30days
cp -r ui-ux-pro-max-skill ~/.claude/skills/ui-ux-pro-max
cp -r vercel-labs-skills ~/.claude/skills/find-skills
cp -r first-principles ~/.claude/skills/first-principles
cp -r baoyu-skills ~/.claude/skills/baoyu-skills
cp -r dbskill ~/.claude/skills/dbskill
cp -r humanizer-zh ~/.claude/skills/humanizer-zh
cp -r dog-frontier ~/.claude/skills/dog-frontier
cp -r dog-tutor ~/.claude/skills/dog-tutor
cp -r humanize-ppt ~/.claude/skills/humanize-ppt
cp -r website-cloner ~/.claude/skills/website-cloner
```

### Verification

```bash
ls ~/.claude/skills/
# adversarial-review/  baoyu-skills/  cc-dispatch/  claude-to-im/  dbskill/  dog-frontier/
# dog-tutor/  exam-tutor/  find-skills/  first-principles/  html-video/  humanize-ppt/
# humanizer-zh/  last30days/  nuwa/  ui-ux-pro-max/  website-cloner/
```

Once installed, skills trigger automatically when Claude detects a matching task — no special command needed.

### Trigger examples

| Skill | Try saying... |
|-------|---------------|
| `adversarial-review` | ""帮我进行对抗式审查" / "多Agent并发审查找BUG" / "adversarial review my code"" |
| `cc-dispatch` | "拆一个 Task Package 给 Claude Code" / "验收这份完成报告" |
| `exam-tutor` | "帮我生成第5章复习资料" / "分析往年卷的高频考点" / "为这道题写一份习题讲解" |
| `html-video` | "把这篇文章做成视频" / "用这个 GitHub 仓库生成一个介绍视频" / "做一个产品宣传动画" |
| `nuwa` | "蒸馏 Paul Graham 的思维方式" / "分析张一鸣的决策框架" / "造一个 skill" |
| `claude-to-im` | "帮我把 Claude 连到 Telegram" / "setup claude-to-im" / "在手机上跟 Claude 聊天" |
| `last30days` | "/last30days Cursor vs Copilot" / "research what people think about..." |
| `ui-ux-pro-max` | "推荐一个 SaaS landing page 的配色" / "生成 design system" / "dashboard 用什么字体" |
| `find-skills` | "有没有能做 PR 描述的 skill" / "find a skill for code review" |
| `first-principles` | ""从第一性原理出发" / "从本质出发重新思考" / "think from first principles"" |
| `baoyu-skills` | "帮我生成幻灯片" / "画一个架构图" / "翻译这篇文章" / "压缩图片" |
| `dbskill` | "/问诊 我的商业模式有问题吗" / "/好问题" / "/决策系统" / "/对标" |
| `humanizer-zh` | "帮我把这段文字去AI味" / "改写得更像人写的" / "去除AI写作痕迹" |
| `dog-frontier` | "帮我设计一个 AI SaaS 落地页" / "审查这个仪表盘的 UX" / "生成设计系统" / "写一个 Vue 组件" |
| `humanize-ppt` | "帮我把这份资料做成PPT" / "给我的deck做演讲体检" / "PPT渲染质检" / "帮我出个PPT大纲" |
| `dog-tutor` | "帮我生成 Linux 入门教程" / "编制一份 R 语言学习材料" / "设计课程大纲" / "写入门指南" |
| `website-cloner` | "克隆这个网站" / "帮我复刻这个页面" / "/clone-website https://..." / "Copy this website" |

---

## Skills

### `adversarial-review` — 对抗式审查 — Adversarial Review

**Purpose**: 让 AI 站在对立面对代码、方案、文章进行对抗式审查——从"我要搞崩你的系统"的角度出发，找出逻辑漏洞、安全风险、边界条件、隐藏 Bug 和思维盲点。

**Workflow**:

```
1. Define Target — Specify the code, plan, or article under review
2. Adversarial Mindset — Adopt a "I want to break your system" perspective
3. Multi-Agent Concurrent Scan — Multiple agents probe different angles simultaneously: logic flaws, security risks, boundary conditions, hidden bugs, thinking blind spots
4. Compile Findings — Structured report with categorized vulnerabilities and blind spots
5. Prioritize & Suggest — Rank findings by impact and suggest remediation strategies
```

**Key features**:
- **Adversarial review mindset** — Approaches from a malicious user perspective to uncover blind spots conventional review misses
- **Multi-agent concurrent review** — Multiple AI agents scan simultaneously from different angles for comprehensive coverage
- **Broad applicability** — Works on code, technical proposals, product plans, and articles/essays
- **Systematic vulnerability discovery** — Identifies logic flaws, security risks, boundary conditions, and hidden bugs
- **Structured reporting** — Produces organized findings with severity levels and remediation suggestions

**Install**: Download `dist/adversarial-review.skill` and drag it into Claude Code.

---

### `cc-dispatch` — Codex × Claude Code Collaboration Protocol

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

### `exam-review-generator` — 期末复习资料生成器

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

### `html-video` — HTML→Video Meta-Layer for Coding Agents

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

### `nuwa` — 女娲 · Distill Anyone's Thinking into an AI Skill

**Purpose**: A meta-skill that distills any person's way of thinking into a runnable AI skill. Launches 6 parallel research agents to scour public sources (writings, interviews, decisions, criticism, timeline), triple-verifies extracted mental models, and generates a complete SKILL.md that acts as a cognitive advisor in that person's voice.

**What it distills**: Expression DNA, 3-7 mental models, 5-10 decision heuristics, anti-patterns, values, intellectual genealogy, and honest limits.

**Workflow**: 6-agent parallel research → triple-verification framework extraction → SKILL.md construction → quality validation → dual-agent refinement.

**Already distilled figures**: Paul Graham, Zhang Yiming, Karpathy, Steve Jobs, Elon Musk, Munger, Feynman, Naval, Taleb, and more (13 person skills + 1 topic skill).

**Install**: Download `dist/nuwa-skill.skill` and drag it into Claude Code. Or: `npx skills add alchaincyf/nuwa-skill`

---

### `claude-to-im` — Claude to IM Bridge

**Purpose**: Bridges Claude Code or Codex sessions to instant messaging platforms (Telegram, Discord, Feishu/Lark, QQ, WeChat) so you can chat with your AI coding agent from your phone. Bidirectional message forwarding with streaming preview, inline permission approval buttons, and session persistence.

**Supported IMs**: Telegram, Discord, Feishu/Lark, QQ, WeChat

**Subcommands**: `setup`, `start`, `stop`, `status`, `logs`, `reconfigure`, `doctor`

**Prerequisites**: Node.js ≥ 20, Claude Code CLI or Codex CLI.

**Install**: Download `dist/claude-to-im-skill.skill` and drag it into Claude Code. Or: `npx skills add op7418/Claude-to-IM-skill`

---

### `last30days` — AI-Powered Topic Research

**Purpose**: AI agent-led search engine researching any topic across Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, and more — scored by real engagement signals (upvotes, likes, comment counts, real-money odds), not SEO. Produces HTML briefs with Best Takes, cross-source clusters, ELI5 mode, comparison mode, and competitor auto-discovery.

**Usage**: `/last30days <topic> [--mode research|compare|hiring|agent|eli5] [--save]`

**Sources (15+)**: Reddit, X, YouTube, TikTok, Instagram, HN, Polymarket, GitHub, Threads, Pinterest, Bluesky, Perplexity, general web.

**Install**: Download `dist/last30days-skill.skill` and drag it into Claude Code. Or: `npx skills add mvanhorn/last30days-skill -g`

---

### `ui-ux-pro-max` — Design Intelligence for AI Coding Agents

**Purpose**: AI-powered design toolkit with 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, and 99 UX guidelines across 16 tech stacks. v2.0 Design System Generator: describe your project → get a complete design system with pattern, colors, typography, effects, and anti-patterns.

**Tech stacks (16)**: HTML+Tailwind, React, Next.js, shadcn/ui, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Jetpack Compose, Angular, Laravel, JavaFX.

**Install**: `npx uipro-cli init --ai <platform>`. Or download `dist/ui-ux-pro-max-skill.skill` and drag into Claude Code.

---

### `find-skills` — Discover and Install Agent Skills

**Purpose**: Helps users discover, evaluate, and install agent skills from the open skills ecosystem. Searches skills.sh leaderboard and `npx skills find <query>`, verifies quality (install count, reputation, stars), and offers one-click install. Part of the vercel-labs/skills project — the `npx skills` CLI ecosystem supporting 70+ agents.

**Workflow**: Understand need → check leaderboard → search → verify quality → present → install.

**Skill categories**: Web Development, Testing, DevOps, Documentation, Code Quality, Design, Productivity.

**Install**: `npx skills add vercel-labs/agent-skills`. Or download `dist/vercel-labs-skills.skill`.

---

### `first-principles` — 第一性原理思考 — First Principles Thinking

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

### `baoyu-skills` — 宝玉技能合集 · 22 Content & Productivity Skills

**Purpose**: A comprehensive collection of 22 Claude Code skills for content creation, AI-powered generation, and productivity. Created by JimLiu. Version 2.0.0, MIT-0.

**Key skills**:
- **Content**: slide decks (17 styles), SVG diagrams (9 types), educational comics (6 art styles), article illustration, infographics (21 layouts), cover images, Xiaohongshu cards, social posting (X/WeChat/Weibo)
- **AI Generation**: image gen via 11 backends, Gemini Web interaction
- **Utilities**: translation (3 modes), image compression, YouTube transcripts, URL→markdown, markdown formatting, WeChat summary, Electron extraction

**Install**: `npx skills add JimLiu/baoyu-skills -g --all`. Or download `dist/baoyu-skills.skill`.

---

### `dbskill` — 商业诊断工具箱 · 21 Business Diagnostic Skills

**Purpose**: Business diagnostic toolbox with 21 Claude Code skills extracted from 12,307 tweets and refined into 4,176 knowledge atoms. Created by dontbesilent. Version 2.14.2, CC BY-NC 4.0.

**Key skills**:
- **Core diagnostics**: business model diagnosis (6 axioms), benchmark analysis, content quality testing, hook optimization, Xiaohongshu titles, AI writing detection
- **Methodology**: "Slow is fast", Adlerian execution diagnosis, Wittgenstein-style concept deconstruction, goal clarification, good question generation
- **State management**: save/restore/report diagnostic sessions across conversations
- **Learning & chatrooms**: interactive learning, Austrian Economics chatroom (Hayek×Mises), directed multi-role chatrooms

**Install**: `npx skills add dontbesilent2025/dbskill -g --all`. Or download `dist/dbskill.skill`.

---

### `humanizer-zh` — AI 写作去痕工具

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

### `dog-frontier` — 前端设计综合技能系统

**Purpose**: A comprehensive frontend design meta-skill that integrates 18 specialized skills through structured multi-turn dialogue. Covers the full chain: UI/UX design systems → Tailwind/shadcn components → Vue/React framework patterns → CSS expertise → landing pages → animation/video → brand design → design tokens (3-layer architecture).

**Integrated skills (18)**: ui-ux-pro-max, frontend-design, shadcn-ui (18.5K installs), tailwind-design-system (1.6K), shadcn-vue (727), vue-component-patterns, css-styling-expert, vanilla-web, brand, design-system, ui-styling, landing-page-generator (1.2K), liquid-theme-standards (1.9K), html-video, sprite-animation, humanizer-zh, shadcn-tailwind — all with full attribution.

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

### `humanize-ppt` — 为演讲而生的PPT系统

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

### `dog-tutor` — 智能教程编制系统

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

### `website-cloner` — AI 网站复刻器

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

## Adding Skills

Each skill lives in its own directory with a `SKILL.md` file. To contribute:

1. Create `your-skill-name/SKILL.md` with YAML frontmatter (`name`, `description`)
2. Package with `python scripts/package_skill.py your-skill-name/`
3. Submit a PR with the directory and the `.skill` file in `dist/`

---

*Built with the Claude skill-creator workflow.*
