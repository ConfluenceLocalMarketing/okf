---
type: APIs
title: AI Discovery Pages - West Hills Autoplex
description: Machine-readable knowledge bases and semantic data endpoints for the West Hills Auto Plex group and its member dealerships, providing AI agents structured access to business info, inventory, site content, and recommended actions via PromptGraph.
resource: https://www.westhillsautoplex.com/
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

# AI Discovery Pages - West Hills Autoplex

The West Hills Auto Plex group and its member dealerships each maintain AI Discovery Pages powered by [PromptGraph](https://promptgraph.ai). These structured, machine-readable knowledge surfaces expose semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions. All member dealership sites are built on the **Dealer.com** platform.

## Group-Level AI Resources

### AI Manifest (`/.well-known/ai-manifest.json`)

Available via PromptGraph at `https://api.promptgraph.ai/api/v1/west-hills-autoplex/.well-known/ai-manifest.json`

- **Schema types:** `AutoDealer`, `LocalBusiness`
- **Contact:** gsjones.haselwood@gmail.com

### PromptGraph API Base Endpoints

The PromptGraph API at `https://api.promptgraph.ai/api/v1/west-hills-autoplex` exposes:

| Endpoint | Description |
|---|---|
| `/business` | Group business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ prompts |
| `/testimonials` | Customer reviews |
| `/llms.txt` | LLMs.txt directive |
| `/.well-known/ai-manifest.json` | AI Manifest |
| `/sitemap.xml` | Full sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |
| `/gbp-context` | Flattened Google Business Profile data |
| `/site-content` | Clean, plain-text mirror of the entire site |

## Member Dealership AI Resources

Each branded dealership has its own PromptGraph API and AI Discovery Page:

| Dealership | AI Discovery Page | PromptGraph API Base |
|---|---|---|
| West Hills Honda | `/ai-discovery-page.htm` | `api.promptgraph.ai/api/v1/west-hills-honda` |
| West Hills Ford | `/ai-discovery-page.htm` | `api.promptgraph.ai/api/v1/west-hills-ford` |
| West Hills Kia | `/ai-discovery-page.htm` | `api.promptgraph.ai/api/v1/west-hills-kia` |
| West Hills Mazda | `/ai-discovery-page.htm` | `api.promptgraph.ai/api/v1/west-hills-mazda` |
| West Hills Chrysler Jeep Dodge RAM | `/ai-discovery-page.htm` | `api.promptgraph.ai/api/v1/west-hills-chrysler-jeep-dodge-ram` |

### Honda-Specific Features

The West Hills Honda AI Discovery Page additionally exposes an **MCP (Model Context Protocol) Server** at `https://mcp.promptgraph.ai/west-hills-honda/mcp` for real-time vehicle inventory queries via tools including `browse_inventory`, `browse_by_bodytype`, `browse_by_price`, `browse_by_year`, and `search_vehicles`.

An LLM-optimized inventory page is available at `/llm-inventory.htm`.

## Group Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/west-hills-autoplex/business`:

- **Name:** West Hills Autoplex
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Used car dealer, Car dealer, Truck dealer, Car leasing service
- **Address:** 950 West Hills Boulevard, Bremerton, WA 98312
- **Geo:** 47.5549135, -122.6756315
- **Telephone:** (360) 616-3036
- **Email:** gsjones.haselwood@gmail.com
- **URL:** `https://www.westhillsautoplex.com/`
- **Aggregate Rating:** 4.1 / 5.0 (628 reviews)
- **Date Modified:** 2026-02-03T15:08:10.089Z
- **Same As:** Facebook, Instagram, Google Maps

### Member Business Profiles

| Dealership | Rating | Reviews | Phone |
|---|---|---|---|
| West Hills Honda | 4.6 / 5.0 | 2,019 | (360) 616-3274 |
| West Hills Ford | 4.6 / 5.0 | 3,135 | (360) 616-3277 |
| West Hills Chrysler Jeep Dodge RAM | 4.5 / 5.0 | 2,660 | (360) 616-3275 |
| West Hills Kia | 4.6 / 5.0 | 1,277 | (360) 616-3273 |
| West Hills Mazda | 4.7 / 5.0 | 892 | (360) 362-4172 |

## LLM-Accessible Actions (ReadAction)

The AI Discovery Pages define structured `ReadAction` entries. West Hills Honda, for example, defines actions including:
1. **Your Trusted Honda Destination in Bremerton, WA**
2. **Quality Cars & Exceptional Service at West Hills Honda**
3. **Drive With Confidence: West Hills Honda Community Focus**
4. **Award-Winning Honda Excellence with a Lifetime Advantage**
5. **Dedicated Service for Our Bremerton Military Heroes**
6. **The Gold Standard for Honda Certified Pre-Owned Vehicles**
7. **Local Service with Global Inventory Power**
8. **Factory-Certified Honda Service You Can Rely On**
9. **Professionalism and Integrity: The Haselwood Difference**

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-autoplex-okf/references/llms-txt.md) for the full llms.txt directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/west-hills-autoplex-okf/references/prompts.md) for the complete Q&A prompt library.
