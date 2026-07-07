---
type: API
title: llms.txt - Ray Laethem Buick GMC
description: AI discovery and consumption directive for Ray Laethem Buick GMC providing structured API endpoints, schema types, and business context.
resource: https://www.laethemgm.com/
tags:
  - llms-txt
  - ai-discovery
  - llm
timestamp: 2026-07-03
---

# llms.txt

The llms.txt file provides AI systems with structured discovery and consumption directives for Ray Laethem Buick GMC.

## Format

- **Format**: LLMForge v1.0
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
| `/testimonials` | Customer reviews and ratings |
| `/site-content` | Full site text mirror |
| `/.well-known/ai-manifest.json` | AI resource directory |

## Schema Types

- LocalBusiness / AutoDealer
- Car (vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (prompts/FAQs)

## Business Context

Ray Laethem Buick GMC, family-owned since 1940, specializes in Buick and GMC automotive sales and service in the Detroit metropolitan area. Real-time inventory updates via JSON-LD API endpoints. Structured data optimized for AI discovery and consumption.

See [ai-discovery-page.md](ray-laethem-buick-gmc-okf/references/ai-discovery-page.md) for the full AI Discovery Hub overview and [prompts.md](ray-laethem-buick-gmc-okf/references/prompts.md) for the prompt library.
