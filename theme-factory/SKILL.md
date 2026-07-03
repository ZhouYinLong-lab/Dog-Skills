---
name: theme-factory
description: >
  主题工厂——为幻灯片、文档、HTML 页面一键应用专业主题样式。
  内置 10 套预设主题（含亮/暗模式），也支持即时生成自定义主题。
  覆盖字体、颜色、间距、圆角、阴影等全套设计令牌。Anthropic 官方出品。
  Trigger keywords: theme factory, 主题工厂, 换主题, 应用主题, 幻灯片主题,
  文档主题, 配色主题, 一键换肤, 亮暗模式, 设计主题, 批量应用样式,
  apply theme, switch theme, 统一风格, 快速美化。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Agent
metadata:
  category: design
  source: anthropics/skills (official)
  version: "1.0.0"
  license: MIT
---

# Theme Factory — 主题工厂

> Anthropic 官方出品。为任何文档一键应用专业设计主题，告别裸奔的默认样式。

## 10 套预设主题

每套主题包含完整的 **亮色/暗色双模式**：
- 字体（标题 + 正文 + 代码）
- 颜色体系（主色 + 辅色 + 强调 + 背景 + 文字）
- 间距比例（基于 4px 网格）
- 圆角 + 阴影 + 边框风格

## 核心能力

- **一键换肤** — 选中目标（幻灯片/文档/HTML），指定主题，自动应用
- **即时自定义** — "帮我生成一套海洋风格的蓝色主题"
- **设计令牌输出** — 生成 CSS 变量 / Tailwind 配置 / DESIGN.md
- **批量统一** — 确保多页幻灯片或整个文档站风格一致

## 安装

```bash
/plugin install example-skills@anthropic-agent-skills
```

## 触发示例

- "给这套幻灯片换一个科技风的暗色主题"
- "帮我生成一套适合医美品牌的柔和主题"
- "apply a minimal warm theme to this document"
- "用主题工厂统一这 5 个页面的风格"
