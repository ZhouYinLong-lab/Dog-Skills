# WX2MD

Export WeChat Official Account article links (`mp.weixin.qq.com`) to local Markdown with front matter and downloaded images.

This project intentionally reuses mature open-source building blocks instead of hand-rolling a browser or Markdown converter:

- Playwright for browser automation.
- BeautifulSoup/lxml for HTML parsing.
- markdownify for HTML to Markdown conversion.
- httpx for image downloading.

The implementation is also inspired by the open-source `jackwener/wechat-article-to-markdown` project, while keeping this repository's CLI small and easy to modify.

## Install

Python 3.9+ is recommended.

```bash
cd wx2md
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
pip install -e .
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pip install -e .
```

If you do not want to install the console command, use:

```bash
python src/main.py "https://mp.weixin.qq.com/s/xxxx"
```

## Usage

```bash
wx2md "https://mp.weixin.qq.com/s/xxxx"
wx2md "https://mp.weixin.qq.com/s/xxxx" --output ./output/articles
wx2md "https://mp.weixin.qq.com/s/xxxx" --no-images
wx2md "https://mp.weixin.qq.com/s/xxxx" --format obsidian
wx2md "https://mp.weixin.qq.com/s/xxxx" --title "Custom Title"
wx2md urls.txt --output ./output/articles
```

`urls.txt` should contain one article URL per line. Empty lines and lines beginning with `#` are ignored.

## Output

Default:

```text
output/
  articles/
    Article Title/
      index.md
      images/
        001.jpg
        002.png
```

Obsidian mode:

```text
output/
  articles/
    Article Title/
      index.md
      attachments/
        001.jpg
        002.png
```

Markdown front matter:

```yaml
---
title: "Article Title"
author: "Account Name"
source: "WeChat Official Account"
url: "https://mp.weixin.qq.com/s/xxxx"
created: "2026-01-01"
exported_at: "2026-07-06T12:00:00+08:00"
---
```

## How It Works

1. Open the URL with Playwright Chromium.
2. Wait for the WeChat article body.
3. Extract:
   - `#activity-name` for title
   - `#js_name` for account name
   - `#publish_time` for publish time
   - `#js_content` for article body
4. Normalize image URLs from `data-src`, `src`, or `data-backsrc`.
5. Download images with `User-Agent` and `Referer` headers.
6. Replace remote image URLs with local relative paths.
7. Convert article HTML to Markdown and write `index.md`.

## Common Issues

### `playwright install chromium` was not run

Install the Chromium browser binary:

```bash
playwright install chromium
```

### Page opens but no body is extracted

The article may be deleted, blocked, require verification, require login, or use a page variant that does not expose `#js_content`.

### Images fail to download

Some WeChat image URLs expire or reject requests. The tool keeps the original remote URL in Markdown when a specific image cannot be downloaded.

### Duplicate article title

The exporter appends `-2`, `-3`, etc. to avoid overwriting an existing folder.

### Filename contains illegal characters

The exporter removes Windows/macOS/Linux-problematic filename characters:

```text
/ \ : * ? " < > |
```

Long titles are truncated to 80 characters.

## WeChat Page Limits

This tool does not bypass login, CAPTCHA, paywalls, anti-abuse checks, deleted content, or regional restrictions. It is intended for personal learning, backup, and knowledge management. Keep the original URL and source attribution in exported notes.

## Development

Run a syntax check:

```bash
python -m compileall src
```

Run a dry extraction against a real article:

```bash
wx2md "https://mp.weixin.qq.com/s/xxxx" --output ./output/articles --headful
```

`--headful` is useful when WeChat shows a verification or browser warning page.
