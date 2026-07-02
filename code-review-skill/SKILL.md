---
name: code-review-skill
description: >
  多 Agent 并行代码审查——5 个审查 Agent 同时从安全性、性能、可维护性、规范符合度、
  边界情况五个维度审查代码，合并成按严重程度分级的报告。内置置信度过滤机制，
  自动过滤假阳性，只报告高置信度问题。适合作为人工审查前的第一道自动化防线。
  Trigger keywords: code review, 代码审查, 多Agent审查, 并行审查, 代码质量检查,
  PR review, 安全审查, 性能审查, 边界检查, review my code, 帮我审查代码,
  查一下代码质量, 提交前检查, pre-commit review。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - TaskCreate
  - WebFetch
metadata:
  category: development
  source: https://github.com/anthropic/claude-plugin-directory
  install: /plugin install code-review@claude-plugin-directory
  version: "1.0.0"
  license: MIT
---

# Code Review — 多 Agent 并行代码审查

> 写完代码，5 个并行 Agent 立刻从 5 个维度同时审查。Critical 和 High 必须先修，Medium 和 Low 可以后续处理。

## 核心流程

```
                    ┌─ Agent 1: 安全性 ──┐
                    ├─ Agent 2: 性能   ──┤
你的代码 ──▶ 分发 ──├─ Agent 3: 可维护性──├──▶ 合并报告 ──▶ 按严重程度分级
                    ├─ Agent 4: 规范   ──┤        │
                    └─ Agent 5: 边界情况──┘   Critical → High → Medium → Low
```

## 关键特性

### 置信度过滤 ⭐ 核心差异化
审查 Agent 发现潜在问题后会自己评估"这个发现靠谱吗？"，置信度低的不会出现在最终报告里。以前没这个机制时，AI 审查经常报一堆假阳性，审查者都懒得看了。

### 五维并行审查
- **安全性**：SQL 注入、XSS、认证绕过、敏感信息泄露
- **性能**：N+1 查询、不必要的循环、内存泄漏
- **可维护性**：代码重复、命名混乱、过度嵌套
- **规范符合度**：是否遵循项目约定和最佳实践
- **边界情况**：null/undefined、空数组、超时、并发

## 安装

```
/plugin install code-review@claude-plugin-directory
```

## 使用方式

```bash
# 审查当前 diff
/code-review

# 指定审查强度
/code-review --effort high

# 发布审查结果到 PR
/code-review --comment
```

## 使用建议

**不能代替人工审查**。AI 写的东西，人工审查是必须的。但作为**第一道防线**非常管用——能在同事审查之前，先过滤掉大部分低级错误。

## 最佳搭配

推荐的代码质量流水线：

```
写代码 → Code Simplifier 优化 → Code Review 审查 → 人工 Review
```

三个步骤串起来，代码质量比单靠人工把关高不少。
