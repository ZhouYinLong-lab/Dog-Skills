---
name: dog-frontier
description: >
  前端设计综合技能系统(Dog-Frontier)。通过多轮对话精确理解需求,整合18个专业前端技能的精华,
  输出高质量、高结构化的前端设计方案与代码。覆盖 UI/UX 设计系统、Tailwind/shadcn 组件库、
  Vue/React 技术栈、CSS 高级技巧、落地页生成、动画视频、品牌设计、设计令牌三大层级等全链路。
  Trigger keywords: 前端设计, 前端开发, UI设计, 设计系统, 落地页, landing page, dashboard,
  仪表盘, 组件开发, Vue组件, React组件, Tailwind, shadcn, 配色方案, 字体搭配, 品牌设计,
  CSS动画, HTML视频, 响应式布局, 前端重构, 界面优化, UX审查, 设计令牌, design tokens,
  Dog-Frontier, 前端综合.
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
  version: "1.0.0"
  license: MIT
  integrated-skills: 18
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

---

## 流程总控

整个技能按以下 5 阶段流水线运行。每阶段完成后,必须通过该阶段的验收门(Gate)才能进入下一阶段。

```
Phase 1: Discovery          Phase 2: Design System        Phase 3: Implementation
┌──────────────┐           ┌──────────────────┐           ┌──────────────────┐
│ 需求勘探      │           │ 设计系统生成      │           │ 代码生成          │
│              │    →      │                  │    →     │                  │
│ 4个关键问题   │   Gate 1  │ 风格+配色+字体    │   Gate 2  │ 组件+布局+页面    │   Gate 3
│ 输出: 需求卡  │           │ 输出: MASTER.md   │           │ 输出: 源代码      │
└──────────────┘           └──────────────────┘           └──────────────────┘
                                                                     │
                                                                     ▼
Phase 5: Quality Review                            Phase 4: Handoff Check
┌──────────────────┐                              ┌──────────────────┐
│ 质量审查          │                              │ 交接检查          │
│                  │    ←                         │                  │
│ 6维度+验收清单    │         Gate 4               │ 格式+完整性验证   │
│ 输出: QA报告      │                              │ 输出: 交接包      │
└──────────────────┘                              └──────────────────┘
```

### 阶段门控 (Gates)

| 门 | 检查内容 | 不通过时的处理 |
|----|----------|---------------|
| **Gate 1** | 4个问题全回答,需求卡片完整 | 回到 Phase 1,追问缺失信息 |
| **Gate 2** | MASTER.md 包含: 风格/配色/字体/效果/反模式 | 回到 Phase 2,补充缺失维度 |
| **Gate 3** | 代码可运行,覆盖所有页面/组件 | 修复问题后重新验证 |
| **Gate 4** | 交接格式合规,文件完整 | 补充缺失文件 |
| **Gate 5** | 6 维度评分 ≥ 35/50 | 修复不达标的维度 |

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
| **总计** | **≥ 22/30** | **30** |

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
"这个页面的配色帮我优化一下"        → Phase 2 (只走设计系统)
"帮我写一个Vue表格组件"            → Phase 3 (只走代码生成)
"审查一下这个页面的UX"             → Phase 5 (只走质量审查)
"把这个设计的文案改得更自然"        → Phase 5 文案流程
"生成设计令牌/design tokens"       → Phase 2 令牌生成
"做一个产品介绍视频"               → Phase 3 动画流程
```

---

## 集成技能总览

| Layer | 技能 | 许可 | 何时调度 |
|-------|------|------|----------|
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

完整归属声明: [ATTRIBUTIONS.md](ATTRIBUTIONS.md)

---

## 文件导航

```
dog-frontier/
├── SKILL.md                     # 本文件 — 流程总控、触发条件、验收标准
├── ATTRIBUTIONS.md              # 18个集成技能的完整归属声明
├── references/
│   ├── workflow.md              # 5阶段详细说明,每阶段输入/输出/步骤/示例
│   ├── handoff-format.md        # 阶段间交接的结构化格式定义
│   └── qa-checklist.md          # 最终验收清单(6维度30项)
├── scripts/
│   └── design-system.py         # 设计系统生成脚本(BM25搜索 + 反模式过滤)
├── assets/
│   ├── design-tokens.md         # 三阶令牌架构参考
│   ├── ui-styles-catalog.md     # 67种UI风格速查
│   ├── vue-patterns.md          # Vue 3组件设计模式
│   ├── css-expertise.md         # CSS高级技巧手册
│   ├── landing-patterns.md      # 12段式落地页结构
│   ├── design-brief.md          # 设计简报模板
│   └── output-formats.md        # 固定输出格式模板
```
