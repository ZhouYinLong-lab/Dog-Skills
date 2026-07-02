---
name: webapp-testing
description: >
  基于 Playwright 的自动化前端测试——一句话驱动全流程：自动写测试脚本、
  启动浏览器、执行测试、截屏输出结果。Anthropic 官方出品，适合部署前全页面截图对比、
  登录流程测试、表单验证等场景。
  Trigger keywords: webapp testing, 前端测试, 自动化测试, Playwright测试,
  浏览器测试, 端到端测试, e2e测试, 页面截图, 测试登录, 部署前测试,
  test my app, 帮我测试, 测一下登录流程, 跑一下测试。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - TaskCreate
metadata:
  category: development
  source: https://github.com/anthropic/claude-plugin-directory
  install: /plugin install webapp-testing@claude-plugin-directory
  version: "1.0.0"
  license: MIT
---

# Webapp Testing — 基于 Playwright 的自动化前端测试

> Anthropic 官方出品，底层基于 Playwright。卖点不是"帮你写测试"，而是全流程自动化。

## 核心能力

### 一句话全流程测试

你跟 Claude Code 说"测一下登录流程"，它自动帮你：

1. **写测试脚本** — 无需手写 await 和 selector
2. **启动 Playwright 浏览器** — 真实的 Chromium 环境
3. **执行测试** — 模拟真实用户操作
4. **截屏输出结果** — 每一步都有截图佐证

### 适用场景

- **登录/注册流程**：填邮箱、验证码、设置密码、跳转欢迎页
- **表单验证**：必填项检查、格式校验、错误提示
- **页面渲染检查**：改了一行 CSS 结果整个页面布局崩了？部署前跑一下全页面截图对比
- **关键用户路径**：从首页到下单的完整流程

## 安装

```
/plugin install webapp-testing@claude-plugin-directory
```

需要 Playwright 环境：
```bash
npx playwright install chromium
```

## 使用方式

```
"测一下登录流程"
"帮我测试这个表单的验证逻辑"
"部署前跑一下所有页面的截图"
"检查支付流程有没有问题"
```

## 使用建议

- **部署前必跑**：全页面截图对比，比肉眼检查靠谱
- **改 CSS 后必跑**：防止一处改动崩了整个布局
- **复杂交互场景**：测试脚本仍需人工校验，AI 可能漏掉边界条件

## 最佳搭配

提交代码前的完整检查流水线：

```
Code Simplifier → Code Review → Webapp Testing → 部署
```

如果 Webapp Testing 发现问题，回到 Code Simplifier 修改后重新走流水线。
