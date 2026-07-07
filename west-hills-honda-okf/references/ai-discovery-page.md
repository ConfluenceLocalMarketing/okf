---
type: APIs
title: AI Discovery Page - West Hills Honda
description: Machine-readable knowledge base and semantic data endpoints for West Hills Honda, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.westhillshonda.com/llms-content.htm
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
# AI Discovery Page - West Hills Honda

West Hills Honda is connected via the **PromptGraph** AI platform built on the **Dealer.com** platform. The site exposes structured, machine-readable knowledge surfaces for AI agents through PromptGraph API endpoints.

Note: The standard AI Discovery Page (`/ai-discovery-page.htm`) is not available on this website. AI resources are accessible via the PromptGraph API and the `/llms-content.htm` page.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-07-01T12:28:54.572Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** gsjones.haselwood@gmail.com

The AI Manifest is accessible via PromptGraph at the API endpoint.

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/west-hills-honda` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD, 945+ vehicles) |
| `/prompts` | Q&A / FAQ prompts (29 prompts) |
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

From `https://api.promptgraph.ai/api/v1/west-hills-honda/business`:

- **Name:** West Hills Honda
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Honda dealer, Car dealer, Truck dealer, Used car dealer, Used truck dealer, Car leasing service
- **Address:** 520 West Hills Blvd., Bremerton, WA 98312
- **Geo:** 47.5567767, -122.6778507
- **Telephone:** (360) 616-3274
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.westhillshonda.com/`
- **Aggregate Rating:** 4.6 / 5.0 (2,019 reviews)
- **Date Modified:** 2026-02-03T15:09:05.943Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Honda models and used multi-make vehicles (945+ vehicles in database) with detailed specifications, pricing, and availability.

## Q&A Prompt Library (29 Prompts)

The `/prompts` endpoint exposes 29 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-honda-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- HondaTrue Certified Pre-Owned program

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-honda-okf/references/testimonials.md) for details.

## LLM-Accessible Actions (Prompts)

The PromptGraph library defines 29 structured prompts covering:
1. **Your Trusted Honda Destination in Bremerton, WA** - Full-service Honda dealership positioning
2. **Quality Cars & Exceptional Service at West Hills Honda** - Sales and service experience
3. **Drive With Confidence: West Hills Honda Community Focus** - Community-oriented dealership
4. **Award-Winning Honda Excellence with a Lifetime Advantage** - Lifetime Powertrain Warranty
5. **Dedicated Service for Our Bremerton Military Heroes** - Military incentives near Naval Base Kitsap
6. **The Gold Standard for Honda Certified Pre-Owned Vehicles** - CPO program
7. **Local Service with Global Inventory Power** - West Hills Autoplex benefits
8. **Factory-Certified Honda Service You Can Rely On** - Service department and Express Service
9. **Professionalism and Integrity: The Haselwood Difference** - Values-based business approach

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/west-hills-honda/.well-known/ai-manifest.json` |
| LLMs.txt | `/llms.txt` |
| LLMs Content Page | `/llms-content.htm` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about West Hills Honda without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-honda-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-honda-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-honda-okf/references/testimonials.md) for customer review data.
