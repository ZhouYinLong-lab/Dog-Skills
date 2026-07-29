---
name: gpt-researcher
description: >
  GPT Researcher — 开源深度研究 Agent，planner + executor 双智能体架构，
  并行抓取 20+ 来源，生成 2000+ 字带引用研究报告。支持 Deep Research 递归模式、
  MCP Server 集成、本地文档研究。适用于投资分析、市场调研、技术咨询、学术综述。
  Trigger keywords: deep research, 深度研究, GPT Researcher, 自动研究, 调研报告,
  行业研究, 市场调研, 技术调研, 竞品分析, 投资分析, 学术综述, 文献调研,
  research report, 自动生成报告, 深度调研, gpt-researcher, 研究报告。
metadata:
  category: thinking
  source: https://github.com/assafelovic/gpt-researcher
  version: "3.5.1"
  license: Apache-2.0
  stars: 28000
---

# GPT Researcher — 开源深度研究 Agent

基于 GPT Researcher v3.5.1（28,000+ GitHub Stars），planner + executor 双 agent 架构的开源深度研究工具。并行抓取 20+ 来源，5 分钟生成 2000+ 字带引用研究报告。

## 架构

```
用户提问 → Planner（拆解问题，生成研究方向）
                ↓
         Executor（并行抓取 20+ 来源）
                ↓
         Publisher（聚合、去重、引用，生成最终报告）
```

| Agent | 职责 |
|-------|------|
| **Planner** | 拆解研究问题，生成一组研究方向/子问题 |
| **Executor** | 并行爬取每个子问题的相关资料（20+ 来源） |
| **Publisher** | 汇总、过滤、源追踪，聚合为最终研究报告 |

### Deep Research 模式

树形递归探索，可配置深度和广度：
- 递归深入子问题，每层自动发现新的研究方向
- 并发处理不同研究分支
- 跨分支智能上下文管理
- 单次约 5 分钟，成本约 $0.40（o3-mini high 模式）

## 前置条件

- **Python 3.11+**
- **OpenAI API Key** — https://platform.openai.com/api-keys
- **Tavily API Key** — https://tavily.com/（免费额度可用）

```bash
pip install gpt-researcher
```

### 环境变量

```bash
export OPENAI_API_KEY="sk-..."
export TAVILY_API_KEY="tvly-..."
```

可选：
```bash
export OPENAI_BASE_URL="http://your-custom-endpoint"  # 自定义 LLM 端点
export RETRIEVER="tavily,duckduckgo"                    # 多检索器
export DOC_PATH="./my-docs"                             # 本地文档路径
```

## 输出目录规则（重要）

**所有研究报告必须输出到 `D:\Projects\Dog\Dog-Research` 目录，每次研究一个独立子文件夹。**

```
D:\Projects\Dog\Dog-Research\
├── ai-agent-framework-comparison-2025\
│   ├── report.md          # 研究报告正文
│   ├── report.pdf         # PDF 版本（可选）
│   ├── report.docx        # Word 版本（可选）
│   ├── sources.json       # 来源列表
│   └── context.json       # 研究上下文
├── llm-security-best-practices\
│   ├── report.md
│   └── ...
└── ...
```

### 文件夹命名规则

- 使用英文小写 + 连字符
- 取研究主题的前 3-5 个关键词
- 示例：`"AI Agent 框架对比 2025"` → `ai-agent-framework-comparison-2025`

## 使用方式

### 方式 1：Python 脚本（推荐）

使用项目提供的 `scripts/research.py` 包装脚本，自动处理输出目录：

```bash
python scripts/research.py "什么是 LLM Agent 框架的最新进展" \
  --report-type research_report \
  --output-base "D:/Projects/Dog/Dog-Research"
```

### 方式 2：直接 Python API

```python
import asyncio
from gpt_researcher import GPTResearcher
from pathlib import Path
import json
import re

async def deep_research(query: str, report_type: str = "research_report"):
    # 创建输出目录
    topic_slug = re.sub(r'[^a-z0-9]+', '-', query.lower().strip())[:60]
    output_dir = Path("D:/Projects/Dog/Dog-Research") / topic_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    researcher = GPTResearcher(
        query=query,
        report_type=report_type,  # research_report | detailed_report | deep_research
        report_source="web",
    )

    # 执行研究
    research_result = await researcher.conduct_research()

    # 生成报告
    report = await researcher.write_report()

    # 保存报告
    (output_dir / "report.md").write_text(report, encoding="utf-8")

    # 保存来源
    sources = researcher.get_research_sources()
    (output_dir / "sources.json").write_text(
        json.dumps(sources, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    # 保存上下文
    context = researcher.get_research_context()
    (output_dir / "context.json").write_text(
        json.dumps(context, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"✅ 研究报告已保存到: {output_dir}")
    print(f"   - report.md ({len(report)} 字符)")
    print(f"   - sources.json ({len(sources)} 个来源)")
    return str(output_dir)

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "Latest AI developments"
    asyncio.run(deep_research(query))
```

### 方式 3：MCP Server（接入 Claude Desktop / Cursor）

```bash
git clone https://github.com/assafelovic/gptr-mcp.git
cd gptr-mcp
pip install -r requirements.txt
cp .env.example .env  # 填入 API Keys
python server.py
```

MCP 工具：`deep_research` / `quick_search` / `write_report` / `get_research_sources` / `get_research_context`

## 报告类型

| 类型 | 说明 | 适用场景 |
|------|------|----------|
| `research_report` | 综合分析 + 引用（默认） | 通用研究 |
| `detailed_report` | 扩展深度报告 | 需要更详细分析 |
| `resource_report` | 资源列表 + 链接 | 快速搜集资料 |
| `outline_report` | 结构化大纲 | 研究前规划 |
| `deep_research` | 递归树形探索 | 深度研究 |

## 本地文档研究

支持将本地文档作为研究来源：

```bash
export DOC_PATH="./my-docs"
```

支持格式：PDF、Word、Excel、Markdown、PowerPoint、CSV、纯文本。

在 Python 中：`report_source="local"` 或 `report_source="hybrid"`（本地+网络）。

## 工作流指南

当用户提出研究类需求时，按以下流程执行：

### 1. 需求澄清
- 确认研究主题和范围
- 确定报告类型（快速概览 vs 深度研究）
- 确认是否需要本地文档作为来源

### 2. 执行研究
- 使用 `scripts/research.py` 或直接 Python API
- 报告自动保存到 `D:\Projects\Dog\Dog-Research/<topic-slug>/`

### 3. 结果呈现
- 告知用户报告保存位置
- 提供核心发现的摘要
- 列出关键来源

## 触发示例

- "帮我做一份 LLM Agent 框架的深度调研报告"
- "调研 2025 年 AI 安全最佳实践"
- "对比分析 LangChain vs LlamaIndex vs Haystack"
- "做一份新能源汽车行业的投资分析报告"
- "帮我调研 RAG 技术的最新进展，输出研究报告"
- "Deep research on quantum computing breakthroughs in 2025"
- "用 GPT Researcher 做市场调研：企业级 AI 助手赛道"
- "快速研究一下 WebAssembly 在边缘计算的應用"

## 与其他研究技能的关系

| 技能 | 定位 | 与本技能的关系 |
|------|------|--------------|
| `storm-research` | Stanford STORM 方法论——用 4 个提示手动引导 Claude 深度研究 | 互补：STORM 是方法论框架，GPT Researcher 是自动化执行引擎 |
| `scientific-research` | 科学研究助手——139 个科研技能 + 78 个数据库 | 不同场景：前者偏学术科研，本技能偏通用调研 |
| `last30days` | 社交媒体舆情研究（Reddit/X/YouTube） | 不同来源：前者聚焦社交平台近期讨论，本技能聚焦全网深度信息 |

## 参考

- GitHub: https://github.com/assafelovic/gpt-researcher
- 文档: https://docs.gptr.dev
- MCP Server: https://github.com/assafelovic/gptr-mcp
- 安装: `npx skills add assafelovic/gpt-researcher`（Claude Code 官方 Skill）
- PIP: `pip install gpt-researcher`
