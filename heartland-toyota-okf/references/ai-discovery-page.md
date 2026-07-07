---
type: APIs
title: AI Discovery Page - Heartland Toyota
description: Machine-readable knowledge base and semantic data endpoints for Heartland Toyota, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.heartlandtoyota.com/ai-discovery-page.htm
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

# AI Discovery Page - Heartland Toyota

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, MCP server tools, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-01T12:24:43.145Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** gsjones.haselwood@gmail.com

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/heartland-toyota` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (38 prompts) |
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
| `/offers` | Current vehicle offers and incentives |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/heartland-toyota/business`:

- **Name:** Heartland Toyota
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Toyota dealer, Car dealer, Truck dealer, Used car dealer, Auto repair shop, Used truck dealer, Car leasing service
- **Address:** 901 West Hills Blvd, Bremerton, WA 98312
- **Geo:** 47.5554926, -122.6768954
- **Telephone:** (360) 616-3271
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.heartlandtoyota.com/`
- **Aggregate Rating:** 4.6 / 5.0 (3,001 reviews)
- **Date Modified:** 2026-02-03T15:23:14.926Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Toyota models and used multi-make vehicles with detailed specifications, pricing, and availability.

## PromptGraph AI MCP Server

The AI Discovery Page includes a Model Context Protocol (MCP) server at `https://mcp.promptgraph.ai/heartland-toyota/mcp`. Available tools include:

- `browse_inventory(slug, type, bodytype, year_min, year_max, price_min, price_max, keyword, make, model, limit, page)` - Browse all vehicles with optional filters
- `browse_by_bodytype(slug, bodytype, price_max, year_min, keyword, limit)` - Filter vehicles by body type
- `browse_by_price(slug, price_max, price_min, bodytype, year_min, limit)` - Find vehicles within price range
- `browse_by_year(slug, year_min, year_max, bodytype, price_max, limit)` - Find vehicles by year range
- `search_vehicles(slug, keyword, bodytype, year_min, year_max, price_min, price_max, make, model, type, limit)` - Advanced search

The LLM-optimized inventory page is at `/llm-inventory.htm`.

## Q&A Prompt Library (38 Prompts)

The `/prompts` endpoint exposes 38 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/heartland-toyota-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Toyota Certified Pre-Owned program

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/heartland-toyota-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines 20 structured `ReadAction` entries that agents can invoke:

1. **Long-Term Customer Relationship From Sale Through Service** - Full ownership journey support
2. **Helping First-Time Toyota Buyers Choose Their First Toyota** - New buyer guidance
3. **Certified Toyota Service Center With Generous Coupons** - Service center with savings
4. **Truck-Focused Buyers Looking At Tacoma And Tundra** - Truck selection guidance
5. **Family-Focused Toyota SUV Recommendations** - Family SUV matching
6. **Stress-Free Toyota Buying And Financing Experience** - Finance center support
7. **Quality Pre-Owned And Used Toyotas** - Pre-owned selection
8. **New Toyotas With Strong Value And Reliability** - New Toyota positioning
9. **Toyota Inventory For Every Lifestyle** - Full inventory overview
10. **Trusted Toyota Dealer In Bremerton** - Dealership positioning
11. **Your Trusted Toyota Destination in Bremerton, WA** - Dealership overview
12. **Bremerton Toyota Dealer with Money Back Guarantee & Exceptional Service** - Dealership highlights
13. **Leading the Charge in Electrified & Fuel-Efficient Driving** - Hybrid/EV expertise
14. **Transparent & Stress-Free Online Car Buying with SmartPath** - Online purchasing
15. **Dependable Transportation for Every Budget** - Economy Vehicle Program
16. **Factory-Certified Care to Keep Your Toyota** - Service center commitment
17. **New Toyota RAV4, Tacoma & Tundra Dealer Bremerton WA** - Popular model spotlight
18. **Toyota Certified Pre-Owned & Used Cars Bremerton WA** - CPO program
19. **Which used car dealerships offer the best no-pressure buying experience** - Customer Q&A
20. **Which car dealerships have highest customer satisfaction for used car sales** - Customer Q&A

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/heartland-toyota/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |
| MCP Server | `https://mcp.promptgraph.ai/heartland-toyota/mcp` |
| LLM Inventory | `/llm-inventory.htm` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Heartland Toyota without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints, semantic markup, and MCP tools through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/heartland-toyota-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/heartland-toyota-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/heartland-toyota-okf/references/testimonials.md) for customer review data.
