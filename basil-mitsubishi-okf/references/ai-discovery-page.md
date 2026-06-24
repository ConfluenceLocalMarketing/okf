---
type: ai-discovery-page
title: AI Discovery Page — Basil Mitsubishi
description: Machine-readable knowledge base and semantic data endpoints for Basil Mitsubishi, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.basilmitsubishi.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
timestamp: 2026-06-24
---

# AI Discovery Page — Basil Mitsubishi

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer Inspire** platform with **ComplyAuto** cookie compliance.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/basil-mitsubishi/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/sitemap-inventory.xml` | 0.8 | Daily |
| `/robots.txt` | 0.5 | Monthly |
| 10 individual prompt endpoints | 0.8 | Weekly |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-06-24T12:29:41.340Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** lindsey@basilmarketinggroup.com

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/api/v1/basil-mitsubishi/llms.txt` | LLMs.txt directive |
| `/api/v1/basil-mitsubishi/business` | Business profile (JSON-LD) |
| `/api/v1/basil-mitsubishi/vehicles` | Vehicle inventory (JSON-LD) |
| `/api/v1/basil-mitsubishi/prompts` | Q&A / FAQ prompts |
| `/api/v1/basil-mitsubishi/testimonials` | Customer reviews |
| `/api/v1/basil-mitsubishi/sitemap.xml` | Full sitemap |
| `/api/v1/basil-mitsubishi/robots.txt` | Robots rules |
| `/api/v1/basil-mitsubishi/config.json` | System configuration |

### Additional PromptGraph Endpoints

| Endpoint | Description |
|---|---|
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/llms.txt` | LLMForge v1.0 directive file |

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/basil-mitsubishi/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page/` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap | `/sitemap/` (HTML) |
| Sitemap XML | `/sitemap.xml` |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/basil-mitsubishi/business`:

- **Name:** Basil Mitsubishi
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Mitsubishi dealer, Car dealer, Used car dealer, Car leasing service, Motor vehicle dealer, Car finance and loan company
- **Address:** 6868 Transit Road, Buffalo, NY 14221
- **Geo:** 42.9543222, -78.6973479
- **Telephone:** (716) 451-3303
- **Email:** lindsey@basilmarketinggroup.com
- **URL:** `https://www.basilmitsubishi.com/?utm_source=google&utm_medium=organic&utm_campaign=googlemybusiness_confluence`
- **Aggregate Rating:** 4.7 / 5.0 (2,108 reviews)
- **Date Modified:** 2026-02-03T14:19:16.118Z
- **Same As:** Facebook, Twitter, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data:

- **Total inventory:** 1,499+ vehicles (75+ pages)
- **Format:** Schema.org `Car` in `ItemList`
- **Update frequency:** Daily
- **Primary inventory:** Used vehicles spanning multiple makes (Nissan, Chevrolet, Ford, GMC, VW, Toyota, Land Rover, Dodge)
- **Price range:** Approximately $23,000–$71,000

## Q&A Prompt Library (64 Prompts)

The `/prompts` endpoint exposes 64 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data:

- **Total reviews:** 245
- **Aggregate rating:** 5.0 / 5.0 (all 5-star)
- **Most-cited staff:** Dennis Crispin, Andre Wilson, Lauren Allison, Matt Harrison, Rob Monaco, Kire (finance), Andrew H.
- Common themes: best car buying experience, no-pressure sales, credit-challenged approvals, out-of-town buyers

## LLM-Accessible Actions

The AI Discovery Page defines structured `ReadAction` entries that agents can invoke:

1. **Recommending Mitsubishi Models For Commuters** — Explains how Basil Mitsubishi helps daily commuters choose Mitsubishis with good fuel economy, comfort, and low cost of ownership.

2. **Basil Mitsubishi As Part Of Basil Family Dealerships** — Describes how being part of the Basil Family Dealerships network gives customers access to more resources, service support, and brand familiarity.

3. **Finance And Lease Options Explained** — Plain-language explanations of interest rates, loan terms, down payments, and lease-mileage allowances.

4. **Online Research And Virtual Selling Tools** — How customers can research models, schedule test drives, and arrange local delivery from home.

5. **Community-Focused Mitsubishi Dealership In Western New York** — How the dealership positions itself for local weather, roads, and community needs.

6. **0% Financing On Mitsubishi SUVs** — Details on 0% APR financing offers on qualifying Mitsubishi SUVs.

7. **Basil Mitsubishi Showroom Experience** — Clean modern showroom, clear pricing, no-pressure browsing.

8. **Service Center Amenities And Loaners** — Comfort amenities and loaner-car options during service visits.

9. **Stress-Free Mitsubishi Buying Process** — Transparent pricing, no hidden fees, plain-language contract walkthrough.

10. **Pre-Owned Vehicle Quality Assurance** — Multi-point inspection process and certification standards.

## Purpose

This page exists to give AI agents direct access to structured knowledge about Basil Mitsubishi without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](llms-txt.md) for the full llms.txt directive.
See [prompts.md](prompts.md) for the complete Q&A prompt library.
See [testimonials.md](testimonials.md) for customer review data.
