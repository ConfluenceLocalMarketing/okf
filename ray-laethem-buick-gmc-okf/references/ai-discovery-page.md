---
type: API
title: AI Discovery Hub - Ray Laethem Buick GMC
description: AI-optimized discovery page with structured endpoints for LLM consumption, including business profile, vehicle inventory, prompts, and site directives.
resource: https://www.laethemgm.com/
tags:
  - ai-discovery
  - promptgraph
  - llm
  - semantic-web
  - api
timestamp: 2026-07-03
---

# AI Discovery Hub

Ray Laethem Buick GMC provides structured endpoints optimized for LLM and AI crawler consumption.

## API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile with address, contact, hours, ratings (JSON-LD) |
| `/vehicles` | Full vehicle inventory with specs, pricing, availability (JSON-LD) |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts for consistent AI responses |
| `/testimonials` | Customer reviews and ratings (JSON-LD) |
| `/site-content` | Clean, plain-text site mirror for LLM ingestion |
| `/llms.txt` | AI discovery and consumption directives |
| `/.well-known/ai-manifest.json` | Machine-readable AI resource directory |

## Schema Types

- AutoDealer (LocalBusiness)
- Car (vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (prompts/FAQs)

See [llms-txt.md](ray-laethem-buick-gmc-okf/references/llms-txt.md) for the AI consumption directive and [prompts.md](ray-laethem-buick-gmc-okf/references/prompts.md) for the prompt library.
