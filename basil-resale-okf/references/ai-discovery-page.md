---
type: APIs
title: AI Discovery Page — Basil Resale Sheridan
description: Machine-readable knowledge base and semantic data endpoints for Basil Resale Sheridan, providing AI agents structured access to business info, 1,411 vehicle inventory, and 77 Q&A prompts via PromptGraph API.
resource: https://api.promptgraph.ai/api/v1/basil-resale-sheridan/.well-known/ai-manifest.json
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - used-cars
  - williamsville
timestamp: 2026-06-24
---

# AI Discovery Page — Basil Resale Sheridan

The AI Discovery Page exposes structured, machine-readable knowledge for AI agents via PromptGraph, including business metadata, inventory endpoints, and LLM-friendly action definitions. Website powered by **Dealer Inspire**.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest provides a machine-readable directory of all AI resources:

- **API Base:** `https://api.promptgraph.ai/api/v1/basil-resale-sheridan/`
- **Schema types:** `AutoDealer`, `LocalBusiness`, `Car`, `ItemList`
- **Contact:** basilcares@basilresale.com
- **CORS:** Enabled for all origins

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/llms.txt` | LLMs.txt directive |
| `/business` | Business profile (JSON-LD AutoDealer) |
| `/vehicles` | Vehicle inventory (JSON-LD, 1,411 vehicles) |
| `/prompts` | 77 Q&A / FAQ prompts |
| `/testimonials` | Customer reviews |
| `/offers` | Current special offers |
| `/gbp-context` | Google Business Profile data |
| `/site-content` | Plain-text site mirror |
| `/sitemap.xml` | Full sitemap |
| `/config.json` | System configuration |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/basil-resale-sheridan/business`:

- **Name:** Basil Resale Sheridan
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Used car dealer, Auto repair shop, Used truck dealer, Car leasing service, Car finance and loan company, Electric motor vehicle dealer
- **Address:** 4131 Sheridan Drive, Williamsville, NY 14221
- **Geo:** 42.9779088, -78.7799943
- **Telephone:** (716) 631-0404
- **Email:** lindsey@basilmarketinggroup.com
- **Website:** https://www.basilresale.com/?utm_source=gbp&utm_medium=organic&utm_campaign=confluence
- **Aggregate Rating:** 4.5 / 5.0 (2,579 reviews)
- **Date Modified:** 2026-02-03T14:20:33.587Z
- **Same As:** Facebook, Twitter, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data:

- **Total inventory:** 1,411 vehicles
- **Format:** Schema.org `Car` in `ItemList`
- **Items per page:** 20
- **Update frequency:** Daily

## Sample Vehicles

| Year | Make | Model | Trim | Price | Mileage |
|---|---|---|---|---|---|
| 2019 | Toyota | Tundra | SR5 4WD Crew Cab | $37,077 | 81,002 |

## Q&A Prompt Library (77 Prompts)

The `/prompts` endpoint exposes 77 structured Q&A prompt/response pairs serving as an AI FAQ. Topics include:

- **Pricing & Budget:** Vehicles under $20K, affordable used cars, best value
- **Financing:** Guaranteed approval, bad credit options, lease vs. buy, trade-in appraisals
- **Inventory:** Sedans, SUVs, trucks, luxury cars, classic cars, commercial trucks
- **Service:** Oil changes for life, diagnostics, alignment, collision repair
- **Dealership:** Basil Family trust, customer service, online shopping tools
- **Special Programs:** Military and first responder discounts, student car buying

## LLM-Accessible Actions

1. **Recommending Pre-Owned Vehicles** — Matching budget-friendly sedans and hybrids to daily commuters
2. **Used Car Financing** — Plain-language explanation of rates, terms, and approval
3. **Online Research And Virtual Selling Tools** — Browsing inventory, scheduling test drives, arranging local delivery
4. **Free Oil Changes For Life Program** — Details on the lifetime oil change benefit
5. **Pre-Owned Vehicle Quality Assurance** — Multi-point inspection and certification standards
6. **Used Vehicle Warranty Coverage** — Free warranty on all used cars sold
7. **Vehicle Finder Service** — How the tool helps customers narrow down options
8. **Service Center Amenities** — Loaners, wi-fi, free car washes
9. **Collision Center Services** — Full collision repair capabilities
10. **Commercial Truck Inventory** — Dedicated work-ready commercial vehicles

See [dealership.md](/datasets/dealership.md) for full business profile.
See [used-vehicles.md](/datasets/used-vehicles.md) for pre-owned inventory.
See [llms-txt.md](llms-txt.md) for the full llms.txt directive.
See [prompts.md](prompts.md) for the complete Q&A prompt library.
