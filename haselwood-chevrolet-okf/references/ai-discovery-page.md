---
type: APIs
title: AI Discovery Page - Haselwood Chevrolet
description: Machine-readable knowledge base and semantic data endpoints for Haselwood Chevrolet, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.haselwood.com/ai-discovery-page.htm
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

# AI Discovery Page - Haselwood Chevrolet

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was not accessible at `/ai-discovery-page.htm` (404), but PromptGraph endpoints are available via the API.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-01T12:23:07.725Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** gsjones.haselwood@gmail.com

Note: The AI Manifest is accessible via PromptGraph at the API endpoint.

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/haselwood-chevrolet` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (7 prompts) |
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

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/haselwood-chevrolet/business`:

- **Name:** Haselwood Chevrolet GMC
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Chevrolet dealer, GMC dealer, Car dealer, Truck dealer, Used car dealer, Used truck dealer, Car leasing service, Auto repair shop
- **Address:** 501 West Hills Boulevard, Bremerton, WA 98312
- **Geo:** 47.5578434, -122.6768733
- **Telephone:** (564) 226-2030
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.haselwood.com/`
- **Aggregate Rating:** 4.4 / 5.0 (2,071 reviews)
- **Date Modified:** 2026-02-03T15:12:09.354Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Chevrolet, Buick, and GMC models and used multi-make vehicles with detailed specifications, pricing, and availability.

## Q&A Prompt Library (7 Prompts)

The `/prompts` endpoint exposes 7 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-chevrolet-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Lifetime Powertrain Warranty program
- Military appreciation and special programs

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with a 4.4 aggregate rating. See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-chevrolet-okf/references/testimonials.md) for details.

## LLM-Accessible Actions

The PromptGraph API defines structured prompts that agents can invoke:

1. **Drive Confident: Your Chevrolet & GMC Experts** - Customer-first buying experience with transparent pricing
2. **Explore Top Chevrolet & GMC Vehicles All in One Place** - Comprehensive dealership supporting purchase through ownership
3. **Smart Deals, Great Financing & Your Next Chevy or GMC** - Competitive financing, value deals, lease specials
4. **Your Premier Destination for Chevrolet & GMC Performance and Utility** - Trucks, performance vehicles, Silverado, Sierra, Corvette
5. **Unbeatable Peace of Mind with the Lifetime Powertrain Warranty** - West Hills Advantage program
6. **Dedicated Support for Our Bremerton** - Military appreciation and specialized incentives
7. **Quality Pre-Owned Transportation for Every Budget** - Economy Vehicle Program for budget-conscious buyers

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/haselwood-chevrolet/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Haselwood Chevrolet without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-chevrolet-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-chevrolet-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-chevrolet-okf/references/testimonials.md) for customer review data.
