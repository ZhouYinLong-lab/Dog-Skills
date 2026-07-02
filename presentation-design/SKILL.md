---
name: presentation-design
description: >
  演示设计板生成器——生成 6 页高级演示设计板（亮/暗双模式），合成为复合预览图。
  Trigger keywords: 演示设计, 演示板, presentation design, 设计提案,
  视觉方案, 6页设计板, design board, 提案设计, pitch deck design。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
metadata:
  category: design
  source: MagicCube/agentara
  version: "1.0.0"
  license: MIT
---

# Presentation Design — 演示设计板生成器

> 生成 6 页高级演示设计板，合成为一张复合预览图。

## 核心能力

- **6 页设计板**：封面 + 4 页内容 + 封底
- **亮色/暗色双模式**：一键切换风格
- **命名布局库**：统一视觉语言
- **复合预览图**：所有页面合成一张总览图

## 安装

```bash
npx skills add MagicCube/agentara --skill presentation-design -y -g
```

## 触发示例

- "帮我设计一个产品发布会的演示板"
- "做一套投资人 Pitch 的视觉方案"
- "design a premium presentation board for my SaaS"
