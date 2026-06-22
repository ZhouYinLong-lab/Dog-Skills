# 工作流详细说明 (Workflow)

> 配合 SKILL.md 的流程总控使用。定义每个阶段的具体步骤、输入、输出和示例。

---

## Phase 1: 需求勘探 (Discovery)

### 目标
将模糊的用户需求转化为结构化的需求卡片,确保后续阶段有明确的输入。

### 输入
用户的原始描述(可能不完整)。

### 步骤

#### Step 1.1: 提4个关键问题

使用 `AskUserQuestion` 逐步明确:

```
Q1: 项目类型? (必答)
  A. 全新项目(从零设计)
  B. 重构现有界面(保留功能,优化UI)
  C. 新增页面/组件(在现有设计系统中扩展)
  D. 设计审查(审查现有UI并提供改进方案)

Q2: 技术栈? (必答)
  A. Vue 3 + Tailwind
  B. React/Next.js + Tailwind
  C. 原生 HTML + CSS + JS
  D. React Native / Flutter
  E. 其他(请说明)

Q3: 页面/组件类型? (必答)
  A. 落地页/营销页    B. 仪表盘/数据看板
  C. 管理后台/SaaS    D. 电商/产品展示
  E. 博客/内容站      F. 作品集
  G. 组件库/单个组件  H. 其他(请说明)

Q4: 风格偏好? (可选,未回答则自动匹配)
  A. 极简    B. 玻璃态    C. 暗色模式    D. Bento网格
  E. 新粗野主义  F. 霓虹/赛博朋克  G. 粘土态
  H. 扁平    I. 无偏好(自动推荐)
```

#### Step 1.2: 输出需求卡片

```markdown
## 需求卡片

| 字段 | 值 |
|------|-----|
| 项目类型 | [全新/重构/新增/审查] |
| 技术栈 | [Vue3+Tailwind/React+Tailwind/原生/...] |
| 页面类型 | [落地页/仪表盘/SaaS/...] |
| 风格偏好 | [具体风格 或 "自动推荐"] |
| 产品领域 | [SaaS/电商/金融/健康/...] |
| 目标受众 | [C端/B端/开发者/...] |
| 额外约束 | [SEO要求/性能要求/品牌指南/...] |
```

### Gate 1 检查
- [ ] 4个问题已回答(Q4 可选除外)
- [ ] 需求卡片所有必填字段完整
- [ ] 产品领域可识别(用于配色匹配)

### 示例

```
用户: "帮我做个AI工具网站的首页"
  → Q1: A(全新项目)
  → Q2: B(React+Tailwind)
  → Q3: A(落地页)
  → Q4: I(自动推荐)
  → 产品领域: AI SaaS
  → 输出需求卡片 ✓ → Gate 1 通过
```

---

## Phase 2: 设计系统生成 (Design System)

### 目标
生成项目的完整设计系统文件,作为所有后续实现的唯一真相源。

### 输入
Phase 1 的需求卡片。

### 步骤

#### Step 2.1: 产品-风格匹配

根据产品领域从 67 种风格中推荐 Top 3:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<产品领域> <风格关键词>" --design-system -p "<项目名>"
```

#### Step 2.2: 生成设计系统文件

输出 `design-system/MASTER.md`,必须包含:

```markdown
# [项目名] 设计系统

## 1. 风格方案
- 主风格: [名称]
- 辅风格: [名称(可选)]
- 模式: [亮色/暗色/自动]

## 2. 配色方案 (4-6个语义色值)
| Token | Hex | 用途 |
|-------|-----|------|
| --bg-primary | #xxx | 主背景 |
| --bg-secondary | #xxx | 卡片/面板 |
| --accent-primary | #xxx | 主强调色 |
| --accent-secondary | #xxx | 辅强调色 |
| --text-primary | #xxx | 主文本 |
| --text-secondary | #xxx | 次要文本 |

## 3. 字体搭配
| 角色 | 字体 | 权重 | 用途 |
|------|------|------|------|
| Display | [字体名] | [weight] | 标题/大数字 |
| Body | [字体名] | [weight] | 正文/控件 |
| Mono | [字体名] | [weight] | 代码/数据 |

## 4. 效果系统
- 阴影: [sm/md/lg/xl 参数]
- 圆角: [sm/md/lg 参数]
- 模糊: [glassmorphism 参数(如适用)]

## 5. 反模式警告
- ❌ [该产品类型应避免的设计陷阱1]
- ❌ [该产品类型应避免的设计陷阱2]

## 6. 预交付清单
- [ ] 配色对比度 ≥ 4.5:1
- [ ] 字体已导入 Google Fonts
- [ ] 暗色模式(如适用)已定义
```

#### Step 2.3: 生成 CSS 变量文件(可选)

如果用户需要即用代码:
```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "<项目名>"
```

### Gate 2 检查
- [ ] MASTER.md 6 个章节全部完成
- [ ] 配色方案包含 4-6 个语义 Token
- [ ] 字体搭配包含 Google Fonts 导入链接
- [ ] 反模式警告非空

---

## Phase 3: 代码生成 (Implementation)

### 目标
根据 MASTER.md 生成可运行的前端代码。

### 子流程

#### 3A: 落地页生成

**输入**: MASTER.md + "落地页"
**调度**: landing-page-generator

```
12 段式结构:
1. Hero → 2. Social Proof → 3. Problem → 4. Solution
→ 5. Features(Bento) → 6. How It Works → 7. Demo/Video
→ 8. Testimonials → 9. Pricing → 10. FAQ
→ 11. Final CTA → 12. Footer
```

**技术栈适配**:
- React → shadcn-ui 组件
- Vue → shadcn-vue 组件
- 原生 → vanilla-web + Tailwind CDN

#### 3B: 仪表盘生成

**输入**: MASTER.md + "仪表盘"
**调度**: ui-ux-pro-max (chart domain)

```
仪表盘布局:
┌──────────────────────────────┐
│ Header / Top Nav             │
├────┬────┬────┬────┬─────────┤
│ KPI│ KPI│ KPI│ KPI│  Chart  │
│  1 │  2 │  3 │  4 │   (Big) │
├────┴────┴────┴────┤         │
│  Chart (Wide)     │         │
├───────────────────┤         │
│  Table/List       │         │
└───────────────────┴─────────┘
```

#### 3C: 组件开发

**输入**: MASTER.md + 组件名
**调度**: 根据技术栈选择

| 技术栈 | 组件库 | 模式参考 |
|--------|--------|----------|
| React+Tailwind | shadcn-ui | shadcn/ui docs |
| Vue+Tailwind | shadcn-vue | vue-component-patterns |
| 原生 HTML | — | vanilla-web + css-styling-expert |

**组件规格模板** (来自 design-system sub-skill):
```markdown
| 属性 | Default | Hover | Active | Disabled |
|------|---------|-------|--------|----------|
| Background | primary | primary-dark | primary-darker | muted |
| Text | white | white | white | muted-fg |
| Border | transparent | primary-dark | primary-darker | muted |
| Shadow | none | sm | none | none |
| Cursor | pointer | pointer | pointer | not-allowed |
```

#### 3D: 动画/视频

**输入**: MASTER.md + 动画需求
**调度**: html-video (视频) / sprite-animation (CSS动画)

```
动画决策:
├── 微交互(按钮/卡片hover) → CSS transition 150-300ms
├── 入场动画(滚动触发) → CSS @keyframes + IntersectionObserver
├── 页面过渡 → Vue <Transition> / React Framer Motion
├── 复杂视频(multi-scene) → html-video (Hyperframes引擎)
└── 精灵动画(循环) → sprite-animation (CSS steps())
```

### Gate 3 检查
- [ ] 代码可在本地运行
- [ ] 所有页面/组件已生成
- [ ] MASTER.md 中的 Token 在代码中正确使用

---

## Phase 4: 交接检查 (Handoff)

### 目标
确保交付物格式规范,文件完整,可被下游工具或人类直接使用。

### 步骤

#### Step 4.1: 格式验证

对照 [handoff-format.md](handoff-format.md) 验证每个输出文件。

#### Step 4.2: 完整性验证

```markdown
## 交付物清单
- [ ] design-system/MASTER.md
- [ ] src/styles/tokens.css (如适用)
- [ ] tailwind.config.js (如适用)
- [ ] 所有页面/组件源文件
- [ ] qa-report.md (Phase 5 输出)
- [ ] README.md (项目说明)
```

### Gate 4 检查
- [ ] 所有文件使用 handoff-format.md 定义的结构
- [ ] 交付物清单全部打勾
- [ ] 输出目录结构清晰

---

## Phase 5: 质量审查 (Quality Review)

### 目标
对交付物执行 6 维度质量检查,输出 QA 报告。

### 步骤

#### Step 5A: 6 维度审查

详见 [qa-checklist.md](qa-checklist.md)。

#### Step 5B: 文案审查 (copy review)

**调度**: humanizer-zh

检查所有面向用户的文案:
- 无 AI 词汇("此外""至关重要""深入探讨""无缝的"等)
- 无三段式法则堆砌
- 无宣传式浮夸语言
- 有具体数据支撑
- 读起来像真人写的

#### Step 5C: UX 审查

**调度**: ui-ux-pro-max (ux domain)

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "animation accessibility z-index loading" --domain ux
```

重点检查:
- 可访问性(对比度/焦点/aria)
- 交互状态(hover/pressed/disabled)
- 动画性能(GPU加速/reduced-motion)
- 表单UX(label/error/feedback)

### Gate 5 检查
- [ ] 6 维度总分 ≥ 22/30
- [ ] 无阻断性缺陷
- [ ] QA 报告已生成

---

## 阶段深度调节

根据任务复杂度,调节各阶段展开程度:

### 轻量任务 (单组件/小修改)
```
Phase 1: 1轮对话 (只问Q2+Q3)
Phase 2: 跳过(使用现有设计系统)
Phase 3: 1轮对话 (直接生成组件)
Phase 4: 跳过(单文件无需交接)
Phase 5: 1轮对话 (快速 Checklist)
```

### 标准任务 (单页面)
```
Phase 1: 2轮对话
Phase 2: 1轮对话
Phase 3: 2-3轮对话
Phase 4: 1轮对话
Phase 5: 1轮对话
```

### 完整项目 (多页面+设计系统)
```
Phase 1: 2-3轮对话
Phase 2: 2轮对话 (含令牌生成)
Phase 3: 每页面2-3轮对话
Phase 4: 1轮对话
Phase 5: 2轮对话 (全面审查)
```
