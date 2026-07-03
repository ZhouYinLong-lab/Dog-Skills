---
name: slack-gif-creator
description: >
  Slack GIF 动图生成器——创建专门针对 Slack 优化的动画 GIF。
  Emoji 128×128、消息 GIF 480×480，自动适配 Slack 的上传限制。
  Anthropic 官方出品。适合团队沟通、Demo 演示、产品功能展示。
  Trigger keywords: slack gif, 动图, GIF, Slack表情, 动画表情,
  做动图, 生成GIF, Slack GIF, animated GIF, 表情包, 演示动图,
  product demo GIF, Slack sticker, 团队表情。
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

# Slack GIF Creator — Slack 动图生成器

> Anthropic 官方出品。创建专门为 Slack 优化的动画 GIF，自动适配尺寸和大小限制。

## 支持的规格

| 类型 | 尺寸 | 用途 |
|------|------|------|
| **Emoji** | 128×128 | Slack 自定义表情 |
| **消息 GIF** | 480×480 | 频道消息里直接播放 |
| **演示 GIF** | 自定义 | 产品 Demo、Bug 复现 |

## 核心能力

- **自动优化** — 帧率、颜色数、文件大小自动控制在 Slack 限制内
- **多种来源** — 从截图序列/屏幕录制/代码动画生成
- **循环流畅** — 无缝循环、正反播放、定格首尾帧

## 安装

```bash
/plugin install example-skills@anthropic-agent-skills
```

## 触发示例

- "把这段屏幕录制做成 Slack GIF"
- "做一个产品功能演示的动图发 Slack"
- "create an animated emoji for our team Slack"
- "帮我做一个 bug 复现的 GIF，发给开发同事"
