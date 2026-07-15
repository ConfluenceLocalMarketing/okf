---
type: APIs
title: Texan Title — AI Discovery Page
description: PromptGraph AI manifest and API endpoints for Texan Title including prompts, testimonials, business profile, and site content.
resource: https://api.promptgraph.ai/api/v1/texan-title/.well-known/ai-manifest.json
tags:
  - ai-discovery
  - promptgraph
  - api
  - json-ld
timestamp: 2026-07-15
---

# Texan Title — AI Discovery Page

## PromptGraph Integration

Texan Title is onboarded with PromptGraph (slug: `texan-title`) providing structured AI-discoverable data.

### AI Manifest

- **Well-Known:** https://api.promptgraph.ai/api/v1/texan-title/.well-known/ai-manifest.json
- **Version:** 1.0
- **Last Updated:** 2026-07-15

### Available Endpoints

| Endpoint | URL | Status |
|----------|-----|--------|
| Prompts | https://api.promptgraph.ai/api/v1/texan-title/prompts | Active (20 prompts) |
| AI Manifest | https://api.promptgraph.ai/api/v1/texan-title/.well-known/ai-manifest.json | Active |
| Sitemap | https://api.promptgraph.ai/api/v1/texan-title/sitemap.xml | Active |
| Robots | https://api.promptgraph.ai/api/v1/texan-title/robots.txt | Active |
| Business | https://api.promptgraph.ai/api/v1/texan-title/business | 404 (not populated) |
| Testimonials | https://api.promptgraph.ai/api/v1/texan-title/testimonials | Empty array |
| LLMs.txt | https://api.promptgraph.ai/api/v1/texan-title/llms.txt | Active |
| GBP Context | https://api.promptgraph.ai/api/v1/texan-title/gbp-context | Available |
| Site Content | https://api.promptgraph.ai/api/v1/texan-title/site-content | Active (46 pages, content empty) |
| Config | https://api.promptgraph.ai/api/v1/texan-title/config.json | Available |

### Schema Types

- LocalBusiness
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

### PromptGraph Prompts (20 items)

The prompts endpoint contains 20 location-specific prompts covering title company discovery, closing cost calculators, 1031 exchanges, lien searches, earnest money, FSBO transactions, and more across Texan Title's service areas.

See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/references/prompts.md) for the full prompt library.
