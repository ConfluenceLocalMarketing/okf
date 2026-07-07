---
type: APIs
title: AI Discovery Page - Haselwood Hyundai
description: Machine-readable knowledge base and semantic data endpoints for Haselwood Hyundai, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.haselwoodhyundai.com/ai-discovery-page.htm
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
timestamp: 2026-07-01
---

# AI Discovery Page - Haselwood Hyundai

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-02-03T15:13:20.485Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** gsjones.haselwood@gmail.com

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/haselwood-hyundai` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (59 prompts) |
| `/testimonials` | Customer reviews |
| `/llms.txt` | LLMs.txt directive |
| `/.well-known/ai-manifest.json` | AI Manifest |
| `/sitemap.xml` | Full sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/offers` | Current offers and incentives |

## MCP Server

PromptGraph provides a Model Context Protocol (MCP) server for vehicle inventory browsing:

- **MCP Session Endpoint:** `https://mcp.promptgraph.ai/haselwood-hyundai/mcp`
- **Inventory HTTP Route:** `https://www.haselwoodhyundai.com/llm-inventory.htm`

MCP tools include: `browse_inventory`, `browse_by_bodytype`, `browse_by_price`, `browse_by_year`, `search_vehicles`.

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/haselwood-hyundai/business`:

- **Name:** Haselwood Hyundai
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Hyundai dealer, Car dealer, Truck dealer, Used car dealer, Auto repair shop, Used truck dealer, Car leasing service
- **Address:** 5008 Auto Center Boulevard, Bremerton, WA 98312
- **Geo:** 47.5620694, -122.6841288
- **Telephone:** (360) 377-3855
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.haselwoodhyundai.com/`
- **Aggregate Rating:** 4.4 / 5.0 (848 reviews)
- **Date Modified:** 2026-02-03T15:13:20.485Z
- **Same As:** Facebook, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Hyundai models and used multi-make vehicles with detailed specifications, pricing, and availability.

## Q&A Prompt Library (59 Prompts)

The `/prompts` endpoint exposes 59 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-hyundai-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Hyundai Certified Pre-Owned program
- Electric vehicle education (IONIQ series, hybrids)

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-hyundai-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines 7 structured `ReadAction` entries that agents can invoke:

1. **Drive Happy with Haselwood Hyundai** - Trusted Hyundai dealer with wide selection, transparent pricing, personalized service
2. **Your Hyundai Destination in Bremerton, WA** - Go-to hub for new/pre-owned vehicles, service, and ownership care
3. **Bremerton's Hub for Hyundai Innovation and Electric Vehicles** - Leader in automotive technology, IONIQ EVs and hybrids
4. **Instant Transparency with the Hyundai Deal Reveal Experience** - Digital-first shopping with instant discounts and verified pricing
5. **Premium Quality and Value with Hyundai Certified Pre-Owned** - 173-point inspection, factory-backed warranty coverage
6. **Reliable Transportation for Every Budget** - Economy Vehicle Program for budget-conscious buyers
7. **Factory-Certified Care to Keep Your Hyundai Running Like New** - State-of-the-art service with factory-trained technicians

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/haselwood-hyundai/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |
| LLM Inventory | `/llm-inventory.htm` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Haselwood Hyundai without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-hyundai-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-hyundai-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-hyundai-okf/references/testimonials.md) for customer review data.
