---
type: API
title: llms.txt - Friendly Ford Las Vegas
description: AI discovery and consumption directive for Friendly Ford Las Vegas providing structured API endpoints, schema types, and business context.
resource: https://www.friendlyfordlasvegas.com/
tags:
  - llms-txt
  - ai-discovery
  - llm
timestamp: 2026-07-03
---

# llms.txt

The llms.txt file provides AI systems with structured discovery and consumption directives for Friendly Ford Las Vegas.

## Format

- **Format**: LLMForge v1.0
- **Schema**: JSON-LD (Schema.org)
- **Last Updated**: 2026-07-03
- **CORS**: Enabled for all origins

## Discovery Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Business profile (address, contact, hours, location) |
| `/vehicles` | Complete inventory with specs and pricing |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts |
| `/site-content` | Full site text mirror |

## Schema Types

- LocalBusiness / AutoDealer
- Car (vehicle inventory)
- ItemList
- Offer
- CreativeWork (prompts/FAQs)

## Business Context

Friendly Ford Las Vegas specializes in automotive sales and service, located at 660 N Decatur Blvd, Las Vegas, NV 89107. Over 470 new Ford vehicles in inventory. Financing options including ITIN program. Factory-trained service department with collision center at 1650 N Decatur Blvd.

See [ai-discovery-page.md](ai-discovery-page.md) for the full AI Discovery Hub overview and [prompts.md](prompts.md) for the prompt library.
