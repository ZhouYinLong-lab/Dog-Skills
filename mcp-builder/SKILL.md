---
name: mcp-builder
description: >
  MCP Builder — Anthropic 官方出品的 MCP Server 开发引导工具。通过四阶段
  （定义工具接口→实现业务逻辑→处理错误和边界情况→测试和部署）带你从零搭建
  高质量的 MCP Server，让 AI 能调用外部工具和 API。每个阶段都有具体提示和最佳实践。
  Trigger keywords: MCP Builder, mcp-builder, MCP Server, Model Context Protocol,
  开发MCP, 构建MCP, 工具集成, API封装, 自定义工具, build MCP server,
  创建MCP服务, 连接外部API, Jira集成, Slack集成, 内部API封装。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
  - TaskCreate
metadata:
  category: development
  source: https://github.com/anthropic/claude-plugin-directory
  install: /plugin install mcp-builder@claude-plugin-directory
  version: "1.0.0"
  license: MIT
---

# MCP Builder — 引导开发 MCP Server 的四阶段辅助工具

> MCP（Model Context Protocol）是 Anthropic 推的开放协议，让 AI 能调用外部工具和 API。听起来挺方便，但实际开发一个 MCP Server 的坑非常多。

MCP Builder 是 Anthropic 官方出的 Skill，通过四个阶段引导你从零搭建高质量 MCP Server。

## 四阶段引导

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  ① 定义接口   │───▶│  ② 实现逻辑   │───▶│  ③ 错误处理   │───▶│  ④ 测试部署   │
│              │    │              │    │              │    │              │
│ 工具名称、    │    │ 业务逻辑编码  │    │ 认证配置、    │    │ 单元测试、    │
│ 参数定义、    │    │ 数据转换、    │    │ 超时处理、    │    │ 集成测试、    │
│ 返回格式      │    │ API 调用      │    │ 并发限制      │    │ 部署上线      │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

不是丢一个模板让你自己琢磨，而是**每一步都带着你做**。

## 安装

```
/plugin install mcp-builder@claude-plugin-directory
```

## 适用场景

- **内部 API 封装**：把公司的数据查询 API、用户管理 API 包装成 MCP Server
- **工具集成**：让 Claude Code 能直接查 Jira ticket、发 Slack 通知、调内部 API
- **数据库连接**：安全地让 AI 查询数据库而不暴露原始凭证
- **自动化工作流**：把重复性的操作固化为 MCP 工具

## 使用方式

```
"帮我创建一个 MCP Server，连接公司的数据查询 API"
"我要让 Claude Code 能发 Jira ticket，帮我搭个 MCP Server"
"把这个 REST API 包装成 MCP 工具"
```

## 实测体验

把公司内部的一个数据查询 API 包装成了 MCP Server，让 Claude Code 能直接查数据库。从写到跑通大概花了两个小时。中间遇到的认证配置、超时处理、并发限制这些问题，MCP Builder 在对应阶段都有具体提示。

## 参考资源

Anthropic 在 Skills 仓库里维护了十几个高质量的 MCP Server 示例，可以参考。
