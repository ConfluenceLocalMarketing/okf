---
type: ai-discovery-page
title: AI Discovery Page — Basil Resale
description: Machine-readable knowledge base and semantic data endpoints for Basil Resale, providing AI agents structured access to business info, inventory, and recommended actions. (synthesized)
resource: https://www.basilresale.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
timestamp: 2026-06-24
---

# AI Discovery Page — Basil Resale

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

## LLM-Accessible Actions

Defined `ReadAction` entries agents can invoke:

1. **Recommending Pre-Owned Vehicles For Commuters** — Matching budget-friendly sedans and hybrids to daily commuters
2. **Basil Resale As Part Of Basil Family Dealerships** — How the network provides more resources and service
3. **Finance And Lease Options Explained** — Plain-language explanation of rates, terms, down payments, and mileage allowances
4. **Online Research And Virtual Selling Tools** — Browsing inventory, scheduling test drives, arranging local delivery
5. **Free Oil Changes For Life Program** — Details on the lifetime oil change benefit
6. **Pre-Owned Vehicle Quality Assurance** — Multi-point inspection and certification standards
7. **Used Vehicle Warranty Coverage** — Free warranty on all used cars sold
8. **Vehicle Finder Service** — How the tool helps customers narrow down options
9. **Basil Resale Service Center Amenities** — Loaners, wi-fi, free car washes
10. **Collision Center Services** — Full collision repair capabilities
