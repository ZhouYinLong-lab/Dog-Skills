---
name: superpowers
description: >
  Superpowers 是一套完整的 AI 软件开发方法论，包含 20+ 可自由组合的 Skill，
  通过五步核心流程（头脑风暴→Git Worktree 隔离→任务规划→子Agent驱动开发→分支收尾）
  彻底改变 Claude Code 的行为模式：从"先斩后奏"变成"先问再做"。
  Trigger keywords: superpowers, 开发方法论, subagent-driven-development,
  brainstorming, 苏格拉底式追问, 开发流程, 任务拆解, 子Agent开发, worktree隔离,
  代码审查流程, AI开发最佳实践, 需求澄清, 写代码前先问我。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - TaskCreate
  - TaskUpdate
  - AskUserQuestion
metadata:
  category: development
  source: https://github.com/anthropics/claude-plugins-official
  install: /plugin install superpowers@claude-plugins-official
  version: "1.0.0"
  license: MIT
---

# Superpowers — AI 软件开发方法论

> 如果你只想装一个 Skill，那就装这个。22 万 GitHub Star 不是白拿的。

Superpowers 不是某一个功能模块，它是一整套软件开发方法论，塞进了 20 多个可自由组合的 Skill 里，核心流程分五步。

## 核心五步流程

```
brainstorming → using-git-worktrees → writing-plans → subagent-driven-development → finishing-a-development-branch
    │                  │                    │                    │                           │
 苏格拉底式追问     创建隔离分支        拆成 2-5 分钟任务    子Agent实现+两级审查        合并/PR/丢弃
```

### 1. Brainstorming（头脑风暴）
在你开始写任何代码之前，Claude Code 会像苏格拉底一样追问你：
- 这个功能给谁用的？
- 要不要登录？数据存本地还是云端？
- 要不要分享功能？
- 边界条件你想好了吗？

**效果**：问到你烦为止。但正是这种追问，能让你在动手之前把需求想清楚。

### 2. Using Git Worktrees（隔离开发）
为每个功能创建独立的 Git Worktree，互不干扰，可以并行开发多个功能。

### 3. Writing Plans（任务规划）
把需求拆成 2-5 分钟能完成的小任务，每个任务有明确的完成标准。

### 4. Subagent-Driven Development（子Agent驱动开发）⭐ 最狠的一招
每完成一个任务，启动一个全新的子 Agent 做**两级审查**：
- **第一级**：检查是否符合 Spec
- **第二级**：检查代码质量

查出 **Critical 级别的问题直接阻断**后续流程，不修好别想往下走。

### 5. Finishing a Development Branch（分支收尾）
合并代码、创建 PR、或丢弃分支——规范化收尾。

## 安装

```
/plugin install superpowers@claude-plugins-official
```

安装后重启 Claude Code。Superpowers 会自动检测你是否在搞开发任务，然后走完整流程。

## 使用感受

装上之后最明显的变化：Claude Code 不再"先斩后奏"。以前让它加个功能，直接噼里啪啦写 500 行代码，写完才发现方向全错。现在它必须先让你看过方案，点了头，才动手。

## 最佳搭配

- **Planning with Files**：Superpowers 管流程约束，Planning with Files 管状态持久化
- **Code Review + Code Simplifier**：在 Subagent 审查之后再加一层质量把关
- **token-optimizer**：控制 Superpowers 多 Agent 流程的 Token 消耗
