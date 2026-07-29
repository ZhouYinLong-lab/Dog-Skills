---
name: ljg-push
description: >
  推送 ljg-* skills——把本地所有更新过的 ljg skills 同步到 GitHub 仓库。
  Trigger keywords: push skills, 推送 skills, 同步 skills, sync ljg, ljg-push.
allowed-tools:
  - Read
  - Write
  - Bash
metadata:
  category: development
  source: https://github.com/lijigang/ljg-skills (6.5k+ stars)
  author: lijigang
  version: "1.0.0"
---

# ljg-push: 推送 ljg-* skills

> 基于 [ljg-skills](https://github.com/lijigang/ljg-skills) (6.5k+ stars)。

## 核心功能

检测本地所有 ljg skills 变更，一键同步到 GitHub 仓库，先推 master（org-mode），再切 md 分支。

## 使用示例
```
推送所有更新的 ljg skills
```

## 安装
```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/skills/_upstream/ljg-skills/
```
