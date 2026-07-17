---
name: read-buddy
description: >
  信息读取中心——18 种信息读取能力的总控路由元技能。覆盖网页·RSS·YouTube·播客·
  X/Twitter·飞书文档·图片OCR·微信读书·小宇宙·个人数据等全来源。根据内容来源
  自动选择读取策略，把任意格式的信息转成结构化 Markdown/JSON/报告。
  与 Dog-Skills 现有工具（markitdown/weread-skill/baoyu-skills）互补协作。
  Trigger keywords: 读网页, 保存文章, 提取字幕, RSS, 播客转文字,
  飞书文档, OCR, 图片识别, 微信读书导出, 小宇宙, X分析,
  热点采集, 口播脚本, 个人数据, 阅读报告, 信息读取,
  read url, save article, YouTube transcript, podcast to text,
  read this page, fetch content, 帮我读, 把这个转成文字.
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
  category: tools
  source: https://github.com/SpaceZephyr/read-buddy (MIT)
  upstream-author: 空格的键盘 (SpaceZephyr)
  sub-skills: 18
  version: "1.0.0"
  license: MIT
---

# Read Buddy — 信息读取中心

> 18 种信息读取能力的总控路由。一句话描述你想读什么，自动选择最佳读取策略。
> 上游来源: [SpaceZephyr/read-buddy](https://github.com/SpaceZephyr/read-buddy) (MIT)，作者：空格的键盘

## 核心理念

```
不是让 AI 凭空总结一段它没读过的材料。
是先把来源内容拿回来，再让 Agent 帮你完成：
  读 → 抽取 → 结构化 → 消化
```

---

## 路由总控

根据用户输入自动判断应该用哪个读取策略。优先级：**Dog-Skills 已有 > Read Buddy 独有 > 组合使用**。

### 路由表

| 用户输入特征 | 首选方案 | 备选方案 | 说明 |
|-------------|---------|---------|------|
| URL / "读这个网页" | **markitdown** (Dog-Skills) | read-url-markdown | markitdown 更成熟；需要 JS 渲染页面时用 read-url-markdown (Chrome CDP) |
| "导出微信读书" | **weread-skill** (Dog-Skills) | read-weread-export | Dog-Skills 已有完整微信读书集成 |
| "分析我的阅读" | **weread-skill** (Dog-Skills) | read-weread-analyzer | 阅读画像/统计/书架分析 |
| "今日笔记" / "划线回顾" | **weread-skill** (Dog-Skills) | read-weread-coach | 每日划线回顾 |
| YouTube 字幕 | **baoyu-skills** (Dog-Skills) | read-youtube-transcript | baoyu-skills 已支持 |
| "翻译这篇文章" | **baoyu-skills** (Dog-Skills) | read-web-article-translator | 中英互译 |
| 长文→摘要/短帖 | **baoyu-skills** (Dog-Skills) | read-content-digest | 内容消化 |
| "RSS 更新" / "订阅源" | **read-rss-aggregator** ⭐ | — | Dog-Skills 无此能力 |
| "AI 热点" / "今日选题" | **topic-collector** (Dog-Skills) | read-topic-collector | 自动多源采集 |
| X/Twitter 推文→MD | **read-x-markdown** ⭐ | — | 需用户知情同意反爬风险 |
| X 博主分析 | **read-x-blogger-analyzer** ⭐ | — | 风格/爆款/增长策略分析 |
| "飞书文档" | **read-feishu-doc** ⭐ | — | 飞书开放 API 读取 |
| 图片/PDF OCR | **read-ocr** ⭐ | — | 提取图中文字 |
| 播客→工作流 | **read-podcast-workflow** ⭐ | — | 更新选择→字幕→消化→飞书保存 |
| 播客→口播脚本 | **read-podcast-script-generator** ⭐ | — | 摘要→第一人称视频口播稿 |
| "小宇宙" / 播客链接 | **read-xiaoyuzhou-article** ⭐ | — | 音频下载→Whisper 转录→文章 |
| YouTube 频道更新 | **read-youtube-feed** ⭐ | — | 获取关注频道近期更新 |
| "同步我的数据" | **read-personal-data-harvester** ⭐ | — | 阅读/观看/收藏历史→本地 SQLite |

⭐ = Read Buddy 独有能力，Dog-Skills 无覆盖。

---

## 18 个子技能总览

### 网页 & 文档读取

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `read-url-markdown` | Chrome CDP 读取网页（含 JS 渲染页面），转 Markdown | Markdown |
| `read-web-scraper` | 轻量网页抓取，HTML→Markdown | Markdown / HTML |
| `read-web-article-translator` | 在线文章翻译为中文并保存 | 中文 Markdown |
| `read-feishu-doc` | 飞书开放 API 读取文档和 blocks | 文档内容 / JSON |

### 视频 & 播客

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `read-youtube-feed` | 获取关注 YouTube 频道近期更新 | 更新列表 |
| `read-youtube-transcript` | 提取 YouTube 字幕并转中文文字稿 | Markdown / JSON |
| `read-podcast-workflow` | 播客更新选择→字幕→消化→飞书保存 | 完整工作流 |
| `read-podcast-script-generator` | 播客笔记→视频口播脚本 | 口播脚本 |
| `read-xiaoyuzhou-article` | 小宇宙音频下载→Groq Whisper 转录→文章 | 文稿 + 文章 |

### 社交媒体 & 热点

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `read-x-markdown` | X/Twitter 推文/线程→Markdown（需用户知情同意） | Markdown + YAML |
| `read-x-blogger-analyzer` | X 博主内容风格、爆款原因、增长策略分析 | 分析报告 |
| `read-rss-aggregator` | OPML RSS 源聚合近期更新 | 更新摘要列表 |
| `read-topic-collector` | AI 热点/产品发布/论文/社区动态多源采集 | 结构化热点清单 |

### 内容消化 & 个人数据

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `read-content-digest` | 长文/播客/访谈→短帖和长文叙事 | 摘要/短帖/长文 |
| `read-ocr` | 图片/PDF/扫描件 OCR 识别 | 结构化 JSON/文本 |
| `read-weread-export` | 导出微信读书划线和想法（Markdown/PDF） | 读书笔记文件 |
| `read-weread-analyzer` | 10 维度阅读分析报告 | 9:16 HTML 报告 |
| `read-weread-coach` | 阶梯书单推荐+写作引用+每日划线回顾 | 推荐/引用/回顾 |
| `read-personal-data-harvester` | 个人阅读/观看/收藏历史→本地 SQLite | SQLite / 结构化数据 |

---

## 使用示例

```
用户: 把这个网页保存成 Markdown
→ 路由到 markitdown (Dog-Skills 优先)

用户: 帮我看看最近 RSS 有什么更新
→ 路由到 read-rss-aggregator (Read Buddy 独有)

用户: 分析一下这个 X 博主的内容风格
→ 路由到 read-x-blogger-analyzer (Read Buddy 独有)

用户: 把这个小宇宙播客转成文章
→ 路由到 read-xiaoyuzhou-article (Read Buddy 独有)

用户: 提取这张图片里的文字
→ 路由到 read-ocr (Read Buddy 独有)

用户: 导出我的微信读书划线
→ 路由到 weread-skill (Dog-Skills 优先)
```

---

## 四层工作架构

```
来源接入层  →  URL·RSS·YouTube·X·飞书·OCR·微信读书·小宇宙·个人平台
内容抽取层  →  HTML清洗·字幕提取·OCR·API blocks·线程解析·RSS条目聚合
结构整理层  →  Markdown·JSON·SQLite·YAML front matter·分析报告
认知处理层  →  摘要·翻译·热点判断·风格分析·选题提炼·长短文改写
```

---

## 安装方式

### 本元技能

```bash
cp -r read-buddy/ ~/.claude/skills/read-buddy/
```

### 上游完整安装（获取所有 18 个子技能）

```bash
npx skills add SpaceZephyr/read-buddy
```

上游子技能遵循 `read-*` 命名规范，每个子目录都是一个独立 Skill，可按需单独复制。

---

## 风控说明

- 只读优先：默认只读取公开内容或用户自己的数据
- 不做账号动作：不执行发帖/点赞/评论等写操作
- 凭据不入库：API Key/Cookie/登录态不提交到仓库
- X 风险提示：使用非官方接口，需用户知情同意
- 个人数据本地化：默认只在用户设备上保存
- 低频采样：按需读取，不给平台造成压力

---

## 上游致谢

本元技能基于 [SpaceZephyr/read-buddy](https://github.com/SpaceZephyr/read-buddy) (MIT License)，作者：空格的键盘（公众号/小红书/B站/知乎）。

Dog-Skills 生态内协作：`markitdown`（网页→MD）、`weread-skill`（微信读书）、`baoyu-skills`（翻译/字幕/内容消化）、`topic-collector`（AI 热点采集）。
