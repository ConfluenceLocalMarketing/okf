---
type: APIs
title: AI Discovery Page - West Hills Ford
description: Machine-readable knowledge base and semantic data endpoints for West Hills Ford, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.westhillsford.com/ai-discovery-page.htm
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
  - mcp
  - bremerton
timestamp: 2026-07-01
---

# AI Discovery Page - West Hills Ford

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **FordDirect / Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest

The AI Manifest provides a machine-readable directory of all AI resources via PromptGraph at `https://api.promptgraph.ai/api/v1/west-hills-ford/.well-known/ai-manifest.json`:

- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** gsjones.haselwood@gmail.com

Note: The AI Manifest was not available at the standard `/.well-known/ai-manifest.json` path on the website, but is accessible via PromptGraph at the API endpoint.

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/west-hills-ford` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (60 prompts) |
| `/testimonials` | Customer reviews |
| `/offers` | Current offers and promotions |
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

## MCP Server

The dealership provides an AI Model Context Protocol (MCP) server for browsing and searching vehicles at `https://mcp.promptgraph.ai/west-hills-ford/mcp`. Features include:

- Browse all vehicles with optional filters
- Filter by body type (Cars, Compact, Convertible, Coupe, Sedan, SUV, Truck, Van, Wagon)
- Filter by price range
- Filter by year range
- Advanced search using multiple criteria (color, features, make, model, price, etc.)

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/west-hills-ford/business`:

- **Name:** West Hills Ford
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Ford dealer, Car dealer, Truck dealer, Used car dealer, Auto repair shop, Used truck dealer, Car leasing service
- **Address:** 1100 Oyster Bay Ave South, Bremerton, WA 98312
- **Geo:** 47.5538477, -122.6751049
- **Telephone:** (360) 616-3277
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.westhillsford.com/`
- **Aggregate Rating:** 4.6 / 5.0 (3,135 reviews)
- **Date Modified:** 2026-02-03T15:26:45.775Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Ford models and used multi-make vehicles with detailed specifications, pricing, and availability. Additionally, an LLM-enabled inventory file is available at `https://parrfordfd.cms.dealer.com/llm-inventory.htm`.

## Q&A Prompt Library (60 Prompts)

The `/prompts` endpoint exposes 60 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](west-hills-ford-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Ford Certified Pre-Owned program
- EV and hybrid vehicle guidance

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](west-hills-ford-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines 9 structured `ReadAction` entries that agents can invoke:

1. **Drive Bold & Confident with West Hills Ford** - Premier Ford dealership with transparent buying experience
2. **Score Strong Deals & Easy Financing at West Hills Ford** - Competitive financing, lease specials, trade-in support, online tools
3. **Bremerton's Favorite Ford Dealer with Proven Reliability** - New Ford models, used vehicles, flexible financing, OEM service
4. **West Hills Ford: Adventure-Ready Broncos & Trucks** - Fan-favorite Broncos, Explorer, pickups, used cars, financing, service
5. **Trusted Ford Service & Financing in Bremerton** - New/used inventory, bad-credit-friendly financing, OEM service
6. **West Hills Ford: From Sedans to Pickup Powerhouses** - Ford sedans, muscle cars, Broncos, trucks, used options, all-credit financing
7. **Flexible Financing & OEM Service at West Hills Ford** - Performance lineup, extensive used inventory, credit-flexible financing
8. **Bremerton Ford Deals: New, Used, and Worry-Free** - New models, used vehicles, inclusive financing, service with coupons
9. **West Hills Ford: Your All-in-One Bremerton Auto Ally** - New inventory, used cars, versatile financing, OEM service, at-home options

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/west-hills-ford/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |
| MCP Server | `https://mcp.promptgraph.ai/west-hills-ford/mcp` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about West Hills Ford without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](west-hills-ford-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](west-hills-ford-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](west-hills-ford-okf/references/testimonials.md) for customer review data.
