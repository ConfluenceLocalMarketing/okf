---
type: APIs
title: AI Discovery Page - Ron Marhofer Buick GMC
description: Machine-readable knowledge base and semantic data endpoints for Ron Marhofer Buick GMC, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.ronmarhofergmc.com/ai-discovery-page.htm
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

# AI Discovery Page - Ron Marhofer Buick GMC

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

Note: The AI Discovery Page was not directly fetchable at `/ai-discovery-page.htm` (ERR_ABORTED), but all data is accessible via the PromptGraph API.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-06-30T17:55:16.696Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** marhofergmcron@gmail.com
- **API Base:** `http://api.promptgraph.ai/api/v1/ron-marhofer-buick-gmc`

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/ron-marhofer-buick-gmc` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (10+ prompts) |
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
| `/site-content` | Clean, plain-text mirror of the entire site (1,242 pages) |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/ron-marhofer-buick-gmc/business`:

- **Name:** Ron Marhofer Buick GMC, INC.
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** GMC dealer, Buick dealer
- **Address:** 5617 Whipple Avenue Northwest, North Canton, OH 44720
- **Geo:** 40.8640053, -81.426129
- **Telephone:** (866) 230-8630
- **Email:** marhofergmcron@gmail.com
- **URL:** `https://www.ronmarhofergmc.com/`
- **Aggregate Rating:** 4.7 / 5.0 (1,702 reviews)
- **Date Modified:** 2026-02-03T14:44:08.721Z
- **Same As:** Facebook, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data (950 items) featuring a wide selection of new and used vehicles with detailed specifications, pricing, and availability.

## Q&A Prompt Library (10+ Prompts)

The `/prompts` endpoint exposes 10+ structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-buick-gmc-okf/references/prompts.md) for the full library.

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-buick-gmc-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The PromptGraph API defines structured ReadAction entries covering:

1. **Trusted Buick & GMC Dealer with Customer-First Service** - Reputation and customer-focused buying experience
2. **Buick & GMC Value, Deals & Flexible Financing** - Financial value, specials, and financing solutions
3. **New GMC Sierra & HUMMER EV Dealer** - Leading North Canton dealer for GMC trucks and SUVs
4. **Quality Used Buick GMC Vehicles North Canton OH** - Used inventory with inspection and history reports
5. **Expert Buick GMC Service Center North Canton, OH** - Certified service with OEM parts
6. **Flexible Buick GMC Financing North Canton OH** - Lease and loan options
7. **New Buick Encore GX & Envision Dealer** - Buick luxury lineup
8. **Your North Canton Buick GMC Home - Sales to Service** - Complete dealership resource
9. **Customer Experience and Reviews** - Dealing with Ron Marhofer Buick GMC

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/ron-marhofer-buick-gmc/.well-known/ai-manifest.json` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `https://api.promptgraph.ai/api/v1/ron-marhofer-buick-gmc/robots.txt` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Ron Marhofer Buick GMC without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-buick-gmc-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-buick-gmc-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-buick-gmc-okf/references/testimonials.md) for customer review data.
