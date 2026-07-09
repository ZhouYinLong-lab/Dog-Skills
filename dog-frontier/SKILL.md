---
name: dog-frontier
description: >
  前端设计综合技能系统(Dog-Frontier)【全栈元技能，已包含 ui-ux-pro-max】。
  通过多轮对话精确理解需求,整合19个专业前端技能的精华,
  输出高质量、高结构化的前端设计方案与代码。覆盖 UI/UX 设计系统、Tailwind/shadcn 组件库、
  Vue/React 技术栈、CSS 高级技巧、落地页生成、动画视频、品牌设计、设计令牌三大层级、
  反「AI味」设计审查等全链路。
  如需轻量独立版，用 ui-ux-pro-max；需要全链路前端方案，用本技能。
  Trigger keywords: 前端设计, 前端开发, UI设计, 设计系统, 落地页, landing page, dashboard,
  仪表盘, 组件开发, Vue组件, React组件, Tailwind, shadcn, 配色方案, 字体搭配, 品牌设计,
  CSS动画, HTML视频, 响应式布局, 前端重构, 界面优化, UX审查, 设计令牌, design tokens,
  反AI味, AI味, 去模板化, 有审美的前端, taste-skill, 独特设计, 审美约束,
  Dog-Frontier, 前端综合, Stripe风格, Apple风格, Notion风格, Airbnb风格,
  Vercel风格, Linear风格, DESIGN.md, design.md, awesome-design-md, 品牌风格,
  大厂设计风格, 按XX风格设计, 设计系统格式, 设计令牌导出.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
  - WebFetch
  - WebSearch
metadata:
  category: design
  version: "2.0.0"
  license: MIT
  integrated-skills: 21
  design-md-format: https://github.com/google-labs-code/design.md (Apache-2.0)
  design-md-library: https://github.com/VoltAgent/awesome-design-md (MIT)
---

# Dog-Frontier — 前端设计综合技能

整合 18 个前端技能的元技能系统。通过结构化多轮对话,将模糊需求转化为高质量交付物。

---

## 触发条件

当用户请求涉及以下任一领域时,激活本技能:

### 设计阶段
- 从零设计新项目前端 → 走[完整流程](references/workflow.md#phase-1-discovery)
- 重构现有界面 → 走[审查流程](references/workflow.md#phase-3-review)
- 生成设计系统/令牌/品牌指南 → 走[设计系统流程](references/workflow.md#phase-2-design-system)

### 开发阶段
- 创建页面(落地页/仪表盘/管理后台) → 走[页面流程](references/workflow.md#phase-3-code-generation)
- 开发组件(按钮/表单/表格/图表/导航) → 走[组件流程](references/workflow.md#phase-3-component)
- 实现动画/视频 → 走[动画流程](references/workflow.md#phase-3-animation)

### 审查阶段
- UI/UX 审查 → 走[审查流程](references/workflow.md#phase-5-review)
- 代码质量检查 → 走[QA流程](references/qa-checklist.md)
- 文案去AI化 → 走[文案流程](references/workflow.md#phase-5-copy)
- 反「AI味」设计审查 → 走[反AI味流程](#anti-ai-taste-审查)

---

## 流程总控

整个技能按以下 5 阶段流水线运行。每阶段完成后,必须通过该阶段的验收门(Gate)才能进入下一阶段。

```
Phase 1: Discovery          Phase 2: Design System        Phase 3: Implementation
┌──────────────┐           ┌──────────────────┐           ┌──────────────────┐
│ 需求勘探      │           │ 设计系统生成      │           │ 代码生成          │
│              │    →      │                  │    →     │                  │
│ 4个关键问题   │   Gate 1  │ 风格+配色+字体    │   Gate 2  │ 组件+布局+页面    │   Gate 3
│ 输出: 需求卡  │           │ +DESIGN.md参考库  │           │ 输出: 源代码      │
└──────────────┘           │ 输出: DESIGN.md   │           └──────────────────┘
                           └──────────────────┘
                                    │
         ┌──────────────────────────┘
         │ 风格选择优先级:
         │ 1. awesome-design-md (58品牌 DESIGN.md 即插即用)
         │ 2. ui-ux-pro-max (67风格 BM25搜索)
         │ 3. 内置设计知识 (兜底)
         │
Phase 5: Quality Review                            Phase 4: Handoff Check
┌──────────────────┐                              ┌──────────────────┐
│ 质量审查          │                              │ 交接检查          │
│                  │    ←                         │                  │
│ 6维度+design.md   │         Gate 4               │ 格式+完整性验证   │
│ lint自动化校验    │                              │ 输出: 交接包      │
│ 输出: QA报告      │                              │                  │
└──────────────────┘                              └──────────────────┘
```

### 阶段门控 (Gates)

| 门 | 检查内容 | 不通过时的处理 |
|----|----------|---------------|
| **Gate 1** | 4个问题全回答,需求卡片完整(含风格品牌名) | 回到 Phase 1,追问缺失信息 |
| **Gate 2** | DESIGN.md 包含: YAML令牌(colors/typography/spacing/rounded) + 8段式Markdown | 回到 Phase 2,补充缺失维度 |
| **Gate 3** | 代码可运行,覆盖所有页面/组件,符合DESIGN.md令牌 | 修复问题后重新验证 |
| **Gate 4** | 交接格式合规,文件完整,含DESIGN.md + export产物 | 补充缺失文件 |
| **Gate 5** | 6 维度评分 ≥ 26/35 + `@google/design.md lint` 零 error | 修复不达标的维度 |

---

## 核心规则

### 1. 必须走完 5 阶段
不允许跳过任何阶段。但可以根据任务类型调整各阶段的深度:
- **轻量任务**(如单个组件): 每阶段压缩至 1-2 轮对话
- **完整项目**(如全新设计): 每阶段展开完整对话

### 2. 每个阶段输出物必须结构化
使用 [handoff-format.md](references/handoff-format.md) 定义的格式进行阶段间交接。

### 3. 技能调度优先级
当多个上游技能可完成同一任务时,按以下优先级选择:
1. 用户已安装的本地技能(零延迟)
2. 安装量 ≥ 1K 的社区技能(稳定性优先)
3. 本技能内置的参考知识(作为兜底)

### 4. 归属透明
每次使用上游技能时,在输出中标注 `[来源: skill-name]`。
完整归属见 [ATTRIBUTIONS.md](ATTRIBUTIONS.md)。

---

## 验收标准

所有交付物必须通过 [qa-checklist.md](references/qa-checklist.md) 的全部检查项。

### 最低通过线

| 维度 | 最低分 | 检查项数 |
|------|--------|----------|
| 视觉质量 | ≥ 4/5 | 5 |
| 可访问性 | ≥ 4/5 | 5 |
| 响应式 | ≥ 4/5 | 5 |
| 性能 | ≥ 3/5 | 5 |
| 代码质量 | ≥ 4/5 | 5 |
| 文案质量 | ≥ 3/5 | 5 |
| 反AI味 | ≥ 4/5 | 5 |
| **总计** | **≥ 26/35** | **35** |

### 阻断性缺陷 (一票否决)

以下任一情况出现,直接判定不通过:
- 移动端(375px)有水平滚动条
- 文字对比度 < 3:1
- 表单无可见 label
- 交互元素无键盘支持
- 输出包含未标注归属的上游技能内容

---

## 快速路由

根据用户输入的关键词,直接跳转到对应阶段:

```
用户说:                           → 从哪开始
"设计一个XX落地页"                 → Phase 1 (完整流程)
"给我做一个 Stripe 风格的管理后台"  → Phase 2 DESIGN.md 匹配 → Phase 3
"按 Notion 的配色重构这个页面"      → Phase 2 awesome-design-md → Phase 3
"这个页面的配色帮我优化一下"        → Phase 2 (只走设计系统)
"帮我写一个Vue表格组件"            → Phase 3 (只走代码生成)
"审查一下这个页面的UX"             → Phase 5 (只走质量审查)
"把这个设计的文案改得更自然"        → Phase 5 文案流程
"生成设计令牌/design tokens"       → Phase 2 令牌生成
"lint一下我的DESIGN.md"            → Phase 5 design.md CLI校验
"导出设计令牌到 Tailwind config"    → Phase 4 @google/design.md export
"做一个产品介绍视频"               → Phase 3 动画流程
"反AI味设计/去模板化/审美审查"     → Phase 5 反AI味流程
```

---

## 集成技能总览

| Layer | 技能 | 许可 | 何时调度 |
|-------|------|------|----------|
| L0 设计格式 | **DESIGN.md 格式标准** (google-labs-code) | Apache-2.0 | Phase 2/4/5 格式规范 |
| L0 设计格式 | **awesome-design-md** (VoltAgent, 58品牌) | MIT | Phase 2 品牌风格即插即用 |
| L1 设计智能 | ui-ux-pro-max | MIT | Phase 2 设计系统 |
| L1 设计智能 | frontend-design | Proprietary | Phase 2 风格选择 |
| L2 组件样式 | shadcn-ui (18.5K) | MIT | Phase 3 React组件 |
| L2 组件样式 | tailwind-design-system (1.6K) | MIT | Phase 3 Tailwind配置 |
| L2 组件样式 | css-styling-expert | MIT | Phase 3 CSS实现 |
| L3 框架 | shadcn-vue (727) | MIT | Phase 3 Vue组件 |
| L3 框架 | vue-component-patterns | MIT | Phase 3 Vue模式 |
| L3 框架 | vanilla-web | MIT | Phase 3 原生HTML |
| L4 品牌令牌 | brand | MIT | Phase 2 品牌 |
| L4 品牌令牌 | design-system | MIT | Phase 2 令牌 |
| L4 品牌令牌 | ui-styling | MIT | Phase 3 样式 |
| L5 页面内容 | landing-page-generator (1.2K) | MIT | Phase 3 落地页 |
| L5 页面内容 | liquid-theme-standards (1.9K) | MIT | Phase 2 主题 |
| L6 动画媒体 | html-video | Apache-2.0 | Phase 3 视频 |
| L6 动画媒体 | sprite-animation | MIT | Phase 3 动画 |
| L7 质量保证 | humanizer-zh | MIT | Phase 5 文案 |
| L7 质量保证 | taste-skill | MIT | Phase 5 反AI味 |
| L7 质量保证 | **@google/design.md CLI** | Apache-2.0 | Phase 5 lint校验 + Phase 4 export |

完整归属声明: [ATTRIBUTIONS.md](ATTRIBUTIONS.md)

---

## DESIGN.md 集成 (v2.0 新增)

Dog-Frontier v2.0 深度集成 Google 的 [DESIGN.md](https://github.com/google-labs-code/design.md) 格式标准和 [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 品牌库。

### 什么是 DESIGN.md？

DESIGN.md 是 Google Stitch 团队制定的**纯文本设计系统格式标准**（Apache 2.0），让 AI agent 能直接读懂设计系统。它由两层组成：

| 层 | 格式 | 用途 |
|----|------|------|
| **YAML Front Matter** | 结构化设计令牌 | 机器可读的 colors/typography/spacing/rounded/components |
| **Markdown Body** | 8 段式规范文档 | 人类可读的设计理论与使用指南 |

### awesome-design-md：58 品牌即插即用

[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（MIT, 91K+ Stars）收集了 58 家知名公司的 DESIGN.md 反向工程文件：

| 分类 | 品牌示例 |
|------|---------|
| AI & LLM | Claude, Mistral AI, ElevenLabs, xAI |
| 开发者工具 | Vercel, Linear, Cursor, Supabase, GitHub |
| 金融科技 | Stripe, Coinbase, Revolut, Wise |
| 生产力 | Notion, Intercom, Cal.com, Zapier |
| 消费科技 | Apple, Spotify, Airbnb, Nike, Tesla |
| 设计工具 | Figma, Framer, Webflow, Miro |
| 汽车 | Ferrari, Tesla, BMW, Lamborghini |

### Phase 2 集成：风格即插即用

当用户说"给我做一个 Stripe 风格的管理后台"时：

```
用户请求 "Stripe风格"
       │
       ▼
┌──────────────────────────────┐
│ Step 2.0: DESIGN.md 匹配     │
│ 从 awesome-design-md 检索    │
│ 匹配 "Stripe" → DESIGN.md   │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ Step 2.1: 令牌提取           │
│ 解析 YAML front matter       │
│ 提取颜色/字体/间距/圆角令牌   │
└──────────┬───────────────────┘
           │
           ▼
┌──────────────────────────────┐
│ Step 2.2: 用户微调(可选)      │
│ "但把主色换成蓝色"            │
│ 覆盖对应令牌值                │
└──────────┬───────────────────┘
           │
           ▼
      输出: DESIGN.md (标准格式)
```

**风格选择优先级**：
1. **awesome-design-md 匹配**（用户指定品牌名）→ 直接复用 DESIGN.md
2. **ui-ux-pro-max BM25 搜索**（用户描述风格特征）→ 从 67 风格中匹配
3. **内置设计知识**（通用/兜底）→ 从零生成

### Phase 5 集成：自动化令牌校验

在质量审查阶段，增加 `@google/design.md` CLI 自动校验：

```bash
# 校验 DESIGN.md 格式正确性
npx @google/design.md lint DESIGN.md

# 检查项:
# ✅ broken-ref: 令牌引用完整性 (error级)
# ✅ contrast-ratio: WCAG AA 对比度 ≥ 4.5:1 (warning级)
# ✅ orphaned-tokens: 未使用的孤岛令牌 (warning级)
# ✅ section-order: 章节顺序合规 (warning级)
# ✅ missing-typography: 字体令牌缺失 (warning级)
```

### Phase 4 集成：导出到框架配置

```bash
# 导出 Tailwind v4 config
npx @google/design.md export DESIGN.md --format tailwind4

# 导出 W3C DTCG JSON
npx @google/design.md export DESIGN.md --format dtcg
```

### MASTER.md → DESIGN.md 格式迁移

| 旧 (MASTER.md) | 新 (DESIGN.md) |
|----------------|----------------|
| 自由格式 Markdown | YAML 令牌 + 8 段式 Markdown |
| Hex 色值散落文中 | `colors.primary: "#xxx"` 结构化令牌 |
| 手动 QA 检查 | `@google/design.md lint` 自动校验 |
| 仅人可读 | 人可读 + AI 可直接消费 |
| 不可导出 | 可导出 Tailwind/W3C DTCG |

---

## Anti-AI-Taste 审查

防止 AI 生成千篇一律的模板化 UI。在 Phase 5 质量审查时,额外执行反「AI味」设计审查。

### AI味反模式清单

| # | AI味模式 | 判定标准 | 替代方案 |
|---|---------|---------|---------|
| 1 | **蓝紫渐变 Hero** | 首屏背景为 linear-gradient(blue, purple) | 纯色 / 照片背景 / 纹理 / 大量留白 |
| 2 | **Inter/Roboto 字体** | 全站使用 AI 默认字体,无品牌感 | 衬线标题 + 无衬线正文 / 定制字体 |
| 3 | **Bento Grid 布局** | 标准圆角卡片网格,无视觉层次 | 不对称网格 / 重叠布局 / 杂志排版 |
| 4 | **Glassmorphism 堆叠** | 半透明模糊卡片 + 彩虹渐变背景 | 纯色卡片 / 细边框 + 阴影层级 |
| 5 | **空洞文案** | "Empower your workflow" 等模板短语 | 具体、有态度的产品文案 |
| 6 | **标准 Tailwind 色板** | 使用默认 blue-500 / gray-100 等 | 自定义 oklch 色值,品牌色系 |
| 7 | **无理由圆角** | 所有卡片都是 rounded-xl,无体系 | 建立圆角层级(token): sm/md/lg/xl |
| 8 | **图标泛滥** | 每个功能卡片都放 Heroicons 图标 | 有节制地使用,考虑自定义图标 |
| 9 | **空白状态模板化** | "No items yet. Create one!" 模式 | 个性化空状态,符合产品语调 |

### 审查流程

```
1. 视觉扫描 → 对照9项反模式清单逐一检查
2. 辨识度测试 → 截图放到 Pinterest/Dribbble 中,能一眼认出吗?
3. 设计溯源 → 每个设计决策有理由,而非「AI习惯这么做」
4. 修复建议 → 对命中的模式给出1-2个替代方案
5. 重验证 → 修复后再次走审查流程,直到通过率 ≥ 80%
```

### 阻断性反模式

以下任一情况直接判定反AI味审查不通过:
- 出现 ≥ 5 项 AI 味反模式
- Hero 区域使用蓝紫渐变且无品牌理由
- 全站仅使用 Inter 字体(无品牌字体注入)
- 3 个以上 Glassmorphism 卡片相邻出现

---

## 文件导航

```
dog-frontier/
├── SKILL.md                     # 本文件 — 流程总控、触发条件、验收标准、DESIGN.md集成
├── ATTRIBUTIONS.md              # 21个集成技能+DESIGN.md生态的完整归属声明
├── README.md                    # 快速开始与 DESIGN.md 生态说明
├── references/
│   ├── workflow.md              # 5阶段详细说明,每阶段输入/输出/步骤/示例
│   ├── handoff-format.md        # 阶段间交接的结构化格式定义(DESIGN.md格式)
│   └── qa-checklist.md          # 最终验收清单(6维度35项+design.md lint)
├── scripts/
│   └── design-system.py         # 设计系统生成脚本(BM25搜索 + 反模式过滤)
├── assets/
│   ├── design-tokens.md         # 三阶令牌架构参考(DESIGN.md YAML格式)
│   ├── ui-styles-catalog.md     # 67种UI风格速查
│   ├── vue-patterns.md          # Vue 3组件设计模式
│   ├── css-expertise.md         # CSS高级技巧手册
│   ├── landing-patterns.md      # 12段式落地页结构
│   ├── design-brief.md          # 设计简报模板
│   └── output-formats.md        # 固定输出格式模板(DESIGN.md标准格式)
```
