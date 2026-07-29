#!/usr/bin/env python3
"""Collect read-only evidence for a research repository evaluation.

Detects project structure, test files, CI configs, packaging, and quality
tooling across Python, JavaScript/TypeScript, Go, Rust, Java, Ruby, C/C++,
and other ecosystems.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Multi-language detection patterns
# ---------------------------------------------------------------------------

# (pattern, is_regex) — regex patterns must match the full relative path
_TEST_PATTERNS: list[tuple[str, bool]] = [
    # Python
    (r"(^|/)(tests?)(/|$)", True),
    (r"(^|/)(test_[^/]+|[^/]+_test)\.py$", True),
    # JavaScript / TypeScript
    (r"(^|/)__(tests?)__(/|$)", True),
    (r"\.(test|spec)\.(ts|tsx|js|jsx|mjs|cjs)$", True),
    (r"(^|/)(test_[^/]+|[^/]+_test)\.(ts|tsx|js|jsx|mjs|cjs)$", True),
    # Go
    (r"(^|/)[^/]+_test\.go$", True),
    # Rust
    (r"(^|/)(tests?)(/|$)", True),  # also catches Rust integration tests/
    (r"(^|/)(test_[^/]+|[^/]+_test)\.rs$", True),
    # Java / Kotlin
    (r"(^|/)src/test(/|$)", True),
    (r"[A-Z][a-zA-Z0-9]*Tests?\.java$", True),
    (r"[A-Z][a-zA-Z0-9]*Tests?\.kt$", True),
    # Ruby
    (r"(^|/)(spec|test)(/|$)", True),
    (r"[^/]+_(spec|test)\.rb$", True),
    # C / C++
    (r"(^|/)(test_[^/]+|[^/]+_test)\.(c|cpp|cc|cxx|h|hpp)$", True),
    (r"(^|/)tests?(/|$)", True),  # generic tests/ dir (catches CTest, etc.)
    # PHP
    (r"(^|/)tests?(/|$)", True),
    (r"[^/]+Test\.php$", True),
    # Swift
    (r"(^|/)Tests?(/|$)", True),
    (r"[^/]+Tests?\.swift$", True),
    # C#
    (r"(^|/)Tests?(/|$)", True),
    (r"[^/]+Tests?\.cs$", True),
    # Dart
    (r"[^/]+_test\.dart$", True),
    # Zig
    (r"(^|/)test(/|$)", True),
    (r"[^/]+_test\.zig$", True),
]

_PACKAGING_FILES: list[str] = [
    # Python
    "pyproject.toml", "setup.py", "setup.cfg",
    # JavaScript / TypeScript
    "package.json",
    # Rust
    "Cargo.toml",
    # Go
    "go.mod",
    # Java / Kotlin
    "pom.xml", "build.gradle", "build.gradle.kts", "settings.gradle", "settings.gradle.kts",
    # C / C++
    "CMakeLists.txt", "Makefile", "meson.build", "BUILD", "WORKSPACE", "configure.ac",
    # .NET
    # (detected via suffix below)
    # Swift
    "Package.swift",
    # Dart / Flutter
    "pubspec.yaml",
    # PHP
    "composer.json",
    # Ruby
    "Gemfile", "*.gemspec",  # gemspec handled below
    # Julia
    "Project.toml",
    # Zig
    "build.zig",
    # Nix
    "flake.nix", "default.nix",
]

_PACKAGING_SUFFIXES: list[str] = [
    ".csproj", ".fsproj", ".vbproj", ".sln",
]

_DEPENDENCY_FILES: list[str] = [
    # Python
    "requirements.txt", "requirements-dev.txt", "requirements-sam.txt",
    "poetry.lock", "uv.lock", "Pipfile.lock",
    # JavaScript / TypeScript
    "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb",
    # Rust
    "Cargo.lock",
    # Go
    "go.sum",
    # Java
    "gradle.lockfile",
    # PHP
    "composer.lock",
    # Ruby
    "Gemfile.lock",
    # Dart
    "pubspec.lock",
    # Julia
    "Manifest.toml",
]

_CI_PATTERNS: list[str] = [
    ".github/workflows/",
    ".gitlab-ci.yml",
    "Jenkinsfile",
    ".circleci/config.yml",
    ".travis.yml",
    ".drone.yml",
    "azure-pipelines.yml",
    ".buildkite/",
    "bitbucket-pipelines.yml",
    ".woodpecker/",
]

_QUALITY_CONFIG_FILES: list[str] = [
    # Python
    "pytest.ini", "tox.ini", ".pre-commit-config.yaml", "ruff.toml", ".ruff.toml",
    "mypy.ini", ".flake8", ".pylintrc",
    # JavaScript / TypeScript
    ".eslintrc.js", ".eslintrc.cjs", ".eslintrc.yaml", ".eslintrc.yml", ".eslintrc.json",
    "eslint.config.js", "eslint.config.mjs", "eslint.config.ts", "eslint.config.mts",
    ".prettierrc", ".prettierrc.json", ".prettierrc.yaml", ".prettierrc.js",
    "prettier.config.js", ".prettierrc.toml",
    # General
    ".editorconfig",
    ".hadolint.yaml", ".hadolint.yml",
    ".markdownlint.json", ".markdownlint.yaml", ".markdownlint.yml",
    # Shell
    ".shellcheckrc",
    # Ruby
    ".rubocop.yml", ".rubocop_todo.yml",
    # Java
    "checkstyle.xml", "google_checks.xml",
    # Rust
    "rustfmt.toml", ".rustfmt.toml", "clippy.toml",
    # Go
    ".golangci.yml", ".golangci.yaml",
]

_DOCUMENTATION_FILES: list[str] = [
    "README.md", "README.rst", "README.txt", "README",
    "CHANGELOG.md", "CHANGELOG.rst", "CHANGES.md", "HISTORY.md",
    "CONTRIBUTING.md", "CONTRIBUTING.rst",
    "SECURITY.md", "SECURITY.rst",
    "CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.rst",
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.rst",
    "AUTHORS", "AUTHORS.md",
    "CITATION", "CITATION.cff",
    "docs", "doc",
]

_COMMUNITY_FILES: list[str] = [
    "LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE.rst",
    "CONTRIBUTING.md", "CONTRIBUTING.rst",
    "SECURITY.md", "SECURITY.rst",
    "CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.rst",
    ".github/ISSUE_TEMPLATE",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/FUNDING.yml",
    ".github/dependabot.yml",
    "AUTHORS", "AUTHORS.md",
]

_DATA_DIR_PREFIXES: tuple[str, ...] = ("data/", "datasets/", "dataset/", "assets/")
_OUTPUT_DIR_PREFIXES: tuple[str, ...] = (
    "outputs/", "output/", "results/", "logs/", "figures/",
    "checkpoints/", "models/", "weights/", "runs/", "artifacts/",
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_git(repo: Path, *args: str, timeout: int = 60) -> tuple[bool, str]:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        check=False,
    )
    return result.returncode == 0, result.stdout.strip()


def git_lines(repo: Path, *args: str, timeout: int = 60) -> list[str]:
    ok, output = run_git(repo, *args, timeout=timeout)
    return output.splitlines() if ok and output else []


def redact_remote(url: str) -> str:
    return re.sub(r"(https?://)[^/@]+@", r"\1<redacted>@", url)


def existing(repo: Path, names: list[str]) -> list[str]:
    return [name for name in names if (repo / name).exists()]


def existing_by_suffix(repo: Path, suffixes: list[str], tracked: list[str]) -> list[str]:
    """Find tracked files ending with any of the given suffixes."""
    return sorted({path for path in tracked if any(path.endswith(s) for s in suffixes)})


def match_test_patterns(repo: Path, tracked: list[str]) -> list[str]:
    """Detect test files using multi-language regex patterns."""
    matched: set[str] = set()
    for path in tracked:
        normalized = path.replace("\\", "/")
        for pattern, is_regex in _TEST_PATTERNS:
            if is_regex:
                if re.search(pattern, normalized):
                    matched.add(path)
                    break
    return sorted(matched)


def find_ci_files(repo: Path, tracked: list[str]) -> list[str]:
    """Find CI configuration files across providers."""
    found: list[str] = []
    for ci_pattern in _CI_PATTERNS:
        if ci_pattern.endswith("/"):
            found.extend(p for p in tracked if p.startswith(ci_pattern))
        elif ci_pattern in tracked or (repo / ci_pattern).exists():
            found.append(ci_pattern)
    return sorted(set(found))


def count_data_files(tracked: list[str]) -> int:
    return sum(
        1 for p in tracked
        if p.replace("\\", "/").startswith(_DATA_DIR_PREFIXES)
    )


def count_output_files(tracked: list[str]) -> int:
    return sum(
        1 for p in tracked
        if p.replace("\\", "/").startswith(_OUTPUT_DIR_PREFIXES)
    )


def detect_languages(tracked: list[str]) -> dict[str, int]:
    """Estimate language breakdown from file extensions."""
    lang_map = {
        ".py": "Python",
        ".ts": "TypeScript", ".tsx": "TypeScript",
        ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript",
        ".go": "Go",
        ".rs": "Rust",
        ".java": "Java",
        ".kt": "Kotlin", ".kts": "Kotlin",
        ".c": "C", ".h": "C",
        ".cpp": "C++", ".cc": "C++", ".cxx": "C++", ".hpp": "C++", ".hh": "C++",
        ".cs": "C#",
        ".rb": "Ruby",
        ".php": "PHP",
        ".swift": "Swift",
        ".dart": "Dart",
        ".zig": "Zig",
        ".jl": "Julia",
        ".r": "R", ".R": "R",
        ".scala": "Scala",
        ".ex": "Elixir", ".exs": "Elixir",
        ".hs": "Haskell",
        ".clj": "Clojure", ".cljs": "Clojure",
        ".lua": "Lua",
        ".sh": "Shell", ".bash": "Shell", ".zsh": "Shell",
        ".sql": "SQL",
        ".ipynb": "Jupyter Notebook",
        ".md": "Markdown", ".mdx": "Markdown",
        ".tex": "LaTeX",
        ".yaml": "YAML", ".yml": "YAML",
        ".json": "JSON",
        ".toml": "TOML",
        ".cfg": "Config", ".ini": "Config",
        ".dockerfile": "Docker", "Dockerfile": "Docker",
        ".cmake": "CMake", "CMakeLists.txt": "CMake",
    }
    counts: Counter[str] = Counter()
    for path in tracked:
        name = Path(path).name
        suffix = Path(path).suffix.lower()
        key = suffix if suffix else f"<{name}>"
        counts[lang_map.get(key, key)] += 1
    return dict(counts.most_common())


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="Repository path")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    parser.add_argument(
        "--timeout", type=int, default=60,
        help="Git command timeout in seconds (default: 60)",
    )
    args = parser.parse_args()

    requested = Path(args.repo).expanduser().resolve()
    ok, root_text = run_git(requested, "rev-parse", "--show-toplevel", timeout=args.timeout)
    if not ok:
        parser.error(f"not a Git repository: {requested}")
    root = Path(root_text).resolve()

    tracked = git_lines(root, "ls-files", timeout=args.timeout)
    status = git_lines(root, "status", "--porcelain=v1", timeout=args.timeout)
    suffix_counts = Counter(Path(path).suffix.lower() or "<none>" for path in tracked)

    remotes: dict[str, str] = {}
    for line in git_lines(root, "remote", "-v", timeout=args.timeout):
        parts = line.split()
        if len(parts) >= 2:
            remotes.setdefault(parts[0], redact_remote(parts[1]))

    contributor_lines = git_lines(root, "shortlog", "-sne", "--all", timeout=args.timeout)
    commit_dates = git_lines(root, "log", "--format=%aI", "--all", timeout=120)
    tracked_bytes = 0
    for relative in tracked:
        path = root / relative
        if path.is_file():
            try:
                tracked_bytes += path.stat().st_size
            except OSError:
                pass

    test_files = match_test_patterns(root, tracked)
    ci_files = find_ci_files(root, tracked)

    ok_branch, branch = run_git(root, "branch", "--show-current", timeout=args.timeout)
    ok_head, head = run_git(root, "rev-parse", "HEAD", timeout=args.timeout)
    ok_upstream, upstream = run_git(root, "rev-parse", "--abbrev-ref", "@{upstream}", timeout=args.timeout)
    ok_count, commit_count = run_git(root, "rev-list", "--count", "HEAD", timeout=args.timeout)

    # Gather packaging files: explicit names + suffix matches
    packaging_named = existing(root, _PACKAGING_FILES)
    packaging_suffix = existing_by_suffix(root, _PACKAGING_SUFFIXES, tracked)

    languages = detect_languages(tracked)

    report: dict[str, Any] = {
        "observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository": {
            "root": str(root),
            "branch": branch if ok_branch else None,
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
            "tags": git_lines(root, "tag", "--list", timeout=args.timeout),
        },
        "inventory": {
            "tracked_file_count": len(tracked),
            "tracked_bytes": tracked_bytes,
            "suffix_counts": dict(sorted(suffix_counts.items())),
            "language_breakdown": languages,
            "tracked_data_files": count_data_files(tracked),
            "tracked_output_files": count_output_files(tracked),
            "test_files": test_files,
            "ci_files": ci_files,
        },
        "project_files": {
            "documentation": existing(root, _DOCUMENTATION_FILES),
            "community": existing(root, _COMMUNITY_FILES),
            "packaging": sorted(set(packaging_named + packaging_suffix)),
            "dependencies": existing(root, _DEPENDENCY_FILES),
            "quality_config": existing(root, _QUALITY_CONFIG_FILES),
        },
    }

    indent = 2 if args.pretty else None
    print(json.dumps(report, ensure_ascii=False, indent=indent, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
