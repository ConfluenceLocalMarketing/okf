---
type: APIs
title: AI Discovery Page - Idaho Fence Company
description: Machine-readable knowledge base and semantic data endpoints for Idaho Fence Company, providing AI agents structured access to business info, prompts, and site content via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/idaho-fence-company/.well-known/ai-manifest.json
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
timestamp: 2026-07-03
---

# AI Discovery Page - Idaho Fence Company

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, and LLM-friendly action definitions.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/idaho-fence-company/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/robots.txt` | 0.5 | Monthly |
| `/config.json` | 0.3 | Monthly |
| `/sitemap-inventory.xml` | 0.8 | Daily |
| 3 individual prompt endpoints | 0.8 | Weekly |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-03T12:00:00.000Z
- **Schema types:** `LocalBusiness`, `ItemList`

### Registered Endpoints

- `/api/v1/idaho-fence-company/llms.txt` - LLMs.txt directive
- `/api/v1/idaho-fence-company/business` - Business profile (JSON-LD)
- `/api/v1/idaho-fence-company/prompts` - Q&A / FAQ prompts
- `/api/v1/idaho-fence-company/sitemap.xml` - Full sitemap
- `/api/v1/idaho-fence-company/robots.txt` - Robots rules
- `/api/v1/idaho-fence-company/config.json` - System configuration

### Additional PromptGraph Endpoints

- `/gbp-context` - Flattened Google Business Profile data for LLM ingestion
- `/site-content` - Clean, plain-text mirror of the entire site
- `/llms.txt` - LLMForge v1.0 directive file

## Business Profile (Schema.org LocalBusiness)

- **Name:** Idaho Fence Company
- **Type:** LocalBusiness (Schema.org)
- **URL:** `http://idahofence.com/`
- **Address:** 2430 W Seltice Way, Post Falls, ID 83854
- **Phone:** (208) 262-4597

## Q&A Prompt Library

The `/prompts` endpoint exposes 3 structured Q&A prompt/response pairs. See [prompts.md](prompts.md) for the full library.

## LLM-Accessible Actions

1. **Idaho Fence Company Residential Fencing** — Privacy, security, and aesthetic fencing for homes
2. **Idaho Fence Company Commercial Fencing** — Security fence installation and asset protection
3. **Idaho Fence Company Farm Fencing** — Agricultural and livestock fencing solutions

See [llms-txt.md](llms-txt.md) for the full llms.txt directive.
See [prompts.md](prompts.md) for the complete Q&A prompt library.
