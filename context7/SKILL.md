---
name: context7
description: >
  Real-time API documentation lookup via Context7 — query up-to-date docs for any library/framework
  directly in the context window. No more stale training data or hallucinated APIs.
  Trigger keywords: API docs, documentation, library docs, 查文档, 最新API, context7, look up docs,
  fetch documentation, 查库文档, up-to-date API, 实时文档.
metadata:
  category: tools
---

# Context7 — Real-Time Documentation Lookup

Retrieve current documentation for software libraries, frameworks, and components via the Context7 API. Use instead of relying on potentially outdated training data.

## Workflow

### Step 1: Search for the Library

```bash
curl -s "https://context7.com/api/v2/libs/search?libraryName=LIBRARY_NAME&query=TOPIC" | jq '.results[0]'
```

**Parameters:**
- `libraryName` (required): e.g. "react", "nextjs", "fastapi", "axios"
- `query` (required): topic description for relevance ranking

**Response:** `id` (library identifier), `title`, `description`, `totalSnippets`

### Step 2: Fetch Documentation

```bash
curl -s "https://context7.com/api/v2/context?libraryId=LIBRARY_ID&query=TOPIC&type=txt"
```

- Use `type=txt` for readable plain-text output
- No API key required (rate-limited for basic usage)
- Be specific with `query` to improve relevance

## Examples

```bash
# React hooks
curl -s "https://context7.com/api/v2/libs/search?libraryName=react&query=hooks" | jq '.results[0].id'
curl -s "https://context7.com/api/v2/context?libraryId=/websites/react_dev_reference&query=useState&type=txt"

# Next.js routing
curl -s "https://context7.com/api/v2/context?libraryId=/vercel/next.js&query=app+router&type=txt"

# FastAPI
curl -s "https://context7.com/api/v2/context?libraryId=/fastapi/fastapi&query=dependency+injection&type=txt"
```

## Tips

- `type=txt` gives more readable output than JSON
- URL-encode spaces in queries (use `+` or `%20`)
- Check additional results if the first isn't correct
- No API key needed for basic usage
