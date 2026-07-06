from __future__ import annotations

import argparse
import mimetypes
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

ILLEGAL_FILENAME_CHARS = r'\/:*?"<>|'
WECHAT_HOSTS = {"mp.weixin.qq.com"}
IMAGE_ATTRS = ("data-src", "src", "data-backsrc", "data-original")


class Wx2MdError(Exception):
    """Expected export failure with a user-readable message."""


@dataclass
class Article:
    url: str
    title: str
    author: str
    created: str
    content: Any
    warnings: list[str] = field(default_factory=list)


@dataclass
class ExportResult:
    url: str
    output_dir: Path
    markdown_path: Path
    image_count: int
    warnings: list[str]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="wx2md",
        description="Export WeChat Official Account articles to local Markdown.",
    )
    parser.add_argument("input", help="WeChat article URL or text file containing URLs.")
    parser.add_argument("--output", default="./output/articles", help="Article collection directory. Default: ./output/articles")
    parser.add_argument("--no-images", action="store_true", help="Keep remote image URLs and skip local downloads.")
    parser.add_argument(
        "--format",
        choices=("standard", "obsidian"),
        default="standard",
        help="Markdown layout flavor. Default: standard",
    )
    parser.add_argument("--title", help="Override article title. Only valid for single URL input.")
    parser.add_argument("--headful", action="store_true", help="Run Chromium with a visible browser window.")
    parser.add_argument("--timeout", type=int, default=30000, help="Page timeout in milliseconds. Default: 30000")
    parser.add_argument("--save-html", action="store_true", help="Also save the processed article HTML.")
    return parser.parse_args(argv)


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def is_wechat_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and parsed.netloc.lower() in WECHAT_HOSTS


def read_inputs(value: str) -> list[str]:
    if is_url(value):
        return [value]

    path = Path(value)
    if not path.exists():
        raise Wx2MdError(f"Input is neither a URL nor an existing file: {value}")

    urls: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        item = line.strip()
        if not item or item.startswith("#"):
            continue
        if not is_url(item):
            raise Wx2MdError(f"Invalid URL in {path}: {item}")
        urls.append(item)

    if not urls:
        raise Wx2MdError(f"No URLs found in file: {path}")
    return urls


def sanitize_filename(title: str, max_length: int = 80) -> str:
    cleaned = title.strip()
    for char in ILLEGAL_FILENAME_CHARS:
        cleaned = cleaned.replace(char, "")
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
    if not cleaned:
        cleaned = "untitled"
    return cleaned[:max_length].rstrip(" .") or "untitled"


def unique_dir(root: Path, title: str) -> Path:
    base = sanitize_filename(title)
    candidate = root / base
    if not candidate.exists():
        return candidate

    index = 2
    while True:
        suffix = f"-{index}"
        truncated = base[: max(1, 80 - len(suffix))].rstrip(" .")
        candidate = root / f"{truncated}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def clean_text(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def first_text(soup: BeautifulSoup, selector: str) -> str:
    node = soup.select_one(selector)
    return clean_text(node.get_text(" ", strip=True) if node else "")


def meta_content(soup: BeautifulSoup, *names: str) -> str:
    for name in names:
        node = soup.find("meta", attrs={"property": name}) or soup.find("meta", attrs={"name": name})
        if node and node.get("content"):
            return clean_text(str(node["content"]))
    return ""


def fetch_html(url: str, timeout: int, headful: bool) -> str:
    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
        from playwright.sync_api import sync_playwright
    except ModuleNotFoundError as exc:
        raise Wx2MdError("Missing dependency: install requirements and run `playwright install chromium`.") from exc

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=not headful)
            context = browser.new_context(
                user_agent=USER_AGENT,
                locale="zh-CN",
                viewport={"width": 1280, "height": 900},
            )
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=timeout)
            try:
                page.wait_for_selector("#js_content", timeout=min(timeout, 12000))
            except PlaywrightTimeoutError:
                pass
            page.wait_for_timeout(800)
            html = page.content()
            context.close()
            browser.close()
            return html
    except PlaywrightError as exc:
        raise Wx2MdError(f"Failed to open page with Playwright: {exc}") from exc


def normalize_article(url: str, html: str, title_override: str | None = None) -> Article:
    try:
        from bs4 import BeautifulSoup
    except ModuleNotFoundError as exc:
        raise Wx2MdError("Missing dependency: install requirements.txt before exporting articles.") from exc

    soup = BeautifulSoup(html, "lxml")
    content = soup.select_one("#js_content")
    if not content:
        raise Wx2MdError("Article body #js_content was not found. The page may require verification or be unavailable.")

    title = clean_text(title_override) or first_text(soup, "#activity-name")
    title = title or meta_content(soup, "og:title", "twitter:title")
    title = title or clean_text(soup.title.get_text(" ", strip=True) if soup.title else "")
    if not title:
        title = "untitled"

    author = first_text(soup, "#js_name")
    author = author or meta_content(soup, "og:site_name", "author")
    created = first_text(soup, "#publish_time")

    for unwanted in content.select("script, style, iframe"):
        unwanted.decompose()

    warnings: list[str] = []
    for image in content.find_all("img"):
        src = image_source(image)
        if src:
            image["src"] = urljoin(url, src)
        else:
            image.decompose()
            warnings.append("Removed an image without data-src/src/data-backsrc.")

    for video in content.find_all("video"):
        poster = video.get("poster")
        if poster:
            video["poster"] = urljoin(url, str(poster).strip())

    return Article(url=url, title=title, author=author, created=created, content=content, warnings=warnings)


def image_source(image: Any) -> str:
    for attr in IMAGE_ATTRS:
        value = image.get(attr)
        if value:
            return str(value).strip()
    return ""


def extension_from_response(url: str, response: httpx.Response) -> str:
    content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()
    guessed = mimetypes.guess_extension(content_type)
    if guessed:
        if guessed == ".jpe":
            return ".jpg"
        return guessed

    path_suffix = Path(urlparse(url).path).suffix.lower()
    if path_suffix in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}:
        return path_suffix
    return ".jpg"


def localize_images(article: Article, article_dir: Path, fmt: str, no_images: bool) -> int:
    try:
        import httpx
    except ModuleNotFoundError as exc:
        raise Wx2MdError("Missing dependency: install requirements.txt before downloading images.") from exc

    image_folder_name = "attachments" if fmt == "obsidian" else "images"
    image_dir = article_dir / image_folder_name
    image_targets = collect_image_targets(article.content)
    if no_images or not image_targets:
        return 0

    image_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    headers = {"User-Agent": USER_AGENT, "Referer": article.url}
    with httpx.Client(headers=headers, follow_redirects=True, timeout=30.0) as client:
        for node, attr in image_targets:
            remote_url = str(node.get(attr) or "")
            if not remote_url:
                continue
            try:
                response = client.get(remote_url)
                response.raise_for_status()
                ext = extension_from_response(remote_url, response)
                count += 1
                filename = f"{count:03d}{ext}"
                target = image_dir / filename
                target.write_bytes(response.content)
                node[attr] = f"./{image_folder_name}/{filename}"
            except Exception as exc:  # noqa: BLE001 - keep export going for partial image failures.
                article.warnings.append(f"Image download failed: {remote_url} ({exc})")
                node[attr] = remote_url
    return count


def collect_image_targets(content: Any) -> list[tuple[Any, str]]:
    targets: list[tuple[Any, str]] = []
    for image in content.find_all("img"):
        if image.get("src"):
            targets.append((image, "src"))
    for video in content.find_all("video"):
        if video.get("poster"):
            targets.append((video, "poster"))
    return targets


def yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def front_matter(article: Article, fmt: str) -> str:
    exported_at = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        "---",
        f"title: {yaml_string(article.title)}",
        f"author: {yaml_string(article.author)}",
        'source: "WeChat Official Account"',
        f"url: {yaml_string(article.url)}",
        f"created: {yaml_string(article.created)}",
        f"exported_at: {yaml_string(exported_at)}",
    ]
    if fmt == "obsidian":
        lines.extend(["tags:", "  - wechat", "  - article"])
    lines.append("---")
    return "\n".join(lines)


def article_to_markdown(article: Article, fmt: str) -> str:
    try:
        from markdownify import markdownify as html_to_markdown
    except ModuleNotFoundError as exc:
        raise Wx2MdError("Missing dependency: install requirements.txt before converting Markdown.") from exc

    markdown = html_to_markdown(
        str(article.content),
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()
    return f"{front_matter(article, fmt)}\n\n# {article.title}\n\n{markdown}\n"


def save_article(article: Article, output_root: Path, fmt: str, no_images: bool, save_html: bool) -> ExportResult:
    article_dir = unique_dir(output_root, article.title)
    article_dir.mkdir(parents=True, exist_ok=False)
    image_count = localize_images(article, article_dir, fmt, no_images)
    markdown = article_to_markdown(article, fmt)
    if image_count:
        image_count = remove_unreferenced_images(article_dir, markdown, fmt)
    markdown_path = article_dir / "index.md"
    markdown_path.write_text(markdown, encoding="utf-8")
    if save_html:
        (article_dir / "article.html").write_text(str(article.content), encoding="utf-8")
    return ExportResult(
        url=article.url,
        output_dir=article_dir,
        markdown_path=markdown_path,
        image_count=image_count,
        warnings=article.warnings,
    )


def remove_unreferenced_images(article_dir: Path, markdown: str, fmt: str) -> int:
    image_folder_name = "attachments" if fmt == "obsidian" else "images"
    image_dir = article_dir / image_folder_name
    if not image_dir.exists():
        return 0

    referenced = set(re.findall(rf"\./{re.escape(image_folder_name)}/([^)\s]+)", markdown))
    kept = 0
    for image_file in image_dir.iterdir():
        if not image_file.is_file():
            continue
        if image_file.name in referenced:
            kept += 1
        else:
            image_file.unlink()
    return kept


def export_one(url: str, args: argparse.Namespace, title_override: str | None = None) -> ExportResult:
    if not is_wechat_url(url):
        raise Wx2MdError(f"Only mp.weixin.qq.com article URLs are supported: {url}")

    html = fetch_html(url, timeout=args.timeout, headful=args.headful)
    article = normalize_article(url, html, title_override=title_override)
    return save_article(
        article=article,
        output_root=Path(args.output),
        fmt=args.format,
        no_images=args.no_images,
        save_html=args.save_html,
    )


def print_result(result: ExportResult) -> None:
    print(f"[OK] {result.url}")
    print(f"     Markdown: {result.markdown_path}")
    print(f"     Images: {result.image_count}")
    for warning in result.warnings:
        print(f"     Warning: {warning}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        urls = read_inputs(args.input)
        if args.title and len(urls) > 1:
            raise Wx2MdError("--title can only be used with a single URL input.")

        failures = 0
        for url in urls:
            try:
                result = export_one(url, args, title_override=args.title)
                print_result(result)
            except Wx2MdError as exc:
                failures += 1
                print(f"[ERROR] {url}: {exc}", file=sys.stderr)
            except KeyboardInterrupt:
                raise
            except Exception as exc:  # noqa: BLE001 - CLI should fail clearly, not with a traceback.
                failures += 1
                print(f"[ERROR] {url}: unexpected failure: {exc}", file=sys.stderr)

        return 1 if failures else 0
    except Wx2MdError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
