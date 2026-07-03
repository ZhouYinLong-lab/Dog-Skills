---
name: code-review
description: >
  代码审查元技能——整合两种互补的审查模式：(1) standard 五维审查（安全性·性能·
  可维护性·规范·边界情况），5 个 Agent 并行+置信度过滤；(2) adversarial 对抗式审查
  （恶意用户视角，"我要搞崩你的系统"），逻辑漏洞·隐藏 Bug·思维盲点。
  两种模式覆盖从工程质量把关到破坏性测试的完整审查链路。
  Trigger keywords: code review, 代码审查, 多Agent审查, 并行审查, 代码质量检查,
  PR review, 安全审查, 性能审查, 边界检查, review my code, 帮我审查代码,
  adversarial review, 对抗式审查, 对抗性审查, red team, 找BUG, 挑毛病,
  攻击测试, 渗透测试思维, 恶意用户视角, 代码审计, 提交前检查, pre-commit review.
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
  source: composite (adversarial-review + code-review-skill merged)
  version: "2.0.0"
  license: MIT
---

# Code Review — 双模式代码审查元技能

> 两种互补的审查模式：standard 把关工程质量，adversarial 模拟攻击者视角。覆盖从常规 PR 到安全审计的完整审查链路。

## 两种模式

```
┌──────────────────────────────────────────────────────────────┐
│                    Code Review                                 │
│                                                               │
│  /review standard     ── 五维工程质量审查                      │
│  /review adversarial  ── 恶意用户视角破坏性测试                │
└──────────────────────────────────────────────────────────────┘
```

---

## Standard 模式 — 五维工程质量审查

5 个 Agent 并行审查 + 置信度过滤：

```
代码 → 安全Agent · 性能Agent · 可维护Agent · 规范Agent · 边界Agent
         │
         ▼
    置信度过滤（自动剔除假阳性）
         │
         ▼
    Critical → High → Medium → Low 分级报告
```

**何时用**：日常 PR、提交前检查、重构后验证。

---

## Adversarial 模式 — 对抗式审查

AI 换一个身份，从"我要用各种奇怪的数据搞崩你的系统"出发：

```
恶意用户视角 → 多Agent并发扫描
    │
    ├── 逻辑漏洞："这个判断条件有没有反例？"
    ├── 安全风险："注入/XSS/权限绕过？"
    ├── 边界条件："传null/负数/超大值会怎样？"
    ├── 隐藏Bug："并发/竞态/死锁？"
    └── 思维盲点："你没想到什么？"
```

**何时用**：安全审计、核心模块上线前、被攻击后的排查。

---

## 使用方式

| 你说 | 模式 |
|------|------|
| "帮我审查代码" / `/code-review` | Standard（默认） |
| "审查 PR 的代码质量" | Standard |
| "帮我做对抗式审查" / "以攻击者视角审查" | Adversarial |
| "全面审计——先 standard 再 adversarial" | 双模式串联 |

---

## 推荐流水线

```
Code Simplifier（先优化结构）
       │
       ▼
Code Review standard（工程质量把关）
       │
       ▼
Code Review adversarial（安全+边界兜底）
       │
       ▼
人工 Review
```
