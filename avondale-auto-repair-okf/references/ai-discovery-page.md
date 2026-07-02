---
type: APIs
title: AI Discovery Page - Avondale Auto Repair
description: Machine-readable knowledge base and semantic data endpoints for Avondale Auto Repair, providing AI agents structured access to business info, prompts, testimonials, and site content via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/avondale-auto-repair/.well-known/ai-manifest.json
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

# AI Discovery Page - Avondale Auto Repair

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, and LLM-friendly action definitions.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/avondale-auto-repair/sitemap.xml` exposes these machine-readable endpoints:

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

- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`

### Registered Endpoints

- `/api/v1/avondale-auto-repair/llms.txt` - LLMs.txt directive
- `/api/v1/avondale-auto-repair/business` - Business profile (JSON-LD)
- `/api/v1/avondale-auto-repair/prompts` - Q&A / FAQ prompts
- `/api/v1/avondale-auto-repair/testimonials` - Customer reviews
- `/api/v1/avondale-auto-repair/sitemap.xml` - Full sitemap
- `/api/v1/avondale-auto-repair/robots.txt` - Robots rules
- `/api/v1/avondale-auto-repair/config.json` - System configuration

### Additional PromptGraph Endpoints

- `/gbp-context` - Flattened Google Business Profile data for LLM ingestion
- `/site-content` - Clean, plain-text mirror of the entire site
- `/llms.txt` - LLMForge v1.0 directive file

## Business Profile

- **Name:** Avondale Auto Repair
- **Phone:** (773) 267-5440
- **Address:** 3425 N Pulaski Rd., Chicago, IL 60641
- **Website:** https://www.avondaleautorepair.com/
- **Same owners as** Logan Square Auto Repair

## Q&A Prompt Library

The `/prompts` endpoint exposes structured Q&A pairs. See [prompts.md](prompts.md) for the full library.

See [llms-txt.md](llms-txt.md) for the full llms.txt directive.
See [prompts.md](prompts.md) for the complete Q&A prompt library.
