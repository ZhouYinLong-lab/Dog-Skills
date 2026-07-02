---
name: token-optimizer
description: >
  优化 Claude Code 上下文 Token 消耗——重新组织项目文档结构，只保留 4 个核心文件
  在启动时自动加载（约 800 token），其他内容按需加载（0 token 成本）。
  实测省 90% token（11000 → 1300），一条命令 30 秒搞定。
  支持 13 种框架专项模板，含 .claudeignore 机制和维护工具链。
  Trigger keywords: token optimizer, token优化, 优化token, 节省token,
  上下文优化, claude-token-optimizer, cto, .claudeignore, 减少token消耗,
  token管理, 清理上下文, 文档结构优化, 按需加载。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
metadata:
  category: tools
  source: https://www.npmjs.com/package/claude-token-optimizer
  install: npx claude-token-optimizer init
  version: "1.0.0"
  license: MIT
---

# token-optimizer — 上下文 Token 消耗优化

> 装完以后立刻见效最明显的一个。实测：优化前每次启动烧 11000 token，优化后降到 1300，省了将近 90%。

## 为什么需要它

Claude Code 启动时自动加载项目根目录下的所有文档文件。如果你的 CLAUDE.md 里塞了三年前的架构决策、去年的 bug 记录、上个月的会话笔记，它全给你加载进去。这些文档可能 90% 跟当前任务无关，但 token 照烧。

## 核心原理

```
优化前：启动加载所有文档 → 11000 token
优化后：只加载 4 个核心文件 → 800 token
        其他内容按需加载 → 0 token 启动成本
```

## 安装

```bash
npx claude-token-optimizer init
```

一条命令，30 秒搞定。自动检测你的技术栈（从 package.json、requirements.txt、go.mod 里读），创建优化后的文档目录结构。

## 维护工具链

| 命令 | 作用 |
|------|------|
| `cto measure` | 查看当前 token 消耗 |
| `cto audit` | 健康检查，扫描冗余内容 |
| `cto compress` | 压缩冗余内容 |
| `cto prune` | 清理过期文档 |
| `cto audit --json` | 输出机器可读结果，可接入 CI |

## 支持的框架

Express、Next.js、Django、Rails、Go 等 13 种框架的专项优化模板。

## 维护建议

每周跑一次 `cto audit`，看到 token 数涨了就做一轮清理。这玩意儿本质上是在给 AI 编程工具做"内存管理"。

## 最佳搭配

- 安装新项目时**第一时间**运行，比后期清理省事得多
- 配合 **Superpowers + Planning with Files**：确保 plan 文件和白名单配置不被误清理
