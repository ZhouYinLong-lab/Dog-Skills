---
name: thinking-toolkit
description: >
  思考决策工具箱元技能——整合 superforecaster（校准预测）、decision-matrix（决策矩阵）、
  bayesian-reasoning（贝叶斯推理）、systems-thinking（系统思维）、scout-mindset-bias-check
  （认知偏见审查）、doctor-strange（平行宇宙沙盘推演）六大思考框架。
  覆盖预测→决策→推理→系统分析→偏见审查→情景模拟的完整深度思考链路。
  Trigger keywords: 思考工具, 决策工具, 深度思考, 预测, 决策矩阵, 贝叶斯推理,
  系统思维, 偏见审查, 沙盘推演, thinking toolkit, superforecaster, decision matrix,
  bayesian reasoning, systems thinking, scout mindset, doctor strange,
  怎么做决定, 帮我分析利弊, 预测一下, 模拟未来, 认知偏见, 理性决策。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - TaskCreate
metadata:
  category: thinking
  source: composite (lyndonkl/claude + Agentara)
  version: "1.0.0"
  license: MIT
---

# Thinking Toolkit — 思考决策工具箱

> 六个专业思考框架整合为一个元技能，覆盖从预测未来到做出决策、从系统分析到偏见审查的完整深度思考链路。

## 子技能矩阵

```
┌──────────────────────────────────────────────────────────────────┐
│                      Thinking Toolkit                             │
│                                                                   │
│  ① superforecaster    ── 五阶段校准预测（不瞎猜，带置信区间）       │
│  ② decision-matrix    ── 多维度决策矩阵（量化权衡）                │
│  ③ bayesian-reasoning ── 贝叶斯推理（基于新证据更新信念）          │
│  ④ systems-thinking   ── 系统思维（反馈回路·杠杆点·涌现行为）      │
│  ⑤ scout-mindset      ── 认知偏见审查（求真相还是捍卫观点？）      │
│  ⑥ doctor-strange     ── 平行宇宙沙盘推演（多Agent模拟不同未来）   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 子技能详解

### ① superforecaster — 校准预测

**做什么**：五阶段结构化预测管线，不瞎猜，输出带置信区间的预测结果。

**五阶段**：
1. 问题拆解 — 把模糊问题转化为可验证的具体命题
2. 基准率估计 — 找类似历史事件的基准概率
3. 证据更新 — 收集当前证据，贝叶斯修正
4. 置信区间 — 给出 25%/50%/75%/90% 分位数
5. 校准复盘 — 记录预测结果，事后对比校准

**触发场景**：
- "预测这个产品三个月后的 DAU"
- "这个行业未来一年的趋势是什么？给出概率估计"
- "帮我做一次校准预测"

---

### ② decision-matrix — 决策矩阵

**做什么**：多维度量化权衡，拒绝拍脑袋决策。

**流程**：
1. 列出所有选项
2. 定义评估维度（成本、收益、风险、时间……）
3. 设定各维度权重
4. 逐项打分
5. 输出加权总分 + 敏感度分析（哪些维度改变会翻转结果）

**触发场景**：
- "三个方案各有优劣，帮我做决策矩阵"
- "要不要跳槽？帮我量化分析"
- "买房 A vs B vs C，多维度比较"

---

### ③ bayesian-reasoning — 贝叶斯推理

**做什么**：基于新证据持续更新信念，区分先验概率和后验概率。

**核心概念**：
- 先验概率 (Prior)：看到新证据前的初始信念
- 似然度 (Likelihood)：在新证据下观察到的可能性
- 后验概率 (Posterior)：更新后的信念

**触发场景**：
- "有新数据了，更新我们对这个假设的置信度"
- "产品数据出来了，之前的判断要不要修正？"
- "用贝叶斯思维分析这个诊断结果"

---

### ④ systems-thinking — 系统思维

**做什么**：跳出线性因果，识别反馈回路、杠杆点和涌现行为。

**分析框架**：
- 因果回路图 (Causal Loop Diagram)
- 存量-流量模型 (Stock-Flow)
- 杠杆点识别 (Leverage Points, 参考 Donella Meadows)
- 延迟效应与 unintended consequences

**触发场景**：
- "为什么公司每次改革都推不动？做系统分析"
- "这个产品指标下降的根本原因是什么？画因果回路图"
- "找到这个系统里最能撬动全局的杠杆点"

---

### ⑤ scout-mindset — 认知偏见审查

**做什么**：区分"士兵心态"（捍卫已有观点）和"侦察兵心态"（寻求真相），审查当前思考中的认知偏见。

**审查清单**：
- 确认偏误 (Confirmation Bias)
- 锚定效应 (Anchoring)
- 可得性启发 (Availability Heuristic)
- 沉没成本谬误 (Sunk Cost Fallacy)
- 过度自信 (Overconfidence)
- 框架效应 (Framing Effect)

**触发场景**：
- "我对这个方案很有信心，帮我检查一下有没有认知偏见"
- "这个判断是客观的还是我想听到的？"
- "用侦察兵心态审视我的观点"

---

### ⑥ doctor-strange — 平行宇宙沙盘推演

**做什么**：启动多个并行子 Agent，每个模拟一个不同的未来走向，对比分析各条路径的终局。

**推演模式**：
- **基线推演**：按当前趋势自然演化
- **乐观推演**：关键变量朝有利方向发展
- **悲观推演**：关键变量朝不利方向发展
- **黑天鹅推演**：极端低概率事件发生

**触发场景**：
- "模拟未来五年 AI 行业的三种走向"
- "如果我们做了 X 决策，三年后最坏和最好的结果是什么？"
- "平行宇宙推演：不融资 vs A轮 vs 直接盈利"

---

## 安装

所有子技能来自 **lyndonkl/claude**（241 skills + 62 agents）和 **Agentara**：

```bash
# lyndonkl 思考决策套装
git clone https://github.com/lyndonkl/claude.git /tmp/lyndonkl-claude
cp -r /tmp/lyndonkl-claude/skills/thinking/* ~/.claude/skills/

# Agentara doctor-strange
npx skills add MagicCube/agentara --skill doctor-strange -y -g
```

## 使用指南

| 你想要... | 对 Claude Code 说 |
|-----------|-------------------|
| 校准预测 | "帮我预测 XXX，用 superforecaster 方法" |
| 量化决策 | "对这几个选项做决策矩阵分析" |
| 更新信念 | "拿到新数据了，贝叶斯更新一下之前的判断" |
| 系统分析 | "画这个问题的因果回路图，找杠杆点" |
| 偏见检查 | "审查我刚才的判断有没有认知偏见" |
| 沙盘推演 | "帮我模拟 XXX 的三种未来走向" |

## 思考流程推荐

```
面对重要决策时：

doctor-strange（模拟不同走向）
       │
       ▼
decision-matrix（量化权衡各选项）
       │
       ▼
bayesian-reasoning（纳入最新证据更新）
       │
       ▼
scout-mindset（检查决策过程中的偏见）
       │
       ▼
superforecaster（对选定方案做校准预测）
       │
       ▼
systems-thinking（评估决策的连锁反应）
```
