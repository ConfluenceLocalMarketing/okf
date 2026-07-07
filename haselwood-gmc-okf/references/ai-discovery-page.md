---
type: APIs
title: AI Discovery Page - Haselwood GMC
description: Machine-readable knowledge base and semantic data endpoints for Haselwood GMC, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.shophaselwoodgmc.com/ai-discovery-page.htm
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
  - bremerton
  - gmc
timestamp: 2026-07-01
---

# AI Discovery Page - Haselwood GMC

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

Note: The AI Discovery Page at `/ai-discovery-page.htm` was not accessible on the website (timeout), but the PromptGraph API is fully functional.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-01T12:22:53.290Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Description:** Full-service GMC dealership in Bremerton, Washington

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/haselwood-gmc` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (40 prompts) |
| `/testimonials` | Customer reviews |
| `/llms.txt` | LLMs.txt directive |
| `/.well-known/ai-manifest.json` | AI Manifest |
| `/sitemap.xml` | Full sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |

### Additional Endpoints

| Endpoint | Description |
|---|---|
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/offers` | Current offers and specials |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/haselwood-gmc/business`:

- **Name:** Haselwood GMC
- **Type:** AutoDealer (Schema.org)
- **Additional Type:** GMC dealer
- **Address:** 501 W Hills Blvd #2, Bremerton, WA 98312
- **Telephone:** (360) 919-2226
- **URL:** `https://www.shophaselwoodgmc.com/`
- **Date Modified:** 2026-05-26T10:39:08.660Z

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring new GMC models and used multi-make vehicles with detailed specifications, pricing, and availability.

## Q&A Prompt Library (40 Prompts)

The `/prompts` endpoint exposes 40 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](haselwood-gmc-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- GMC Certified Pre-Owned program
- Electric vehicle inquiries (HUMMER EV, Sierra EV)

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data. The PromptGraph testimonials collection is currently empty. See [testimonials.md](haselwood-gmc-okf/references/testimonials.md) for details from Google Business Profile.

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/haselwood-gmc/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Haselwood GMC without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](haselwood-gmc-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](haselwood-gmc-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](haselwood-gmc-okf/references/testimonials.md) for customer review data.
