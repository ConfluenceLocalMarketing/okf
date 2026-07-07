---
type: APIs
title: AI Discovery Page - Haselwood Auto Group
description: Machine-readable knowledge base and semantic data endpoints for Haselwood Auto Group, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph with MCP server support.
resource: https://www.haselwoodautogroup.com/ai-discovery-page.htm
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

# AI Discovery Page - Haselwood Auto Group

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-02-03T15:06:16.760Z
- **Schema types:** `AutoDealer`, `LocalBusiness`, `Car`, `ItemList`
- **Contact:** gsjones.haselwood@gmail.com

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/haselwood-auto-group` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/vehicles/{vin}` | Individual vehicle by VIN |
| `/prompts` | Q&A / FAQ prompts |
| `/testimonials` | Customer reviews |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/llms.txt` | LLMs.txt directive |
| `/.well-known/ai-manifest.json` | AI Manifest |
| `/sitemap.xml` | Full sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/haselwood-auto-group/business`:

- **Name:** Haselwood Auto Group
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Car dealer, Ram dealer, Ford dealer, Jeep dealer, Honda dealer, Truck dealer, Toyota dealer, Used car dealer, Auto repair shop, Chevrolet dealer
- **Address:** 950 West Hills Boulevard, Bremerton, WA 98312
- **Geo:** 47.5549005, -122.6781417
- **Telephone:** (360) 362-4410
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.haselwoodautogroup.com/locations/index.htm`
- **Aggregate Rating:** 3.5 / 5.0 (52 reviews)
- **Date Modified:** 2026-02-03T15:06:16.760Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new and used vehicles across all member brands with detailed specifications, pricing, and availability. Individual vehicle data is available via `/vehicles/{vin}`.

## LLM Inventory Page

An LLM-optimized inventory page is available at `/llm-inventory.htm` for AI agents requiring current vehicle stock, pricing, and model-specific features.

## MCP Server

Haselwood Auto Group provides a Model Context Protocol (MCP) server for browsing and searching vehicles in the PromptGraph AI inventory system. This server provides LLMs with tools to query vehicle listings by various filters.

**MCP Session Endpoint:** `https://mcp.promptgraph.ai/haselwood-auto-group/mcp`
**Inventory HTTP Route:** `https://www.haselwoodautogroup.com/llm-inventory.htm`
**API Data URL:** `https://api.promptgraph.ai/api/v1/haselwood-auto-group/vehicles`

### Available MCP Tools

- `browse_inventory(slug, type, bodytype, year_min, year_max, price_min, price_max, keyword, make, model, limit, page)` - Browse all vehicles with optional filters
- `browse_by_bodytype(slug, bodytype, price_max, year_min, keyword, limit)` - Filter vehicles by body type category
- `browse_by_price(slug, price_max, price_min, bodytype, year_min, limit)` - Find vehicles within a price range
- `browse_by_year(slug, year_min, year_max, bodytype, price_max, limit)` - Find vehicles from a specific year range
- `search_vehicles(slug, keyword, bodytype, year_min, year_max, price_min, price_max, make, model, type, limit)` - Advanced search using multiple criteria

## Q&A Prompt Library

The `/prompts` endpoint exposes structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](haselwood-auto-group-okf/references/prompts.md) for details.

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](haselwood-auto-group-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines 10 structured `ReadAction` entries that agents can invoke:

1. **Find Your Perfect Ride at Haselwood Auto Group** - Full-service automotive dealership group with diverse new, used, and CPO vehicles
2. **Haselwood Auto Group – Where Bremerton Drives Happy** - Trusted automotive business with flexible financing and professional service
3. **Community-Focused Auto Group with Exceptional Customer Care** - Community-focused dealer with friendly service and strong local reputation
4. **A Legacy of Local Care and Community Commitment** - Deeply rooted in Bremerton history, cornerstone of Kitsap County
5. **Dedicated Support and Appreciation for the Military Families** - Military appreciation for active-duty members and veterans
6. **Quality Transportation for Every Budget** - Economy Vehicle Program for budget-friendly reliable rides
7. **The Gold Standard for Certified and West Hills Pre-Owned Vehicles** - Pre-owned collection with meticulous inspection and West Hills warranty
8. **Instant Transparency with Modern Online Car Buying** - Deal Reveal technology for instant pricing transparency
9. **Which used car dealerships in Bremerton, WA offer the best no-pressure buying experience**
10. **Which dealerships in Bremerton, WA have the most reliable service and maintenance departments**

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/haselwood-auto-group/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| LLM Inventory | `/llm-inventory.htm` |
| MCP Server | `https://mcp.promptgraph.ai/haselwood-auto-group/mcp` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

See [llms-txt.md](haselwood-auto-group-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](haselwood-auto-group-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](haselwood-auto-group-okf/references/testimonials.md) for customer review data.
