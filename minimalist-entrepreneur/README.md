# 极简创业 AI 商业顾问

> 基于 Sahil Lavingia《小而美》的 10 个 Claude Code Skill · 一人公司全链路

## 这是什么？

把你读过的创业书变成能直接对话的 AI 商业顾问。Sahil Lavingia 把《The Minimalist Entrepreneur》提炼成 10 个可交互的 Claude Code Skill，覆盖从找方向到做决策的完整链路。

## 快速开始

### 1. 安装

```bash
# 在 Claude Code 中运行：
/plugin marketplace add slavingia/skills
/plugin install minimalist-entrepreneur
```

重启 Claude Code 对话即可。

### 2. 使用

直接用自然语言对话：

- "帮我验证一个创业想法"
- "我该不该做这个功能？"
- "我的产品该怎么定价？"
- "怎么找到第一批客户？"

Claude Code 会自动匹配对应的 Skill，像商业顾问一样一步步追问你。

## 10 个 Skill 速览

| # | 命令 | 一句话核心 |
|---|------|-----------|
| 1 | `/find-community` | 你不需要找社群，你已经属于好几个了——关键是里面的人在反复抱怨什么 |
| 2 | `/validate-idea` | 别问"酷不酷"，问"有人付钱吗" |
| 3 | `/mvp` | 只做一件事，能在周末交付的才做 |
| 4 | `/processize` | 先手动跑 10 次，把步骤写在纸上，再写代码 |
| 5 | `/first-customers` | 100 个客户之前别搞发布会，从亲友一圈圈往外卖 |
| 6 | `/pricing` | 从第一天就收费，免费和 1 块钱之间是质变不是量变 |
| 7 | `/marketing-plan` | 先花时间再花钱，博客免费社交免费，跑通了再投广告 |
| 8 | `/grow-sustainably` | 盈利给你无限跑道，别人可能超过你但 10 年后你还在 |
| 9 | `/company-values` | 价值观用故事写不是口号，Nordstrom 接受轮胎退货才是价值观 |
| 10 | `/minimalist-review` | 八个问题筛完，答案通常就清楚了——最通用的一个 |

## 实操案例：两个 Skill 接力验证想法

想法："做一个共享旅游相册小程序"

### 第一轮：`/validate-idea`

它不问"这个想法酷不酷"，而是追问：
- "谁具体有这个问题？10 个人说得出来吗？"
- "他们现在怎么解决的？有多痛？"
- **"你自己愿意付钱吗？"**

当你说"我自己不太愿意付，想靠广告"——它立刻指出：**你自己都不愿意付钱，目标用户大概率也不会。**

### 第二轮：`/minimalist-review`

8 条极简原则同时过筛：
- "小程序能在一个周末交付吗？"→ 不能
- "有人付过钱吗？"→ 没有
- "是你的朋友在抱怨，还是你自己觉得应该有？"→ 自己觉得的

**8 维筛完，6 个亮红灯。结论：别做小程序，先手动建一个共享相册，跑 3 次看看朋友们真的会主动上传吗。**

### 看到了什么？

只用 `/validate-idea`，你知道"想法还没验证"。加了 `/minimalist-review` 之后，结论更清晰：不是"验证不够"，是从一开始就不该以"做小程序"的方式推进。

**这就是链路的意义：接力用，你看到的不是某个点的问题，而是整条路径的问题。**

## 不止创业

哪怕不创业，至少有 5 个 Skill 对你有用：

| Skill | 日常用途 |
|-------|---------|
| `/find-community` | 找到你真正属于的圈子 |
| `/validate-idea` | 判断"做这个值不值" |
| `/processize` | 把想法变成"今天就能动手做的事" |
| `/pricing` | 搞清楚"我该收多少钱" |
| `/minimalist-review` | 过筛任何"我到底该不该做"的纠结 |

## 推荐阅读

- 《The Minimalist Entrepreneur》by Sahil Lavingia（中文版《小而美》）
- [slavingia/skills](https://github.com/slavingia/skills) — 原始仓库

## 许可

MIT License · Copyright (c) Sahil Lavingia
