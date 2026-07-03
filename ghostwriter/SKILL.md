---
name: ghostwriter
description: >
  【从零创作】AI 代笔专家——用你自己的语气从零写新消息，不是改已有文本。
  分析你的历史消息提取语气特征后，帮你写邮件/Slack/微信回复，读起来像你本人在打字。
  如需修改已有文本去AI味，用 humanizer-zh。
  Trigger keywords: 代笔, ghostwriter, 帮我回复, 代写消息,
  模仿我的语气, 写邮件, 回微信, 回Slack, 用自己的话,
  自然语气, 像我自己写的, 个人风格, 帮我写个回复。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
metadata:
  category: content
  source: sorawit-w/agent-skills
  version: "1.0.0"
  license: MIT
---

# Ghostwriter — AI 代笔专家

> 用你自己的语气写消息，零 AI 痕迹。读完你的历史消息后，写出来的东西像你本人在打字。

## 核心能力

- **语气克隆**：分析你的历史消息，提取语气特征
- **零 AI 痕迹**：去除"AI 味"——不啰嗦、不官方、不模板化
- **多平台适配**：邮件（正式）、Slack（半正式）、微信（随意）
- **长度控制**：你说"短一点"就真的是短一点

## 安装

```bash
/plugin marketplace add sorawit-w/agent-skills
/plugin install agent-skills@sorawit-w
```

## 触发示例

- "帮我回这封邮件，用我的语气，简短一点"
- "这个Slack消息怎么回？读起来要像我说的"
- "draft a reply to my manager, keep it in my voice"
- "帮我想一个拒绝饭局的微信回复，自然一点"
