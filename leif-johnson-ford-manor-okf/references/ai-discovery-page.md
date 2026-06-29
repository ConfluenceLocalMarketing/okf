---
type: API
title: AI Discovery Hub — Leif Johnson Ford of Manor
description: AI-optimized discovery page with structured endpoints for LLM consumption, including business profile, vehicle inventory, prompts, and site directives.
resource: https://www.leifjohnsonfordofmanor.com/ai-discovery-hub/
tags:
  - ai-discovery
  - promptgraph
  - llm
  - semantic-web
  - api
timestamp: 2026-06-29
---

# AI Discovery Hub

Leif Johnson Ford of Manor maintains an [AI Discovery Hub](https://www.leifjohnsonfordofmanor.com/ai-discovery-hub/) and [AI Discovery Page](https://www.leifjohnsonfordofmanor.com/ai-discovery-page/) with structured endpoints optimized for LLM and AI crawler consumption.

## Global Directives

| Resource | URL |
|---|---|
| AI Manifest | `https://api.promptgraph.ai/api/v1/leif-johnson-manor/.well-known/ai-manifest.json` |
| llms.txt | `https://api.promptgraph.ai/api/v1/leif-johnson-manor/llms.txt` |
| robots.txt | `https://api.promptgraph.ai/api/v1/leif-johnson-manor/robots.txt` |
| Sitemap | `https://api.promptgraph.ai/api/v1/leif-johnson-manor/sitemap.xml` |
| Config | `https://api.promptgraph.ai/api/v1/leif-johnson-manor/config.json` |

## API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile with address, contact, hours, ratings (JSON-LD) |
| `/vehicles` | Full vehicle inventory with specs, pricing, availability (JSON-LD) |
| `/prompts` | 107 structured Q&A prompts for consistent AI responses |
| `/testimonials` | Customer reviews and ratings (JSON-LD) |
| `/gbp-context` | Google Business Profile data including reviews, posts, images |
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

See [llms-txt.md](llms-txt.md) for the AI consumption directive and [prompts.md](prompts.md) for the prompt library.
