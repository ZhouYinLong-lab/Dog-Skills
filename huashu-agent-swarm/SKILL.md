---
name: huashu-agent-swarm
description: >
  多Agent蜂群并行协作——纯git自组织，无master agent，每个agent独立认领任务、
  写代码、推送。适合大型项目开发。Trigger keywords: 蜂群模式, 多agent,
  并行开发, agent swarm, 启动蜂群, infinite agent loop.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
metadata:
  category: development
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# 无限Agent蜂群模式

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。
> 受 Nicholas Carlini 用 16 个 Claude 实例自主构建 C 编译器启发。

## 核心机制

- 无 master agent，纯 git 自组织
- 每个 agent 独立认领任务、写代码、推送
- 通过 git 进行任务分配和冲突解决
- 适合大型多文件、多模块项目开发

## 使用示例
```
启动蜂群模式开发这个新功能模块
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
