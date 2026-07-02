---
name: ralph-loop
description: >
  Ralph Loop — 防止 AI 提前结束未完成任务的循环机制。本质是一个 bash 循环脚本，
  每次迭代启动一个全新的 AI 实例（干净上下文），从 PRD 里挑出未完成的任务、
  实现它、跑测试、通过则提交并标记完成，然后把关键信息写进 progress.txt。
  持续循环直到所有任务完成。每轮全新上下文，避免传统对话中上下文臃肿导致的质量下降。
  Trigger keywords: ralph loop, 循环开发, 自动迭代, 持续开发, 上下文隔离,
  批量任务, PRD驱动开发, 自动化开发循环, 迭代开发, ralph, progress.txt,
  自动完成任务, 持续集成开发。
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
metadata:
  category: development
  source: https://github.com/snarktank/ralph.git
  install: git clone https://github.com/snarktank/ralph.git
  version: "1.0.0"
  license: MIT
---

# Ralph Loop — 防止 AI 提前结束任务的循环机制

> Ralph Loop 干的事非常单一：如果 AI 想提前结束还没完成的任务，它会拦截并退回给 AI 重新处理，直到任务真正开发完成。

## 核心原理

```
┌─────────────────────────────────────────────┐
│                 Ralph Loop                    │
│                                               │
│  ① 读取 PRD → 挑出未完成的任务                 │
│        ↓                                      │
│  ② 启动全新 AI 实例（干净上下文）              │
│        ↓                                      │
│  ③ 实现任务 → 跑测试 → 通过 → 提交             │
│        ↓                                      │
│  ④ 标记完成 → 关键信息写入 progress.txt        │
│        ↓                                      │
│  ⑤ 检查是否所有任务完成？                      │
│     ├─ 否 → 回到 ①                             │
│     └─ 是 → 结束                               │
└─────────────────────────────────────────────┘
```

## 为什么有效

### 上下文隔离是关键

传统对话中 AI 的上下文会越来越臃肿，输出质量断崖式下降。Ralph 每轮都是全新上下文，没有历史包袱，只看：
- 当前任务
- `progress.txt` 里的关键信息

这种"干净启动"保证了每一轮的质量一致性。

## 安装

```bash
git clone https://github.com/snarktank/ralph.git
cp -r ralph/scripts ./
./scripts/ralph/ralph.sh
```

## 前置条件（必须！）

1. **PRD story 足够小**：每个 story 必须小到一个上下文窗口能完成。太大了 AI 会跑偏。
2. **项目必须配 typecheck 和测试**：没有反馈回路的话，AI 写出来的东西会越跑越歪。
3. **每个 story 有明确的验收标准**：AI 需要知道自己做完了没有。

## 使用建议

- **适合大项目**：几十个 story 的自动化迭代
- **不适合小需求**：配置成本高于直接让 Claude Code 做
- **CI 集成**：可以放入 CI 流水线，让 AI 在无人值守下持续开发

## 风险提示

- 没有人工审查环节，代码质量依赖测试覆盖率和 typecheck
- 如果 PRD 写得不清楚，AI 可能越做越偏
- 建议配合 Code Review 和 Code Simplifier 使用，在提交前加质量门
