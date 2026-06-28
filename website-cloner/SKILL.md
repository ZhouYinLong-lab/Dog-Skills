---
name: website-cloner
description: >
  Reverse-engineer and clone any website into a clean Next.js + shadcn/ui + Tailwind v4 codebase using AI coding agents.
  Multi-phase pipeline: reconnaissance → foundation → component specs → parallel build in git worktrees → assembly → visual QA.
  Supports Claude Code, Codex CLI, Cursor, Windsurf, Gemini CLI, Copilot, Cline, Roo Code, and more.
  Trigger keywords: clone website, copy website, replicate website, reverse engineer website, rebuild website,
  pixel-perfect clone, make a copy of this site, rebuild this page, 克隆网站, 抄袭网站, 复制网站, 逆向工程网站,
  像素级复刻, 网站复刻, /clone-website.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - TaskCreate
  - TaskUpdate
  - EnterWorktree
  - ExitWorktree
metadata:
  version: "1.0.0"
  license: MIT
  original-author: JCodesMore
  original-repo: https://github.com/JCodesMore/ai-website-cloner-template
  original-stars: 22390
---

# Website Cloner — AI 网站复刻技能

> 基于 [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) by **JCodesMore** (22.4K ⭐, MIT License)

点对点复刻任意网站为干净的 Next.js + shadcn/ui + Tailwind v4 代码库。多阶段流水线：侦察 → 基础设施 → 组件规格 → 并行构建 → 装配 → 视觉 QA。

---

## 触发条件

当用户请求涉及以下场景时,激活本技能:

- "克隆这个网站" / "帮我复刻这个页面"
- "Copy this website" / "Make a pixel-perfect clone of..."
- "Rebuild this site in Next.js"
- "/clone-website <url>"
- 任何涉及网站逆向工程、像素级复刻、从已有网站生成代码的需求

用户需提供目标 URL。支持多个 URL 并行处理。

---

## 前置要求

1. **浏览器自动化工具必须可用。** 检查可用的浏览器 MCP 工具（Chrome MCP, Playwright MCP, Browserbase MCP, Puppeteer MCP 等）。优先使用 Chrome MCP。如果没有检测到任何浏览器工具,询问用户如何连接。**本技能依赖浏览器自动化,不可跳过。**
2. **目标项目脚手架就绪。** Next.js + shadcn/ui + Tailwind v4 的基础项目应该已就位。如果用户还没有,引导他们从 [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) 创建自己的副本。
3. Node.js 24+, npm/pnpm。

---

## 技术栈

- **Next.js 16** — App Router, React 19, TypeScript strict
- **shadcn/ui** — Radix primitives + Tailwind CSS v4
- **Tailwind CSS v4** — oklch design tokens
- **Lucide React** — 默认图标(克隆过程中会被提取的 SVG 替换)

---

## 范围默认值

目标 URL 解析到的任何内容都在范围内。除非用户另有指定:

- **保真度:** 像素级 — 颜色、间距、排版、动画精确匹配
- **范围内:** 视觉布局和样式、组件结构和交互、响应式设计、演示用模拟数据
- **范围外:** 真实后端/数据库、身份认证、实时功能、SEO 优化、无障碍审计
- **定制化:** 无 — 纯模拟

如用户提供额外指示(特定保真度级别、定制化、额外上下文),以用户指示为准。

---

## 核心原则

以下是区分成功克隆和"差不多"的关键原则,必须在每个决策中内化:

### 1. 完整性优于速度

每个构建者 agent 必须获得做好工作所需的一切: 截图、精确 CSS 值、带本地路径的已下载资源、真实文本内容、组件结构。如果构建者需要猜测任何东西 — 颜色、字号、padding 值 — 你的提取就失败了。多花一分钟提取一个属性,好过交付不完整的简报。

### 2. 小任务,完美结果

当一个 agent 拿到"构建整个功能区域"的任务时,它会粗略处理 — 近似间距、猜测字号,做出"差不多"但明显错误的东西。当它拿到一个单独的、有精确 CSS 值的组件时,每次都能做对。

审查每个区域的复杂度。简单的 banner 加 heading 和 button?一个 agent。复杂的区域有 3 种不同的卡片变体,每种都有独特的 hover 状态和内部布局?每种卡片变体一个 agent,再加一个做区域包装器。不确定时,拆得更小。

**复杂度预算规则:** 如果一个构建者 prompt 超过 ~150 行规格内容,这个区域对一个 agent 来说太复杂了。拆成更小的块。这是机械检查 — 不要用"但它们都相关"来覆盖它。

### 3. 真实内容,真实资源

从真实网站提取实际文本、图片、视频和 SVG。这是克隆,不是模型。使用 `element.textContent`,下载每个 `<img>` 和 `<video>`,提取内联 `<svg>` 元素为 React 组件。只在内容明显是服务端生成且每次会话唯一时才生成内容。

**分层资源很重要。** 看起来像一张图片的区域通常是多层 — 背景水彩/渐变、前景 UI 模型 PNG、叠加图标。检查每个容器的完整 DOM 树,列举其中所有 `<img>` 元素和背景图片,包括绝对定位的叠加层。缺少叠加图片即使背景正确也会让克隆显得空洞。

### 4. 基础设施优先

在所有基础设施存在之前什么都不能构建: 带有目标网站设计令牌(颜色、字体、间距)的全局 CSS、内容结构的 TypeScript 类型、全局资源(字体、favicons)。这是顺序的、不可协商的。之后的所有内容可以并行。

### 5. 提取外观和行为

网站不是截图 — 它是活的东西。元素会移动、变化、出现和消失在滚动、悬停、点击、调整大小和时间响应中。如果只提取每个元素的静态 CSS,你的克隆在截图中看起来正确但实际使用时毫无生气。

对每个元素,提取其**外观**(通过 `getComputedStyle()` 的精确计算 CSS)和**行为**(什么变化、什么触发变化、过渡如何发生)。不是"看起来像 16px" — 提取实际的计算值。不是"导航栏在滚动时变化" — 记录精确的触发条件(滚动位置、IntersectionObserver 阈值、视口交叉)、前后状态(两组 CSS 值)和过渡(持续时间、缓动、CSS transition vs. JS 驱动 vs. CSS `animation-timeline`)。

### 6. 构建前识别交互模型

这是克隆中最昂贵的错误: 当原始网站是滚动驱动时构建基于点击的 UI,反之亦然。在编写任何交互区域的构建者 prompt 之前,你必须明确回答: **这个区域是由点击、滚动、悬停、时间还是某种组合驱动的?**

如何确定:
1. **不要先点击。** 缓慢滚动通过区域,观察事物是否随着滚动自己变化。
2. 如果是,那就是滚动驱动。提取机制: `IntersectionObserver`、`scroll-snap`、`position: sticky`、`animation-timeline` 或 JS 滚动监听器。
3. 如果滚动时什么都没变,然后再点击/悬停测试点击/悬停驱动的交互。
4. 在组件规格中明确记录交互模型: "INTERACTION MODEL: scroll-driven with IntersectionObserver" 或 "INTERACTION MODEL: click-to-switch with opacity transition."

### 7. 提取每种状态,不仅是默认状态

许多组件有多个视觉状态 — 标签栏在不同标签下显示不同卡片,页头在滚动位置 0 和 100 时看起来不同,卡片有悬停效果。你必须提取所有状态,不仅是页面加载时可见的。

### 8. 规格文件是真理之源

每个组件在调度任何构建者之前都必须在 `docs/research/components/` 中获得一个规格文件。这个文件是你提取工作和构建者 agent 之间的契约。构建者在其 prompt 中内联接收规格文件内容 — 该文件也作为可审计的产物保存。

### 9. 构建必须始终编译

每个构建者 agent 必须在完成前验证 `npx tsc --noEmit` 通过。合并工作树后,你验证 `npm run build` 通过。破损的构建永不可接受,即使是暂时的。

---

## 工作流概览

```
Phase 1: Reconnaissance        Phase 2: Foundation          Phase 3: Component Spec & Build
┌──────────────┐              ┌──────────────────┐         ┌──────────────────────────┐
│ Screenshots  │              │ Update fonts     │         │ Extract → Write Spec     │
│ Design tokens│──────────────▶│ Update globals   │────────▶│   → Dispatch Builder     │
│ Behaviors    │              │ Create types     │         │   → Merge Worktree       │
│ Page topology│              │ Download assets  │         │   → Verify Build         │
└──────────────┘              └──────────────────┘         └──────────────────────────┘
                                                                    │
                                                                    ▼
Phase 5: Visual QA Diff        Phase 4: Page Assembly
┌──────────────────────┐      ┌──────────────────────┐
│ Side-by-side compare │◀─────│ Wire all sections    │
│ Section-by-section   │      │ Page-level behaviors │
│ Fix discrepancies    │      │ npm run build passes │
└──────────────────────┘      └──────────────────────┘
```

---

## Phase 1: 侦察 (Reconnaissance)

使用浏览器 MCP 导航到目标 URL。

### 截图
- 在桌面端 (1440px) 和移动端 (390px) 视口下截取**全页截图**
- 保存到 `docs/design-references/`,使用描述性名称
- 这些是你的主参考 — 构建者稍后将收到区域特定的裁剪/截图

### 全局提取
在做任何其他事情之前从页面提取:

**字体** — 检查 `<link>` 标签中的 Google Fonts 或自托管字体。检查关键元素(标题、正文、代码、标签)上的计算 `font-family`。记录实际使用的每个字体族、字重和样式。使用 `next/font/google` 或 `next/font/local` 在 `src/app/layout.tsx` 中配置。

**颜色** — 从页面的计算样式中提取网站调色板。在 `:root` 和 `.dark` CSS 变量块中用目标网站的实际颜色更新 `src/app/globals.css`。在合适的地方映射到 shadcn 的令牌名称(background, foreground, primary, muted 等)。为不适合 shadcn 令牌的颜色添加自定义属性。

**Favicons & Meta** — 下载 favicons, apple-touch-icons, OG images, webmanifest 到 `public/seo/`。更新 `layout.tsx` metadata。

**全局 UI 模式** — 识别任何站点范围的 CSS 或 JS: 自定义滚动条隐藏、页面容器上的 scroll-snap、全局关键帧动画、backdrop filters、用作叠加层的渐变、**平滑滚动库**(Lenis, Locomotive Scroll — 检查 `.lenis`, `.locomotive-scroll` 或自定义滚动容器类)。将这些添加到 `globals.css` 并记录需要安装的任何库。

### 强制交互扫描

**滚动扫描:** 通过浏览器 MCP 从顶部到底部缓慢滚动页面。在每个区域暂停观察。

**点击扫描:** 点击每个看起来可交互的元素: 按钮、标签、卡片、链接。记录会发生什么。

**悬停扫描:** 悬停在每个可能有悬停状态的元素上: 按钮、卡片、链接、图片、导航项。

**响应式扫描:** 通过浏览器 MCP 在 3 种视口宽度下测试: 桌面 1440px, 平板 768px, 移动端 390px。

将发现保存到 `docs/research/BEHAVIORS.md`。

### 页面拓扑
从顶部到底部绘制页面每个不同区域的映射。给每个区域起一个工作名称。记录:
- 它们的视觉顺序
- 哪些是固定/粘性叠加层 vs. 流内容
- 整体页面布局(滚动容器、列结构、z-index 层级)
- 区域之间的依赖关系
- **每个区域的交互模型**(静态、点击驱动、滚动驱动、时间驱动)

保存为 `docs/research/PAGE_TOPOLOGY.md` — 这成为你的装配蓝图。

---

## Phase 2: 基础设施构建 (Foundation Build)

这是顺序的,自己完成(不委托给 agent):

1. **更新字体** — 在 `layout.tsx` 中匹配目标网站的实际字体
2. **更新 globals.css** — 目标网站的颜色令牌、间距值、关键帧动画、工具类和任何**全局滚动行为**
3. **创建 TypeScript 接口** — 在 `src/types/` 中为观察到的内容结构创建类型
4. **提取 SVG 图标** — 找到页面上所有内联 `<svg>` 元素,去重并保存为 `src/components/icons.tsx` 中的具名 React 组件
5. **下载全局资源** — 编写并运行 Node.js 脚本(`scripts/download-assets.mjs`)下载所有图片、视频和其他二进制资源
6. 验证: `npm run build` 通过

---

## Phase 3: 组件规格与调度 (Component Specification & Dispatch)

这是核心循环。对页面拓扑中的每个区域(从上到下),做三件事: **提取**, **编写规格文件**, 然后**调度构建者**。

### Step 1: 提取

对每个区域,使用浏览器 MCP 提取一切:

1. **截图** 单独区域,保存到 `docs/design-references/`
2. **提取 CSS** — 对区域中每个元素使用 `getComputedStyle()`,运行完整的 DOM 树遍历提取脚本
3. **提取多状态样式** — 对于有多个状态的元素,分别捕获并做 diff
4. **提取真实内容** — 所有文本、alt 属性、aria labels、placeholder 文本
5. **识别资源** — 该区域使用的已下载图片/视频和图标组件
6. **评估复杂度** — 该区域包含多少个不同的子组件?

### Step 2: 编写组件规格文件

为每个区域(或子组件)在 `docs/research/components/` 中创建规格文件。**不可跳过。**

模板包含: Overview, DOM Structure, Computed Styles (精确值), States & Behaviors (触发条件、前后状态、过渡), Per-State Content (如适用), Assets, Text Content (逐字), Responsive Behavior。

### Step 3: 调度构建者

根据复杂度,在工作树中调度构建者 agent:

- **简单区域**(1-2 个子组件): 一个构建者 agent 获得整个区域
- **复杂区域**(3+ 不同子组件): 拆分。每个子组件一个 agent,再加一个区域包装器 agent

每个构建者 agent 接收:
- 其组件规格文件的完整内容(内联在 prompt 中)
- 区域截图路径
- 要导入的共享组件
- 目标文件路径
- 验证指令: `npx tsc --noEmit` 在完成前必须通过

**不要等待。** 一旦为一个区域调度了构建者,立即继续提取下一个区域。构建者在工作树中并行工作。

### Step 4: 合并

当构建者 agent 完成:
- 合并他们的工作树分支到主分支
- 你有每个 agent 构建了什么的完整上下文,智能解决冲突
- 每次合并后,验证构建: `npm run build`
- 如有类型错误,立即修复

---

## Phase 4: 页面装配 (Page Assembly)

所有区域构建并合并后,在 `src/app/page.tsx` 中连接一切:
- 导入所有区域组件
- 实现页面级布局(滚动容器、列结构、粘性定位、z-index 分层)
- 连接真实内容到组件 props
- 实现页面级行为: scroll snap、滚动驱动动画、暗亮过渡、交集观察器、平滑滚动
- 验证: `npm run build` 干净通过

---

## Phase 5: 视觉 QA 对比 (Visual QA Diff)

装配后,**不要**宣布克隆完成。进行并排比较截图:

1. 并排打开原始网站和你的克隆(或在同一视口宽度下截图)
2. 从上到下逐区域比较,桌面端 (1440px)
3. 移动端 (390px) 再次比较
4. 对发现的每个差异:
   - 检查组件规格文件 — 值是否被正确提取?
   - 如规格错误: 从浏览器 MCP 重新提取,更新规格,修复组件
   - 如规格正确但构建者做错了: 修复组件以匹配规格
5. 测试所有交互行为: 滚动页面、点击每个按钮/标签、悬停在交互元素上
6. 验证平滑滚动、页头过渡、标签切换、动画

只有在此视觉 QA 通过后,克隆才算完成。

---

## 调度前检查清单

调度任何构建者 agent 之前,验证每项都可打勾。如不能,回去提取更多:

- [ ] 规格文件写入 `docs/research/components/<name>.spec.md`,所有部分已填写
- [ ] 规格中每个 CSS 值来自 `getComputedStyle()`,不是估算
- [ ] 交互模型已识别并记录(static / click / scroll / time)
- [ ] 对有状态的组件: 每个状态的内容和样式已捕获
- [ ] 对滚动驱动的组件: 触发阈值、前后样式和过渡已记录
- [ ] 对悬停状态: 前后值和过渡时间已记录
- [ ] 区域中所有图片已识别(包括叠加层和分层组合)
- [ ] 响应式行为至少记录了桌面端和移动端
- [ ] 文本内容逐字来自网站,不是改写
- [ ] 构建者 prompt 在 ~150 行规格以内;如超过,区域需要拆分

---

## 不应该做的事

- **不要构建基于点击的标签页,当原始网站是滚动驱动的(反之亦然)。** 先通过滚动确定交互模型。这是最昂贵的错误之一。
- **不要只提取默认状态。** 如有标签,点击每个标签并提取内容/卡片。
- **不要遗漏叠加/分层图片。** 背景水彩 + 前景 UI 模型 = 2 张图片。
- **不要将视频/动画内容构建为静态模型。** 检查是否使用了 `<video>`、Lottie 或 canvas。
- **不要近似 CSS 类名。** 提取精确值,不要猜测 Tailwind 类名。
- **不要在构建者 prompt 中引用外部文档。** 每个构建者在其 prompt 中内联获得完整 CSS 规格。
- **不要跳过资源提取。** 没有真实图片、视频和字体,无论 CSS 多么完美,克隆看起来都是假的。
- **不要给构建者 agent 太大的范围。** 如果 prompt 越来越长,这说明需要拆分成更小的任务。
- **不要忘记平滑滚动库。** 检查 Lenis、Locomotive Scroll 等。
- **不要在没有规格文件的情况下调度构建者。**

---

## 完成报告

完成后,报告:
- 构建的区域总数
- 创建的组件总数
- 编写的规格文件总数(应与组件数匹配)
- 下载的资源总数(图片、视频、SVG、字体)
- 构建状态(`npm run build` 结果)
- 视觉 QA 结果(剩余的任何差异)
- 任何已知差距或限制

---

## 支持平台

| Agent | 状态 |
|-------|------|
| **Claude Code** | **推荐** — Opus 4.7 |
| Codex CLI | 支持 |
| OpenCode | 支持 |
| GitHub Copilot | 支持 |
| Cursor | 支持 |
| Windsurf | 支持 |
| Gemini CLI | 支持 |
| Cline | 支持 |
| Roo Code | 支持 |
| Continue | 支持 |
| Amazon Q | 支持 |
| Augment Code | 支持 |
| Aider | 支持 |

---

## 用途场景

- **平台迁移** — 将自有网站从 WordPress/Webflow/Squarespace 重建为现代 Next.js 代码库
- **源代码丢失** — 网站还在运行但仓库不见了,开发人员离职了,或技术栈已过时
- **学习** — 通过真实代码解构生产站点如何实现特定布局、动画和响应式行为

## 禁止用途

- **钓鱼或冒充** — 本项目不得用于欺骗性目的、冒充或任何违法活动
- **冒充他人设计** — logos、品牌资源和原始文案属于其所有者
- **违反服务条款** — 有些网站明确禁止抓取或复制,请先检查

---

*Original author: [JCodesMore](https://github.com/JCodesMore) · Source: [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) · License: MIT*
