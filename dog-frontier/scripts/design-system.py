#!/usr/bin/env python3
"""
Dog-Frontier 设计系统生成器
============================
整合 ui-ux-pro-max 的搜索能力 + frontend-design 的设计哲学,
输出结构化的 MASTER.md 设计系统文件。

使用:
    python design-system.py "<产品描述>" --project "项目名" [--style "风格偏好"] [--output dir]

来源:
    - 搜索算法: ui-ux-pro-max (nextlevelbuilder, MIT)
    - 设计哲学: frontend-design (Anthropic)
    - 令牌架构: design-system sub-skill (claudekit, MIT)
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# === 配置 ===
SKILLS_BASE = Path.home() / ".claude" / "skills"
UI_UX_PRO_MAX = SKILLS_BASE / "ui-ux-pro-max"

# === 产品-风格匹配表 (来源: ui-ux-pro-max) ===
PRODUCT_STYLE_MAP = {
    "saas": ["minimalism", "glassmorphism", "flat-design", "gradient"],
    "ecommerce": ["photo-based", "bold-typography", "minimalism", "vibrant"],
    "fintech": ["dark-mode", "glassmorphism", "flat-design", "geometric"],
    "healthcare": ["soft-ui", "organic", "neumorphism", "clean"],
    "education": ["clean", "accessible", "flat-design", "minimalism"],
    "gaming": ["cyberpunk", "vaporwave", "neon", "dark-mode"],
    "social": ["vibrant", "gradient", "y2k", "glassmorphism"],
    "portfolio": ["brutalism", "editorial", "minimalism", "swiss"],
    "dashboard": ["bento-grid", "dark-mode", "flat-design", "minimalism"],
    "ai": ["ai-native", "minimalism", "dark-mode", "glassmorphism"],
    "beauty": ["soft-ui", "organic", "glassmorphism", "warm"],
    "food": ["photo-based", "warm", "organic", "vintage"],
    "luxury": ["editorial", "swiss", "minimalism", "elegant"],
}

# === 反模式数据库 (来源: ui-ux-pro-max product domain) ===
ANTIPATTERNS = {
    "saas": [
        "避免密集数据表格 — 用卡片网格替代",
        "避免过多强调色 — 1个主色 + 1个辅色已足够",
        "避免纯暗黑无层次 — 用玻璃态或阴影制造深度",
    ],
    "ecommerce": [
        "避免文字覆盖超过图片20% — Facebook Ads会惩罚",
        "避免冷色调 — 食品/时尚类用暖色系更吸引点击",
        "避免隐藏价格 — 电商用户最关心的信息应第一眼可见",
    ],
    "fintech": [
        "避免过于花哨 — 金融产品需要信任感,花哨降低可信度",
        "避免只用颜色表示涨跌 — 加图标/箭头作为补充指示",
        "避免默认显示敏感数据 — 余额/卡号应有隐私模式",
    ],
    "healthcare": [
        "避免暗色模式 — 医疗信息在亮色下更易读",
        "避免小字号 — 中老年用户需要 ≥16px 正文字号",
        "避免霓虹/赛博朋克风格 — 降低专业感和信任度",
    ],
    "default": [
        "避免三种AI默认配色: (1)暖奶油+#F4F1EA+赤陶 (2)纯黑+酸绿 (3)报纸式细线分隔",
        "避免无意义的01/02/03编号 — 除非内容真的是有序序列",
        "避免所有卡片等大 — Bento Grid 的模块化大小不一更有层次",
    ],
}


def get_product_domain(description: str) -> str:
    """从产品描述中推断产品领域"""
    keywords = {
        "saas": ["saas", "软件", "平台", "工具", "后台", "管理"],
        "ecommerce": ["电商", "商城", "商店", "购物", "商品", "零售"],
        "fintech": ["金融", "支付", "银行", "交易", "理财", "保险", "crypto", "区块链"],
        "healthcare": ["医疗", "健康", "医院", "诊所", "患者", "药品", "养生"],
        "education": ["教育", "学习", "课程", "培训", "学校", "学院", "导师"],
        "gaming": ["游戏", "电竞", "娱乐", "赛事", "竞技"],
        "beauty": ["美容", "护肤", "spa", "美发", "美甲", "化妆"],
        "food": ["餐饮", "食品", "餐厅", "外卖", "美食", "烹饪"],
        "luxury": ["奢侈", "高端", "精品", "定制", "尊享"],
        "ai": ["ai", "人工智能", "智能", "gpt", "模型", "自动化", "机器学习"],
        "dashboard": ["仪表盘", "数据", "看板", "报表", "统计", "分析"],
    }
    desc_lower = description.lower()
    scores = {}
    for domain, kws in keywords.items():
        scores[domain] = sum(1 for kw in kws if kw in desc_lower)
    if not scores or max(scores.values()) == 0:
        return "saas"  # 默认
    return max(scores, key=scores.get)


def generate_master_md(project: str, domain: str, styles: list, description: str) -> str:
    """生成 MASTER.md 内容"""
    antipattern_list = ANTIPATTERNS.get(domain, ANTIPATTERNS["default"])
    antipattern_md = "\n".join(f"- ❌ {a}" for a in antipattern_list)

    return f"""<!-- @source: dog-frontier/phase-2 -->
<!-- @phase: design-system -->
<!-- @date: {datetime.now().strftime('%Y-%m-%d')} -->
<!-- @design_system_version: 1.0.0 -->

# {project} 设计系统

## 1. 风格方案

```yaml
style:
  primary: {styles[0] if styles else 'minimalism'}
  secondary: {styles[1] if len(styles) > 1 else 'none'}
  mode: auto
  source: ui-ux-pro-max (nextlevelbuilder, MIT)
  philosophy: frontend-design — 设计应植根于产品本身

design_rationale: |
  产品领域"{domain}"的最佳匹配风格为{styles[0] if styles else 'minimalism'}。
  该风格选择基于对{description}的目标受众和使用场景分析。
```

## 2. 配色方案

> 运行 `python3 {UI_UX_PRO_MAX}/scripts/search.py "{domain}" --domain color` 获取精确配色。

```yaml
colors:
  bg_primary: {{ hex: "#0A0A0F", token: "--bg-primary" }}
  bg_secondary: {{ hex: "#131320", token: "--bg-secondary" }}
  accent_primary: {{ hex: "#6366F1", token: "--accent-primary" }}
  accent_secondary: {{ hex: "#22D3EE", token: "--accent-secondary" }}
  text_primary: {{ hex: "#F8FAFC", token: "--text-primary" }}
  text_secondary: {{ hex: "#94A3B8", token: "--text-secondary" }}
  semantic:
    success: {{ hex: "#22C55E", token: "--color-success" }}
    error: {{ hex: "#EF4444", token: "--color-error" }}
    warning: {{ hex: "#EAB308", token: "--color-warning" }}
```

## 3. 字体搭配

> 运行 `python3 {UI_UX_PRO_MAX}/scripts/search.py "{domain} modern" --domain typography` 获取精确搭配。

```yaml
typography:
  display: {{ family: "Space Grotesk", weight: "700", google_fonts: "@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700')" }}
  body: {{ family: "Inter", weight: "400;500;600", google_fonts: "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600')" }}
  mono: {{ family: "JetBrains Mono", weight: "400;500", google_fonts: "@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500')" }}
```

## 4. 效果系统

```yaml
effects:
  shadows:
    sm: "0 1px 2px rgba(0,0,0,0.05)"
    md: "0 4px 6px -1px rgba(0,0,0,0.1)"
    lg: "0 10px 15px -3px rgba(0,0,0,0.1)"
  radius:
    sm: "4px"
    md: "8px"
    lg: "12px"
  glass:
    blur: "12px"
    border: "rgba(255,255,255,0.1)"
    bg: "rgba(255,255,255,0.05)"
```

## 5. 反模式警告

{antipattern_md}

## 6. 预交付清单

- [ ] 配色对比度 ≥ 4.5:1 (正文)
- [ ] 字体已导入 Google Fonts
- [ ] 暗色模式(如适用)已定义
- [ ] 触控目标 ≥ 44×44px
- [ ] 4 断点测试通过 (375/768/1024/1440)
"""


def main():
    parser = argparse.ArgumentParser(description="Dog-Frontier 设计系统生成器")
    parser.add_argument("description", help="产品描述,如 'AI SaaS 仪表盘'")
    parser.add_argument("--project", "-p", required=True, help="项目名称")
    parser.add_argument("--style", "-s", help="风格偏好(可选)")
    parser.add_argument("--output", "-o", default="design-system", help="输出目录")
    args = parser.parse_args()

    # Step 1: 推断产品领域
    domain = get_product_domain(args.description)
    styles = PRODUCT_STYLE_MAP.get(domain, ["minimalism"])

    if args.style:
        styles.insert(0, args.style)

    print(f"产品领域: {domain}")
    print(f"推荐风格: {', '.join(styles[:3])}")

    # Step 2: 尝试调用 ui-ux-pro-max 获取精确数据
    search_script = UI_UX_PRO_MAX / ".claude" / "skills" / "ui-ux-pro-max" / "scripts" / "search.py"
    # Fallback path
    if not search_script.exists():
        alt_paths = [
            UI_UX_PRO_MAX / "scripts" / "search.py",
            UI_UX_PRO_MAX / "src" / "ui-ux-pro-max" / "scripts" / "search.py",
        ]
        for p in alt_paths:
            if p.exists():
                search_script = p
                break

    if search_script.exists():
        try:
            result = subprocess.run(
                [sys.executable, str(search_script), args.description,
                 "--design-system", "-p", args.project, "-f", "markdown"],
                capture_output=True, text=True, timeout=30,
                cwd=str(UI_UX_PRO_MAX)
            )
            if result.returncode == 0 and result.stdout.strip():
                print("[OK] ui-ux-pro-max 搜索成功")
                detailed_output = result.stdout
            else:
                print(f"[WARN] ui-ux-pro-max 搜索返回非零: {result.returncode}")
                detailed_output = None
        except Exception as e:
            print(f"[WARN] 无法调用 ui-ux-pro-max: {e}")
            detailed_output = None
    else:
        print(f"[WARN] 未找到 ui-ux-pro-max 搜索脚本 ({search_script})")
        detailed_output = None

    # Step 3: 生成 MASTER.md
    master_content = generate_master_md(args.project, domain, styles, args.description)

    # Step 4: 写入文件
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    master_path = output_dir / "MASTER.md"
    master_path.write_text(master_content, encoding="utf-8")
    print(f"[OK] MASTER.md → {master_path}")

    # 附加详细输出
    if detailed_output:
        detail_path = output_dir / "DESIGN_SYSTEM_DETAIL.md"
        detail_path.write_text(detailed_output, encoding="utf-8")
        print(f"[OK] DESIGN_SYSTEM_DETAIL.md → {detail_path}")

    print("\n=== 下一步 ===")
    print(f"1. 审查 {master_path}")
    print(f"2. 运行: python3 skills/ui-ux-pro-max/scripts/search.py \"{args.description}\" --domain color")
    print(f"3. 运行: python3 skills/ui-ux-pro-max/scripts/search.py \"{args.description}\" --domain typography")
    print(f"4. 进入 Phase 3: 代码生成")


if __name__ == "__main__":
    main()
