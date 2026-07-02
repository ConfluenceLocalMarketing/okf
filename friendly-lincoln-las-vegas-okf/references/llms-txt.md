---
type: API
title: llms.txt - Friendly Lincoln Las Vegas
description: AI discovery and consumption directive for Friendly Lincoln Las Vegas providing structured API endpoints, schema types, and business context.
resource: https://www.teamlincolnlasvegas.com/
tags:
  - llms-txt
  - ai-discovery
  - llm
  - promptgraph
  - lincoln
timestamp: 2026-07-03
---

# llms.txt

The llms.txt file provides AI systems with structured discovery and consumption directives for Friendly Lincoln Las Vegas.

## Format

- **Format**: LLMForge v1.0 compatible
- **Schema**: JSON-LD (Schema.org)
- **Primary Discovery**: `/.well-known/ai-manifest.json`
- **Last Updated**: 2026-07-03
- **CORS**: Enabled for all origins

## Discovery Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Business profile (address, contact, hours, location) |
| `/vehicles` | Complete inventory with specs and pricing |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts |
| `/llms.txt` | AI discovery and consumption directives |
| `/.well-known/ai-manifest.json` | AI resource directory |

## Schema Types

- LocalBusiness / AutoDealer
- Car (vehicle inventory)
- ItemList
- Offer
- Review / AggregateRating
- CreativeWork (prompts/FAQs)

## Business Context

Friendly Lincoln Las Vegas (listed as Team Lincoln Las Vegas in client records) specializes in Lincoln luxury vehicle sales and factory-trained service. Located at 5445 Drexel Rd, Las Vegas, NV 89130. Licensed AutoDealer with full inventory and service capabilities.

See [ai-discovery-page.md](ai-discovery-page.md) for the full AI Discovery Hub overview and [prompts.md](prompts.md) for the prompt library.
