---
name: brand-workshop
description: >
  品牌全案设计工作坊——Discovery（发现）→ Concept（概念）→ Creation（创作）三阶段，
  输出完整品牌标识包：Logo 多方案、品牌标语、品牌简介、DESIGN.md 设计令牌。
  Trigger keywords: 品牌设计, 品牌工作坊, brand workshop, 做Logo,
  品牌全案, brand identity, 设计令牌, 创业品牌, tagline, 标语设计。
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
metadata:
  category: design
  source: sorawit-w/agent-skills
  version: "1.0.0"
  license: MIT
---

# Brand Workshop — 品牌全案设计工作坊

> Discovery → Concept → Creation：三阶段输出完整品牌标识包。

## 三阶段流程

```
Discovery           Concept            Creation
┌──────────┐      ┌──────────┐      ┌──────────┐
│ 品牌定位  │     │ 概念发散  │     │ Logo 设计 │
│ 目标用户  │────▶│ 风格探索  │────▶│ 标语输出  │
│ 竞品分析  │     │ 方案筛选  │     │ 设计令牌  │
│ 核心价值  │     │ 3-5个方向 │     │ 品牌手册  │
└──────────┘      └──────────┘      └──────────┘
```

## 输出物

- **Logo 设计**：多方案比选，每种方案有设计理念说明
- **品牌标语 (Tagline)**：3-5 个候选，附适用场景
- **品牌简介 (Brand Brief)**：一页纸品牌定位文档
- **DESIGN.md 设计令牌**：颜色体系、字体搭配、间距规范

## 安装

```bash
/plugin marketplace add sorawit-w/agent-skills
/plugin install agent-skills@sorawit-w
```

## 触发示例

- "帮我的冥想 App 做一整套品牌设计"
- "run the full brand workshop for my SaaS startup"
- "帮我设计一个新产品的品牌标识"
