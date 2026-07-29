#!/usr/bin/env python3
"""
GPT Researcher 包装脚本 — 自动将研究报告保存到 Dog-Research 目录。

每个研究主题一个独立子文件夹，包含 report.md + sources.json + context.json。

用法:
    python research.py "研究主题" [--report-type TYPE] [--output-base DIR]

示例:
    python research.py "AI Agent 框架对比 2025"
    python research.py "LLM 安全最佳实践" --report-type deep_research
    python research.py "量子计算最新进展" --output-base "D:/Projects/Dog/Dog-Research"
"""

import asyncio
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def slugify(text: str, max_len: int = 60) -> str:
    """将中文/英文主题转为文件夹名。"""
    # 先尝试提取英文部分，如果没有则用拼音风格简化
    # 保留字母数字和中文（中文转拼音太复杂，这里直接用时间戳兜底）
    text = text.strip().lower()
    # 移除特殊字符，保留字母、数字、中文、空格
    cleaned = re.sub(r"[^\w\s-]", "", text)
    # 空白转连字符
    slug = re.sub(r"[-\s]+", "-", cleaned).strip("-")
    if not slug or len([c for c in slug if c.isascii() and c.isalpha()]) < 3:
        # 主要是中文，用时间戳 + 前几个字
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        slug = f"research-{timestamp}"
    return slug[:max_len]


async def run_research(
    query: str,
    report_type: str = "research_report",
    output_base: str = "D:/Projects/Dog/Dog-Research",
    report_source: str = "web",
) -> Path:
    """执行深度研究并保存结果。

    Args:
        query: 研究主题
        report_type: 报告类型 (research_report|detailed_report|resource_report|outline_report|deep_research)
        output_base: 输出根目录
        report_source: 来源 (web|local|hybrid)

    Returns:
        输出目录路径
    """
    from gpt_researcher import GPTResearcher

    topic_slug = slugify(query)
    output_dir = Path(output_base) / topic_slug
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🔬 开始研究: {query}")
    print(f"📂 输出目录: {output_dir}")
    print(f"📋 报告类型: {report_type}")
    print()

    researcher = GPTResearcher(
        query=query,
        report_type=report_type,
        report_source=report_source,
    )

    # 执行研究（爬取 + 聚合）
    print("⏳ 正在搜集资料（并行抓取 20+ 来源）...")
    research_result = await researcher.conduct_research()
    print(f"✅ 资料搜集完成")

    # 生成报告
    print("📝 正在生成研究报告...")
    report = await researcher.write_report()
    print(f"✅ 报告生成完成 ({len(report)} 字符)")

    # 保存报告
    report_path = output_dir / "report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"📄 报告已保存: {report_path}")

    # 保存来源
    try:
        sources = researcher.get_research_sources()
        sources_path = output_dir / "sources.json"
        sources_path.write_text(
            json.dumps(sources, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"📎 来源已保存: {sources_path} ({len(sources)} 个来源)")
    except Exception as e:
        print(f"⚠️  来源保存失败: {e}")

    # 保存研究上下文
    try:
        context = researcher.get_research_context()
        context_path = output_dir / "context.json"
        context_path.write_text(
            json.dumps(context, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"📦 上下文已保存: {context_path}")
    except Exception as e:
        print(f"⚠️  上下文保存失败: {e}")

    # 保存元信息
    meta = {
        "query": query,
        "report_type": report_type,
        "report_source": report_source,
        "generated_at": datetime.now().isoformat(),
        "output_dir": str(output_dir),
    }
    meta_path = output_dir / "meta.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print()
    print(f"🎉 研究完成！所有文件已保存到: {output_dir}")
    print(f"   ├── report.md")
    print(f"   ├── sources.json")
    print(f"   ├── context.json")
    print(f"   └── meta.json")

    return output_dir


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="GPT Researcher — 开源深度研究 Agent 包装脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python research.py "AI Agent 框架对比"
  python research.py "LLM 安全最佳实践" --report-type deep_research
  python research.py "新能源汽车市场分析" --output-base "D:/Projects/Dog/Dog-Research"
        """,
    )
    parser.add_argument("query", help="研究主题")
    parser.add_argument(
        "--report-type",
        default="research_report",
        choices=["research_report", "detailed_report", "resource_report", "outline_report", "deep_research"],
        help="报告类型 (默认: research_report)",
    )
    parser.add_argument(
        "--output-base",
        default="D:/Projects/Dog/Dog-Research",
        help="输出根目录 (默认: D:/Projects/Dog/Dog-Research)",
    )
    parser.add_argument(
        "--report-source",
        default="web",
        choices=["web", "local", "hybrid"],
        help="研究来源 (默认: web)",
    )

    args = parser.parse_args()
    output_dir = asyncio.run(
        run_research(
            query=args.query,
            report_type=args.report_type,
            output_base=args.output_base,
            report_source=args.report_source,
        )
    )
    # 输出目录路径供外部脚本捕获
    print(f"\nOUTPUT_DIR={output_dir}")


if __name__ == "__main__":
    main()
