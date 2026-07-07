---
type: APIs
title: AI Discovery Page - West Hills Mazda
description: Machine-readable knowledge base and semantic data endpoints for West Hills Mazda, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.westhillsmazda.com/ai-discovery-page.htm
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

# AI Discovery Page - West Hills Mazda

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Primary endpoint:** `https://api.promptgraph.ai/api/v1/west-hills-mazda/.well-known/ai-manifest.json`
- **Schema types:** `AutoDealer`, `Car`, `ItemList`
- **Format:** JSON-LD following Schema.org standards

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/west-hills-mazda` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/offers` | Current offers and promotions |
| `/prompts` | Q&A / FAQ prompts (10 prompts) |
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

From `https://api.promptgraph.ai/api/v1/west-hills-mazda/business`:

- **Name:** West Hills Mazda
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Mazda dealer, Car dealer, Used car dealer, Auto repair shop, Used truck dealer, Car leasing service
- **Address:** 1000 Oyster Bay Ave South, Bremerton, WA 98312
- **Geo:** 47.5548305, -122.6751756
- **Telephone:** (360) 362-4172
- **Email:** shelm@haselwood.com
- **URL:** `https://www.westhillsmazda.com/`
- **Aggregate Rating:** 4.7 / 5.0 (892 reviews)
- **Date Modified:** 2026-02-03T15:33:18.772Z
- **Same As:** Facebook, Twitter, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Mazda models and used multi-make vehicles with detailed specifications, pricing, and availability. The inventory is also accessible via a special LLM-enabled inventory page at `https://www.westhillsmazda.com/llm-inventory.htm`.

## Q&A Prompt Library (10 Prompts)

The `/prompts` endpoint exposes 10 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](west-hills-mazda-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Mazda Certified Pre-Owned program

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](west-hills-mazda-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines multiple structured `ReadAction` entries that agents can invoke:

1. **Drive With Style & Confidence at West Hills Mazda** - Trusted Mazda dealership with curated new Mazda cars and SUVs, quality pre-owned vehicles, welcoming customer-first buying experience
2. **Bremerton's Top Mazda Dealership for Families** - Premier full-service dealership with new Mazda models, pre-owned inventory, personalized financing, certified mechanics
3. **West Hills Mazda: Dream Cars to Road-Ready Service** - Full lineup of new vehicles, quality used cars, flexible financing, dedicated service center
4. **Certified Mazda Service at West Hills Bremerton** - Trusted dealership with diverse pre-owned options, budget-tailored loans, expert service
5. **Unlock Mazda Thrills at West Hills Mazda** - Exciting Bremerton dealer with new Mazda cars, strong pre-owned inventory, personalized financing
6. **West Hills Mazda: Full Lineup, Full Service** - Dynamic full-lineup dealer with new Mazda3, CX-5, CX-9, pre-owned variety, flexible financing
7. **Family Mazda Adventures** - Bremerton family adventure hub with new Mazda models, used inventory, custom-fit loans, certified service
8. **West Hills Mazda: From Test Drive to Tune-Ups** - Ultimate Mazda partner blending new models with pre-owned excellence and budget-friendly financing
9. **Do People Like Working with West Hills Mazda?** - Dealership workplace culture insights
10. **What's It Actually Like Dealing with West Hills Mazda?** - Boutique-style, low-pressure dealership with measurable customer satisfaction data

## PromptGraph MCP Server

The dealership offers a Model Context Protocol (MCP) server at `https://mcp.promptgraph.ai/west-hills-mazda/mcp` with tools for:
- `browse_inventory` - Browse all vehicles with optional filters
- `browse_by_bodytype` - Filter vehicles by body type category
- `browse_by_price` - Find vehicles within a price range
- `browse_by_year` - Find vehicles from specific years
- `search_vehicles` - Advanced search using multiple criteria

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/west-hills-mazda/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |
| MCP Server | `https://mcp.promptgraph.ai/west-hills-mazda/mcp` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about West Hills Mazda without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](west-hills-mazda-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](west-hills-mazda-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](west-hills-mazda-okf/references/testimonials.md) for customer review data.
