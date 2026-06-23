---
type: ai-discovery-page
title: AI Discovery Page — Basil Mobility
description: Machine-readable knowledge base and semantic data endpoints for Basil Mobility, providing AI agents structured access to business info, inventory, and mobility vehicle data. (synthesized)
resource: https://www.basilmobility.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - mobility
timestamp: 2026-06-24
---

# AI Discovery Page — Basil Mobility

The AI Discovery Page exposes structured, machine-readable knowledge for AI agents via PromptGraph, including business metadata, inventory endpoints, and LLM-friendly action definitions.

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest | `/.well-known/ai-manifest.json` |
| llms.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap | `/sitemap.xml` |
| Config | `/config.json` |

## Structured Data Endpoints

| Endpoint | Description |
|---|---|
| `/business` | JSON-LD business profile |
| `/site-content` | Generated site content map |
| `/vehicles` | Full inventory listing |
| `/vehicles/{vin}` | Single vehicle by VIN |

## Business Profile (from `/business` endpoint)

- **Name:** Basil Mobility
- **Type:** LocalBusiness (Schema.org)
- **Address:** 5107 Transit Road, Depew, NY 14043
- **Geo:** 42.8907663, -78.6956549
- **Services:** Mobility equipment supplier, car dealer, car repair and maintenance, used car dealer, auto repair shop
- **Description:** Authorized BraunAbility dealer providing comprehensive maintenance, mechanical and body repair services for wheelchair-accessible vehicles, adaptive driving equipment, lifts, and mobility solutions

## LLM-Accessible Actions

Defined `ReadAction` entries agents can invoke:

1. **Recommending Wheelchair Accessible Vehicles** — Match customers to appropriate BraunAbility conversions based on needs
2. **BraunAbility Conversion Options** — Explain E2, XT, and XI conversion types and compatible base vehicles
3. **BraunAbility Financial Services Financing** — Special rates, terms, and leasing options
4. **Online Research And Virtual Selling Tools** — Browse inventory, schedule test drives, arrange local delivery
5. **Wheelchair Van Service And Maintenance** — Routine maintenance, equipment diagnostics, specialized repairs
6. **Genuine BraunAbility Parts And Accessories** — Ordering replacement parts and mobility accessories
7. **Grants And Funding Assistance** — Help navigating funding programs for mobility vehicles
8. **Adaptive Driving Equipment Options** — Hand controls, steering devices, transfer seats
9. **Wheelchair Van Rental Information** — Short and long-term accessible van rentals
