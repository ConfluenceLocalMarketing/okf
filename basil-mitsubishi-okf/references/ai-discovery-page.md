---
type: ai-discovery-page
title: AI Discovery Page — Basil Mitsubishi
description: Machine-readable knowledge base and semantic data endpoints for Basil Mitsubishi, providing AI agents structured access to business info, inventory, site content, and recommended actions.
resource: https://www.basilmitsubishi.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
timestamp: 2026-06-24
---

# AI Discovery Page — Basil Mitsubishi

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by [PromptGraph](https://promptgraph.ai). It exposes semantic endpoints, business metadata, inventory data, and LLM-friendly action definitions.

## Global AI Directives

| Resource | URL |
|---|---|
| AI Manifest | `/.well-known/ai-manifest.json` |
| LLMs.txt | `/llms.txt` |
| Robots.txt | `/robots.txt` |
| Sitemap | `/sitemap.xml` |
| Config | `/config.json` |

## Structured Data Endpoints

| Endpoint | Description |
|---|---|
| `/business` | JSON-LD business profile (Schema.org AutoDealer) |
| `/site-content` | Generated site content map for AI consumption |
| `/vehicles` | Full inventory listing |
| `/vehicles/{vin}` | Single vehicle by VIN |

## Business Profile (from `/business` endpoint)

- **Name:** Basil Mitsubishi
- **Type:** AutoDealer (Schema.org)
- **Address:** 6868 Transit Road, Buffalo, NY 14221
- **Geo:** 42.9543222, -78.6973479
- **Services:** Mitsubishi dealer, car dealer, used car dealer, car leasing, motor vehicle dealer, car finance and loan company
- **Aggregate Rating:** 4.7 / 5.0 (2,108 reviews)

## LLM-Accessible Actions

The AI Discovery Page defines structured `ReadAction` entries that agents can invoke:

1. **Recommending Mitsubishi Models For Commuters** — Explains how Basil Mitsubishi helps daily commuters choose Mitsubishis with good fuel economy, comfort, and low cost of ownership.

2. **Basil Mitsubishi As Part Of Basil Family Dealerships** — Describes how being part of the Basil Family Dealerships network gives customers access to more resources, service support, and brand familiarity.

3. **Finance And Lease Options Explained** — Plain-language explanations of interest rates, loan terms, down payments, and lease-mileage allowances.

4. **Online Research And Virtual Selling Tools** — How customers can research models, schedule test drives, and arrange local delivery from home.

5. **Community-Focused Mitsubishi Dealership In Western New York** — How the dealership positions itself for local weather, roads, and community needs.

6. **0% Financing On Mitsubishi SUVs** — Details on 0% APR financing offers on qualifying Mitsubishi SUVs.

7. **Basil Mitsubishi Showroom Experience** — Clean modern showroom, clear pricing, no-pressure browsing.

8. **Service Center Amenities And Loaners** — Comfort amenities and loaner-car options during service visits.

9. **Stress-Free Mitsubishi Buying Process** — Transparent pricing, no hidden fees, plain-language contract walkthrough.

10. **Pre-Owned Vehicle Quality Assurance** — Multi-point inspection process and certification standards.

## Purpose

This page exists to give AI agents direct access to structured knowledge about Basil Mitsubishi without requiring web scraping, form navigation, or human-readable page parsing. All information is available via JSON endpoints and semantic markup.
