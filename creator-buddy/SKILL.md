---
name: creator-buddy
description: >
  内容运营情报中心——5 个内容运营研究技能的总控路由元技能。从小红书·公众号·B站·抖音
  的真实数据中搜索热点、拆爆款、分析赛道、生成标题。把"今天写什么"从玄学变成
  可复用的数据工作流。与 Dog-Skills 现有工具（last30days/dbskill）互补：
  last30days 侧重海外平台，creator-buddy 补中文内容生态。
  Trigger keywords: 找选题, 热点搜索, 爆款分析, 起标题, 小红书搜索,
  公众号爆款, B站趋势, 赛道分析, 内容运营, 竞品分析,
  今天写什么, 选题建议, 标题优化, 爆款标题, 平台搜索,
  content research, viral analysis, trend search,
  Xiaohongshu hot, WeChat viral, Bilibili trending.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
metadata:
  category: business
  source: https://github.com/SpaceZephyr/creator-buddy (MIT)
  upstream-author: 空格的键盘 (SpaceZephyr)
  sub-skills: 5
  version: "1.0.0"
  license: MIT
---

# Creator Buddy — 内容运营情报中心

> 5 个内容运营研究技能的总控路由。从小红书/公众号/B站真实数据中找选题、拆爆款、起标题。
> 上游来源: [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) (MIT)，作者：空格的键盘

## 核心理念

```
不是让 AI 凭感觉给你编选题。
是先把平台上的真实内容、互动数据、标题结构和传播信号拉回来，
再让 Agent 帮你判断：
  哪些话题正在涨 · 哪些标题值得拆 · 哪些内容形式在被收藏
  哪些爆款只是噪声 · 你的下一篇该往哪里打
```

---

## 路由总控

| 用户输入特征 | 路由到 | 输出 |
|-------------|--------|------|
| 小红书 + 关键词 | **xhs-hotnotes** | 热门笔记 HTML 报告 + JSON |
| "全平台搜" / "跨平台对比" | **global-content-search** | 小红书/B站/抖音跨平台检索 |
| 公众号 + 关键词 | **gzh-explosive-content-detector** | 爆款文章 HTML 报告 |
| "赛道分析" / "这个领域什么火" | **baokuan-article-analysis** | 赛道级聚合排名 + data.json |
| "起标题" / "爆款标题" / "帮我起个标题" | **baokuan-title-generator** (Dog-Skills 独立技能) | 16 法标题矩阵 + Top 5 推荐 |

### 与 Dog-Skills 现有工具的分工

| 场景 | 用哪个 | 为什么 |
|------|--------|--------|
| 海外热点 / Reddit / HN / X | **last30days** | 专注海外平台，实时互动信号 |
| 小红书 / 公众号 / B站 / 抖音 | **creator-buddy** | 专注中文内容生态 |
| 中文标题公式 | **dbskill** 或 **baokuan-title-generator** | 前者偏方法论，后者偏批量生成 |
| 全球跨平台 | **last30days** + **creator-buddy** | 组合使用 |

---

## 5 个子技能详解

### 1. xhs-hotnotes — 小红书热门笔记搜索

```bash
export REDFOX_API_KEY="your_api_key_here"
python3 skills/xhs-hotnotes/scripts/fetch_xhs_hot_articles.py \
  --keyword "Codex,AI编程" --start-date 2026-06-23
```

**能力**：关键词搜索→热门笔记排序→互动指标（点赞/收藏/评论）→相关性评分
**输出**：HTML 报告 + JSON

### 2. global-content-search — 全域内容搜索

```bash
# 小红书搜索
node skills/global-content-search/src/xiaohongshu/search-cli.js \
  --platform xiaohongshu --keyword "AI编程" --limit 20

# B站搜索
node skills/global-content-search/src/xiaohongshu/search-cli.js \
  --platform bilibili --keyword "AI编程" --limit 10

# 抖音（需本地只读 CLI）
export DOUYIN_COMMAND="/path/to/douyin-readonly-cli"
node skills/global-content-search/src/xiaohongshu/search-cli.js \
  --platform douyin --keyword "AI工具"
```

**平台覆盖**：小红书 / B站 / 抖音（扩展入口）
**访问顺序**：Agent Reach 优先 → Guaikei API 兜底（小红书）
**额外能力**：查详情、查评论、查创作者作品

### 3. gzh-explosive-content-detector — 公众号爆款检测

```bash
python3 skills/gzh-explosive-content-detector/scripts/fetch_gzh_trends.py \
  --keyword "AI编程,Codex,Claude Code" --start-date 2026-06-23
```

**能力**：公众号关键词搜索→互动数据（阅读/分享/点赞）→爆款识别
**输出**：HTML 报告

### 4. baokuan-article-analysis — 赛道级爆款聚合分析

```bash
python3 skills/baokuan-article-analysis/scripts/daily_sector_trends.py \
  --sector "AI Coding=Codex,Claude Code,AI编程" \
  --days 7 --output-dir ./reports
```

**能力**：赛道级聚合→去重→排名→风格分析→趋势判断
**输出**：HTML 报告 + `data.json` 结构化数据

### 5. baokuan-title-generator — 爆款标题生成器

**Dog-Skills 已独立封装**：[`baokuan-title-generator`](../baokuan-title-generator/)

**能力**：16 种爆款标题方法→批量候选→逐条评分→标风险→5 角色推荐→A/B 建议
**方法论来源**：100 篇真实科技类 10 万+ 标题样本

---

## 与 last30days 的协作模式

```
"我想做一个关于 AI Agent 的深度内容"
       │
       ├─→ last30days: 查 Reddit/HN/X 上老外在讨论什么
       │   输出: 海外视角的选题信号
       │
       └─→ creator-buddy: 查小红书/公众号/B站上国内在火什么
           输出: 中文生态的爆款模式 + 标题方案
       
       交叉对比 → 找到"海外有热度 + 国内缺内容"的选题蓝海
```

---

## 四层工作架构

```
平台访问  →  Redfox·Agent Reach·OpenCLI·bili-cli·公开API·只读CLI
数据整理  →  去重·排序·评分·截断·结构化JSON
报告生成  →  HTML报告·排名卡片·互动指标·标题样本
运营判断  →  选题方向·标题机制·内容形式·传播原因
```

---

## 安装方式

### 本元技能

```bash
cp -r creator-buddy/ ~/.claude/skills/creator-buddy/
```

### 上游完整安装（获取所有 5 个子技能+脚本）

```bash
npx skills add zephyrwang6/creator-buddy
```

部分子技能需要 API Key：`REDFOX_API_KEY`（小红书）、`GUAIKEI_API_TOKEN`（小红书兜底）。凭据不入库，只放本地环境变量。

---

## 风控说明

- 只读公开数据：默认只读取公开页面和公开 API
- 不做账号动作：不执行发帖/点赞/评论/关注等写操作
- 凭据不入库：API Key/Cookie/登录态不提交到仓库
- 低频使用：小批量、低并发、按需采样
- 分享前脱敏：移除 token/邮箱/手机号/后台链接

---

## 上游致谢

本元技能基于 [SpaceZephyr/creator-buddy](https://github.com/SpaceZephyr/creator-buddy) (MIT License)，作者：空格的键盘。

Dog-Skills 生态内协作：`baokuan-title-generator`（爆款标题独立技能）、`last30days`（海外平台热点）、`dbskill`（小红书标题公式/内容诊断）。
