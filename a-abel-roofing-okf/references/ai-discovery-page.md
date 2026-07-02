---
type: APIs
title: AI Discovery Page - A-Abel Roofing
description: Machine-readable knowledge base and semantic data endpoints for A-Abel Roofing, providing AI agents structured access to business info, prompts, testimonials, and site content via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/a-abel-roofing/.well-known/ai-manifest.json
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

# AI Discovery Page - A-Abel Roofing

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, and LLM-friendly action definitions.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/a-abel-roofing/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/robots.txt` | 0.5 | Monthly |
| `/config.json` | 0.3 | Monthly |
| `/sitemap-inventory.xml` | 0.8 | Daily |
| 10+ individual prompt endpoints | 0.8 | Weekly |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-02T15:28:42.862Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`

### Registered Endpoints

- `/api/v1/a-abel-roofing/llms.txt` - LLMs.txt directive
- `/api/v1/a-abel-roofing/business` - Business profile (JSON-LD)
- `/api/v1/a-abel-roofing/prompts` - Q&A / FAQ prompts
- `/api/v1/a-abel-roofing/testimonials` - Customer reviews
- `/api/v1/a-abel-roofing/sitemap.xml` - Full sitemap
- `/api/v1/a-abel-roofing/robots.txt` - Robots rules
- `/api/v1/a-abel-roofing/config.json` - System configuration

### Additional PromptGraph Endpoints

- `/gbp-context` - Flattened Google Business Profile data for LLM ingestion
- `/site-content` - Clean, plain-text mirror of the entire site
- `/llms.txt` - LLMForge v1.0 directive file

## Business Profile (Schema.org LocalBusiness)

- **Name:** A-Abel Roofing
- **Type:** LocalBusiness (Schema.org)
- **URL:** `https://aabelroofing.com/`
- **Contact:** aabelroofing.com/contact

## Q&A Prompt Library

The `/prompts` endpoint exposes 10+ structured Q&A prompt/response pairs. See [prompts.md](prompts.md) for the full library.

## LLM-Accessible Actions

1. **Owens Corning Platinum Roofing South Suburbs** — Premium roofing contractor with highest-quality systems
2. **Midlothian Roofing with Honest Service** — Local roofer for new roofs, repairs, gutters, skylights
3. **South Chicago Suburbs Roofing Experts** — Exterior specialists with 5-year workmanship warranty
4. **Seamless Aluminum Gutters Experts** — Custom .032 gauge aluminum, hidden hangers
5. **Durable Seamless Gutter Systems** — Leak-proof continuous design, multiple sizes
6. **Aluminum Soffit Fascia Protection** — .019 thick aluminum, moisture/rot prevention
7. **Complete Roof Tear-Off Specialists** — Full removal/replacement using Owens Corning systems

See [llms-txt.md](llms-txt.md) for the full llms.txt directive.
See [prompts.md](prompts.md) for the complete Q&A prompt library.
