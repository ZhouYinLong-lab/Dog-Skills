---
name: planning-with-files
description: >
  把开发规划持久化到项目 Markdown 文件中，解决 AI 编程最大的痛点——上下文压缩导致
  架构决策和设计细节丢失。强制性将每次讨论的设计点、决策、进度自动写入 plan 文件，
  下次开新对话时 Claude Code 读到这些文件即可恢复状态。
  Trigger keywords: planning with files, 规划文件, 上下文持久化, 开发规划,
  设计决策记录, plan this feature, 持久化规划, 防止上下文丢失, 状态恢复,
  开发进度追踪, 架构决策记录。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - TaskCreate
  - Agent
metadata:
  category: development
  source: https://github.com/anthropic/claude-plugin-directory
  install: /plugin install planning-with-files@claude-plugin-directory
  version: "1.0.0"
  license: MIT
---

# Planning with Files — 开发规划持久化

> AI 编程最让人不省心的不是代码写得不对，是上下文压缩。三天后重开对话，它完全不记得之前的架构方案。

Planning with Files 解决的就是这个问题。

## 核心原理

把所有开发规划、设计决策、进度追踪都写进项目里的 Markdown 文件。不是"建议你记下来"这种软性建议，是**强制性的**。

```
每个设计讨论 → 自动更新对应 plan 文件
下次新对话   → Claude Code 读文件 → 状态恢复
```

## 安装

```
/plugin install planning-with-files@claude-plugin-directory
```

## 使用方式

装完之后对 Claude Code 说一句：

```
plan this feature
```

它会自动创建 Markdown 规划文件。后续所有的对话、操作都记录在这些文件里。就算你关掉终端出去吃个饭，回来重开对话，它看一眼文件就知道做到哪了。

## 为什么需要它

Claude Code 的上下文窗口有限。对话一长，为了省 token，会把前面的内容压缩成摘要。这个压缩过程里，很多关键的开发决策和设计细节就丢了。

**Planning with Files 的本质是：用文件系统做"外置记忆"。**

## 最佳搭配

- **Superpowers**：一个管流程约束（先问再做），一个管状态持久化（写到文件）。两个互补，形成完整的开发闭环。
- **token-optimizer**：确保 plan 文件不会被当作冗余内容清理掉
