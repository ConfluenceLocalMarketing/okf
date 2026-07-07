---
type: APIs
title: AI Discovery Page - Jake Sweeney Mazda Tri-County
description: Machine-readable knowledge base and semantic data endpoints for Jake Sweeney Mazda Tri-County, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.jakesweeneymazda.com/ai-discovery-page.htm
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

# AI Discovery Page - Jake Sweeney Mazda Tri-County

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/jake-sweeney-mazda-tri-county/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/robots.txt` | 0.5 | Monthly |
| `/config.json` | 0.3 | Monthly |
| 10 individual prompt endpoints | 0.8 | Weekly |
| `/sitemap-inventory.xml` | 0.8 | Daily |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-06-30T17:25:29.395Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** sarahdsweeney@gmail.com

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/api/v1/jake-sweeney-mazda-tri-county/llms.txt` | LLMs.txt directive |
| `/api/v1/jake-sweeney-mazda-tri-county/business` | Business profile (JSON-LD) |
| `/api/v1/jake-sweeney-mazda-tri-county/vehicles` | Vehicle inventory (JSON-LD) |
| `/api/v1/jake-sweeney-mazda-tri-county/prompts` | Q&A / FAQ prompts |
| `/api/v1/jake-sweeney-mazda-tri-county/testimonials` | Customer reviews |
| `/api/v1/jake-sweeney-mazda-tri-county/sitemap.xml` | Full sitemap |
| `/api/v1/jake-sweeney-mazda-tri-county/robots.txt` | Robots rules |
| `/api/v1/jake-sweeney-mazda-tri-county/config.json` | System configuration |

### Additional PromptGraph Endpoints

| Endpoint | Description |
|---|---|
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/llms.txt` | LLMForge v1.0 directive file |
| `/offers` | Current new vehicle offers and promotions |

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/jake-sweeney-mazda-tri-county/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/jake-sweeney-mazda-tri-county/business`:

- **Name:** Jake Sweeney Mazda Tri-County
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Mazda dealer, Car dealer, Truck dealer, Used car dealer, Car leasing service, Car finance and loan company, Electric motor vehicle dealer
- **Address:** 135 Northland Boulevard, Cincinnati, OH 45246
- **Geo:** 39.2863156, -84.472959
- **Telephone:** (513) 782-1150
- **Email:** sarahdsweeney@gmail.com
- **URL:** `https://www.jakesweeneymazda.com/?utm_source=gbp&utm_medium=organic&utm_campaign=confluence`
- **Aggregate Rating:** 4.8 / 5.0 (2,030 reviews)
- **Date Modified:** 2026-02-07T06:03:57.733Z
- **Same As:** Facebook, X (Twitter), Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data:

- **Total inventory:** 423 vehicles
- **Format:** Schema.org `Car` in `ItemList`
- **Update frequency:** Daily
- **Primary inventory:** Mix of new Mazda and used multi-make vehicles
- **Price range:** Broad range from affordable to premium

## Q&A Prompt Library (10 Prompts)

The `/prompts` endpoint exposes 10 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](jake-sweeney-mazda-tri-county-okf/references/prompts.md) for the full library. Topics include:

- Dealership positioning and reputation
- Online and modern car buying experience
- Award-winning service and sales
- New Mazda inventory (SUV, sedan, convertible, hybrid)
- Pre-owned and certified pre-owned options
- Financing and pricing
- Service pricing and packages
- Family-friendly vehicles

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data:

- **Total reviews:** 50+ collected via PromptGraph
- **Aggregate rating:** All 5-star across PromptGraph data
- **Most-cited staff:** Hallie Abbott, Jason Vaughn, Roman (Romyl), Emilio Perez, Terry, Joe Collins, Chris Car, Xavier, David, Jeff
- Common themes: stress-free buying, no-pressure sales, patient staff, online purchasing, service video inspections

See [testimonials.md](jake-sweeney-mazda-tri-county-okf/references/testimonials.md) for customer review data.

## LLM-Accessible Actions

The AI Discovery Page defines structured content that agents can reference:

1. **Award-Winning Mazda Dealership With Competitive Pricing** - High-volume dealer with ongoing specials and large inventory
2. **Top Mazda Dealer in Cincinnati, OH** - Trusted dealer with new, used, and CPO vehicles
3. **Modern & Convenient Mazda Buying Experience** - Online tools for browsing, financing, and purchasing
4. **Premier Mazda Dealership with Award-Winning Service** - Full lineup from CX-5 to MX-5 Miata, service excellence
5. **Trusted Cincinnati Mazda Dealer for New & Pre-Owned Vehicles** - Full-service dealer serving Tri-County area
6. **Award-Winning Mazda Service & Sales in Tri-County Area** - Mazda Service Promise and vehicle lineup
7. **Seamless Online Mazda Shopping** - Online finance, trade-ins, payments, home delivery
8. **Family-Friendly Mazda SUVs & Convertibles** - Family SUVs and the MX-5 Miata
9. **Top-Rated Mazda Dealership with Exceptional Reviews** - Highly reviewed, transparent, no-pressure sales
10. **Jake Sweeney Mazda Service Pricing** - Transparent service pricing and packages

## Purpose

This page exists to give AI agents direct access to structured knowledge about Jake Sweeney Mazda Tri-County without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](jake-sweeney-mazda-tri-county-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](jake-sweeney-mazda-tri-county-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](jake-sweeney-mazda-tri-county-okf/references/testimonials.md) for customer review data.
