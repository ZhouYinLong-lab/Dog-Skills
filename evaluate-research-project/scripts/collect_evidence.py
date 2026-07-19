#!/usr/bin/env python3
"""Collect read-only evidence for a research repository evaluation."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def run_git(repo: Path, *args: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )
    return result.returncode == 0, result.stdout.strip()


def git_lines(repo: Path, *args: str) -> list[str]:
    ok, output = run_git(repo, *args)
    return output.splitlines() if ok and output else []


def redact_remote(url: str) -> str:
    return re.sub(r"(https?://)[^/@]+@", r"\1<redacted>@", url)


def existing(repo: Path, names: list[str]) -> list[str]:
    return [name for name in names if (repo / name).exists()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    args = parser.parse_args()

    requested = Path(args.repo).expanduser().resolve()
    ok, root_text = run_git(requested, "rev-parse", "--show-toplevel")
    if not ok:
        parser.error(f"not a Git repository: {requested}")
    root = Path(root_text).resolve()

    tracked = git_lines(root, "ls-files")
    status = git_lines(root, "status", "--porcelain=v1")
    py_files = [path for path in tracked if path.endswith(".py")]
    suffix_counts = Counter(Path(path).suffix.lower() or "<none>" for path in tracked)

    remotes: dict[str, str] = {}
    for line in git_lines(root, "remote", "-v"):
        parts = line.split()
        if len(parts) >= 2:
            remotes.setdefault(parts[0], redact_remote(parts[1]))

    contributor_lines = git_lines(root, "shortlog", "-sne", "--all")
    commit_dates = git_lines(root, "log", "--format=%aI", "--all")
    tracked_bytes = 0
    for relative in tracked:
        path = root / relative
        if path.is_file():
            try:
                tracked_bytes += path.stat().st_size
            except OSError:
                pass

    test_files = [
        path
        for path in tracked
        if re.search(r"(^|/)(tests?)(/|$)|(^|/)(test_[^/]+|[^/]+_test)\.py$", path.replace("\\", "/"))
    ]
    workflow_files = [path for path in tracked if path.startswith(".github/workflows/")]

    ok, branch = run_git(root, "branch", "--show-current")
    ok_head, head = run_git(root, "rev-parse", "HEAD")
    ok_upstream, upstream = run_git(root, "rev-parse", "--abbrev-ref", "@{upstream}")
    ok_count, commit_count = run_git(root, "rev-list", "--count", "HEAD")

    report: dict[str, Any] = {
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": {
            "root": str(root),
            "branch": branch if ok else None,
            "head": head if ok_head else None,
            "upstream": upstream if ok_upstream else None,
            "remotes": remotes,
            "dirty": bool(status),
            "status": status,
        },
        "history": {
            "commit_count": int(commit_count) if ok_count and commit_count.isdigit() else None,
            "contributor_identity_count": len(contributor_lines),
            "first_commit_date": commit_dates[-1] if commit_dates else None,
            "latest_commit_date": commit_dates[0] if commit_dates else None,
            "tags": git_lines(root, "tag", "--list"),
        },
        "inventory": {
            "tracked_file_count": len(tracked),
            "tracked_bytes": tracked_bytes,
            "python_file_count": len(py_files),
            "suffix_counts": dict(sorted(suffix_counts.items())),
            "tracked_data_files": sum(path.startswith("data/") for path in tracked),
            "tracked_output_files": sum(path.startswith("outputs/") for path in tracked),
            "test_files": test_files,
            "workflow_files": workflow_files,
        },
        "project_files": {
            "documentation": existing(
                root,
                ["README.md", "README.rst", "CHANGELOG.md", "docs", "reports"],
            ),
            "community": existing(
                root,
                [
                    "LICENSE",
                    "LICENSE.md",
                    "CONTRIBUTING.md",
                    "SECURITY.md",
                    "CODE_OF_CONDUCT.md",
                    ".github/ISSUE_TEMPLATE",
                    ".github/PULL_REQUEST_TEMPLATE.md",
                ],
            ),
            "packaging": existing(
                root,
                ["pyproject.toml", "setup.py", "setup.cfg", "package.json", "Cargo.toml", "go.mod"],
            ),
            "dependencies": existing(
                root,
                [
                    "requirements.txt",
                    "requirements-dev.txt",
                    "requirements-sam.txt",
                    "poetry.lock",
                    "uv.lock",
                    "Pipfile.lock",
                    "package-lock.json",
                    "pnpm-lock.yaml",
                ],
            ),
            "quality_config": existing(
                root,
                ["pytest.ini", "tox.ini", ".pre-commit-config.yaml", "ruff.toml", ".ruff.toml", "mypy.ini"],
            ),
        },
    }

    indent = 2 if args.pretty else None
    print(json.dumps(report, ensure_ascii=False, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
