---
type: API
title: AI Discovery Hub - Varsity Lincoln
description: AI-optimized discovery page with structured endpoints for LLM consumption, including business profile, vehicle inventory, prompts, and site directives for Varsity Lincoln in Novi, Michigan.
resource: https://www.varsitylincoln.com/
tags:
  - ai-discovery
  - promptgraph
  - llm
  - semantic-web
  - api
  - novi
  - michigan
timestamp: 2026-07-03
---

# AI Discovery Hub

Varsity Lincoln maintains AI-optimized discovery endpoints with structured data optimized for LLM and AI crawler consumption via PromptGraph.

## Global Directives

| Resource | URL |
|---|---|
| AI Manifest | `https://api.promptgraph.ai/api/v1/varsity-lincoln/.well-known/ai-manifest.json` |
| llms.txt | `https://api.promptgraph.ai/api/v1/varsity-lincoln/llms.txt` |
| robots.txt | `https://api.promptgraph.ai/api/v1/varsity-lincoln/robots.txt` |
| Sitemap | `https://api.promptgraph.ai/api/v1/varsity-lincoln/sitemap.xml` |
| Config | `https://api.promptgraph.ai/api/v1/varsity-lincoln/config.json` |

## API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile with address, contact, hours, ratings (JSON-LD) |
| `/vehicles` | Full vehicle inventory with specs, pricing, availability (JSON-LD) |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts for consistent AI responses |
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

## Business Context

Varsity Lincoln is the #1 Volume Lincoln Dealer in the World for 22 consecutive years, located at 49251 Grand River, Novi, MI 48374. Real-time inventory updates via JSON-LD API endpoints. Structured data optimized for AI discovery and consumption.

See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/varsity-lincoln-okf/references/llms-txt.md) for the AI consumption directive.
See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/varsity-lincoln-okf/references/prompts.md) for the prompt library.
