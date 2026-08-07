---
type: APIs
title: AI Discovery Infrastructure - Hyundai Montgomery
description: Machine-readable knowledge base and semantic data endpoints for Hyundai Montgomery, providing AI agents structured access to business info, prompts, and site directives via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/hyundai-montgomery/sitemap.xml
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
  - montgomery
timestamp: 2026-08-08
---

# AI Discovery Infrastructure - Hyundai Montgomery

Hyundai Montgomery's AI discovery infrastructure is provided by [PromptGraph](https://promptgraph.ai) at `https://api.promptgraph.ai/api/v1/hyundai-montgomery`. The site is built on the **Dealer Inspire** platform.

Note: The dealership does not publish a dedicated `/ai-discovery-page` on its own website. AI discovery is instead exposed through the PromptGraph API and the AI Manifest file.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of AI resources:

- **Last updated:** 2026-08-07T16:49:15.489Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`

## PromptGraph API Endpoints

The PromptGraph API exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (20 prompts) |
| `/testimonials` | Customer reviews |
| `/offers` | Current offers and incentives |
| `/llms.txt` | LLMs.txt directive |
| `/.well-known/ai-manifest.json` | AI Manifest |
| `/sitemap.xml` | Sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the site |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/hyundai-montgomery/business`:

- **Name:** Hyundai Montgomery
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Hyundai dealer, Car dealer, Truck dealer, Used car dealer, Used truck dealer, Car leasing service, Car accessories store, Truck accessories store
- **Address:** 4701 Carmichael Rd., Montgomery, AL 36106
- **Telephone:** (334) 686-1615
- **URL:** `https://www.hyundaimontgomery.com/`
- **Aggregate Rating:** 4.4 / 5.0 (3,545 reviews)
- **Hours:** Mon-Fri 9:00 AM - 7:00 PM, Sat 9:00 AM - 6:00 PM

## Google Business Profile Context

The `/gbp-context` endpoint provides flattened Google Business Profile data for LLM ingestion, including:

- **Service items:** Vehicle Financing, Used Car Specials, New Car Specials, Vehicle Delivery, Online Car Buying, Online Appointment Scheduling, Trade Appraisals
- **Place ID:** ChIJDX1tIPgqjIgRnJGUf_LR5-o
- **Average rating:** 4.4 / 5.0 (3,545 reviews)
- **Last sync:** 2026-08-05T13:48:55.604Z

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns JSON-LD inventory data. As of 2026-08-08, the structured endpoint returned `numberOfItems: 0` (empty ItemList), while the dealership website displays over 1,000 new and 319 used vehicles. Inventory data should be sourced from the website for current availability.

## Q&A Prompt Library (20 Prompts)

The `/prompts` endpoint exposes 20 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-montgomery/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries (Venue, Kona, Sonata, Elantra, IONIQ 5, IONIQ 6, Tucson, Santa Fe, Palisade, Santa Cruz)
- Financing, leasing, and trade-in questions
- Used vehicle shopping (SUVs, cars under $20,000, certified pre-owned)
- Dealership reputation and customer ratings

## Testimonials Endpoint

The `/testimonials` endpoint returns customer review data. As of 2026-08-08, the structured endpoint returned an empty testimonials list. Customer reviews are instead visible on the dealership website (Google and DealerRater). See [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-montgomery/references/testimonials.md) for details.

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/hyundai-montgomery/.well-known/ai-manifest.json` |
| LLMs.txt | `https://api.promptgraph.ai/api/v1/hyundai-montgomery/llms.txt` |
| Robots.txt | `https://api.promptgraph.ai/api/v1/hyundai-montgomery/robots.txt` |
| Sitemap XML | `https://api.promptgraph.ai/api/v1/hyundai-montgomery/sitemap.xml` |
| Config | `https://api.promptgraph.ai/api/v1/hyundai-montgomery/config.json` |

## Purpose

This infrastructure exists to give AI agents direct access to structured knowledge about Hyundai Montgomery without requiring web scraping or human-readable page parsing. Business info, prompts, and site directives are available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-montgomery/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-montgomery/references/prompts.md) for the complete Q&A prompt library.
