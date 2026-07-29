---
name: huashu-article-edit
description: >
  标准化文章编辑流程——先读完全文列出所有修改项，确认后才动手，每改3-5项汇报进度。
  防止会话截断导致编辑丢失（增量保存）。Trigger keywords: 编辑文章, 修改文章,
  调整内容, 改一下这篇, article edit.
allowed-tools:
  - Read
  - Write
  - Edit
metadata:
  category: content
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# 文章编辑 Skill

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。

## 核心流程

1. 通读全文，列出所有修改项
2. 用户确认修改范围
3. 逐项执行，每3-5项汇报进度
4. 增量保存，防止会话截断丢失
5. 完成后输出变更总结

## 使用示例
```
编辑这篇文章，把语气改得更轻松一些
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
