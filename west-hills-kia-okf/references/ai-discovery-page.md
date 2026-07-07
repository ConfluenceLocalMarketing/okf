---
type: APIs
title: AI Discovery Page - West Hills Kia
description: Machine-readable knowledge base and semantic data endpoints for West Hills Kia, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.westhillskia.com/ai-discovery-page.htm
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
  - kia
timestamp: 2026-07-01
---

# AI Discovery Page - West Hills Kia

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-01T12:31:13.424Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`, `Review`, `AggregateRating`, `Offer`
- **Contact:** dgandel@westhillshonda.com

Note: The AI Manifest is accessible via PromptGraph API and may not be available at the standard `/.well-known/ai-manifest.json` path.

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/west-hills-kia` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (10 prompts) |
| `/testimonials` | Customer reviews |
| `/llms.txt` | LLMs.txt directive |
| `/.well-known/ai-manifest.json` | AI Manifest |
| `/sitemap.xml` | Full sitemap |
| `/config.json` | System configuration |

### Additional Endpoints

| Endpoint | Description |
|---|---|
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/offers` | Current offers and incentives |

## MCP Server

West Hills Kia provides a Model Context Protocol (MCP) server for AI agent inventory queries:

- **MCP Endpoint:** `https://mcp.promptgraph.ai/west-hills-kia/mcp`
- **HTTP Inventory Route:** `/llm-inventory.htm`

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/west-hills-kia/business`:

- **Name:** West Hills Kia
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Kia dealer, Car dealer, Used car dealer, Auto repair shop, Used truck dealer, Car leasing service
- **Address:** 515 West Hills Blvd, Bremerton, WA 98312
- **Geo:** 47.5567436, -122.6790752
- **Telephone:** (360) 616-3273
- **Email:** dgandel@westhillshonda.com
- **URL:** `https://www.westhillskia.com/`
- **Aggregate Rating:** 4.6 / 5.0 (1,277 reviews)
- **Date Modified:** 2026-02-03T15:32:15.927Z
- **Same As:** Facebook, Twitter, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Kia models (EVs, hybrids, SUVs, sedans) and used multi-make vehicles with detailed specifications, pricing, and availability.

## Q&A Prompt Library (10 Prompts)

The `/prompts` endpoint exposes 10 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-kia-okf/references/prompts.md) for the full library. Topics include:

- Dealership positioning and customer service
- New and pre-owned vehicle inquiries
- Financing and trade-in questions
- Service and parts inquiries
- Customer experience and dealership reputation

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 4-5 star ratings. See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-kia-okf/references/testimonials.md) for details.

## Offers Endpoint

The `/offers` endpoint provides current sales, lease, and financing offers.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines multiple structured `ReadAction` entries that agents can invoke:

1. **Your Go-To Kia Destination in West Hills** - Trusted Kia dealership with extensive inventory and stress-free buying
2. **Bremerton's Premier Kia Dealership** - Full-service dealership with new Kia models and pre-owned range
3. **West Hills Kia: Hybrids, SUVs & Seamless Financing** - Bremerton's go-to for new Kia hybrids and SUVs
4. **Certified Care at West Hills Kia Bremerton** - Trusted Kia hub with certified auto mechanics
5. **Drive New Kia Style from West Hills Bremerton** - Exciting Bremerton dealer showcasing new Kia stars
6. **West Hills Kia: Fair Prices, Full-Service Reliability** - Reliable full-service dealership
7. **Bremerton Kia Hybrids & Service Excellence** - Powerhouse for hybrid Kias
8. **Your West Hills Kia: New Rides to Expert Repairs** - Ultimate Kia destination
9. **Do people like working with West Hills Kia?** - Employee and customer feedback synthesis
10. **What's it actually like dealing with West Hills Kia?** - On-the-ground customer experience
11. **Are customers happy after buying from West Hills Kia?** - Long-term owner satisfaction
12. **Does West Hills Kia treat people fairly?** - Fairness, MSRP integrity, and community benefits
13. **Would you trust West Hills Kia with a big purchase?** - Institutional reliability and safety

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/west-hills-kia/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about West Hills Kia without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-kia-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-kia-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-kia-okf/references/testimonials.md) for customer review data.
