---
name: code-simplifier
description: >
  AI 生成代码后自动二次优化——不改代码行为，只优化结构和可读性。消除重复代码、
  减少嵌套层级、简化复杂逻辑、提取公共可复用函数。代码行数通常减少 30-40%，
  嵌套深度从 4-5 层降到 1-2 层。
  Trigger keywords: code simplifier, 代码简化, 代码优化, 简化代码, 重构,
  减少嵌套, 消除重复, 提取公共函数, simplify code, 精简代码, 代码瘦身,
  优化可读性, 写完代码后优化, AI代码优化。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
metadata:
  category: development
  source: https://github.com/anthropic/claude-plugin-directory
  install: /plugin install code-simplifier@claude-plugin-directory
  version: "1.0.0"
  license: MIT
---

# Code Simplifier — AI 代码自动二次优化

> AI 生成代码有一个通病：啰嗦。变量名重复声明、if 嵌套四五层、明明三行能写完的逻辑硬拆成三十行。这些代码能跑，但过两个月再看，你根本不想维护。

Code Simplifier 在代码生成之后自动做二次优化。

## 核心能力

### 不改行为，只优化结构

功能逻辑原封不动，只优化：

- **消除重复代码**：合并相同的逻辑块，提取重复模式
- **减少嵌套层级**：if 嵌套从 4-5 层降到 1-2 层
- **简化复杂逻辑**：三行能写完的不用三十行
- **提取公共函数**：识别可复用的代码块，提取为独立函数
- **统一命名风格**：变量命名更一致、更语义化

### 实测效果

- 代码行数通常减少 **30-40%**
- 嵌套深度从 4-5 层降到 1-2 层
- 变量命名更一致

## 安装

```
/plugin install code-simplifier@claude-plugin-directory
```

## 使用方式

```bash
# 简化当前改动
/simplify

# 在 Claude Code 里对 AI 说
"简化刚才生成的代码"
"帮我优化这个模块的可读性"
```

## 推荐流水线

```
① 写代码 ──→ ② Code Simplifier 优化 ──→ ③ Code Review 审查 ──→ ④ 人工 Review
```

**为什么是这个顺序？**
- 先简化再审查——简化后的代码更容易发现真正的问题
- Code Review 能检查简化过程是否引入了意外行为
- 最后人工把关——AI 写 + AI 审 + 人审 = 三重保障
