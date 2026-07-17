# Dog-Skills

<div align="center">

[![Skills](https://img.shields.io/badge/Skills-117-blue?style=for-the-badge&logo=claude&logoColor=white)](https://github.com/ZhouYinLong-lab/Dog-Skills)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://github.com/ZhouYinLong-lab/Dog-Skills/blob/main/LICENSE)
[![CI](https://img.shields.io/badge/CI-passing-brightgreen?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/ZhouYinLong-lab/Dog-Skills/actions)
[![Category](https://img.shields.io/badge/Categories-7-orange?style=for-the-badge)](https://github.com/ZhouYinLong-lab/Dog-Skills#skills)
[![PRs](https://img.shields.io/badge/PRs-welcome-purple?style=for-the-badge)](https://github.com/ZhouYinLong-lab/Dog-Skills/pulls)

</div>

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
cp -r comprehensive-thinking ~/.claude/skills/comprehensive-thinking
cp -r first-principles ~/.claude/skills/first-principles
cp -r feynman-learning ~/.claude/skills/feynman-learning
cp -r gpt-researcher ~/.claude/skills/gpt-researcher
cp -r hv-analysis ~/.claude/skills/hv-analysis
cp -r nuwa-skill ~/.claude/skills/nuwa
cp -r last30days-skill ~/.claude/skills/last30days
cp -r life-designer ~/.claude/skills/life-designer
cp -r ljg-blind ~/.claude/skills/ljg-blind
cp -r ljg-book ~/.claude/skills/ljg-book
cp -r ljg-constraint ~/.claude/skills/ljg-constraint
cp -r ljg-rank ~/.claude/skills/ljg-rank
cp -r ljg-roundtable ~/.claude/skills/ljg-roundtable
cp -r ljg-skills ~/.claude/skills/ljg-skills
cp -r storm-research ~/.claude/skills/storm-research
cp -r thinking-toolkit ~/.claude/skills/thinking-toolkit

# 💻 Development
cp -r architecture-diagram ~/.claude/skills/architecture-diagram
cp -r cc-dispatch ~/.claude/skills/cc-dispatch
cp -r code-review ~/.claude/skills/code-review
cp -r website-cloner ~/.claude/skills/website-cloner
cp -r claude-to-im-skill ~/.claude/skills/claude-to-im
cp -r superpowers ~/.claude/skills/superpowers
cp -r planning-with-files ~/.claude/skills/planning-with-files
cp -r code-simplifier ~/.claude/skills/code-simplifier
cp -r fireworks-tech-graph ~/.claude/skills/fireworks-tech-graph
cp -r webapp-testing ~/.claude/skills/webapp-testing
cp -r ralph-loop ~/.claude/skills/ralph-loop
cp -r mcp-builder ~/.claude/skills/mcp-builder
cp -r neat-freak ~/.claude/skills/neat-freak
cp -r repo-evaluator ~/.claude/skills/repo-evaluator

# 🎨 Design & Frontend
cp -r animation-craft ~/.claude/skills/animation-craft
cp -r apple-design ~/.claude/skills/apple-design
cp -r dashi-ppt ~/.claude/skills/dashi-ppt
cp -r design-buddy ~/.claude/skills/design-buddy
cp -r dog-ppt ~/.claude/skills/dog-ppt
cp -r excalidraw-diagram ~/.claude/skills/excalidraw-diagram
cp -r text-logic-diagram ~/.claude/skills/text-logic-diagram
cp -r ui-ux-pro-max-skill ~/.claude/skills/ui-ux-pro-max
cp -r dog-frontier ~/.claude/skills/dog-frontier
cp -r html-video ~/.claude/skills/html-video
cp -r huashu-design ~/.claude/skills/huashu-design
cp -r ljg-card ~/.claude/skills/ljg-card
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
cp -r baokuan-title-generator ~/.claude/skills/baokuan-title-generator
cp -r humanizer-zh ~/.claude/skills/humanizer-zh
cp -r baoyu-skills ~/.claude/skills/baoyu-skills
cp -r humanize-ppt ~/.claude/skills/humanize-ppt
cp -r khazix-writer ~/.claude/skills/khazix-writer
cp -r ppt-master ~/.claude/skills/ppt-master
cp -r writing-assistant ~/.claude/skills/writing-assistant
cp -r scientific-writing-editor ~/.claude/skills/scientific-writing-editor
cp -r ghostwriter ~/.claude/skills/ghostwriter
cp -r huashu-proofreading ~/.claude/skills/huashu-proofreading
cp -r huashu-slides ~/.claude/skills/huashu-skills

# 📚 Learning & Teaching
cp -r dog-tutor ~/.claude/skills/dog-tutor
cp -r learning-studio ~/.claude/skills/learning-studio
cp -r teach ~/.claude/skills/teach
cp -r tutor ~/.claude/skills/exam-tutor

# 💼 Business & Strategy
cp -r creator-buddy ~/.claude/skills/creator-buddy
cp -r dbskill ~/.claude/skills/dbskill
cp -r huashu-data-pro ~/.claude/skills/huashu-data-pro
cp -r ljg-invest ~/.claude/skills/ljg-invest
cp -r minimalist-entrepreneur ~/.claude/skills/minimalist-entrepreneur

# 🔍 Tools & Discovery
cp -r agency-agents-zh ~/.claude/skills/agency-agents-zh
cp -r read-buddy ~/.claude/skills/read-buddy
cp -r topic-collector ~/.claude/skills/topic-collector
cp -r vercel-labs-skills ~/.claude/skills/find-skills
cp -r weread-skill ~/.claude/skills/weread-skill
cp -r token-optimizer ~/.claude/skills/token-optimizer
cp -r handshake ~/.claude/skills/handshake
cp -r markitdown ~/.claude/skills/markitdown
cp -r vibe-sing ~/.claude/skills/vibe-sing
cp -r family-doctor ~/.claude/skills/family-doctor
```

### Verification

```bash
ls ~/.claude/skills/
# 🧠: comprehensive-thinking/  feynman-learning/  first-principles/  gpt-researcher/  hv-analysis/  last30days/  life-designer/  ljg-blind/  ljg-book/  ljg-constraint/  ljg-rank/  ljg-roundtable/  ljg-skills/  nuwa/  storm-research/  thinking-toolkit/
# 📚: dog-tutor/  exam-tutor/  learning-studio/  teach/
# 💻: architecture-diagram/  cc-dispatch/  claude-to-im/  code-review/  code-simplifier/  fireworks-tech-graph/  mcp-builder/  neat-freak/  planning-with-files/  ralph-loop/  repo-evaluator/  superpowers/  webapp-testing/  website-cloner/
# 🎨: algorithmic-art/  animation-craft/  apple-design/  article-poster/  brand-workshop/  canvas-design/  dashi-ppt/  design-buddy/  dog-frontier/  dog-ppt/  excalidraw-diagram/  html-video/  huashu-design/  ljg-card/  lottie-animation/  pixel-art/  dog-poster/  presentation-design/  slack-gif-creator/  soviet-storybook-grotesque/  text-logic-diagram/  theme-factory/  torn-paper-collage-poster/  ui-ux-pro-max/
# 📝: baokuan-title-generator/  baoyu-skills/  ghostwriter/  huashu-proofreading/  huashu-skills/  humanize-ppt/  humanizer-zh/  khazix-writer/  ppt-master/  scientific-writing-editor/  writing-assistant/
# 💼: creator-buddy/  dbskill/  huashu-data-pro/  ljg-invest/  minimalist-entrepreneur/
# 🔍: agency-agents-zh/  family-doctor/  find-skills/  handshake/  markitdown/  read-buddy/  token-optimizer/  topic-collector/  vibe-sing/  weread-skill/
```

Once installed, skills trigger automatically when Claude detects a matching task — no special command needed.

---

## Trigger examples

### 🧠 Thinking & Research

| Skill | Try saying... |
|-------|---------------|
| [`comprehensive-thinking`](comprehensive-thinking/) | "全面思考这个问题 / think comprehensively about this" |
| [`first-principles`](first-principles/) | "从第一性原理出发" / "从本质出发重新思考" / "think from first principles" |
| [`storm-research`](storm-research/) | "用 STORM 方法做技术调研" / "做一份深度研究简报" / "Stanford STORM research" |
| [`feynman-learning`](feynman-learning/) | "用费曼学习法帮我理解" / "用费曼技巧深度学习" / "Feynman technique" |
| [`gpt-researcher`](gpt-researcher/) | "帮我做一份 LLM Agent 框架的深度调研" / "调研 2025 年 AI 安全最佳实践" / "deep research on quantum computing" |
| [`hv-analysis`](hv-analysis/) | "用横纵分析法研究一下Cursor / deep research on a product using HV analysis" |
| [`nuwa`](nuwa-skill/) | "蒸馏 Paul Graham 的思维方式" / "分析张一鸣的决策框架" / "造一个 skill" |
| [`last30days`](last30days-skill/) | "/last30days Cursor vs Copilot" / "research what people think about..." |
| [`life-designer`](life-designer/) | "帮我设计人生，我最近有点迷茫 / life design — help me figure out my next move / 我想生成三个奥德赛计划" |
| [`ljg-blind`](ljg-blind/) | "扫描我的思维盲区 / 照一照我有什么盲区 / 我昨天想漏了什么 / 检查认知盲区" |
| [`ljg-book`](ljg-book/) | "帮我拆一下《思考，快与慢》 / analyze this book's x→f→f(x)" |
| [`ljg-constraint`](ljg-constraint/) | "找这个领域的约束 / 分析这个角色的三层约束 / 这个行业的硬约束是什么 / 为什么产品和增长总吵架" |
| [`ljg-rank`](ljg-rank/) | "给这个领域降秩 / 找这个领域的根骨架 / 背后的生成器是什么 / 把复杂领域砍到极简" |
| [`ljg-roundtable`](ljg-roundtable/) | "开个圆桌讨论AI创造力 / 请几个人辩论自由意志 / 多方视角讨论这个议题" |
| [`ljg-skills`](ljg-skills/) | "安装 ljg 技能集 / ljg 有哪些技能 / ljg-skills 思维工具 / 用什么思维工具分析约束" |
| [`scientific-research`](scientific-research/) | "帮我做一份关于 XX 的科学研究综述" / "systematic literature review" / "学术文献调研" |
| [`thinking-toolkit`](thinking-toolkit/) | "帮我做校准预测" / "对这三个方案做决策矩阵" / "用贝叶斯更新我的判断" / "沙盘推演未来走向" |

### 💻 Development

| Skill | Try saying... |
|-------|---------------|
| [`architecture-diagram`](architecture-diagram/) | "帮我画一个微服务架构图 / Generate an architecture diagram for my system / 画一个 AWS serverless 架构图" |
| [`cc-dispatch`](cc-dispatch/) | "拆一个 Task Package 给 Claude Code" / "验收这份完成报告" |
| [`codex-claude-pm`](codex-claude-pm/) | "Codex 作为 PM 帮我分配任务给 Claude Code" / "拆分 task package" / "Codex 审查实现结果" |
| [`fireworks-tech-graph`](fireworks-tech-graph/) | "画一张RAG架构图，暗黑风格 / generate a microservices diagram in blueprint style" |
| [`code-review`](code-review/) | "帮我审查代码" / "/code-review"→工程质量 / "做对抗式审查" / "adversarial review"→攻击视角 |
| [`website-cloner`](website-cloner/) | "克隆这个网站" / "帮我复刻这个页面" / "/clone-website https://..." |
| [`claude-to-im`](claude-to-im-skill/) | "帮我把 Claude 连到 Telegram" / "setup claude-to-im" / "在手机上跟 Claude 聊天" |
| [`superpowers`](superpowers/) | "开始一个新功能开发" / "帮我按 Superpowers 流程来" / "brainstorm this feature" |
| [`planning-with-files`](planning-with-files/) | "plan this feature" / "帮我做开发规划" / "记录这个设计决策" |
| [`code-simplifier`](code-simplifier/) | "简化刚才生成的代码" / "优化这个模块的可读性" / "/simplify" |
| [`webapp-testing`](webapp-testing/) | "测一下登录流程" / "部署前跑截图对比" / "帮我写 e2e 测试" |
| [`ralph-loop`](ralph-loop/) | "自动迭代完成这些 story" / "启动循环开发" / "批量实现 PRD 任务" |
| [`repo-evaluator`](repo-evaluator/) | "评估这个 GitHub 仓库" / "这个开源项目靠谱吗" / "对比这三个类似项目" |
| [`mcp-builder`](mcp-builder/) | "帮我创建一个 MCP Server" / "把这个 API 包装成 MCP 工具" / "build an MCP server" |
| [`neat-freak`](neat-freak/) | "整理一下项目文档 / sync up, tidy up docs, audit the rules" |

### 🎨 Design & Frontend

| Skill | Try saying... |
|-------|---------------|
| [`algorithmic-art`](algorithmic-art/) | "生成一幅流场艺术画" / "用 p5.js 画分形" / "create generative art" |
| [`animation-craft`](animation-craft/) | "审查一下这个组件的动画" / "这个动效怎么感觉怪怪的" / "review my animations" |
| [`apple-design`](apple-design/) | "做一个 iOS 风格的底部抽屉" / "像 Apple 那样丝滑的弹窗" / "create fluid gesture animation" |
| [`article-poster`](article-poster/) | "把这篇文章做成信息图海报" / "生成知识卡片"→数据可视化风 |
| [`brand-workshop`](brand-workshop/) | "帮我做品牌全案设计" / "run brand workshop for my startup" / "设计Logo和标语" |
| [`canvas-design`](canvas-design/) | "帮我设计活动海报" / "生成宣传单页"→通用设计风 |
| [`dashi-ppt`](dashi-ppt/) | "做PPT导出PPTX" / "浏览器里编辑幻灯片" / "12套主题选一套做演示" |
| [`design-buddy`](design-buddy/) | "给这篇文章配图" / "画个用户旅程图" / "做公众号排版" / "生成故事分镜" |
| [`dog-frontier`](dog-frontier/) | "帮我设计一个 AI SaaS 落地页" / "审查这个仪表盘的 UX" / "生成设计系统" / "反AI味审查" |
| [`dog-ppt`](dog-ppt/) | "帮我做PPT但不知道用哪个工具" / "选哪个PPT skill" / "怎么做论文答辩PPT" |
| [`dog-poster`](dog-poster/) | "帮我做海报"【先问风格再路由】 / "同主题三种风格各来一张" / "poster studio" |
| [`excalidraw-diagram`](excalidraw-diagram/) | "画个架构草图，我之后还要改" / "用 Excalidraw 画个流程图" / "create a hand-drawn diagram" |
| [`html-video`](html_video/) | "把这篇文章做成视频" / "用这个 GitHub 仓库生成一个介绍视频" / "做一个产品宣传动画" |
| [`huashu-design`](huashu-design/) | "帮我设计一个AI产品落地页的视觉风格 / recommend design philosophy for my brand" |
| [`ljg-card`](ljg-card/) | "把这段话铸成一张信息图 / cast this content into a PNG visual card" |
| [`lottie-animation`](lottie-animation/) | "帮我做一个心跳动效" / "生成 Lottie 动画" / "create a Lottie animation" |
| [`pixel-art`](pixel-art/) | "画一幅像素画" / "做一个等距像素场景" / "create pixel art" |
| [`presentation-design`](presentation-design/) | "设计演示方案板" / "做一套投资人Pitch视觉方案" / "design presentation board" |
| [`slack-gif-creator`](slack-gif-creator/) | "做一张 Slack 动图" / "把录屏转 GIF 发 Slack" / "create animated emoji" |
| [`soviet-storybook-grotesque`](soviet-storybook-grotesque/) | "把这张照片变成苏联童书风" / "东欧绘本风格插画" |
| [`text-logic-diagram`](text-logic-diagram/) | "把这段论述画成逻辑图" / "文章结构可视化" / "递进/层次/对比/矩阵图" |
| [`theme-factory`](theme-factory/) | "给幻灯片换一个科技风主题" / "生成一套品牌配色" / "apply a dark theme" |
| [`torn-paper-collage-poster`](torn-paper-collage-poster/) | "做一张撕纸拼贴海报" / "Zine 风格展览海报"→手工拼贴艺术风 |
| [`ui-ux-pro-max`](ui-ux-pro-max-skill/) | "推荐一个 SaaS landing page 的配色" / "生成 design system" / "dashboard 用什么字体" |

### 📝 Content & Writing

| Skill | Try saying... |
|-------|---------------|
| [`baokuan-title-generator`](baokuan-title-generator/) | "帮我起个爆款标题" / "这篇文章叫什么好" / "标题优化" / "多组标题" |
| [`baoyu-skills`](baoyu-skills/) | "帮我生成幻灯片" / "画一个架构图" / "翻译这篇文章" / "压缩图片" |
| [`humanizer-zh`](humanizer-zh/) | "帮我把这段文字去AI味"【改已有文本】 / "改写得更像人写的" |
| [`humanize-ppt`](humanize-ppt/) | "帮我把这份资料做成PPT" / "给我的deck做演讲体检" / "PPT渲染质检" |
| [`khazix-writer`](khazix-writer/) | "写公众号文章, 帮我写稿子, 续写这篇文章 / "write a WeChat article", "continue writing this draft in Khazix's style", "turn this brief into a long-form article", "expand on this outline"" |
| [`ppt-master`](ppt-master/) | "帮我把这份PDF做成PPT" / "生成一份麦肯锡风的10页幻灯片" / "make a PowerPoint from this document" |
| [`writing-assistant`](writing-assistant/) | "帮我写一篇博客" / "写一份项目报告" / "draft a memo" |
| [`scientific-writing-editor`](scientific-writing-editor/) | "润色这篇论文" / "写基金申请书" / "回复审稿意见" |
| [`ghostwriter`](ghostwriter/) | "帮我回这封邮件（用我的语气）"【从零创作】 / "draft a reply in my voice" |
| [`huashu-proofreading`](huashu-proofreading/) | "这篇文章AI味太重了，帮我审校一下 / proofread this article to reduce AI detection rate" |
| [`huashu-slides`](huashu-slides/) | "帮我把这份资料做成PPT / make a presentation from this document" |

### 📚 Learning & Teaching

| Skill | Try saying... |
|-------|---------------|
| [`exam-tutor`](tutor/) | "帮我生成第5章复习资料" / "分析往年卷的高频考点" / "为这道题写一份习题讲解" |
| [`dog-tutor`](dog-tutor/) | "帮我生成 Linux 入门教程" / "编制一份 R 语言学习材料" / "设计课程大纲" |
| [`learning-studio`](learning-studio/) | "把机器学习做成一套课程" / "compare 三本书的观点" / "苏格拉底阅读模式" |
| [`teach`](teach/) | "teach me Rust" / "教我学吉他" / "帮我做一个交互式Python入门" / "interactive learning" |

### 💼 Business & Strategy

| Skill | Try saying... |
|-------|---------------|
| [`creator-buddy`](creator-buddy/) | "找选题 / 小红书搜热点 / 公众号爆款分析 / B站趋势 / 赛道分析" |
| [`dbskill`](dbskill/) | "/问诊 我的商业模式有问题吗" / "/好问题" / "/决策系统" / "/对标" |
| [`huashu-data-pro`](huashu-data-pro/) | "分析这份投放数据做ROI复盘 / analyze this Excel data and create a report" |
| [`ljg-invest`](ljg-invest/) | "分析这个项目值不值得投 / 写一份投资分析报告 / 这个公司是秩序创造机器吗" |
| [`minimalist-entrepreneur`](minimalist-entrepreneur/) | "帮我验证一个创业想法 / 一人公司怎么做 / 我该不该做这个功能 / validate my startup idea" |

### 🔍 Tools & Discovery

| Skill | Try saying... |
|-------|---------------|
| [`find-skills`](vercel-labs-skills/) | "有没有能做 PR 描述的 skill" / "find a skill for code review" |
| [`read-buddy`](read-buddy/) | "读网页/RSS/播客/飞书/OCR/小宇宙/X分析——帮你把信息拿回来" |
| [`topic-collector`](topic-collector/) | "今日AI热点 / 采集选题 / 看看今天有什么新闻 / daily AI briefing" |
| [`weread-skill`](weread-skill/) | "帮我查查我的书架" / "分析我的阅读统计" / "搜索某本书的评分" |
| [`wx2md`](wx2md/) | "帮我把这个公众号文章转成 Markdown" / "导出微信文章" / "WeChat article to Markdown" |
| [`token-optimizer`](token-optimizer/) | "优化项目 token 消耗" / "cto audit" / "帮我清理上下文" / "检查 token 用量" |
| [`handshake`](handshake/) | "/handshake 校准协作风格" / "帮我做 whoami 画像" / "calibrate how we work" |
| [`markitdown`](markitdown/) | "帮我把这个PDF转成Markdown / convert this Word doc to Markdown for Obsidian / 用MarkItDown批量转换文档" |
| [`vibe-sing`](vibe-sing/) | "/vibe-sing 给我来一首" / "/vibe-sing pro 完整版" / "写完了唱首歌" |
| [`agency-agents-zh`](agency-agents-zh/) | "帮我找一个XX专家 / 切换到代码审查员角色 / 用什么角色做小红书运营 / 加载安全工程师角色 / 以产品经理身份分析 / 作为前端开发者实现" |
| [`family-doctor`](family-doctor/) | "分析我最近一周的健康数据" / "血压高帮我查原因" / "解读体检报告" / "制定减脂计划" |

---

## Skills

| 🧠 Thinking `24` | 💻 Development `14` | 🎨 Design `31` | 📝 Content `24` | 📚 Learning `6` | 💼 Business `4` | 🔍 Tools `12` |
|-----------------|---------------------|----------------|----------------|-----------------|-----------------|---------------|

---

### 🧠 Thinking & Research

---

#### `comprehensive-thinking` — 全面思考

**Purpose**: Use when Codex must make a high-quality judgment on any complex problem, not only technical problems.

**Workflow**:

```
1. Define key questions and domain — surface deep goals, identify the real problem, set boundaries
2. Apply domain master theories — ground analysis in established frameworks and mental models
3. Collect critical facts and synthesize — gather evidence guided by theory, form a comprehensive theory system for the problem
4. Adversarial dialectic — strongest counter-opinion, premise analysis, competitive explanations
5. Holistic understanding and verifiable closure — systematic understanding with boundaries, validation paths, and confidence levels
```

**Key features**:
- Five-layer structured analysis from problem definition to actionable judgment
- Applicable to any high-stakes domain: architecture, strategy, engineering, financial, product
- Includes adversarial dialectic step to surface blind spots and prevent confirmation bias
- Premise dialectical analysis traces every premise to its source (fact, speculation, inference, authority, narrative inertia)
- Emphasizes systematic, hierarchical, deep understanding — not just opinions or task lists
- Designed for scenarios where cost of being wrong is high: financial truth, live trading, multi-module systems

**Install**: Download `dist/comprehensive-thinking.skill` and drag it into Claude Code.

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

#### `gpt-researcher` — 开源深度研究 Agent · GPT Researcher

**Purpose**: 基于 GPT Researcher v3.5.1（28,000+ ⭐）的开源深度研究 Agent。Planner + Executor 双智能体架构，并行抓取 20+ 来源，5 分钟生成 2000+ 字带引用研究报告。支持 Deep Research 递归模式、MCP Server 集成、本地文档研究。

**Architecture**:

```
用户提问 → Planner（拆解问题，生成研究方向）
                ↓
         Executor（并行抓取 20+ 来源）
                ↓
         Publisher（聚合、去重、引用，生成最终报告）
```

**Key features**:
- 双 Agent 架构：Planner 拆解问题 + Executor 并行抓取 + Publisher 聚合报告
- 2000+ 字研究报告，20+ 引用来源
- Deep Research 递归模式：树形探索，~5 分钟，~$0.40/次
- 报告输出到 `D:\Projects\Dog\Dog-Research/<topic-slug>/`，每次研究独立文件夹
- 支持 PDF/Word/Markdown 本地文档作为研究来源
- MCP Server 模式可接入 Claude Desktop、Cursor 等工具
- 5 种报告类型：research_report / detailed_report / resource_report / outline_report / deep_research

**Install**: `pip install gpt-researcher` + `cp -r gpt-researcher ~/.claude/skills/gpt-researcher/`

---

#### `hv-analysis` — 横纵分析法深度研究

**Purpose**: 横纵分析法深度研究——纵轴追踪历史+横轴竞品对比→交叉洞察→精美PDF报告

**Workflow**:

```
1. 纵轴分析 — 追踪目标从诞生到当下的完整生命历程，识别关键转折点和演化脉络
2. 横轴分析 — 在当下时间截面上与竞品进行系统性横向对比，评估相对位置
3. 交叉洞察 — 将纵轴与横轴的分析结果交叉，产出独到的战略洞察
4. 报告生成 — 将研究成果组织为排版精美的 PDF 研究报告
```

**Key features**:
- 双轴分析框架：纵轴追踪历史演化 + 横轴竞品对比，双维度系统性研究
- 交叉洞察：两条轴交汇产出孤立分析无法发现的独特见解
- 精美 PDF 报告：研究成果自动组织为排版精美的 PDF 文档
- 适用范围广：产品、公司、概念、人物的系统性深度研究均可应用
- 中英双语触发：支持中文（横纵分析/研究一下/深度研究）和英文（deep research/hv analysis）触发词

**Install**: Download `dist/hv-analysis.skill` and drag it into Claude Code.

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

#### `life-designer` — 人生设计师 — Life Designer

**Purpose**: 斯坦福人生设计课 AI 助手 — 基于设计思维方法论，通过深度苏格拉底式追问帮你设计三个完全不同的五年人生版本，输出个人人生设计蓝图

**Workflow**:

```
1. 现状诊断 — 评估健康/工作/娱乐/爱四个仪表盘，区分重力问题与可设计的真问题
2. 指南针校准 — 探索工作观与人生观，构建一致性指南针
3. 心流发现 — 识别能量模式与心流时刻，记录美好时光日志
4. 奥德赛计划 — 生成三个完全不同的五年人生版本（Plan A/B/C）
5. 原型行动 — 设计低成本原型访谈与体验，制定下一步行动清单
6. 蓝图输出 — 输出 8000-12000 字的个人人生设计蓝图
```

**Key features**:
- 6-9 轮深度苏格拉底式追问，帮你从迷茫到清晰
- 四仪表盘现状评估（健康/工作/娱乐/爱）
- 区分重力问题（不可解决）与可设计的真问题
- 校准工作观与人生观指南针，确保方向一致
- 生成三个完全不同的五年奥德赛计划（Plan A/B/C）
- 输出 8000-12000 字个人人生设计蓝图，含原型行动清单

**Install**: Download `dist/life-designer.skill` and drag it into Claude Code.

---

#### `ljg-blind` — 盲区扫描

**Purpose**: 盲区扫描 — 读取你与 AI 的历史对话，照出暴露的思维盲区（不是不懂的知识，是让某类真相一直看不见的思维习惯），精准定位后给出针对性补全建议。

**Workflow**:

```
1. 获取对话材料 — 读取用户与 AI 的历史对话记录
2. 扫描盲区信号 — 按 5 种信号（绕开点 / 空转框架 / 单一取景框 / 未检前提 / 相邻空缺）逐一过检
3. 选一个盲区 — 依据杠杆、真盲、对位三条判据排序，宁一个说透，不五个都点一遍
4. 深度诊断 — 分析形成机制，给出原文证据，找到它让你看不见什么
5. 补全建议 — 对症阅读（标注具体章节）+ 可操作的实践练习 + 信号词
```

**Key features**:
- 5 种盲区信号扫描：绕开点、空转框架、单一取景框、未检前提、相邻空缺
- 每条判断落到具体对话原文，凭证据不凭感觉
- 三类判据（杠杆 / 真盲 / 对位）精准选出最要紧的一个盲区
- 深度诊断：说清盲区的形成机制和为什么你自己看不见
- 对症补全方案：书籍章节、实践练习、信号词
- 有温度有毛刺的母语语气，禁用自夸修辞

**Install**: Download `dist/ljg-blind.skill` and drag it into Claude Code.

---

#### `ljg-book` — ljg-book：读懂一本书的 x → f → f(x)

**Purpose**: 拆书——x→f→f(x)逻辑链：问题→核心回答→改变什么判断或行动

**Key features**:
- 用 x→f→f(x) 逻辑链拆解任何一本书，提炼核心结构
- 精准定位作者处理的真问题（x），而非表面议题
- 提取核心回答（f）——概念、区分、框架、方法、模型或叙事视角
- 追问回答如何改变判断或行动（f(x)），将知识与决策连接
- 从"读了什么"到"改变了什么"，打通信息到行动的完整闭环

**Install**: Download `dist/ljg-book.skill` and drag it into Claude Code.

---

#### `ljg-constraint` — 约束引擎

**Purpose**: 约束引擎 — 给一个领域、专业、角色、产品或争论，找出真正框住它的几条约束，判明它们属于硬约束（世界层）、软约束（规则层）还是自设约束（认知层），看清这组约束框出的解空间，解释为什么这个角色的行为是必然的。

**Workflow**:

```
1. 铺约束候选 — 对着领域/角色追问目标、不可行假设、激励不对称、信息不对称、时间尺度
2. 分层归位 — 每条候选定位到硬约束（世界层）/软约束（规则层）/自设约束（认知层）
3. 真伪定性 — 追查被当作硬约束的条目的不可违背性
4. 找约束错配 — 在争论中找出各方默认约束的不同
5. 找矛盾对 — 识别互相打架的约束及其导致的拧巴行为
6. 找身份约束 — 找出拿掉就不再是它自己的那一条
7. 两把透镜收口 — f论（定义域）与进化论（选择压）双重审视
```

**Key features**:
- 三层约束硬度判别：硬约束（世界层不可违背）、软约束（规则层可违但有代价）、自设约束（认知层可重写）
- 从约束到解空间到行为的完整推理链——解释为什么某个角色只能那么做
- 约束错配诊断——争论双方以为在争方案，其实在争不同的题面
- 矛盾对识别——发现互相打架的约束及其导致的拧巴行为
- 输出一气呵成的分析文配 ASCII 结构图，推理自推不分章节

**Install**: Download `dist/ljg-constraint.skill` and drag it into Claude Code.

---

#### `ljg-rank` — 降秩引擎

**Purpose**: 降秩引擎 — 给一个领域，找出背后真正撑着它的几根独立的生成器。

**Workflow**:

```
1. 陈述领域 — 用户描述要分析的领域或现象集合
2. 现象枚举 — 列出该领域的所有已知现象和表现
3. 归约追问 — 不断追问"这个现象背后靠什么撑着"，砍掉冗余现象
4. 秩的判定 — 识别独立生成器（不可再少的根骨架）
5. 回推验证 — 用生成器逐一还原现象，验证是否够用
```

**Key features**:
- 十几个现象砍到不可再少的根骨架，动一根就塌
- 砍完能把现象一个个生回来才算数
- 不是总结要点，不是关键要素，是底层生成器
- 适用于理解复杂领域、找到本质驱动力、构建思维模型

**Install**: Download `dist/ljg-rank.skill` and drag it into Claude Code.

---

#### `ljg-roundtable` — 圆桌讨论

**Purpose**: 圆桌讨论 — 一个议题，一场圆桌：主持人请来 3-5 位真实人物（历史的当代的都行），定义开场，逐轮交锋，每轮收一张 ASCII 结构图，用户用指令控节奏，散场后生成完整讨论记录。

**Workflow**:

```
1. 定议题 — 用户提供议题，或主持人先问议题
2. 请人 — 邀请 3-5 位真实人物（至少一位行外人），每人附立场说明
3. 开场 — 主持人定义核心概念，每人依次发言，格式固定
4. 讨论循环 — 交替发言 → 主持人综述 + ASCII 结构图 → 用户指令（可/止/深入此节/引入新人物）
5. 收场 — 全局总结 + 完整知识网络 ASCII 图 + 开放问题列表
6. 存档 — 输出一字不差的完整讨论记录
```

**Key features**:
- 邀请 3-5 位真实人物（历史的当代的都行），多视角探讨复杂议题
- 主持人引导深度交锋，每轮只追一个核心争议点
- 每轮生成 ASCII 结构图（2x2 矩阵、光谱轴、因果环、层级树）
- 用户通过指令控制节奏：可/止/深入此节/引入新人物
- 收场生成完整知识网络图与开放问题列表
- 最终输出一字不差的完整讨论记录

**Install**: Download `dist/ljg-roundtable.skill` and drag it into Claude Code.

---

#### `ljg-skills` — ljg-skills — 思维工具 + 深度学习 + 内容可视化技能集

**Purpose**: lijigang 的 Claude Code 技能集（23 技能 + 2 工作流）— 思维工具 + 深度学习 + 内容可视化的精品集合。

**Workflow**:

```
1. 用户描述需求（思维工具 / 深度学习 / 内容可视化）
2. 元技能识别 ljg-skills 生态中的匹配子技能
3. 引导安装和使用相关子技能
4. 对用户具体任务应用选定的技能工作流
```

**Key features**:
- 元技能包装 23 个专业子技能 + 2 个工作流，一站式发现和安装
- 覆盖约束分析、降秩引擎、盲区扫描、圆桌讨论等思维工具，支持拆书、论文溯源、白话引擎等深度学习能力
- 提供投资分析、内容铸卡等可视化与决策工具
- 中英双语触发，支持丰富的自然语言描述入口
- 本 skill 为元技能包装，帮助你发现、安装和使用 ljg-skills 生态

**Install**: npx skills add lijigang/ljg-skills -g --all

---

#### `scientific-research` — 科学研究方法 — Scientific Research

**Purpose**: 系统性科学研究方法——提出研究问题、文献综述、方法论设计、结果分析与讨论。适用于学术论文、技术报告、实验设计等场景。

**Workflow**:

```
1. 问题定义 — 明确研究问题、假设与目标
2. 文献综述 — 系统检索、筛选与综合相关文献
3. 方法设计 — 选择研究方法、数据收集与分析策略
4. 结果分析 — 数据解释、可视化与发现总结
5. 讨论与结论 — 结果解读、局限性与未来工作
```

**Key features**:
- 覆盖科学研究全流程：从问题提出到论文撰写
- 结构化方法论引导，确保研究严谨性
- 适用于自然科学、社会科学、工程研究等多领域
- 内置文献综述框架与质量评估标准

**Install**: Download `dist/scientific-research.skill` and drag it into Claude Code.

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

#### `architecture-diagram` — Architecture Diagram Generator — 架构图生成器

**Purpose**: 多轮结构化提问理解系统架构，生成精美深色主题自包含 HTML+SVG 架构图

**Workflow**:

```
1. 多轮结构化提问 → 理解系统架构、组件关系、数据流向
2. 确定图表类型 → 系统架构图/云基础设施图/微服务拓扑图/安全架构图/网络拓扑图
3. 生成 HTML+SVG → 精美深色主题自包含架构图
4. 迭代优化 → 根据反馈调整布局和标注
```

**Key features**:
- 多轮结构化提问精准理解系统架构需求
- 生成深色主题自包含 HTML+SVG 文件，无需外部依赖
- 支持 6+ 架构图类型：系统架构、云基础设施、微服务拓扑、安全架构、网络拓扑、部署架构
- 输出可直接分享和嵌入文档的独立文件
- 覆盖从技术方案到演示汇报的架构可视化场景

**Install**: cp -r architecture-diagram/ ~/.claude/skills/architecture-diagram/

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

#### `codex-claude-pm` — Codex as Product Manager for Claude Code

**Purpose**: 让 Codex 担任产品经理和审查者，将软件开发任务拆分为精确的 Task Package 并委托给 Claude Code 执行。Codex 负责规划、审查和验收，Claude Code 负责实现——形成结构化的工单系统而非开放式对话。

**Workflow**:

```
Codex (PM)  ──[Task Package]──▶  Claude Code (Executor)
                                        │
Codex (QA)  ◀──[Completion Report]──────┘
```

**Key features**:
- 结构化任务拆分与验收标准
- Completion Report 格式：状态/改动文件/AC 检查清单/测试输出/偏差说明
- Change Request 增量修订机制
- 节省 Codex 配额：精确的 Task Package 减少来回确认

**Install**: cp -r codex-claude-pm/ ~/.claude/skills/codex-claude-pm/

---

#### `fireworks-tech-graph` — Fireworks Tech Graph — 技术图生成器

**Purpose**: 自然语言→SVG+PNG技术图，8种风格·14种图类型·完整UML支持·AI/Agent领域Pattern

**Workflow**:

```
1. User describes system or architecture in natural language (Chinese or English)
2. AI analyzes the request and recommends the optimal diagram type from 14 types
3. User selects from 8 visual styles (flat, dark geek, blueprint, Notion minimal, glassmorphism, Claude official, OpenAI official, dark luxury)
4. AI generates the diagram as publishable SVG + PNG with selected style
5. User iterates via natural language feedback for refinement
```

**Key features**:
- 8 visual styles: flat, dark geek, blueprint, Notion minimal, glassmorphism, Claude official, OpenAI official, dark luxury
- 14 diagram types: architecture diagram, data flow, flowchart, sequence diagram, full UML suite, ER diagram, mind map, timeline, network topology, and more
- Built-in AI/Agent domain patterns: RAG, Agentic Search, Mem0, Multi-Agent, Tool Call
- Natural language input in Chinese or English — no diagramming tools needed
- Direct publishable SVG + PNG output, ready for documentation and presentations

**Install**: git clone https://github.com/yizhiyanhua-ai/fireworks-tech-graph.git ~/.claude/skills/fireworks-tech-graph

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

#### `neat-freak` — 洁癖 — Knowledge Base Neat-Freak

**Purpose**: 洁癖级知识库清理——CLAUDE.md/docs/memory三层同步+规范审计，跨平台通用

**Key features**:
- 三层知识同步 — Agent memory / CLAUDE.md / docs 三层知识一致性审查与同步
- 规范审计 — 检查命名约定、必备文件、死引用等项目规范执行情况
- 四层自检体系 — 事实层→逻辑层→风格层→情绪层，层层把关知识质量
- 知识毕业机制 — 稳定知识自动从 memory 提升到 CLAUDE.md/docs，保持知识库精简
- 跨平台通用 — Claude Code / Codex / OpenCode / OpenClaw 均适用

**Install**: Download `dist/neat-freak.skill` and drag it into Claude Code.

---

### 🎨 Design & Frontend

---

#### `ui-ux-pro-max` — Design Intelligence for AI Coding Agents

**Purpose**: AI-powered design toolkit with 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, and 99 UX guidelines across 16 tech stacks. v2.0 Design System Generator: describe your project → get a complete design system with pattern, colors, typography, effects, and anti-patterns.

**Tech stacks (16)**: HTML+Tailwind, React, Next.js, shadcn/ui, Vue, Nuxt, Svelte, Astro, SwiftUI, React Native, Flutter, Jetpack Compose, Angular, Laravel, JavaFX.

**Install**: `npx uipro-cli init --ai <platform>`. Or download `dist/ui-ux-pro-max-skill.skill` and drag into Claude Code.

---

#### `dashi-ppt` — 浏览器可编辑 HTML 演示生成器

**Purpose**: 基于 12 套预置视觉主题，生成可在浏览器中编辑、自动保存、一键导出 PPTX/PDF 的 HTML 演示。核心哲学"锁模板填文案"——AI 只填 content slot，不改视觉结构。三道校验保证交付质量。唯一支持浏览器在线编辑+自动保存的 PPT 技能。

**Key features**:
- **12 套工业化主题**：轻拟态/炫光紫绿/深浅代码/玻璃糖果/色谱图表/深色图谱/冷白调研/黑金实验/深蓝杂志/金色指数/高能增长/声波霓虹，每套数十个页面组件
- **结构化 goal.json 驱动**：AI 按 layout 契约填 copyKeys，不改视觉结构
- **浏览器在线编辑**：侧边栏改文案/换图/调属性 → 自动写回 index.html → 一键导出 PPTX/PDF
- **三道校验流水线**：validate:goal-spec → validate:swiss → validate:goal-copy
- **layout:query 查询系统** + **props:safe 安全写入**，填错自动拦截
- 内置 10 款 woff2 字体、Unicorn Studio 动效背景、i18n 国际化、媒体素材管线

**Install**: `cp -r dashi-ppt/ ~/.claude/skills/dashi-ppt/`

> 完整 PPT 技能对比与选型指南：[`ppt/README.md`](ppt/README.md)

---

#### `design-buddy` — 视觉生产中台

**Purpose**: 19 种设计生产能力的总控路由元技能。覆盖图表·幻灯片·海报·Logo·品牌UI·公众号排版·故事板·文章配图·生成艺术·Gemini文生图等全视觉链路。从内容出发自动选择图表类型、风格系统和输出格式。与 Dog-Skills 现有设计技能互补——优先推荐已有技能，Design Buddy 补独有能力（文章→逻辑图/公众号富HTML排版/故事分镜/Gemini后端/零代码生图Skill）。

**Key features**:
- 19 个子技能覆盖图表/品牌/视觉/页面/故事五大类
- 四层架构：内容理解 → 视觉决策 → 资产生成 → 交付整理
- 智能路由：Dog-Skills 已有覆盖优先，Design Buddy 独有能力补充
- 支持 GPT-image-2/Gemini/Mermaid/p5.js 多后端
- 60+ 品牌 DESIGN.md 自动匹配生成品牌风格 UI

**Install**: `cp -r design-buddy/ ~/.claude/skills/design-buddy/`

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
cd html-video
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


#### `huashu-design` — 设计哲学顾问

**Purpose**: 设计哲学顾问——20种设计哲学·5大流派·3方向并行Demo·专家评审


**Key features**:
- 20种设计哲学知识库，覆盖信息建筑、运动诗学、极简主义、实验先锋、东方哲学5大流派
- 从设计哲学库中精准推荐3个最适合方向，并行生成视觉Demo直观对比
- 每个方向附带AI提示词DNA，可在Midjourney等AI工具中复现迭代
- 设计完成后自动进行专家评审，提供结构化反馈与改进建议
- 适用于品牌设计、产品落地页、UI视觉风格等多种场景

**Install**: Download `dist/huashu-design.skill` and drag it into Claude Code.

---


#### `ljg-card` — ljg-card: 铸

**Purpose**: 内容铸卡——将内容转化为PNG视觉卡片。7种模具：长阅读卡(-l)、信息图(-i)、多卡片(-m)、视觉笔记(-v)、漫画(-c)、白板(-w)、大字碑刻图(-b,1080×1440).

**Key features**:
- 7 种视觉模具覆盖主流展示场景：长阅读卡、信息图、多卡片、视觉笔记、漫画、白板、大字碑刻图
- 一段文字或文章链接直接生成 PNG 视觉卡片，开箱即用无需复杂配置
- 每种模具针对特定场景优化（小红书竖版、信息图分享、演示白板等）
- 自然语言触发，支持中英文双语指令
- 大字碑刻模式 1080×1440 专为移动端社交媒体设计

**Install**: Download `dist/ljg-card.skill` and drag it into Claude Code.

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

#### `dog-ppt` — AI 做 PPT 总控路由

**Purpose**: 不做 PPT，帮你在 8+ 个 PPT 技能中选对工具。三步选型法：先判断交付物（可编辑PPTX？视觉卡？网页演示？演讲辅助？）→ 再判断内容类型（论文？网页？轻内容？品牌发布？）→ 最后匹配合适的技能。覆盖 Dog-Skills 内置 8 个 PPT 相关技能和外部推荐技能。

**Key features**:
- 8+ PPT 技能选型地图：ppt-master（正式交付）/ huashu-slides（端到端）/ humanize-ppt（体检质检）/ huashu-design（视觉包装）/ baoyu-skills（轻内容）/ dog-frontier（网页演示）/ brand-workshop（品牌定调）/ presentation-design（方案板）
- 外部推荐：paper-deck（论文PPT）/ guizang-ppt-skill（视觉冲击）/ html-ppt-skill（演讲辅助）/ qiaomu（上游整理）
- 四个实用规则：要可编辑→ppt-master / 要视觉→huashu-design / 要论文→paper-deck / 要演讲→html-ppt-skill
- 核心洞察：内容整理 × 视觉表达 × 演示交付——三步拆开做

**Install**: `cp -r dog-ppt/ ~/.claude/skills/dog-ppt/`

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

#### `excalidraw-diagram` — 手绘风技术图生成器

**Purpose**: 自然语言描述系统，输出可编辑的 `.excalidraw` 文件。内置 Prompt 优化层（图类型识别→组件梳理→关系映射→布局推荐），确认后生成手绘风格的白板图。与 architecture-diagram（正式文档风）和 fireworks-tech-graph（多风格成品图）形成互补三角——Excalidraw 走"AI起稿→人工精调"的协作路线。

**Workflow**:

```
1. Prompt 分析 → 识别图类型 + 梳理组件 + 明确关系 + 推荐布局
2. 用户确认 → 展示结构化图描述，用户修改或确认
3. 生成 .excalidraw → 写入本地 JSON 文件，可拖入 excalidraw.com 编辑
```

**Key features**:
- **9 种图类型**：流程图·关系图·思维导图·架构图·数据流图·泳道图·类图·时序图·ER 图
- **Prompt 优化层**：生成前自动梳理组件和关系，减少返工
- **手绘风格**：strokeSharpness round + roughness + hachure 填充，白板质感
- **语义 8 色系统**：按组件类型自动分色（蓝=服务/绿=数据库/红=外部/橙=消息队列...）
- **可编辑输出**：.excalidraw JSON 可在 excalidraw.com / VS Code / Obsidian 中继续编辑
- **迭代修改协议**：支持增量修改节点·连线·布局·颜色，无需整图重新生成

**Install**: `cp -r excalidraw-diagram/ ~/.claude/skills/excalidraw-diagram/`

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

#### `animation-craft` — 动画工艺元技能

**Purpose**: 整合 Emil Kowalski 三件套（animation-vocabulary + emil-design-eng + review-animations）为一站式动画工艺流水线。三阶段：术语转换（模糊感觉→精确术语）→ 设计工程（按10条工艺规则生成代码）→ 质量审查（Before→After→Why 输出）。解决 AI 生成动画"生硬、缓动不对、时长不合理"的常见问题。

**Workflow**:

```
Phase 1: Vocabulary    →  模糊感觉 → 精确动画术语（"弹出来" → spring scale-in）
Phase 2: Design-Eng    →  按工艺规则生成/优化代码（时长·缓动·GPU属性·无障碍）
Phase 3: Review        →  10条硬标准逐项审查 → Before → After → Why
```

**Key features**:
- 动画术语词汇表：入场/出场/序列/状态切换/反馈/缓动/滚动 7 大类精确术语
- 10 条设计工程规则：时长控制（≤300ms）、缓动选择（入场=ease-out）、GPU 属性、弹出层 transform-origin、弹簧物理参数
- 10 条审查硬标准：动画有目的·频率匹配·缓动正确·时长·transform-origin·可中断·GPU属性·无障碍·非镜像·统一
- 审查输出 Before → After → Why 三段式，每条含代码对比
- 模糊描述→精确术语→优化代码→质量审查，完整闭环

**Install**: `cp -r animation-craft/ ~/.claude/skills/animation-craft/`

---

#### `apple-design` — Apple 设计哲学（Web 实现版）

**Purpose**: 将 Apple WWDC 流体界面设计原则翻译为 Web 端的 CSS/JS 实现。16 条原则覆盖：即时响应·直接操作·中断性·弹簧物理·速度传递·动量投影·橡皮筋边界·空间一致性·帧级流畅·材质景深·排版·色彩·触觉·无障碍（三种媒体查询）。

**Key features**:
- 16 条 Apple 设计原则，每条含 Web 实现代码（CSS + JS）
- 弹簧物理参数指南（Damping Ratio + Response，按交互类型推荐）
- 材质层级系统：5 层 backdrop-filter 方案（L0 背景 → L4 系统覆盖）
- Apple 排版规范：SF Pro 字间距/行高/动态字重，rem/em 布局
- 三种无障碍媒体查询：prefers-reduced-motion / reduced-transparency / contrast
- 动量投影公式（指数衰减）+ 橡皮筋阻力函数（渐进边界）
- 与 animation-craft 互补：apple-design 提供哲学层，animation-craft 提供工艺执行层

**Install**: `cp -r apple-design/ ~/.claude/skills/apple-design/`

---

#### `slack-gif-creator` — Slack GIF 动图

**Purpose**: Anthropic 官方出品。创建 Slack 优化的动画 GIF——Emoji 128×128、消息 480×480，自动适配限制。

**Key features**:
- Emoji / 消息 GIF / 演示 GIF 三种规格
- 自动优化帧率和文件大小
- 从截图、录屏、代码动画生成

**Install**: `/plugin install example-skills@anthropic-agent-skills`

---

#### `text-logic-diagram` — 文章→逻辑图

**Purpose**: 将论述性文本拆解为递进·流程·循环·层次·对比·矩阵六种逻辑关系，生成深色/浅色双主题自包含 HTML+SVG 图。与 architecture-diagram（系统架构）和 fireworks-tech-graph（技术图）互补——本技能专注"论述逻辑"可视化。多段落一次拆解多张图。

**Key features**:
- 六种逻辑关系类型：递进/流程/循环/层次/对比/矩阵，各有独立视觉规范
- 深色主题（Cursor暖色深底+赭石强调色）和浅色主题（羊皮纸底+暖棕）
- 概念抽象：每节点≤15字，自动提取关键词
- 多段落处理：每段独立 SVG，同文件顺序排列，含主题切换按钮
- JetBrains Mono 等宽字体，节点阴影+圆角，支持箭头/虚线/曲线连接

**Install**: `cp -r text-logic-diagram/ ~/.claude/skills/text-logic-diagram/`

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

### `huashu-proofreading` — AI味审校

**Purpose**: 三遍审校降AI味——内容→AI腔识别→节奏打磨，系统化降至30%以下

**Workflow**:

```
1. 第一遍：内容审校 — 事实核查、逻辑链验证、信息准确性检查
2. 第二遍：AI腔识别与改写 — 6大类AI腔识别（套话、句式、词汇、结构、态度、细节缺失）
3. 第三遍：节奏打磨 — 句长变化、段落呼吸、排版微调，自然度优化
```

**Key features**:
- 三遍审校系统化流程：内容审校 → AI腔识别与改写 → 节奏打磨
- 6大类AI腔识别：套话、句式、词汇、结构、态度、细节缺失
- 事实核查与逻辑链验证，确保内容准确性和推理严谨
- 句长变化与段落呼吸优化，让文本更自然流畅
- 排版微调细致打磨，消除AI句式模板化痕迹
- 系统化降低AI检测率至30%以下

**Install**: Download `dist/huashu-proofreading.skill` and drag it into Claude Code.

---

---

#### `baokuan-title-generator` — 爆款标题生成器

**Purpose**: 科技/AI/互联网领域公众号 10 万+ 爆款标题生成器。16 种爆款标题方法（强时效·实体锚定·数字反差·极值·内幕感·冲突对立·反差转折·亲测态度·任务结果·生活痛点·身份场景·收益损失·对话剧本·问题悬念·隐藏机制·场景画面），输入内容→建简报→多方法批量生成→逐条评分标风险→按用途分角色推荐→Top 5 + A/B 建议。方法论提炼自 1000+ 篇真实科技类 10 万+ 标题样本(2026年)。

**Workflow**:

```
内容简报 → 类型路由 → 多方法批量生成(≥6种方法) → 评分去重风险校验 → 标题矩阵 + Top 5 + 角色推荐 + A/B 建议
```

**Key features**:
- 16 种爆款标题方法，每种有真实爆文范例和公式
- 7 个增强器可叠加：时间前置/热词前置/具体化/省略号留白/身份反差/信息缺口/口语语气
- 内容类型→方法路由表：新闻→强时效, 产品测评→亲测转折, 趋势分析→冲突对立, 教程→数字结果
- 百分制评分（点击潜力30+一致性25+实体力15+表达力15+传播力10+风险5）
- 输出含公众号头条/小红书封面/B站标题/资讯快讯四角色推荐
- 绝不牺牲标题与正文的一致性——点进去必须能兑现

**Install**: `cp -r baokuan-title-generator/ ~/.claude/skills/baokuan-title-generator/`

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

#### `khazix-writer` — 卡兹克公众号长文写作

**Purpose**: 数字生命卡兹克（Khazix）的公众号长文写作skill。

**Key features**:
- HKR质检体系（Happy·Knowledge·Resonance）确保内容质量与读者共鸣
- AI角色边界分工，明确AI与人类在创作中的各自职责
- 四层自检体系，从多维度审核文章质量，层层把关
- 支持续写、扩写、根据素材产出长文，灵活适配各种写作需求
- 可模仿指定风格进行写作，按你的风格出稿
- 适用于公众号文章、长文、稿子等多种写作场景

**Install**: Download `dist/khazix-writer.skill` and drag it into Claude Code.

---

#### `ppt-master` — AI 生成真正可编辑的 PowerPoint · PPT Master

**Purpose**: AI 从任意文档（PDF/Word/Markdown/URL）生成真正可编辑的 .pptx 文件——原生 PowerPoint 形状、图表和动画（DrawingML），不是截图拼凑的假 PPT。27,000+ GitHub Star，MIT 开源。

**Author**: [Hugo He](https://github.com/hugohe3) · Original repo: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (27,000+ ⭐, MIT License)

**How it works**:

```
输入文档 → AI 生成 SVG（设计稿）→ Python 转换 SVG → DrawingML → 输出原生可编辑 .pptx
```

**Key features**:

- **真正可编辑** — 每个文本框、形状、图表都是 DrawingML 原生对象，可在 PowerPoint 中独立编辑
- **20 套内置模板** — Anthropic 风、麦肯锡风、Google 风、学术答辩风、科技创业风等
- **多尺寸输出** — 16:9、4:3、小红书竖版 3:4、朋友圈 1:1、A4，支持自定义
- **6000+ Tabler 图标** + **33 种图表模板** — 无需外部下载，按需引用
- **原生动画系统** — 页面过渡 + 元素入场动画，三种触发方式（on-click / after-previous / with-previous）
- **旁白转语音** — 演讲者备注 → AI 语音旁白（90+ 语言）→ PowerPoint 一键导出 MP4 视频
- **本地运行** — 文档不离开电脑，零数据泄露风险
- **支持自定义模板** — 可上传自己的 .pptx 作为样式模板

**Trigger examples**:
- "帮我把这份 PDF 做成 PPT，麦肯锡风，10 页以内"
- "把这篇 Markdown 转成学术答辩风格的幻灯片"
- "用这个 Word 文档生成投资人 Pitch，16:9，带动画"
- "给这份 PPT 加上演讲旁白，导出 MP4"
- "make a PowerPoint from this document with Google style"

**Install**: `/plugin marketplace add hugohe3/ppt-master` + `/plugin install ppt-master@ppt-master`（Claude Code 插件）。或 `npx skills add hugohe3/ppt-master`。Python 3.10+ 环境需 `pip install -r requirements.txt`。

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

#### `huashu-slides` — AI 演示文稿工作流

**Purpose**: 端到端PPT制作——18种设计风格·三种协作模式→可编辑PPTX

**Workflow**:

```
1. 内容结构化 — 将原始资料整理为结构化演示文稿框架
2. 设计系统选择 — 从18种设计风格（浮世绘、包豪斯、Snoopy、像素画等）中匹配视觉方案
3. AI插画生成 — 由 AI 根据内容自动生成配套插画
4. 幻灯片组装 — 将结构、设计、插画组合为完整幻灯片
5. 细节打磨 — 精细化调整每个页面直到满意
```

**Key features**:
- 5阶段端到端流水线：内容结构化→设计系统→AI插画→幻灯片组装→细节打磨
- 18种设计风格预设，覆盖浮世绘、包豪斯、Snoopy、像素画等多种视觉风格
- 三种协作模式，适配个人创作、团队协作等不同工作场景
- 输出可编辑PPTX文件，原生形状和文本均可修改
- 支持从一句话描述到完整演示文稿的全自动生成

**Install**: git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/

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

#### `teach` — Knowledge · Skills · Wisdom 三层学习框架

**Purpose**: Matt Pocock 的三层学习框架——Knowledge（知识获取）→ Skills（交互练习）→ Wisdom（社区智慧）。AI 变成你的私人导师：从高质量资源提取知识生成 HTML 交互课件，设计动手练习并给即时反馈，对于 AI 教不了的判断力，帮你找到真实的社区和人。

**Workflow**:

```
1. Mission → 了解用户为什么想学，写入 MISSION.md
2. Research → 从高质量资源提取知识，写入 RESOURCES.md
3. Reference → 生成速查表和术语表（reference/*.html）
4. Lessons → 设计交互式课件（lessons/0001-*.html）
5. Practice → 设计动手练习，给即时反馈
6. Wisdom → 对教不了的部分，推荐真实社区和人
7. Record → 记录学习洞察，追踪最近发展区
```

**Key features**:
- 三层学习框架：Knowledge（知识获取）→ Skills（动手练习）→ Wisdom（社区智慧）
- 每句话都有引用来源，不信任 AI 参数化知识
- 交互式 HTML 课件 + 即时反馈练习，Tufte 风格排版
- 结构化教学空间：MISSION.md / RESOURCES.md / reference / lessons / learning-records
- 承认 AI 边界——教不了 Wisdom，帮你找到真实社区和人
- 基于最近发展区设计练习难度，区分存储强度与流畅感

**Install**: Download `dist/teach.skill` and drag it into Claude Code.

---


### 💼 Business & Strategy

---

#### `creator-buddy` — 内容运营情报中心

**Purpose**: 5 个内容运营研究技能的总控路由元技能。从小红书·公众号·B站·抖音的真实数据中搜索热点、拆爆款、分析赛道、生成标题。与 last30days（海外平台）互补形成完整选题研究体系：creator-buddy 覆盖中文内容生态，last30days 覆盖海外平台。

**5 个子技能**: xhs-hotnotes（小红书热榜）/ global-content-search（全域搜索：小红书+B站+抖音）/ gzh-explosive-content-detector（公众号爆款检测）/ baokuan-article-analysis（赛道级爆款聚合）/ baokuan-title-generator（16法爆款标题，已独立封装）。

**Key features**:
- 四层架构：平台访问 → 数据整理（JSON）→ 报告生成（HTML）→ 运营判断
- 只读公开数据，不做账号动作，低频按需采样
- 部分子技能需 API Key（REDFOX_API_KEY/GUAIKEI_API_TOKEN），凭据不入库
- 与 last30days 协作模式：海外信号 + 中文生态 = 选题蓝海

**Install**: `cp -r creator-buddy/ ~/.claude/skills/creator-buddy/`

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

### `huashu-data-pro` — 数据分析与办公提效助手

**Purpose**: 数据分析与办公提效——Excel·ROI·可视化·5种报告风格→交互式HTML+PDF

**Key features**:
- 端到端数据分析工作流，覆盖数据处理、分析洞察、报告撰写与数据可视化
- Excel 数据分析与公式处理，支持复杂表格和数据处理任务
- 投放复盘与 ROI 测算，从数据到洞察的完整分析链路
- 5 种报告风格输出，支持交互式 HTML 和 PDF 格式
- 图表生成与数据可视化，直观呈现分析结果
- 周报/月报自动生成，覆盖汇报场景需求

**Install**: Download `dist/huashu-data-pro.skill` and drag it into Claude Code.

---

#### `ljg-invest` — 投资分析

**Purpose**: 投资分析 — 给一个项目（公司名、BP、创始人对话），写一份深度投资分析报告。核心判断只有一个：这个项目是不是一台"秩序创造机器"。

**Workflow**:

```
1. 项目信息收集 — 收集公司名、BP、创始人对话等信息，知名公司直接搜索最新数据
2. 秩序创造判定 — 从飞轮效应、抗冲击能力、资源引力三个角度判断：是不是秩序创造机器
3. 创生公式提炼 — 写出一句话的核心算法，追问验证次数与差异
4. 市场认知差分析 — 市场看见的 vs 我们看见的，定位 S 曲线阶段与认知折价
5. 投资建议输出 — 交换建议（投/观察/放弃）+ 核心假设 + 退出信号 + 未解问题
```

**Key features**:
- 不走传统投资分析路，核心判断：项目是不是一台"秩序创造机器"
- 五区块报告结构：这是什么 → 秩序创造判定 → 创生公式 → 市场认知差 → 投资建议
- 敢下判断，每个判断带证据，禁用模糊表达（"既可能好也可能坏"禁止）
- 基于"财富是被欲望照亮的秩序"核心定义，钱只是秩序的计量单位
- 数据分析禁止编造，查不到的直接标注，不硬撑
- 每个决策押在明确的假设上，配具体的退出信号

**Install**: Download `dist/ljg-invest.skill` and drag it into Claude Code.

---

#### `minimalist-entrepreneur` — 极简创业 AI 商业顾问 · Minimalist Entrepreneur

**Purpose**: 基于 Sahil Lavingia《The Minimalist Entrepreneur》（《小而美》）方法论，10 个 Claude Code Plugin 技能覆盖一人公司全链路：找社群 → 验证想法 → MVP → 流程化 → 首批100客户 → 定价 → 营销 → 稳健增长 → 公司价值观 → 极简复盘。核心理念：不融资、先盈利、手动跑通再产品化、从第一天就收费。

**10 步创业全链路**:

```
找社群        验证想法         MVP          流程化       首批100客户
/find-       /validate-      /mvp        /processize    /first-
community    idea                                        customers
   │             │              │              │              │
   └─────────────┴──────┬───────┴──────────────┴──────────────┘
                        │
       定价             营销          稳健增长      公司价值观      极简复盘
       /pricing     /marketing-     /grow-        /company-     /minimalist-
                      plan        sustainably      values        review
```

**10 个 Skill 速览**:

| # | 命令 | 一句话核心 |
|---|------|-----------|
| 1 | `/find-community` | 你不需要找社群，你已经在好几个里了——关键是里面的人在反复抱怨什么 |
| 2 | `/validate-idea` | 别问"酷不酷"，问"有人付钱吗" |
| 3 | `/mvp` | 只做一件事，能在周末交付的才做 |
| 4 | `/processize` | 先手动跑 10 次，把步骤写在纸上，再写代码 |
| 5 | `/first-customers` | 100 个客户之前别搞发布会，从亲友一圈圈往外卖 |
| 6 | `/pricing` | 从第一天就收费，免费和 1 块钱之间是质变不是量变 |
| 7 | `/marketing-plan` | 先花时间再花钱，博客免费社交免费，跑通了再投广告 |
| 8 | `/grow-sustainably` | 盈利给你无限跑道，别人可能超过你但 10 年后你还在 |
| 9 | `/company-values` | 价值观用故事写不是口号，Nordstrom 接受轮胎退货才是价值观 |
| 10 | `/minimalist-review` | 八个问题筛完，答案通常就清楚了——最通用的决策过滤器 |

**Key features**:
- 10 个 Skill 形成完整创业链路，每一步都是下一步的前提
- 对话式 AI 商业顾问：带着真实想法来，它一步步追问，不给答案只给问题
- `/minimalist-review` 是最通用的决策过滤器：8 条极简原则从 8 个维度同时过筛
- 两个 Skill 接力使用能看到整条路径的问题，而非孤立的一个点
- 不止创业：至少 5 个 Skill 对副业、社群、任何"做不做"的决策有帮助
- 基于 Sahil Lavingia 真实经历：Gumroad 从裁员到只剩自己一人再到盈利的全过程

**Install**: `/plugin marketplace add slavingia/skills` → `/plugin install minimalist-entrepreneur`（推荐）。或: `cp -r minimalist-entrepreneur ~/.claude/skills/minimalist-entrepreneur/`（文档包装器）。

**Source**: [slavingia/skills](https://github.com/slavingia/skills) (9000+ ⭐) by Sahil Lavingia (Pinterest 联合创始人, Gumroad 创始人). MIT License.

---

### 🔍 Tools & Discovery

---

#### `agency-agents-zh` — Agency Agents 中文版 — 266 个 AI 专家角色库

**Purpose**: 266 个即插即用的 AI 专家角色库 — 覆盖工程、设计、产品、营销、金融、安全、游戏等 20 个部门。

**Workflow**:

```
1. 理解需求 — 分析用户任务目标和领域，确定需要的专家角色类型
2. 推荐角色 — 从 266 个角色库中匹配最合适的角色，说明角色定位和能力
3. 角色激活 — 加载对应角色提示词，按角色定义的工作流程和交付标准执行
4. 多角色协作 — 可选：通过编排器让多位专家按 DAG 自动协作完成复杂任务
```

**Key features**:
- 266 个即插即用的 AI 专家角色，覆盖工程、设计、产品、营销、金融、安全、游戏等 20 个部门
- 每个角色都有独立的人设、专业流程和可交付成果，非通用提示词模板
- 含 50 个中国市场原创智能体（小红书/抖音/微信/B站/飞书/钉钉等）
- 搭配编排器 agency-orchestrator，一句话即可让多位专家按 DAG 自动协作

**Install**: Download `dist/agency-agents-zh.skill` and drag it into Claude Code.

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

#### `markitdown` — MarkItDown — 微软开源文档转换神器

**Purpose**: 微软开源文档转换工具 — PDF/Word/PPT/Excel/HTML 等 20+ 种格式一键转干净 Markdown，Obsidian 知识库入库利器

**Workflow**:

```
1. 输入文档 — 接收 PDF/Word/PPT/Excel/HTML/EPUB/图片/音频 等 20+ 种格式
2. 格式解析 — 自动识别文档类型，调用对应解析引擎进行结构化提取
3. 内容保留 — 保留标题层级、有序/无序列表、表格、超链接、代码块等结构
4. Markdown 输出 — 生成语法正确、语义完整的干净 Markdown 文件
```

**Key features**:
- **20+ 格式支持** — PDF、Word、PPT、Excel、HTML、EPUB、图片（OCR）、音频（语音转文字）等，覆盖日常所有文档类型
- **结构完美保留** — 标题层级、列表、表格、链接、代码块，转出 Markdown 结构完整可直接使用
- **Obsidian 知识库入库利器** — 批量转换文档后一键导入 Obsidian 个人知识库
- **RAG 文档预处理** — 将各种格式的文档统一转为干净 Markdown，方便向量化嵌入和检索
- **AI 阅读友好** — 转出 Markdown 语义结构清晰，AI 分析处理时无信息损失

**Prerequisites**: Python 3.10+，安装 `pip install markitdown`

**Install**: Download `dist/markitdown.skill` and drag it into Claude Code.

---

#### `read-buddy` — 信息读取中心

**Purpose**: 18 种信息读取能力的总控路由元技能。覆盖网页·RSS·YouTube·播客·X/Twitter·飞书文档·图片OCR·微信读书·小宇宙·个人数据等全来源。根据内容来源自动选择读取策略，优先推荐 Dog-Skills 已有工具（markitdown/weread-skill/baoyu-skills），Read Buddy 独有能力（RSS聚合/OCR/飞书/小宇宙/X分析/播客工作流/个人数据采集）作为补充。

**18 个子技能**: read-url-markdown / read-web-scraper / read-web-article-translator / read-x-markdown / read-x-blogger-analyzer / read-youtube-feed / read-youtube-transcript / read-podcast-workflow / read-podcast-script-generator / read-xiaoyuzhou-article / read-rss-aggregator / read-topic-collector / read-content-digest / read-feishu-doc / read-ocr / read-weread-export / read-weread-analyzer / read-weread-coach / read-personal-data-harvester。

**Key features**:
- 四层工作架构：来源接入 → 内容抽取 → 结构化整理 → 认知处理
- 智能路由：Dog-Skills 已有优先，Read Buddy 独有能力补充
- 只读优先 + 凭据不入库 + 个人数据本地化 + 低频采样
- 补全 Dog-Skills 缺失的 RSS/OCR/飞书/小宇宙/X分析/播客/个人数据能力

**Install**: `cp -r read-buddy/ ~/.claude/skills/read-buddy/`

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

#### `topic-collector` — AI 热点自动采集

**Purpose**: AI 热点自动采集器——多源并行搜索 AI 领域最新动态，生成结构化选题清单。覆盖 AI 博主/KOL·Product Hunt 新产品·Hacker News·学术论文·模型厂商官方·Reddit 社区热议 5 大数据源。聚焦 Vibe Coding·Claude 生态·AI Agent·AI 知识管理·模型更新·新产品·海外热点 7 大领域。

**Key features**:
- 五大数据源并行采集：AI 博主实践/创业公司新产品/AI 研究动态/模型厂商官方/技术社区讨论
- 七大聚焦领域优先级排序，自动生成带原文链接的结构化热点清单
- 输出含选题建议，直接指导下一篇内容方向
- 与 last30days（海外实时信号）和 creator-buddy（中文平台运营）形成选题研究三角
- 时效性优先：24 小时内内容，每条必须带可点击 URL

**Install**: `cp -r topic-collector/ ~/.claude/skills/topic-collector/`

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

#### `wx2md` — WeChat Official Account to Markdown Exporter

**Purpose**: 将微信公众号文章从 mp.weixin.qq.com 导出为本地 Markdown 文件，包含 front matter 和本地化图片。支持 Playwright 页面加载、DOM 提取、图片下载、Markdown 转换、批量 URL 处理和导出验证。

**Workflow**:

```
1. 输入公众号文章链接
2. Playwright 加载页面 → DOM 结构化提取
3. 图片自动下载并本地引用
4. 生成带 front matter 的干净 Markdown 文件
5. 可选验证：检查导出完整性
```

**Key features**:
- 支持单篇文章和批量 URL 处理
- 自动下载文章内嵌图片到本地
- 生成标准化 front matter (标题/日期/作者/来源)
- 输出适合 Obsidian 等知识库工具的 Markdown 格式

**Install**: cp -r wx2md/ ~/.claude/skills/wx2md/

---

## Skill Categories

| Category | Skills |
|----------|--------|
| 🧠 **Thinking & Research** | first-principles, storm-research, feynman-learning, gpt-researcher, nuwa, last30days, life-designer, scientific-research, thinking-toolkit |
| 💻 **Development** | architecture-diagram, cc-dispatch, codex-claude-pm, code-review, website-cloner, claude-to-im, superpowers, planning-with-files, code-simplifier, webapp-testing, ralph-loop, mcp-builder, repo-evaluator |
| 🎨 **Design & Frontend** | ui-ux-pro-max, dog-frontier, html-video, lottie-animation, brand-workshop, pixel-art, dog-poster, presentation-design, article-poster, canvas-design, algorithmic-art, slack-gif-creator, theme-factory, soviet-storybook-grotesque, torn-paper-collage-poster |
| 📝 **Content & Writing** | humanizer-zh, baoyu-skills, humanize-ppt, ppt-master, writing-assistant, scientific-writing-editor, ghostwriter |
| 📚 **Learning & Teaching** | dog-tutor, exam-tutor, learning-studio, teach |
| 💼 **Business & Strategy** | dbskill |
| 🔍 **Tools & Discovery** | family-doctor, find-skills, handshake, markitdown, token-optimizer, vibe-sing, weread-skill, wx2md |

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
