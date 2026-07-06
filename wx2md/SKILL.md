---
name: wx2md
description: Export WeChat Official Account article links from mp.weixin.qq.com to local Markdown with front matter and localized images. Use when the user wants a CLI/script or workflow for saving WeChat public account articles as Markdown for personal learning, archive, AI input, Obsidian notes, or knowledge management. Supports Playwright-based page loading, WeChat DOM extraction, image downloading, Markdown conversion, batch URL files, and validation of export output.
---

# WX2MD

Use this skill to fetch a WeChat Official Account article and export it as a local Markdown note with metadata and images.

## Tool

The bundled CLI lives in this skill folder:

```powershell
cd wx2md
pip install -r requirements.txt
playwright install chromium
pip install -e .
wx2md "https://mp.weixin.qq.com/s/xxxx"
```

Direct script mode also works:

```powershell
cd wx2md
python src/main.py "https://mp.weixin.qq.com/s/xxxx" --output ./output/articles
```

## Workflow

1. Validate the input is either a WeChat article URL or a text file containing URLs.
2. Use Playwright Chromium to load the page because WeChat pages often need browser DOM execution.
3. Extract metadata with WeChat selectors:
   - `#activity-name` for title
   - `#js_name` for account/author
   - `#publish_time` for publish time
   - `#js_content` for article body
4. Normalize image URLs using `data-src`, then `src`, then `data-backsrc`.
5. Download images with `User-Agent` and `Referer` headers unless `--no-images` is set.
6. Replace image URLs with local relative paths.
7. Convert the article body HTML to Markdown.
8. Write `index.md` under `output/articles/<sanitized title>/`.

## Commands

```powershell
wx2md "https://mp.weixin.qq.com/s/xxxx"
wx2md "https://mp.weixin.qq.com/s/xxxx" --output ./output/articles
wx2md "https://mp.weixin.qq.com/s/xxxx" --no-images
wx2md "https://mp.weixin.qq.com/s/xxxx" --format obsidian
wx2md "https://mp.weixin.qq.com/s/xxxx" --title "custom title"
wx2md urls.txt --output ./output/articles
```

## Output

Default output:

```text
output/
  articles/
    Article Title/
      index.md
      images/
        001.jpg
        002.png
```

Obsidian output uses `attachments/` for images and adds simple front matter tags.

## Verification

After export, check:

- `index.md` exists.
- Front matter includes title, author, source, URL, created, and exported_at.
- Local image files exist unless `--no-images` was used.
- Markdown image links are relative and render from `index.md`.
- The body contains the article's major headings, paragraphs, quotes, and images.

## Limits

This tool does not bypass login, CAPTCHA, region restrictions, deleted content, paywalls, or anti-abuse controls. If the browser cannot load the article or `#js_content` is empty, report a clear error and preserve the original link for manual handling.

Use only for personal learning, backup, and knowledge management. Preserve original source and URL.
