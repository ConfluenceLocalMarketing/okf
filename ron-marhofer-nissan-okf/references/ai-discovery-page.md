---
type: APIs
title: AI Discovery Page - Ron Marhofer Nissan
description: Machine-readable knowledge base and semantic data endpoints for Ron Marhofer Nissan, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.ronmarhofernissan.com/ai-discovery-page.htm
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
timestamp: 2026-07-01
---

# AI Discovery Page - Ron Marhofer Nissan

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-06-30T17:52:02.516Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** marhoferc@gmail.com

Note: The AI Manifest was not available at the standard `/.well-known/ai-manifest.json` path on the website (404), but is accessible via PromptGraph at the API endpoint.

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/ron-marhofer-nissan` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (62 prompts) |
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

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/ron-marhofer-nissan/business`:

- **Name:** Ron Marhofer Nissan
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Nissan dealer, Car dealer, Car repair and maintenance service, Truck dealer, Used car dealer, Used truck dealer, Car leasing service, Motor vehicle dealer, Car inspection station, Car finance and loan company
- **Address:** 247 Howe Avenue, Cuyahoga Falls, OH 44221-4903
- **Geo:** 41.1198309, -81.4855967
- **Telephone:** (330) 940-4001
- **Email:** marhoferc@gmail.com
- **URL:** `https://www.ronmarhofernissan.com/`
- **Aggregate Rating:** 4.7 / 5.0 (2,283 reviews)
- **Date Modified:** 2026-02-03T14:39:14.726Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Nissan models and used multi-make vehicles with detailed specifications, pricing, and availability.

## Q&A Prompt Library (62 Prompts)

The `/prompts` endpoint exposes 62 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Nissan Certified Pre-Owned program

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines 9 structured `ReadAction` entries that agents can invoke:

1. **Trusted Nissan Dealer with Customer-First Service** - Customer-focused sales process with transparent pricing
2. **Full-Service Nissan Sales & Certified Maintenance** - Complete Nissan destination with sales, service, and parts
3. **Serving Our Community with Trusted Nissan Service** - Community-focused dealership with local relationships
4. **Cuyahoga Falls Nissan Dealer with Customer Service and a Smile** - Go-to dealership serving Akron, Stow, Hudson, Kent
5. **New Nissan Models & Specials in Cuyahoga Falls OH** - Popular models with current specials and incentives
6. **Nissan Certified Pre-Owned Excellence Near Akron OH** - Factory-backed CPO program with warranty and roadside assistance
7. **Expert Nissan Service & Maintenance in Cuyahoga Falls** - Certified technicians, genuine parts, online scheduling
8. **Flexible Nissan Financing & Leasing Cuyahoga Falls OH** - Stress-free options, competitive rates, online pre-approval
9. **Used Cars & Trucks at Ron Marhofer Nissan Cuyahoga Falls** - Large used inventory with competitive pricing

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/ron-marhofer-nissan/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Ron Marhofer Nissan without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](llms-txt.md) for the full llms.txt directive.
See [prompts.md](prompts.md) for the complete Q&A prompt library.
See [testimonials.md](testimonials.md) for customer review data.
