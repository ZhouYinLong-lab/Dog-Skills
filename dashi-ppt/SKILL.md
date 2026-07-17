---
name: dashi-ppt
description: >
  浏览器可编辑 HTML 演示生成器——12 套工业化视觉主题，结构化 goal.json 驱动，
  React 渲染引擎，侧边栏在线编辑自动保存，一键导出 PPTX/PDF。
  核心哲学"锁模板填文案"：AI 只填 content slot，不改视觉结构。
  三道校验（goal-spec→swiss→goal-copy）保证交付质量。
  Trigger keywords: 做PPT, 可编辑PPT, 浏览器编辑PPT, HTML演示,
  导出PPTX, 模板PPT, 品牌演示, 12套主题, 在线编辑幻灯片,
  editable slides, browser PPT, dashi ppt, 大石PPT,
  锁模板, 填文案, 可视化编辑PPT.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
metadata:
  category: design
  source: https://github.com/chuspeeism/dashiAI-ppt-skill (MIT)
  version: "0.4.4"
  license: MIT
---

# Dashi PPT — 浏览器可编辑 HTML 演示生成器

> 基于 12 套预置视觉主题，生成可在浏览器中编辑、自动保存、一键导出 PPTX/PDF 的 HTML 演示。
> "锁模板填文案"——AI 不改视觉结构，只填内容槽位。三道校验保证输出不翻车。
> 上游来源: [chuspeeism/dashiAI-ppt-skill](https://github.com/chuspeeism/dashiAI-ppt-skill) (MIT)

## 在 PPT 技能矩阵中的位置

```
            自由发挥 ←──────────→ 工程化可控
                │                  │
          ppt-master          dashi-ppt ⭐
          (AI决定一切)         (AI填模板, 人审+改)
                                  │
                          唯一浏览器编辑+自动保存
                          唯一三道校验流水线
```

**与其他 PPT 技能的核心区别**：参见 [`ppt/README.md`](../ppt/README.md)

---

## 12 套视觉主题

| # | 主题 | 风格 | 适合 |
|---|------|------|------|
| `theme01` | 轻拟态风 | 柔和阴影+圆角 | 产品介绍 / 企业汇报 |
| `theme02` | 炫光紫绿风 | 科技感渐变 | AI/自动驾驶/机器人主题 |
| `theme03` | 深浅代码风 | 终端暗色+等宽字体 | 技术方案 / 开发者大会 |
| `theme04` | 玻璃糖果风 | 毛玻璃+渐变 | 年轻化品牌 / 消费产品 |
| `theme05` | 色谱图表风 | 数据驱动配色 | 数据报告 / 市场分析 |
| `theme06` | 深色图谱风 | 高密度信息 | 战略分析 / 投资报告 |
| `theme07` | 冷白调研风 | 干净学术感 | 调研报告 / 白皮书 |
| `theme08` | 黑金实验风 | 奢华暗色 | 高端发布 / 品牌提案 |
| `theme09` | 深蓝杂志风 | 编辑排版 | 品牌故事 / 人物访谈 |
| `theme10` | 金色指数风 | 金融数据 | 投资报告 / 金融分析 |
| `theme11` | 高能增长风 | 增长指标 | 商业计划 / 增长复盘 |
| `theme12` | 声波霓虹风 | 霓虹视觉 | 音乐娱乐 / 潮流活动 |

每套主题内含数十个页面组件（封面候选×5 + 正文页×N），通过 `layout:query` 按角色筛选。

---

## 核心工作流

```
用户需求
    │
    ▼
① 提炼目标 → title / goal / audience / themePack
    │
    ▼
② 选页 → layout:query (按角色查询候选)
    │
    ▼
③ 填槽 → 按 copyKeys 填文案 (不改视觉结构)
    │
    ▼
④ 安全校验 → props:safe + validate:goal-spec
    │
    ▼
⑤ 渲染 → goal.json → index.html (自包含离线HTML)
    │
    ▼
⑥ 质检 → validate:swiss + validate:goal-copy
    │
    ▼
⑦ 浏览器编辑 → 侧边栏改文案/换图/调属性 → 自动保存
    │
    ▼
⑧ 导出 → 一键 PPTX / PDF
```

---

## goal.json 结构

```json
{
  "title": "项目标题",
  "goal": "本次演示要达成的目标",
  "audience": "目标受众",
  "owner": "制作者",
  "randomSeed": "主题-日期-随机词",
  "pageCount": 10,
  "themePack": "theme01",
  "slides": [
    {"layout": "theme01_page001", "props": {"kicker": "副标题", "titleTop": "上标题", "titleBottom": "下标题", "lead": "引导语"}},
    {"layout": "theme01_page006", "props": {"kicker": "核心数字", "value": "970", "unit": "亿美元"}}
  ]
}
```

**关键约束**：
- 封面只能从前 5 页选 1 页
- 同一 deck 内 layout 不可重复
- copyKeys 列出的文案槽必须全部覆写
- 数组按 fillPlan 的 visibleCount 填满
- 媒体槽只填 canPresetMedia: true 的槽

---

## 渲染命令

```bash
# macOS / Linux
<skill-root>/scripts/render_goal_deck.sh output/<deck>/goal.json output/<deck>/ppt/index.html

# Windows PowerShell
& "<skill-root>/scripts/render_goal_deck.ps1" "output/<deck>/goal.json" "output/<deck>/ppt/index.html"
```

前置条件：Node.js 20+，首次运行自动安装依赖。

---

## 浏览器编辑

生成的 HTML 在 `http://127.0.0.1:<port>/` 预览：
- 翻页浏览
- 侧边栏编辑文案
- 替换图片/视频素材
- 切换页面切换动画
- 自动保存到 `index.html` 本体
- 导出 HTML / PDF / PPTX

> `file://` 打开的本地文件不支持自动保存和导出。

---

## 安装方式

### Claude Code

```bash
cp -r dashi-ppt/ ~/.claude/skills/dashi-ppt/
```

### 上游完整安装（含渲染引擎和主题）

```bash
npx skills add chuspeeism/dashiAI-ppt-skill
```

本 wrapper 提供路由指南和结构化使用说明。完整渲染能力需上游 `project/` 目录。

---

## 与 Dog-Skills PPT 生态协作

```
dog-ppt (路由器) → 判断场景 → dashi-ppt / ppt-master / huashu-slides / ...
                                │
                          dashi-ppt 适合:
                          - 内容明确 + 缺设计 → 12主题选一套
                          - 要稳定输出 → 锁模板填文案
                          - 要边看边调 → 浏览器编辑+自动保存
                          - 最终要 PPTX → 一键导出
```

完整 PPT 技能对比和选型指南：[`ppt/README.md`](../ppt/README.md)

---

## 上游致谢

基于 [chuspeeism/dashiAI-ppt-skill](https://github.com/chuspeeism/dashiAI-ppt-skill) (MIT License) v0.4.4。内置 React 渲染引擎 + 12 套主题 + html-deck-to-pptx 导出。
