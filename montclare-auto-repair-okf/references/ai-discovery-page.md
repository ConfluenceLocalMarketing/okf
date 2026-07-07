---
type: APIs
title: AI Discovery Page - Montclare Auto Repair
description: Machine-readable knowledge base and semantic data endpoints for Montclare Auto Repair, providing AI agents structured access to business info, prompts, testimonials, and site content via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/montclare-auto-repair/.well-known/ai-manifest.json
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
timestamp: 2026-07-02
---

# AI Discovery Page - Montclare Auto Repair

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai).

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/montclare-auto-repair/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/robots.txt` | 0.5 | Monthly |
| `/sitemap-inventory.xml` | 0.8 | Daily |
| 10+ individual prompt endpoints | 0.8 | Weekly |

## AI Manifest (`/.well-known/ai-manifest.json`)

- **Schema types:** `LocalBusiness`, `ItemList`, `Review / AggregateRating`, `Offer`, `CreativeWork`

### Registered Endpoints

- `/api/v1/montclare-auto-repair/llms.txt` - LLMs.txt directive
- `/api/v1/montclare-auto-repair/business` - Business profile (JSON-LD)
- `/api/v1/montclare-auto-repair/prompts` - Q&A / FAQ prompts
- `/api/v1/montclare-auto-repair/testimonials` - Customer reviews
- `/api/v1/montclare-auto-repair/sitemap.xml` - Full sitemap
- `/api/v1/montclare-auto-repair/robots.txt` - Robots rules
- `/api/v1/montclare-auto-repair/config.json` - System configuration

### Additional PromptGraph Endpoints

- `/gbp-context` - Flattened Google Business Profile data
- `/site-content` - Clean, plain-text mirror of the entire site

## Business Profile

- **Name:** Montclare Auto Repair (Montclare Automotive Corp.)
- **Phone:** (773) 237-2672
- **Address:** 6902 W. Diversey Ave., Chicago, IL 60707
- **Website:** http://www.montclareautorepair.com/
- **Established:** February 2024

## Q&A Prompt Library

The `/prompts` endpoint exposes 10+ structured Q&A pairs. See [prompts.md](montclare-auto-repair-okf/references/prompts.md) for the full library.

See [llms-txt.md](montclare-auto-repair-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](montclare-auto-repair-okf/references/prompts.md) for the complete Q&A prompt library.
