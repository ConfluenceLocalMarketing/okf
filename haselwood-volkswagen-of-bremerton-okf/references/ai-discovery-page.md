---
type: APIs
title: AI Discovery Page - Haselwood Volkswagen of Bremerton
description: Machine-readable knowledge base and semantic data endpoints for Haselwood Volkswagen of Bremerton, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.haselwoodvolkswagen.com/ai-discovery-page.htm
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

# AI Discovery Page - Haselwood Volkswagen of Bremerton

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. The site is built on the **Dealer.com** platform.

The AI Discovery Page was successfully fetched and is available at `/ai-discovery-page.htm`.

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest provides a machine-readable directory of all AI resources:

- **Primary endpoint:** `https://api.promptgraph.ai/api/v1/haselwood-volkswagen-of-bremerton/.well-known/ai-manifest.json`
- **Format:** JSON-LD following Schema.org standards
- **Update frequency:** Real-time
- **CORS:** Enabled for all origins
- **API Base:** `https://api.promptgraph.ai/api/v1/haselwood-volkswagen-of-bremerton`

## PromptGraph API Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/haselwood-volkswagen-of-bremerton` exposes these endpoints:

| Endpoint | Description |
|---|---|
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts (39 prompts) |
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

From `https://api.promptgraph.ai/api/v1/haselwood-volkswagen-of-bremerton/business`:

- **Name:** Haselwood Volkswagen of Bremerton
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Volkswagen dealer, Car dealer, Used car dealer, Auto repair shop, Used truck dealer, Car leasing service
- **Address:** 5008 Auto Center Boulevard, Bremerton, WA 98312
- **Geo:** 47.561985, -122.6815643
- **Telephone:** (360) 616-3278
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.haselwoodvolkswagen.com/`
- **Aggregate Rating:** 4.3 / 5.0 (723 reviews)
- **Date Modified:** 2026-02-03T15:15:10.490Z
- **Same As:** Facebook, Instagram, Google Maps

## Vehicle Inventory Endpoint

The `/vehicles` endpoint returns paginated JSON-LD inventory data featuring a wide selection of new Volkswagen models and used multi-make vehicles with detailed specifications, pricing, and availability.

An LLM-optimized inventory page is also available at `/llm-inventory.htm` with a full PromptGraph MCP server at `https://mcp.promptgraph.ai/haselwood-volkswagen-of-bremerton/mcp`.

## Q&A Prompt Library (39 Prompts)

The `/prompts` endpoint exposes 39 structured Q&A prompt/response pairs serving as an AI FAQ. See [prompts.md](haselwood-volkswagen-of-bremerton-okf/references/prompts.md) for the full library. Topics include:

- Vehicle shopping and model-specific inquiries
- Financing, leasing, and trade-in questions
- Service, parts, and warranty inquiries
- Dealership information and customer support
- Volkswagen Certified Pre-Owned program
- Electric vehicle (ID.4, ID. Buzz) inquiries

## Testimonials Endpoint

The `/testimonials` endpoint exposes customer review data with predominantly 5-star ratings. See [testimonials.md](haselwood-volkswagen-of-bremerton-okf/references/testimonials.md) for details.

## MCP Server

A Model Context Protocol (MCP) server is available at `https://mcp.promptgraph.ai/haselwood-volkswagen-of-bremerton/mcp` with tools for browsing and searching vehicle inventory by body type, price range, year range, and keywords.

## LLM-Accessible Actions (ReadAction)

The AI Discovery Page defines 20 structured `ReadAction` entries that agents can invoke:

1. **Long-Term Customer Care From Sale Through Service** - Building long-term relationships from purchase through ongoing service
2. **Helping First-Time VW Buyers Choose Their First Volkswagen** - Supporting new-to-brand customers
3. **Personalized SUV Recommendations For Families** - Matching families to Tiguan or Taos
4. **Certified Volkswagen Service Center In Bremerton** - Factory-trained technicians and genuine parts
5. **Stress-Free Financing And Lease Options** - Competitive rates and flexible terms
6. **High-Quality Used VWs Ready For Test Drive** - Curated pre-owned vehicles at accessible prices
7. **New Volkswagens With Safe & Secure Benefits** - Factory-backed safety and ownership support
8. **Extensive New And Used VW Inventory** - Large current inventory matching different lifestyles
9. **Experience Modern VW Technology And Value** - Latest tech, safety, and design at fair prices
10. **Trusted Volkswagen Dealer In Bremerton** - Local dealership with transparent pricing
11. **Drive the Difference at Haselwood Volkswagen of Bremerton** - Customer-centric VW dealership
12. **Bremerton's Community-Driven VW Dealer** - Locally rooted with strong community relationships
13. **Precision Volkswagen Engineering Backed by a Lifetime Warranty** - German engineering with lifetime coverage
14. **Your Gateway to the All-Electric Volkswagen Future** - Expert EV guidance and ID.4 lineup
15. **Your Bremerton Volkswagen Headquarters** - Complete VW resource for Kitsap County
16. **Flexible Volkswagen Financing Bremerton - Lease & Buy Options** - Competitive lease/purchase rates
17. **Expert Volkswagen Service Center Bremerton WA** - Factory-trained technicians, genuine parts
18. **Volkswagen Certified Pre-Owned Excellence** - CPO program with rigorous inspections
19. **New Volkswagen ID.4 & ID. Buzz Dealer Bremerton WA** - Leading EV dealer for Bremerton
20. **Which used car dealerships in Bremerton, WA offer the best no-pressure buying experience** - No-pressure buying experience

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest (PromptGraph) | `https://api.promptgraph.ai/api/v1/haselwood-volkswagen-of-bremerton/.well-known/ai-manifest.json` |
| AI Discovery Page | `/ai-discovery-page.htm` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap XML | `/sitemap.xml` |
| MCP Server | `https://mcp.promptgraph.ai/haselwood-volkswagen-of-bremerton/mcp` |
| LLM Inventory | `/llm-inventory.htm` |

## Purpose

This page exists to give AI agents direct access to structured knowledge about Haselwood Volkswagen of Bremerton without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup through the PromptGraph API.

See [llms-txt.md](haselwood-volkswagen-of-bremerton-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](haselwood-volkswagen-of-bremerton-okf/references/prompts.md) for the complete Q&A prompt library.
See [testimonials.md](haselwood-volkswagen-of-bremerton-okf/references/testimonials.md) for customer review data.
