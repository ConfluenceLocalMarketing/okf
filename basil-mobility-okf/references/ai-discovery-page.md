---
type: APIs
title: AI Discovery Page - Basil Mobility
description: Machine-readable knowledge base and semantic data endpoints for Basil Mobility, providing AI agents structured access to business info, inventory, and mobility vehicle data via PromptGraph.
resource: https://www.basilmobility.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - mobility
  - json-ld
  - ai-manifest
timestamp: 2026-06-24
---

# AI Discovery Page - Basil Mobility

The AI Discovery Page exposes structured, machine-readable knowledge for AI agents via PromptGraph, including business metadata, inventory endpoints, and LLM-friendly action definitions. Website powered by **Dealer Inspire**.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-06-24T12:37:22.625Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** basilcares@basilresale.com

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/api/v1/basil-mobility/llms.txt` | LLMs.txt directive |
| `/api/v1/basil-mobility/business` | Business profile (JSON-LD) |
| `/api/v1/basil-mobility/vehicles` | Vehicle inventory (JSON-LD, 1,158 vehicles) |
| `/api/v1/basil-mobility/prompts` | 74 Q&A / FAQ prompts |
| `/api/v1/basil-mobility/testimonials` | Customer reviews |
| `/api/v1/basil-mobility/sitemap.xml` | Full sitemap |
| `/api/v1/basil-mobility/robots.txt` | Robots rules |
| `/api/v1/basil-mobility/config.json` | System configuration |
| `/gbp-context` | Google Business Profile data |
| `/site-content` | Plain-text site mirror |

## Business Profile (Schema.org LocalBusiness)

From `https://api.promptgraph.ai/api/v1/basil-mobility/business`:

- **Name:** Basil Mobility
- **Type:** LocalBusiness (Schema.org)
- **Additional Types:** Mobility equipment supplier, Car dealer, Car repair and maintenance service, Used car dealer, Auto repair shop
- **Address:** 5107 Transit Road, Depew, NY 14043-4436
- **Geo:** 42.8907663, -78.6956549
- **Telephone:** (716) 206-5266
- **Description:** Authorized BraunAbility dealer providing comprehensive maintenance, mechanical and body repair services for wheelchair-accessible vehicles, adaptive driving equipment, lifts, and mobility solutions.
- **Date Modified:** 2026-04-07T06:36:48.880Z
- **Same As:** Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data:

- **Total inventory:** 1,158 vehicles
- **Format:** Schema.org `Car` in `ItemList`
- **Update frequency:** Daily
- **Inventory mix:** Chevrolet (50%), Ford (25%), GMC, Buick, Pontiac; includes SUVs, trucks, classic cars, and commercial vehicles
- **Year range:** 1963–2026
- **Mileage range:** 1–98,980 miles

## Featured PromptGraph Vehicles

| Year | Make | Model | Trim | Price |
|---|---|---|---|---|
| 2026 | Chrysler | Pacifica (BraunAbility) | - | $55,980 |
| 2026 | Toyota | Sienna (BraunAbility XT) | - | $88,150 |

## Q&A Prompt Library (74 Prompts)

The `/prompts` endpoint exposes 74 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/basil-mobility-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping (side-entry, rear-entry, lowered-floor, hybrid accessible vans)
- Adaptive equipment (hand controls, steering aids, transfer seats, wheelchair lifts)
- Service and repair (ramp/lift diagnostics, power door, hydraulics, electronics)
- Financing (BraunAbility financing, grants, low-income approvals, trade-in)
- Rentals (short and long-term accessible van rentals)
- Dealership information and customer support

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/basil-mobility/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page/` |
| LLMs.txt | `/llms.txt` |
| Sitemap XML | `/sitemap.xml` |
| Robots.txt | `/robots.txt` |

## LLM-Accessible Actions

1. **Recommending Wheelchair Accessible Vehicles** - Match customers to appropriate BraunAbility conversions based on needs
2. **BraunAbility Conversion Options** - Explain E2, XT, and XI conversion types and compatible base vehicles
3. **BraunAbility Financial Services Financing** - Special rates, terms, and leasing options
4. **Online Research And Virtual Selling Tools** - Browse inventory, schedule test drives, arrange local delivery
5. **Wheelchair Van Service And Maintenance** - Routine maintenance, equipment diagnostics, specialized repairs
6. **Genuine BraunAbility Parts And Accessories** - Ordering replacement parts and mobility accessories
7. **Grants And Funding Assistance** - Help navigating funding programs for mobility vehicles
8. **Adaptive Driving Equipment Options** - Hand controls, steering devices, transfer seats
9. **Wheelchair Van Rental Information** - Short and long-term accessible van rentals
10. **Pre-Owned Vehicle Quality Assurance** - Multi-point inspection and certification standards

## Purpose

This page exists to give AI agents direct access to structured knowledge about Basil Mobility without requiring web scraping or form navigation. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/basil-mobility-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/basil-mobility-okf/references/prompts.md) for the complete Q&A prompt library.
