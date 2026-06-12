#!/usr/bin/env python3
"""Markdown 格式自检工具。

检查项：
- 标题层级是否正确（不跳级）
- $ 和 $$ 是否成对闭合
- $$ 是否单独占行
- 是否误用 \\(...\\) 或 \\[...\\]
- 独立公式前后是否有空行
- 图片链接是否有效
- 是否包含必需章节
"""

import re
import sys
import os
from pathlib import Path


def check_headings(lines):
    """检查标题层级，返回问题列表。"""
    issues = []
    prev_level = 0
    heading_pattern = re.compile(r'^(#{1,6})\s')

    for i, line in enumerate(lines, 1):
        m = heading_pattern.match(line)
        if m:
            level = len(m.group(1))
            if level > prev_level + 1 and prev_level > 0:
                issues.append(
                    f"行 {i}：标题从 H{prev_level} 跳到 H{level}，缺少中间层级"
                )
            prev_level = level

    return issues


def check_dollar_pairs(lines):
    """检查 $ 和 $$ 是否成对。"""
    issues = []
    text = '\n'.join(lines)

    # Count $$ blocks (ignore $ inside $$)
    # Simple approach: check if $$ count is even
    dd_count = text.count('$$')
    if dd_count % 2 != 0:
        issues.append(f"$$ 数量为 {dd_count}（奇数），存在未闭合的公式块")

    # Check inline $ (excluding $$)
    # Replace $$ with placeholder, then count $
    text_no_dd = text.replace('$$', '')
    dollar_count = text_no_dd.count('$')
    if dollar_count % 2 != 0:
        # Find line numbers of unmatched $
        lines_with_dollar = []
        in_dd = False
        for i, line in enumerate(lines, 1):
            if '$$' in line:
                in_dd = not in_dd
                continue
            if in_dd:
                continue
            if line.count('$') % 2 != 0:
                lines_with_dollar.append(str(i))
        if lines_with_dollar:
            issues.append(
                f"行内 $ 不匹配，问题行：{', '.join(lines_with_dollar[:10])}"
            )

    return issues


def check_dd_standalone(lines):
    """检查 $$ 是否单独占行。"""
    issues = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('$$') and len(stripped) > 2:
            # $$ has content after it on same line
            if not (stripped == '$$' or stripped.startswith('$$ ')):
                issues.append(f"行 {i}：$$ 不单独占行（行内容：{stripped[:60]}）")

    return issues


def check_forbidden_delimiters(lines):
    """检查是否使用了 \\(...\\) 或 \\[...\\]。"""
    issues = []
    for i, line in enumerate(lines, 1):
        if '\\(' in line or '\\)' in line:
            issues.append(f"行 {i}：使用了禁止的 \\(...\\) 格式，应改为 $...$")
        if '\\[' in line or '\\]' in line:
            issues.append(f"行 {i}：使用了禁止的 \\[...\\] 格式，应改为 $$...$$")

    return issues


def check_display_math_blank_lines(lines):
    """检查独立公式（$$）前后是否有空行。"""
    issues = []
    for i in range(1, len(lines) - 1):
        stripped = lines[i].strip()
        if stripped == '$$':
            # Check line before (should be blank or start of file)
            if i > 0 and lines[i - 1].strip() != '':
                issues.append(f"行 {i + 1}：$$ 前缺少空行")
            # Check line after
            if i < len(lines) - 1 and lines[i + 1].strip() != '' and lines[i + 1].strip() != '$$':
                # Next line might be formula content, which is fine
                # The closing $$ check is more important
                pass

    # Check closing $$ has blank line after
    in_display = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '$$':
            if not in_display:
                in_display = True
            else:
                in_display = False
                if i < len(lines) - 1 and lines[i + 1].strip() != '':
                    # Check if next non-empty line is another $$ or a heading
                    next_line = lines[i + 1].strip()
                    if not next_line.startswith('$$') and not next_line.startswith('#'):
                        issues.append(f"行 {i + 1}：结束 $$ 后缺少空行")

    return issues


def check_image_links(lines, base_dir):
    """检查图片链接是否存在。"""
    issues = []
    image_pattern = re.compile(r'!\[.*?\]\((.*?\.(?:png|jpg|jpeg|gif|svg))\)')

    for i, line in enumerate(lines, 1):
        for m in image_pattern.finditer(line):
            img_path = m.group(1)
            # Handle relative paths
            abs_path = os.path.join(base_dir, img_path)
            abs_path = os.path.normpath(abs_path)
            if not os.path.exists(abs_path):
                issues.append(f"行 {i}：图片链接无效 — {img_path}")

    return issues


def check_required_sections(lines):
    """检查是否包含必需章节。"""
    text = '\n'.join(lines)
    required = [
        (r'##\s+0\.\s*本章考试相关性总结', '0. 本章考试相关性总结'),
        (r'##\s+1\.\s*本章知识结构', '1. 本章知识结构'),
        (r'##\s+2\.\s*核心知识点', '2. 核心知识点'),
        (r'##\s+3\.\s*典型题型总结', '3. 典型题型总结'),
        (r'##\s+4\.\s*本章复习清单', '4. 本章复习清单'),
    ]

    issues = []
    for pattern, name in required:
        if not re.search(pattern, text):
            issues.append(f"缺少必需章节：{name}")

    return issues


def check_markdown(filepath):
    """对单个 Markdown 文件执行所有检查。"""
    if not os.path.exists(filepath):
        print(f"[ERROR] 文件不存在：{filepath}")
        return 1

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    base_dir = os.path.dirname(os.path.abspath(filepath))

    all_issues = []
    all_issues.extend(check_headings(lines))
    all_issues.extend(check_dollar_pairs(lines))
    all_issues.extend(check_dd_standalone(lines))
    all_issues.extend(check_forbidden_delimiters(lines))
    all_issues.extend(check_display_math_blank_lines(lines))
    all_issues.extend(check_image_links(lines, base_dir))
    all_issues.extend(check_required_sections(lines))

    print(f"文件：{filepath}")
    print(f"总行数：{len(lines)}")
    print(f"检查项目：7")
    print(f"发现问题：{len(all_issues)}")
    print()

    if all_issues:
        print("--- 问题列表 ---")
        for issue in all_issues:
            print(f"  ✗ {issue}")
        print()
        print(f"[FAIL] 发现 {len(all_issues)} 个问题，需要修复。")
        return 1
    else:
        print("[PASS] 所有检查通过。")
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法：python check_md.py <markdown_file> [markdown_file...]")
        sys.exit(1)

    exit_code = 0
    for filepath in sys.argv[1:]:
        result = check_markdown(filepath)
        exit_code = max(exit_code, result)
        if len(sys.argv) > 2:
            print()

    sys.exit(exit_code)
