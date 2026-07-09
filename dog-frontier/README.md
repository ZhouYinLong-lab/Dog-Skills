# Dog-Frontier — 前端设计综合技能

> 整合 21 个前端技能的元技能系统。v2.0 深度集成 Google DESIGN.md 格式标准 + awesome-design-md 58 品牌库。

## v2.0 新特性：DESIGN.md 生态集成

### 什么是 DESIGN.md？

[Google DESIGN.md](https://github.com/google-labs-code/design.md)（Apache 2.0）是一种纯文本设计系统格式——YAML 设计令牌 + Markdown 规范文档，让 AI agent 能直接读懂设计系统。

[awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（MIT, 91K+ Stars）收集了 58 家知名公司的 DESIGN.md 文件，包括 Stripe、Apple、Vercel、Airbnb、Notion、Linear、Nike、Tesla、Figma 等。

### 三件事

| 功能 | 说明 | 阶段 |
|------|------|------|
| 🎨 **风格即插即用** | 说"给我做一个 Stripe 风格的后台"，自动匹配 DESIGN.md | Phase 2 |
| 🔍 **自动令牌校验** | `npx @google/design.md lint` 检查对比度、引用完整性 | Phase 5 |
| 📤 **一键导出框架配置** | `npx @google/design.md export --format tailwind4` | Phase 4 |

### 风格选择优先级

```
1. awesome-design-md 匹配 (58品牌 DESIGN.md 即插即用)
2. ui-ux-pro-max BM25 搜索 (67风格)
3. 内置设计知识 (兜底)
```

## 来源

| 项目 | 作者 | 许可 | 链接 |
|------|------|------|------|
| DESIGN.md 格式标准 | Google Labs | Apache-2.0 | [github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md) |
| awesome-design-md | VoltAgent | MIT | [github.com/VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) |
| Dog-Frontier | Dog-Skills | MIT | 本仓库 |

## 快速开始

```
# 触发
"给我做一个 Stripe 风格的管理后台"
"按 Notion 的配色重构这个页面"
"lint 一下我的 DESIGN.md"
```

详见 [SKILL.md](SKILL.md) 和 [ATTRIBUTIONS.md](ATTRIBUTIONS.md)。
