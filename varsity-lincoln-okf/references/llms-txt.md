---
type: API
title: llms.txt - Varsity Lincoln
description: AI discovery and consumption directive for Varsity Lincoln providing structured API endpoints, schema types, and business context for the Novi, Michigan Lincoln dealership.
resource: https://www.varsitylincoln.com/
tags:
  - llms-txt
  - ai-discovery
  - promptgraph
  - llm
  - novi
  - michigan
timestamp: 2026-07-03
---

# llms.txt

The llms.txt file provides AI systems with structured discovery and consumption directives for Varsity Lincoln.

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

Varsity Lincoln, located at 49251 Grand River, Novi, MI 48374, is the #1 Volume Lincoln Dealer in the World for 22 consecutive years. Part of Varsity Automotive Group. Real-time inventory updates via JSON-LD API endpoints. Structured data optimized for AI discovery and consumption.

See [ai-discovery-page.md](varsity-lincoln-okf/references/ai-discovery-page.md) for the full AI Discovery Hub overview.
See [prompts.md](varsity-lincoln-okf/references/prompts.md) for the prompt library.
