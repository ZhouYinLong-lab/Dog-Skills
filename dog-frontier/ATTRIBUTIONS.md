# Dog-Frontier 归属声明 (Attributions)

Dog-Frontier 是一个**元技能(Meta-Skill)** — 它通过编排调度和知识整合来协调多个上游专业技能,
而非复制其源代码或内容。本文件记录所有上游技能的版权信息、许可协议和原始出处。

---

## 概念说明

### 什么是"整合"而非"复制"

| 方式 | 说明 |
|------|------|
| ❌ 不做的 | 直接复制上游 SKILL.md 内容、代码片段或数据文件 |
| ✅ 做的 | 通过路由决策引用上游技能 → 调度执行 → 整合输出 |
| ✅ 做的 | 提炼通用设计原则(非技能特有内容)供快速参考 |
| ✅ 做的 | 组合多个技能的输出为统一的交付物 |

### 类比说明

Dog-Frontier 之于前端技能生态,如同 **Webpack** 之于 JavaScript 模块:
- Webpack 不重新实现 lodash、React 或 Vue,而是将它们打包整合
- Dog-Frontier 不重新实现 ui-ux-pro-max、shadcn-ui 或 html-video,而是将它们编排整合

---

## Layer 0: 设计格式与品牌库 (Design Format & Brand Library) — v2.0 新增

### DESIGN.md 格式标准 (google-labs-code/design.md)
- **名称**: DESIGN.md Format Specification
- **版权持有者**: Google LLC
- **许可**: Apache License 2.0
- **仓库**: https://github.com/google-labs-code/design.md
- **核心贡献**:
  - 双层文档格式：YAML 设计令牌（机器可读）+ Markdown 规范文档（人类可读）
  - `@google/design.md` CLI 工具（lint / diff / export / spec）
  - 7 条 lint 规则（broken-ref, contrast-ratio, orphaned-tokens, section-order 等）
  - 可导出 Tailwind v3/v4 config、W3C DTCG JSON
  - 8 段式规范章节顺序（Overview → Colors → Typography → Layout → Elevation → Shapes → Components → Do's and Don'ts）
- **Dog-Frontier 使用方式**: Phase 2 输出格式标准, Phase 4 export 框架配置, Phase 5 lint 自动化校验

### awesome-design-md (VoltAgent/awesome-design-md)
- **名称**: Awesome DESIGN.md
- **版权持有者**: VoltAgent
- **许可**: MIT License
- **仓库**: https://github.com/VoltAgent/awesome-design-md
- **Stars**: 91,000+
- **核心贡献**:
  - 58 家知名公司/品牌的 DESIGN.md 反向工程文件
  - 覆盖 8 大分类: AI/LLM、开发者工具、后端/DevOps、金融科技、生产力/SaaS、消费科技、汽车、设计工具
  - 每个品牌包含 DESIGN.md + preview.html + preview-dark.html
  - 9 段式扩展格式（基于 Google Stitch 格式 + Agent Prompt Guide + 设计禁区）
- **Dog-Frontier 使用方式**: Phase 2 品牌风格即插即用 — 用户说"Stripe风格"时自动匹配对应 DESIGN.md

---

## 上游技能归属

### Layer 1: 设计智能 (Design Intelligence)

#### ui-ux-pro-max
- **名称**: UI UX Pro Max
- **版权持有者**: nextlevelbuilder © 2024-2026
- **许可**: MIT License
- **仓库**: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- **市场**: Claude Code Plugin Marketplace (`nextlevelbuilder/ui-ux-pro-max-skill`)
- **核心贡献**:
  - 67 种 UI 风格的分类体系和检索系统
  - 161 种行业配色方案的 1:1 产品匹配
  - 57 种字体搭配的策展与 Google Fonts 集成
  - 99 条 UX 准则的结构化文档
  - 16 个技术栈的专项指南
  - v2.0 设计系统生成器(BM25 排序 + 反模式过滤)
- **Dog-Frontier 使用方式**: 通过 Python CLI 脚本调用其搜索和设计系统生成功能;引用其 UX 准则用作质量检查清单

#### frontend-design
- **名称**: Frontend Design
- **版权持有者**: Anthropic (Claude Code Plugin Marketplace)
- **许可**: Proprietary (完整条款见 LICENSE.txt)
- **市场**: Claude Code Plugin Marketplace (`claude-plugins-official/frontend-design`)
- **核心贡献**:
  - "从主题出发"的设计哲学 — 设计应植根于产品本身的世界
  - 排版个性理论 — 字体是页面个性的载体
  - 两轮工作法 — 先出设计计划(令牌系统),再审阅独特性,最后写代码
  - 克制的设计原则 — 在一个地方大胆,其余保持安静
  - 文案即设计材料 — 从用户侧写、主动语态、处理失败和空状态
- **Dog-Frontier 使用方式**: 引用其设计哲学作为"风格选择"和"代码生成"阶段的指导思想

---

### Layer 2: 组件与样式 (Components & Styling)

#### shadcn-ui (giuseppe-trisciuoglio/developer-kit)
- **名称**: shadcn-ui
- **版权持有者**: Giuseppe Trisciuoglio © 2024-2026
- **许可**: MIT License
- **技能页**: https://skills.sh/giuseppe-trisciuoglio/developer-kit/shadcn-ui
- **安装量**: 18,500+
- **核心贡献**: shadcn/ui 组件库的 AI Agent 集成指南,包括组件初始化、主题配置、组件添加和自定义模式
- **Dog-Frontier 使用方式**: 在用户选择 React 技术栈时,路由至此技能获取组件安装和配置指导

#### tailwind-design-system (giuseppe-trisciuoglio/developer-kit)
- **名称**: Tailwind Design System
- **版权持有者**: Giuseppe Trisciuoglio © 2024-2026
- **许可**: MIT License
- **技能页**: https://skills.sh/giuseppe-trisciuoglio/developer-kit/tailwind-design-system
- **安装量**: 1,600+
- **核心贡献**: Tailwind CSS 设计系统生成,包括颜色配置、字体扩展、间距系统和组件变体
- **Dog-Frontier 使用方式**: 在生成设计系统时引用其 Tailwind 配置模式

#### shadcn-tailwind (tenequm/claude-plugins)
- **名称**: shadcn-tailwind
- **版权持有者**: tenequm
- **许可**: MIT License
- **技能页**: https://skills.sh/tenequm/claude-plugins/shadcn-tailwind
- **安装量**: 88+
- **核心贡献**: shadcn/ui + Tailwind CSS 组合样式最佳实践
- **Dog-Frontier 使用方式**: 补充 shadcn + Tailwind 集成模式

#### css-styling-expert (cin12211/orca-q)
- **名称**: CSS Styling Expert
- **版权持有者**: cin12211
- **许可**: MIT License
- **技能页**: https://skills.sh/cin12211/orca-q/css-styling-expert
- **安装量**: 101+
- **核心贡献**: CSS 高级技巧、布局策略、动画技术和浏览器兼容性指南
- **Dog-Frontier 使用方式**: 在代码生成阶段引用其 CSS 高级技巧速查

---

### Layer 3: 框架专项 (Framework Specific)

#### shadcn-vue (noartem/laravel-vue-skills)
- **名称**: shadcn-vue
- **版权持有者**: noartem
- **许可**: MIT License
- **技能页**: https://skills.sh/noartem/laravel-vue-skills/shadcn-vue
- **安装量**: 727+
- **核心贡献**: shadcn/ui 的 Vue 3 移植版本(基于 Radix Vue),包括组件安装、配置和 Tailwind 集成
- **Dog-Frontier 使用方式**: 在用户选择 Vue 技术栈时,路由至此技能获取 Vue 版组件指导

#### vue-component-patterns (thebushidocollective/han)
- **名称**: Vue Component Patterns
- **版权持有者**: The Bushido Collective
- **许可**: MIT License
- **技能页**: https://skills.sh/thebushidocollective/han/vue-component-patterns
- **安装量**: 62+
- **核心贡献**: Vue 3 Composition API 组件设计模式,包括 Props/Emits 类型安全、Composables 提取和状态管理
- **Dog-Frontier 使用方式**: 在 Vue 代码生成阶段引用其组件模式规范

#### vanilla-web (janjaszczak/cursor)
- **名称**: Vanilla Web
- **版权持有者**: janjaszczak
- **许可**: MIT License
- **技能页**: https://skills.sh/janjaszczak/cursor/vanilla-web
- **安装量**: 239+
- **核心贡献**: 原生 HTML/CSS/JS 最佳实践,无框架依赖的 Web 开发指南
- **Dog-Frontier 使用方式**: 在用户选择原生技术栈时路由至此技能

---

### Layer 4: 品牌与设计令牌 (Brand & Tokens)

#### brand (ui-ux-pro-max sub-skill)
- **名称**: Brand Skill (ckm:brand)
- **版权持有者**: claudekit (ui-ux-pro-max 作者)
- **许可**: MIT License
- **核心贡献**: 品牌识别指南、声音框架、视觉识别系统、品牌资产管理
- **Dog-Frontier 使用方式**: 在品牌设计任务中引用其品牌指南模板

#### design-system (ui-ux-pro-max sub-skill)
- **名称**: Design System Skill (ckm:design-system)
- **版权持有者**: claudekit (ui-ux-pro-max 作者)
- **许可**: MIT License
- **核心贡献**: 三阶令牌架构(原始→语义→组件)、CSS 变量系统、间距/字体比例、组件规格
- **Dog-Frontier 使用方式**: 在设计令牌生成阶段引用其令牌架构模式

#### ui-styling (ui-ux-pro-max sub-skill)
- **名称**: UI Styling Skill (ckm:ui-styling)
- **版权持有者**: claudekit (ui-ux-pro-max 作者)
- **许可**: MIT License
- **核心贡献**: shadcn/ui 组件使用指南、Tailwind 自定义配置、Canvas 视觉设计系统
- **Dog-Frontier 使用方式**: 在组件实现阶段引用其样式指南

---

### Layer 5: 页面与内容 (Pages & Content)

#### landing-page-generator (kostja94/marketing-skills)
- **名称**: Landing Page Generator
- **版权持有者**: kostja94
- **许可**: MIT License
- **技能页**: https://skills.sh/kostja94/marketing-skills/landing-page-generator
- **安装量**: 1,200+
- **核心贡献**: 落地页自动生成流程,包括结构规划、文案生成和CTA优化
- **Dog-Frontier 使用方式**: 引用其 12 段式落地页结构框架

#### liquid-theme-standards (benjaminsehl/liquid-skills)
- **名称**: Liquid Theme Standards
- **版权持有者**: Benjamin Sehl / Shopify
- **许可**: MIT License
- **技能页**: https://skills.sh/benjaminsehl/liquid-skills/liquid-theme-standards
- **安装量**: 1,900+ (benjaminsehl) + 91+ (shopify)
- **核心贡献**: 主题设计标准、设计规范文件格式和主题一致性验证
- **Dog-Frontier 使用方式**: 引用其主题标准方法论用于设计系统一致性检查

---

### Layer 6: 动画与多媒体 (Animation & Media)

#### html-video (nexu-io/html-video)
- **名称**: html-video
- **版权持有者**: nexu-io © 2026
- **许可**: Apache License 2.0
- **仓库**: https://github.com/nexu-io/html-video
- **核心贡献**:
  - HTML→Video 元层架构 (prompt/link/repo → MP4)
  - 21 个许可清洁的视频模板(数据可视化/标题特效/产品宣传/片尾)
  - Hyperframes + Remotion 双渲染引擎
  - Content-Graph 多帧故事板 IR
  - AI 配乐(MiniMax) + 旁白 TTS
- **Dog-Frontier 使用方式**: 在视频/动画需求时路由至 html-video 技能,引用其模板分类

#### sprite-animation (nexu-io/open-design)
- **名称**: Sprite Animation
- **版权持有者**: nexu-io
- **许可**: MIT License
- **技能页**: https://skills.sh/nexu-io/open-design/sprite-animation
- **安装量**: 242+
- **核心贡献**: CSS 精灵动画技术,包括帧动画、steps() 缓动和性能优化
- **Dog-Frontier 使用方式**: 在动画需求中引用其精灵动画技术

---

### Layer 7: 质量保证 (Quality Assurance)

#### humanizer-zh (基于 blader/humanizer)
- **名称**: Humanizer-zh (中文人性化)
- **版权持有者**: blader (原始 humanizer 技能) + hardikpandya/stop-slop (参考)
- **许可**: MIT License
- **仓库**: https://github.com/blader/humanizer
- **核心贡献**:
  - 基于维基百科 "AI 写作特征" 指南(由 WikiProject AI Cleanup 维护)
  - 24 种 AI 写作模式检测(夸大象征意义、宣传性语言、-ing 肤浅分析、模糊归因等)
  - 中文适配的检测规则和改写策略
  - 5 维度质量评分体系(直接性/节奏/信任度/真实性/精炼度)
- **Dog-Frontier 使用方式**: 在文案生成和审查阶段引用其检测规则,确保输出文案自然无AI痕迹

---

## 未直接集成但推荐的技能

以下技能因与 Dog-Frontier 功能互补,建议用户根据需要单独安装:

| 技能 | 安装命令 | 场景 |
|------|----------|------|
| **jezweb/claude-skills@shadcn-ui** | `npx skills add jezweb/claude-skills@shadcn-ui -g -y` | 备选 shadcn 方案 (3K+ installs) |
| **secondsky/claude-skills@shadcn-vue** | `npx skills add secondsky/claude-skills@shadcn-vue -g -y` | 备选 Vue shadcn 方案 |

---

## 许可合规声明

### Dog-Frontier 自身
- **许可**: MIT License
- **版权**: © 2026 Dog-Skills Collection

### 上游许可兼容性
所有集成的上游技能均采用**宽松许可**(MIT 或 Apache-2.0),允许:
- ✅ 商业使用
- ✅ 修改和衍生作品
- ✅ 私人使用
- ✅ 分发

唯一的例外是 `frontend-design` (Proprietary),Dog-Frontier 仅引用其公开的设计哲学理念,
不包含其任何专有代码或内容。

### 归属方式
Dog-Frontier 通过以下方式确保上游作者获得应有的 credit:
1. 本 ATTRIBUTIONS.md 文件完整记录所有上游信息
2. SKILL.md 中的集成技能表格标注来源和许可
3. 设计输出中标注所使用的上游技能
4. 代码注释中标注参考来源

---

## 参考文献

- [Google DESIGN.md Format Specification](https://github.com/google-labs-code/design.md) — DESIGN.md 格式标准
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 58 品牌 DESIGN.md 合集
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — humanizer-zh 的理论基础
- [shadcn/ui](https://ui.shadcn.com) — shadcn-ui 和 shadcn-vue 的底层组件库
- [Tailwind CSS](https://tailwindcss.com) — 多个技能使用的 CSS 框架
- [Radix UI](https://www.radix-ui.com) — shadcn/ui 的底层无样式组件原语
- [Radix Vue](https://www.radix-vue.com) — shadcn-vue 的底层无样式组件原语
- [Hyperframes](https://github.com/heygen-com/hyperframes) — html-video 的默认渲染引擎
- [Remotion](https://remotion.dev) — html-video 的备选渲染引擎

---

*最后更新: 2026-07-09*
*如需更新或更正归属信息,请提交 PR 至 Dog-Skills 仓库。*
