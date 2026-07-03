---
name: repo-evaluator
description: >
  GitHub 仓库评估器——多 Agent 并行评估任意开源项目的 6 类 30 项指标：
  社区健康度（贡献者/增长率/Bus Factor）、维护性（提交频率/Issue解决时间）、
  安全性（安全策略/漏洞披露）、文档质量（README/API文档/Changelog）、
  采纳度（Stars/Forks/依赖数）、代码质量（测试覆盖率/CI/CD/审查实践）。
  每项指标附源 URL 和时间戳，输出结构化评分报告。
  Trigger keywords: 评估仓库, 评估项目, 仓库评估, repo evaluation,
  开源项目评估, GitHub评估, 项目质量, 代码质量评估, 社区健康,
  选开源项目, 评估依赖, oss evaluation, project audit, repo audit,
  帮我看看这个仓库, 这个项目靠谱吗, evaluate repository。
allowed-tools:
  - Read
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - TaskCreate
metadata:
  category: development
  source: https://github.com/maxamillion/skill-oss-project-kpi-evaluation
  version: "1.0.0"
  license: MIT
---

# Repo Evaluator — GitHub 仓库评估器

> 多 Agent 并行，6 类 30 项指标，全面评估一个开源项目是否靠谱。

## 六维评估

```
┌──────────────────────────────────────────────────────────────┐
│                  Repo Evaluator                               │
│                                                               │
│  ① 社区健康 (16.67%) ─ 贡献者数量·增长率·Bus Factor·参与度    │
│  ② 维护性   (16.67%) ─ 提交频率·发布节奏·Issue/PR解决时间     │
│  ③ 安全性   (16.67%) ─ 安全策略·漏洞披露·依赖状态             │
│  ④ 文档质量 (16.67%) ─ README·API文档·指南·Changelog         │
│  ⑤ 采纳度   (16.67%) ─ Stars·Forks·下载量·依赖项目数          │
│  ⑥ 代码质量 (16.67%) ─ 测试·覆盖率·CI/CD·代码审查             │
└──────────────────────────────────────────────────────────────┘
```

## 核心特点

- **多 Agent 并行** — 6 个 Agent 同时评估 6 个维度
- **证据驱动** — 每项指标附源 URL + 时间戳，可追溯验证
- **加权评分** — 等权重综合评分，一眼判断项目健康度
- **输出报告** — 结构化 markdown 报告，含优势/风险/建议

## 安装

```bash
npx skills add maxamillion/skill-oss-project-kpi-evaluation
```

## 使用方式

| 你说 | 效果 |
|------|------|
| "评估这个仓库 https://github.com/xxx/yyy" | 6 Agent 并行评估→综合报告 |
| "帮我看看这个开源项目靠不靠谱" | 同上 |
| "对比这三个类似的开源项目" | 3 × 6 Agent 并行→对比报告 |
| "评估我们自己的仓库，看看哪里可以改进" | 自评报告+改进建议 |

## 适合场景

- 选型：几个开源库选哪个？
- 依赖审查：引入的依赖健康吗？有没有 bus factor=1 的风险？
- 自评：自己的开源项目社区健康如何？文档够不够？
- 投资尽调：这个开源项目值得投资/合作吗？
