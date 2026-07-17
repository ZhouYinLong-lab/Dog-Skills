---
name: dog-ppt
description: >
  AI 做 PPT 总控路由元技能(Dog-PPT)。不做 PPT，帮你在 8+ 个 PPT 技能中选对工具。
  核心逻辑：先判断交付物（可编辑PPTX？视觉卡？网页演示？演讲辅助？）→
  再判断内容类型（论文？网页？PDF？视频？轻内容？）→ 最后匹配合适的技能。
  覆盖 Dog-Skills 已有（ppt-master/huashu-slides/humanize-ppt/huashu-design/
  baoyu-skills/brand-workshop/presentation-design）和外部推荐技能。
  Trigger keywords: 做PPT, 做幻灯片, 演示文稿, 怎么做PPT, AI做PPT,
  选哪个PPT工具, PPT技能, 用什么做PPT, slides, presentation,
  帮我做PPT, 做deck, pitch deck, 汇报PPT, 论文PPT, 学术演示,
  上台演示, 培训课件, 产品发布PPT, 用什么工具做PPT最好.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
  - AskUserQuestion
metadata:
  category: design
  source: 硬核词元 公众号文章 + Dog-Skills 生态整合
  version: "1.0.0"
  license: MIT
---

# Dog-PPT — AI 做 PPT 总控路由

> 不做 PPT，帮你在 8+ 个技能中选对工具。
> 核心信条：**先问要交付什么，再问用什么工具。**

## 为什么需要这个元技能

很多人用 AI 做 PPT 犯的错误：

```
❌ "哪个工具最强？" → 每个都试一遍 → 每个都差一点
✅ "我要交付什么？" → 匹配对的工具 → 一次到位
```

如果你要交给客户继续修改 → 你需要**原生可编辑 PPTX**。
如果你要发小红书或公众号 → 你需要**视觉包装能力**。
如果你面对论文/网页/PDF/视频 → 你缺的不是排版，是**信息结构化**。
如果你要上台讲 → 你需要的是**演讲辅助**，不是"多少页"。

---

## 三步选型法

```
Step 1: 判断交付物
       │
       ├─ 可编辑 .pptx（要发给别人改）→ ppt-master / humanize-ppt
       ├─ 知识图卡/封面/视觉资产 → huashu-design / huashu-slides
       ├─ 网页幻灯片/在线演示 → dog-frontier(HTML) 或 frontend-slides
       └─ 上台演讲（计时器+逐字稿）→ html-ppt-skill
       │
Step 2: 判断内容类型
       │
       ├─ 论文/学术 → paper-deck
       ├─ 网页/PDF/视频/杂乱资料 → qiaomu（先整理再输出）
       ├─ 正式商务/客户交付 → ppt-master
       ├─ 轻内容/卡通/短视频配图 → baoyu-skills
       └─ 品牌/产品发布 → guizang-ppt-skill / brand-workshop
       │
Step 3: 匹配技能 → 生成
```

---

## 技能选型地图

### Dog-Skills 已内置

| 技能 | 最擅长 | 输出 | 适用场景 |
|------|--------|------|---------|
| **ppt-master** | 正式交付 | 原生可编辑 PPTX | 发给老板/客户/团队继续改 |
| **huashu-slides** | 端到端幻灯片 | PPTX + AI 插画 | 从内容到成品演示文稿 |
| **humanize-ppt** | PPT 体检+质检 | PPTX | 已有 deck 需要优化渲染/排版/演讲备注 |
| **huashu-design** | 视觉包装 | 视觉 Demo + AI 提示词 | 公众号封面/知识卡/图文资产/演示原型 |
| **baoyu-skills** | 轻内容幻灯片 | 图片幻灯片 | 卡通 NPC/短视频配图/轻量图解 |
| **dog-frontier** | 网页演示 | HTML/CSS/JS | 在线演示/动画页面/交互式 slides |
| **brand-workshop** | 品牌定调 | Logo + 标语 + DESIGN.md | 先定品牌再出 PPT 统一风格 |
| **presentation-design** | 视觉方案板 | 设计板预览 | 客户端 Pitch/投资人演示方案比选 |

### Design Buddy 补充

| 技能 | 最擅长 | 输出 | 适用场景 |
|------|--------|------|---------|
| **space-slide-deck** | 品牌自动匹配 | PNG + PPTX/PDF | 60+ 品牌设计系统智能匹配，Markdown 一键转 deck |

### 外部推荐技能

| 技能 | 最擅长 | 输出 | 适用场景 |
|------|--------|------|---------|
| **paper-deck** | 论文→PPT | PPTX | 读懂论文→拆框架→提炼图表→组会/论文解读 |
| **guizang-ppt-skill** | 视觉冲击 | PPTX | 瑞士风/杂志感/大留白/产品发布/高级汇报 |
| **html-ppt-skill** | 演讲辅助 | HTML | 计时器/逐字稿/备注/彩排，培训/课程/路演 |
| **qiaomu** | 上游整理 | 知识库→PPT/脑图/讲稿 | 网页/PDF/视频/文章杂乱时先结构化 |
| **frontend-slides** | 网页幻灯片 | HTML/CSS | 有前端基础，要动画和在线编辑自由度 |

---

## 实用选择规则

```
要交付可编辑文件   →  ppt-master
要做视觉包装       →  huashu-design 或 guizang-ppt-skill
要讲论文和资料     →  先用 paper-deck 或 qiaomu
要上台演示         →  别忘了 html-ppt-skill
要轻内容亲和       →  baoyu-skills
要先定品牌调性     →  brand-workshop → 再选 PPT 技能
```

---

## 常见场景路由

| 用户说什么 | 路由方案 |
|-----------|---------|
| "帮我把这份资料做成PPT给老板汇报" | **ppt-master** — 需要可编辑 PPTX |
| "帮我把这个PDF做成PPT" | **qiaomu** 先结构化 → **ppt-master** 生成 |
| "我要在学术会议上讲论文" | **paper-deck** 拆论文 → **html-ppt-skill** 辅助演讲 |
| "做一个产品发布会的演示" | **guizang-ppt-skill** 视觉冲击 或 **brand-workshop** + **huashu-slides** |
| "做小红书风格的知识卡片" | **huashu-design** — 信息图/知识卡 |
| "把这篇文章做成 PPT 发公众号" | **huashu-slides** 端到端成品 |
| "我有个 deck 需要优化一下" | **humanize-ppt** — 体检+质检+渲染优化 |
| "要做一个在线培训课件" | **html-ppt-skill** 演讲辅助 + **dog-frontier** 网页演示 |
| "轻量的卡通风格教程 PPT" | **baoyu-skills** — 卡通 NPC 风格 |
| "先给我做几套视觉方案选一下" | **presentation-design** — 6 页方案板含亮暗双模式 |
| "不确定要什么风格" | **dog-ppt** 先做需求勘探 → 推荐 2-3 个方向 |

---

## 关键洞察

AI 做 PPT 不是找一个万能工具，是把三件事拆开：

```
内容整理      →  视觉表达      →  演示交付
(qiaomu)       (huashu-design   (html-ppt-skill
 paper-deck)    guizang-ppt      ppt-master
                brand-workshop)   huashu-slides)
```

拆开之后，每一步都更稳，结果也更像一个真正可用的作品。

---

## 安装方式

```bash
cp -r dog-ppt/ ~/.claude/skills/dog-ppt/
```

Dog-Skills 内置的 PPT 相关技能（ppt-master/huashu-slides/humanize-ppt/huashu-design/baoyu-skills/brand-workshop/presentation-design/dog-frontier）各自独立安装。外部推荐技能通过各自渠道安装。

---

## 触发示例

- "帮我做 PPT，但我不知道用哪个技能"
- "我要给客户做一个产品介绍的演示文稿，用哪个工具？"
- "怎么做论文答辩 PPT？"
- "我要上台讲一个培训，需要计时器和备注"
- "把这个文档做成 PPT，但是要能继续编辑的"
- "做一份适合发小红书的 PPT"
- "AI 做 PPT 到底用什么最好？"
- "帮我选一个做 PPT 的 skill"
