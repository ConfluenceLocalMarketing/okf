---
type: API
title: llms.txt — Leif Johnson Ford of Austin
description: AI discovery and consumption directive for Leif Johnson Ford of Austin providing structured API endpoints, schema types, and business context.
resource: https://api.promptgraph.ai/api/v1/leif-johnson-austin/llms.txt
tags:
  - llms-txt
  - ai-discovery
  - promptgraph
  - llm
timestamp: 2026-06-30
---

# llms.txt

The [llms.txt](https://api.promptgraph.ai/api/v1/leif-johnson-austin/llms.txt) file provides AI systems with structured discovery and consumption directives for Leif Johnson Ford of Austin.

## Format

- **Format**: LLMForge v1.0
- **Schema**: JSON-LD (Schema.org)
- **Primary Discovery**: `/.well-known/ai-manifest.json`
- **Last Updated**: 2026-06-29
- **CORS**: Enabled for all origins

## Discovery Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Business profile (address, contact, hours, location) |
| `/vehicles` | Complete inventory with specs and pricing |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts |
| `/testimonials` | Customer reviews and ratings |
| `/gbp-context` | Google Business Profile context |
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

Leif Johnson Ford of Austin specializes in automotive sales and service. Family-owned and operated for nearly 60 years. Real-time inventory updates via JSON-LD API endpoints. Structured data optimized for AI discovery and consumption.

See [ai-discovery-page.md](ai-discovery-page.md) for the full AI Discovery Hub overview and [prompts.md](prompts.md) for the prompt library.
