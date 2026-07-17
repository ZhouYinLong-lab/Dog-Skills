# Dog-Skills PPT 技能全景

> 11 个 PPT 相关技能的分工地图。先判断你要什么，再选工具——不要"哪个最强"，要"哪个最对"。

---

## 三轴定位图

```
                        制作方式 →
                 AI自由生成          模板/规则约束         工程化流水线
           ┌──────────────────┬──────────────────┬──────────────────┐
  可编辑   │                  │                  │                  │
  PPTX     │   ppt-master     │                  │   dashi-ppt ⭐   │
  交付     │   (自由发挥PPTX)  │                  │   (goal.json    │
           │                  │                  │    三道校验      │
           │                  │                  │    浏览器可编辑) │
           ├──────────────────┼──────────────────┼──────────────────┤
  HTML     │   dog-frontier   │   huashu-slides  │                  │
  网页     │   (网页幻灯片)    │   (18风格+AI插图) │                  │
  演示     │                  │   humanize-ppt   │                  │
           │                  │   (PPT体检质检)   │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
  视觉     │   huashu-design  │   space-slide-   │                  │
  包装     │   (封面/知识卡)   │   deck           │                  │
  图片     │   baoyu-skills   │   (60+品牌匹配)   │                  │
           │   (轻内容/卡通)   │                  │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
  方案     │   presentation-  │                  │                  │
  比选     │   design         │                  │                  │
           │   (6页方案板)     │                  │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
  品牌     │   brand-workshop │                  │                  │
  定调     │   (Logo+标语     │                  │                  │
           │    +DESIGN.md)   │                  │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
  演讲     │                  │   html-ppt-skill*│                  │
  辅助     │                  │   (计时器/逐字稿) │                  │
           ├──────────────────┼──────────────────┼──────────────────┤
  上游     │                  │                  │                  │
  整理     │                  │   qiaomu*        │                  │
           │                  │   paper-deck*    │                  │
           └──────────────────┴──────────────────┴──────────────────┘

  * 外部技能（不在 Dog-Skills 仓库内，dog-ppt 路由表引用）
  内置技能均位于仓库顶层目录，dashi-ppt 为新增纳管技能。
```

---

## 按使用场景速查

| 你要... | 用哪个 | 为什么 |
|---------|--------|--------|
| 发给客户/老板继续改 | **ppt-master** | 原生可编辑 PPTX，自由度高 |
| 浏览器里边看边调，满意再导出 PPTX | **dashi-ppt** | 唯一支持浏览器编辑+自动保存 |
| 要稳定输出不怕翻车（12主题选一套） | **dashi-ppt** | 三道校验 + layout 契约，"锁模板填文案" |
| 从内容到成品一键搞定 | **huashu-slides** | 端到端，18 视觉风格 + AI 插画 |
| 手里有 deck 要优化排版/备注 | **humanize-ppt** | PPT 体检+质检+渲染优化 |
| 做知识卡/封面/图文素材 | **huashu-design** | 视觉包装，非整份 PPT |
| 轻量卡通风教程/图片幻灯片 | **baoyu-skills** | 亲和力，非严肃商务 |
| 品牌定调（先有风格再出 PPT） | **brand-workshop** | Logo+标语+DESIGN.md 令牌 |
| 先看几套方案再定方向 | **presentation-design** | 6 页方案板，亮暗双模式 |
| 网页动画演示/交互式 slides | **dog-frontier** | HTML+CSS+JS 自由度高 |
| 论文→学术汇报 | **paper-deck** * | 读懂论文→拆框架→提炼图表 |
| 产品发布会/高级汇报气场 | **guizang-ppt** * | 瑞士风/杂志感/大留白 |
| 培训/课程（要计时器+逐字稿） | **html-ppt-skill** * | 演讲辅助，非"多少页" |
| 内容杂乱先整理再出 PPT | **qiaomu** * | 上游结构化：网页/PDF/视频→知识库→PPT |
| Markdown 一键转品牌匹配 deck | **space-slide-deck** | 60+ 品牌 DESIGN.md 自动匹配 |
| 不知道选哪个 | **dog-ppt** | 元技能路由器，三步选型法 |

---

## 每个技能的结构与特征

### ppt-master
```
结构: SKILL.md（Prompt驱动）
输入: 自然语言描述内容
输出: 原生可编辑 .pptx
特征: 自由度最高，AI 决定一切——排版/配色/字体/页数。
      适合"我要一个关于XX的PPT"，不适合"我要精确控制每页布局"。
弱点: 输出不可预测，可能需要多轮调整。
```

### dashi-ppt ⭐
```
结构: SKILL.md + project/（React渲染引擎 + 12主题源码 + 10款woff2字体
      + 布局查询系统 + 属性校验器 + PPTX/PDF导出 + 浏览器预览服务
      + scripts/校验/渲染/导出脚本）
输入: goal.json（title + goal + audience + themePack + slides[layout+props]）
输出: index.html（可浏览器编辑）→ PPTX/PDF
特征: 最工程化。"锁模板填文案"——AI只填content slot，不改视觉结构。
      12 套工业化主题各有契约（copyKeys/copyBudgets/mediaSlots），
      三道校验（goal-spec → swiss → goal-copy）保证输出质量。
      浏览器侧边栏可改文案/换图/调属性，自动保存。
弱点: 受12主题限制，不能自由发挥视觉。需要 Node.js 20+ 运行渲染脚本。
```

### huashu-slides
```
结构: SKILL.md（Prompt驱动 + 18风格参考 + AI插图生成）
输入: 自然语言 / 文档 / Markdown
输出: .pptx（含 AI 生成的插图）
特征: 端到端成品，从内容理解到视觉风格到插图到PPTX一条龙。
      18 种设计风格可选，适合需要完整视觉方案的场景。
弱点: 不如 ppt-master 可编辑，不如 dashi-ppt 可控。
```

### humanize-ppt
```
结构: SKILL.md（Prompt驱动 + 演讲体检清单）
输入: 已有 PPT/PDF/文档
输出: 优化后 .pptx + 演讲备注 + 体检报告
特征: 唯一做"PPT 体检"的技能。渲染质检、排版优化、演讲备注补全。
      不负责从零生成，负责把已有的变得更好。
弱点: 不创建新内容，只优化已有内容。
```

### huashu-design
```
结构: SKILL.md（Prompt驱动 + 20种设计哲学库 + 5大流派）
输入: 品牌/产品描述
输出: 视觉 Demo + AI 提示词 DNA
特征: 不是做 PPT，是做"视觉方向"。先确定设计哲学，再生成视觉参考。
      适合还不知道要什么风格的情况。
弱点: 输出是视觉方案不是成品PPT，需要下游技能承接。
```

### baoyu-skills
```
结构: SKILL.md（22 个独立子技能集合 + 11种生图后端）
输入: 自然语言
输出: 图片幻灯片 / 卡通 NPC / 轻量图解 / 短视频配图
特征: 轻量、亲和、非正式。不是商务PPT工具，是内容创作者的配图工坊。
弱点: 不适合正式商务场景。
```

### brand-workshop
```
结构: SKILL.md（三阶段: Discovery→Concept→Creation）
输入: 品牌/产品描述
输出: Logo多方案 + 标语 + 品牌简介 + DESIGN.md设计令牌
特征: 品牌全案设计。PPT 的前置步骤——先定品牌调性，再用其他技能出 PPT。
弱点: 不做PPT，做品牌。需要下游技能配合。
```

### presentation-design
```
结构: SKILL.md（Prompt驱动 + 命名布局库）
输入: 演示需求描述
输出: 6页设计板（封面+4内容+封底，亮暗双模式）
特征: 方案比选工具。生成多套视觉方案让客户/投资人选，不是最终交付物。
弱点: 设计板不是可编辑PPTX。
```

### dog-frontier
```
结构: SKILL.md + references/ + assets/ + scripts/
      (21技能整合 + 5阶段流水线 + DESIGN.md集成)
输入: 前端设计需求
输出: HTML/CSS/JS 网页演示
特征: 全链路前端设计元技能。做网页幻灯片时可调用内部动画/品牌/组件子技能。
弱点: 输出HTML非PPTX，重前端，不是PPT专用工具。
```

### space-slide-deck
```
结构: SKILL.md + references/15+风格 + scripts/generate + merge导出
输入: Markdown / 长文
输出: 逐页PNG + PPTX/PDF
特征: 60+品牌 DESIGN.md 智能匹配。Design Buddy 子技能，Markdown→deck一条龙。
弱点: 依赖 Gemini/GPT-image-2 生图后端，输出PNG非原生PPTX元素。
```

---

## 四个核心差异维度

### 1. AI 能做什么 vs 人保留什么

```
AI 自由发挥多 ←──────────────────────────→ 人控制多

ppt-master    huashu-slides   dashi-ppt     humanize-ppt
(全AI做)      (AI做+选风格)   (AI填模板)    (人已有deck)
```

### 2. 输出是一次性的还是可继续编辑的

```
一次性成品 ←────────────────────────────→ 可持续编辑

space-slide-deck   huashu-slides   ppt-master   dashi-ppt
(PNG图片)          (PPTX可改)      (PPTX可改)    (浏览器编辑+导出PPTX)
```

### 3. 内容从哪来

```
从零创作 ←──────────────────────────────→ 基于已有内容

ppt-master    huashu-slides   humanize-ppt   paper-deck    qiaomu
(说需求)      (说需求/给文档)  (给deck)       (给论文)      (给任何资料)
```

### 4. 视觉质量 vs 内容质量

```
偏视觉 ←────────────────────────────────→ 偏内容

guizang-ppt   huashu-design   dashi-ppt    paper-deck    humanize-ppt
(视觉冲击)    (设计哲学)      (均衡)       (论文拆解)    (内容体检)
```

---

## 组合使用示例

```
场景1: 新品牌产品发布
  brand-workshop(定调) → dashi-ppt(出deck) → humanize-ppt(质检)
  先有Logo+配色+标语 → 选12套中匹配主题 → 优化排版和备注

场景2: 日常汇报
  ppt-master(直接生成) → 人工修改
  或者: qiaomu(整理资料) → ppt-master(出PPTX)

场景3: 论文答辩
  paper-deck(拆论文) → humanize-ppt(加备注+体检) → html-ppt-skill(上台排练)

场景4: 内容传播（小红书/公众号）
  huashu-design(视觉方向) → baoyu-skills(出图) 或 huashu-slides(成品PPTX)

场景5: 不确定要什么
  dog-ppt → 三步选型 → 匹配最佳技能
```

---

## 选型决策树

```
开始
 │
 ├─ 你已经有 deck 了？
 │   ├─ 是 → 要优化？ → humanize-ppt
 │   └─ 否 ↓
 │
 ├─ 交付物是什么格式？
 │   ├─ 可编辑 PPTX → ppt-master 或 dashi-ppt
 │   │   ├─ 要稳定可控 → dashi-ppt（12主题，锁模板填文案）
 │   │   └─ 要自由发挥 → ppt-master
 │   ├─ HTML 网页 → dog-frontier
 │   ├─ 图片/知识卡 → huashu-design 或 baoyu-skills
 │   └─ 演讲辅助 → html-ppt-skill*
 │
 ├─ 内容是什么类型？
 │   ├─ 论文/学术 → paper-deck* + humanize-ppt
 │   ├─ 产品发布 → brand-workshop + dashi-ppt
 │   ├─ 杂乱资料 → qiaomu*(先整理) + ppt-master
 │   └─ 轻内容/卡通 → baoyu-skills
 │
 └─ 不确定 → dog-ppt（元技能路由器）
```

> `*` 外部技能，需单独安装。内置技能均在 Dog-Skills 仓库顶层目录中。
