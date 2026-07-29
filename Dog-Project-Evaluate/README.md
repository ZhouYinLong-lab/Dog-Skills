# Evaluate Research Project

三通道独立评估研究项目：课程作业完成度 → 论文投稿水平 → 开源项目成熟度。

## 与 repo-evaluator 的区别

| | evaluate-research-project | repo-evaluator |
| --- | --- | --- |
| 评估范围 | 课程作业 + 论文 + OSS 三通道 | 纯 GitHub 仓库六维评估 |
| 论文投稿判定 | ✅ 含 venue tier、接收概率、拒稿点分析 | ❌ |
| 课程评分 | ✅ 含 rubric 映射、完成度检查 | ❌ |
| 对抗性审稿 | ✅ 模拟严格审稿人找决定性拒稿点 | ❌ |
| 开源成熟度 | ✅ 六维评分（与 repo-evaluator 共用维度） | ✅ 六维评分 |
| 适用场景 | 学生项目、研究原型、毕业论文、预投稿自检 | 选型依赖评估、开源项目审计 |

两者在 OSS 评分维度上互补：本技能侧重"这个研究仓库能不能当开源项目用"，repo-evaluator 侧重"这个开源项目值不值得依赖"。

## 目录结构

```
evaluate-research-project/
├── SKILL.md                      # 技能定义与完整工作流
├── README.md                     # 本文件
├── references/
│   └── rubrics.md                # 三通道评分量规（证据标准、评分维度、校准区间）
└── scripts/
    └── collect_evidence.py       # 只读证据采集脚本（Git 元数据、文件清单、项目结构）
```

## 使用方式

触发关键词示例：
- "帮我评估这个项目什么水平"
- "这个大作业能拿多少分"
- "这个仓库能投什么会议"
- "评估一下这个开源项目的成熟度"
- "evaluate this course project / research prototype"
