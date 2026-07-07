---
type: APIs
title: AI Discovery - BMW of Cincinnati North
description: Machine-readable knowledge base and semantic data endpoints for BMW of Cincinnati North, providing AI agents structured access to business info, inventory, and content via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/bmw-of-cincinnati-north/business
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

# AI Discovery - BMW of Cincinnati North

The site is powered by **PromptGraph** at the slug `bmw-of-cincinnati-north`, exposing structured semantic endpoints for AI agents. The website is built on the **Dealer.com** platform.

The dedicated AI Discovery Page at `/ai-discovery-page.htm` returned a 404. All structured data is available through the PromptGraph API at `https://api.promptgraph.ai/api/v1/bmw-of-cincinnati-north/`.

## PromptGraph API Sitemap

The PromptGraph sitemap at `https://api.promptgraph.ai/api/v1/bmw-of-cincinnati-north/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/robots.txt` | 0.5 | Monthly |
| `/config.json` | 0.3 | Monthly |
| 16 individual prompt endpoints | 0.8 | Weekly |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Last updated:** 2026-06-30T17:38:19.481Z
- **Schema types:** `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`
- **Contact:** info@bmwofcincinnatinorth.com

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/api/v1/bmw-of-cincinnati-north/llms.txt` | LLMs.txt directive |
| `/api/v1/bmw-of-cincinnati-north/business` | Business profile (JSON-LD) |
| `/api/v1/bmw-of-cincinnati-north/vehicles` | Vehicle inventory (JSON-LD) |
| `/api/v1/bmw-of-cincinnati-north/prompts` | Q&A / FAQ prompts |
| `/api/v1/bmw-of-cincinnati-north/testimonials` | Customer reviews |
| `/api/v1/bmw-of-cincinnati-north/sitemap.xml` | Full sitemap |
| `/api/v1/bmw-of-cincinnati-north/robots.txt` | Robots rules |
| `/api/v1/bmw-of-cincinnati-north/config.json` | System configuration |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/bmw-of-cincinnati-north/business`:

- **Name:** BMW of Cincinnati North
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** BMW dealer, Car dealer, Used car dealer, Car manufacturer, Used truck dealer, Car leasing service, Car accessories store, Car finance and loan company
- **Address:** 105 West Kemper Road, Cincinnati, OH 45246
- **Geo:** 39.287233, -84.475458
- **Telephone:** (513) 782-1122
- **Email:** info@bmwofcincinnatinorth.com
- **URL:** `https://www.bmwofcincinnatinorth.com/?utm_source=gbp&utm_medium=organic&utm_campaign=confluence`
- **Aggregate Rating:** 4.8 / 5.0 (2,500 reviews)
- **Price Range:** $$$
- **Same As:** Google Maps, Facebook, X (Twitter), Instagram

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data:

- **Total inventory:** 664 vehicles
- **Format:** Schema.org `Car` in `ItemList`
- **Update frequency:** Daily
- **Primary inventory:** Mix of new BMW and used multi-make vehicles
- **Price range:** Broad range from affordable to premium

## Current Offers Endpoint (13 Offers)

The `/offers` endpoint exposes current promotional offers:
- Lease specials: 2026 X3, X5, X5 PHEV, 330i, 530i, X1 - all June 2026 programs
- CPO APR promotions: 1.99% (iX), 2.99% (i4/i5/i7), 4.99% (other CPO models)
- BMW Certified Loyalty Credit: $500
- Military and First Responder Credit: $500
- College Grad Offer: $1,000
- No Payments for 3 months

## Q&A Prompt Library (16 Prompts)

The `/prompts` endpoint exposes 16 structured Q&A prompt/response pairs. See [prompts.md](bmw-of-cincinnati-north-okf/references/prompts.md) for the full library. Topics include:

- New inventory and dealership information
- Certified pre-owned BMW near Cincinnati
- BMW electric vehicles and EV dealer
- Service and maintenance
- Lease and finance offers
- Luxury BMW SUVs
- High-performance BMW M Series
- New BMW convertibles and coupes
- Financing pre-approval
- Genuine BMW parts and accessories
- BMW test drive appointments
- Used luxury BMW cars
- Oil change and maintenance specials
- Family-owned dealership
- Electric BMW i4/iX test drive
- General dealership information

## Testimonials Endpoint

The `/testimonials` endpoint returned an empty array, indicating no testimonials have been collected through PromptGraph for this dealership.

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/bmw-of-cincinnati-north/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` (404 - not deployed) |
| LLMs.txt | `/llms.txt` (redirected - available via PromptGraph API) |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |

## LLM-Accessible Actions

The PromptGraph platform defines structured knowledge resources that agents can invoke:

1. **BMW Dealer Cincinnati North New Inventory** - Browse new BMW inventory
2. **Certified Pre-Owned BMW Near Cincinnati** - CPO program details
3. **BMW Electric Vehicles EV Dealer Cincinnati** - Electric BMW models and technology
4. **BMW Service and Maintenance Cincinnati** - Service offerings and booking
5. **BMW Lease and Finance Offers Cincinnati** - Current lease and finance programs
6. **Luxury BMW SUVs for Sale Cincinnati** - SUV lineup including X1-X7
7. **High-Performance BMW M Series** - M performance vehicle information
8. **New BMW Convertibles and Coupes** - Convertible and coupe lineup
9. **BMW Financing Pre-Approval** - Financing application guidance
10. **Genuine BMW Parts and Accessories** - OEM parts and accessories
11. **BMW Test Drive Appointment** - Test drive booking
12. **Used Luxury BMW Cars Cincinnati** - Pre-owned BMW inventory
13. **BMW Oil Change and Maintenance Specials** - Service specials
14. **Family-Owned BMW Dealership Cincinnati** - Jake Sweeney heritage
15. **Electric BMW i4 iX Test Drive Cincinnati** - EV test drive experience
16. **Tell Me About BMW of Cincinnati North** - General dealership overview

## Purpose

This page documents the structured AI-accessible resources for BMW of Cincinnati North. All information is available via JSON endpoints and semantic markup through the PromptGraph API at `https://api.promptgraph.ai/api/v1/bmw-of-cincinnati-north/`.

See [llms-txt.md](bmw-of-cincinnati-north-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](bmw-of-cincinnati-north-okf/references/prompts.md) for the complete Q&A prompt library.
