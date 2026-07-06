# Open Source Notes

This tool intentionally builds on mature open-source libraries:

- Playwright: browser automation for pages that need DOM execution.
- BeautifulSoup and lxml: HTML parsing.
- markdownify: HTML to Markdown conversion.
- httpx: image downloads with headers and timeouts.

Relevant prior art:

- `jackwener/wechat-article-to-markdown` provides a similar WeChat article export workflow with metadata extraction, Markdown conversion, and local image rewriting.

This implementation keeps the local CLI small, readable, and easy to extend. It does not copy upstream project code.
