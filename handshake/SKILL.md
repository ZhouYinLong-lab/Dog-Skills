---
name: handshake
description: >
  协作风格校准——开工前与 Claude 的简短校准仪式。通过 6 个维度刻度
  和 RPG 职业分类，让 Claude 真正了解你想怎么协作，从此不再给千篇一律的回答。
  Trigger keywords: handshake, 协作风格, 校准, 个性化, whoami,
  工作风格, 协作偏好, 了解我, 沟通风格, 怎么跟我合作。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Agent
  - AskUserQuestion
metadata:
  category: tools
  source: sorawit-w/agent-skills
  version: "1.0.0"
  license: MIT
---

# Handshake — 协作风格校准

> 开工前的简短校准仪式。让 Claude 真正了解你想怎么协作，不再给千篇一律的回答。

## 核心能力

- **6 维度刻度**：详细程度、技术深度、幽默感、质疑程度、创意自由度、简洁度
- **RPG 职业分类**：你是什么类型的协作者？（架构师/黑客/探险家/外交官……）
- **便携工作手册**：生成一份可复用的协作画像，跨会话生效

## 安装

```bash
/plugin marketplace add sorawit-w/agent-skills
/plugin install agent-skills@sorawit-w
```

## 触发示例

- "/handshake — 校准一下我们的协作方式"
- "帮我做一份 whoami 画像"
- "calibrate how we work — I'm tired of generic answers"
