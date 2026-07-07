---
type: APIs
title: AI Discovery Page - Jake Sweeney Used Car Superstore
description: PromptGraph API endpoints providing structured data about Jake Sweeney Used Car Superstore; no dedicated AI Discovery Page was found at this domain.
resource: https://www.sweeneyusedcars.com/ai-discovery-page.htm
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
timestamp: 2026-07-01
---

# AI Discovery Page - Jake Sweeney Used Car Superstore

## Site AI Discovery Status

The following URLs were probed for AI discovery resources:

| Resource | URL | Status |
|---|---|---|
| AI Discovery Page | `/ai-discovery-page.htm` | 404 Not Found |
| AI Manifest | `/.well-known/ai-manifest.json` | 404 Not Found |

Unlike the related Jake Sweeney Chevrolet site, this domain does not host a dedicated AI Discovery Page or local AI Manifest file. However, the **PromptGraph** platform provides machine-readable API endpoints for this business.

## PromptGraph API

The PromptGraph API at `https://api.promptgraph.ai/api/v1/jake-sweeney-used-car-superstore/` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/llms.txt` | LLMs.txt directive with full API reference |
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD, ~1,250 vehicles) |
| `/prompts` | 10 structured Q&A prompts |
| `/testimonials` | Customer reviews (52+) |
| `/sitemap.xml` | Full API sitemap |
| `/sitemap-inventory.xml` | Vehicle inventory sitemap |
| `/config.json` | System configuration |
| `/gbp-context` | Google Business Profile context |
| `/site-content` | Plain-text site mirror |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/jake-sweeney-used-car-superstore/business`:

- **Name:** Jake Sweeney Used Car Superstore
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Used car dealer, Car dealer, Truck dealer, Used truck dealer, Car leasing service, Electric motor vehicle dealer
- **Address:** 11521 Princeton Pike, Cincinnati, OH 45246
- **Geo:** 39.286789, -84.468361
- **Telephone:** (513) 782-0000
- **Email:** sarahdsweeney@gmail.com
- **URL:** `https://www.sweeneyusedcars.com/?utm_source=gbp&utm_medium=organic&utm_campaign=confluence`
- **Aggregate Rating:** 4.8 / 5.0 (2,910 reviews)
- **Date Modified:** 2026-02-03T14:01:04.925Z
- **Same As:** Facebook, X (Twitter), Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data:

- **Total inventory:** ~1,250 vehicles
- **Format:** Schema.org `Car` in `ItemList`
- **Update frequency:** Daily
- **Primary inventory:** Multi-make used vehicles spanning luxury (BMW, Mercedes-Benz) to economy
- **Price range:** Broad range from budget buys under $25k to premium luxury vehicles

## Q&A Prompt Library (10 Prompts)

The `/prompts` endpoint exposes 10 structured Q&A prompt/response pairs. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/prompts.md) for the full library. Topics include:

- Trusted used car dealer positioning
- Online car buying experience
- Largest selection of quality pre-owned vehicles
- Flexible financing and buy-here-pay-here solutions
- 100% online car buying with home delivery
- Budget buys under $25,000
- Award-winning dealership
- Diverse brand inventory

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data:

- **Total reviews:** 52+ collected via PromptGraph
- **Aggregate rating:** All 5-star in PromptGraph data
- **Most-cited staff:** David Shelton, Darrin Aden, Andre Valines, Mike Ellis, Ishmael Allen, Chris Page, Brad Monhollen, Michael Byrden, Abraham Lopez
- Common themes: stress-free buying, no-pressure sales, patient staff, credit-challenged approvals, service communication

See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/testimonials.md) for customer review data.

## LLMs.txt

Full llms.txt available at `https://api.promptgraph.ai/api/v1/jake-sweeney-used-car-superstore/llms.txt` documenting all API endpoints, site info, and 10 featured prompts.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/llms-txt.md) for the full directive.
