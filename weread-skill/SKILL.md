---
name: weread-skill
description: >
  微信读书 AI 助手 — 连接你的微信读书账号，用 AI 搜书、查笔记、看书评、分析阅读数据。
  支持查阅书架、阅读统计、笔记和划线、书籍搜索、书籍详情、个性化推荐。
  Trigger keywords: 微信读书, 搜书, 我的书架, 阅读笔记, 阅读统计, 划线, 书评,
  推荐书, 读书数据, 微信读书助手, WeRead, weread, 查找书籍, 阅读记录, 我的书评。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebFetch
  - WebSearch
metadata:
  category: tools
  source: https://weread.qq.com/r/weread-skills
  author: 微信读书 (Tencent)
  install: npx skills add Tencent/WeChatReading -g
  version: "1.0.0"
  license: MIT
---

# 微信读书 Skill — WeRead AI Assistant

连接你的微信读书账号，用 AI 搜书、查笔记、看书评、分析阅读数据。

## 安装

本 Skill 是对 `Tencent/WeChatReading` 的本地封装。首次使用时请先安装上游包：

```bash
npx skills add Tencent/WeChatReading -g
```

## 功能

1. **查阅书架** — 浏览你的个人书架，快速了解藏书全貌
2. **阅读统计** — 时长、天数、偏好深度分析，量化你的阅读习惯
3. **笔记和划线** — 查看个人划线和想法，导出笔记，回顾阅读中的思考
4. **书籍搜索** — 在书城搜索任意书籍，快速获取书名、作者、评分等关键信息
5. **书籍详情** — 查看书籍详情、章节目录、阅读进度，了解你的阅读旅程
6. **推荐好书** — 基于你的阅读偏好，个性化推荐或相似书籍推荐

## 使用前提

1. 拥有微信读书账号
2. 在 [微信读书 Skill 页面](https://weread.qq.com/r/weread-skills) 登录获取 API Key
3. 安装 `Tencent/WeChatReading` Skill

## 触发示例

- "帮我查查我的书架上有哪些书"
- "分析我的阅读统计数据"
- "搜索《三体》这本书的评分"
- "查看我最近的笔记和划线"
- "基于我的阅读记录推荐几本书"
- "看看我今年读了多少书"
