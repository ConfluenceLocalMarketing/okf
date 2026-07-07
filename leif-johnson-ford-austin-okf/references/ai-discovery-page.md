---
type: API
title: AI Discovery Hub - Leif Johnson Ford of Austin
description: AI-optimized discovery page with structured endpoints for LLM consumption, including business profile, vehicle inventory, prompts, and site directives.
resource: https://www.leifjohnsonford.com/ai-discovery-hub/
tags:
  - ai-discovery
  - promptgraph
  - llm
  - semantic-web
  - api
timestamp: 2026-06-30
---

# AI Discovery Hub

Leif Johnson Ford of Austin maintains an [AI Discovery Hub](https://www.leifjohnsonford.com/ai-discovery-hub/) with structured endpoints optimized for LLM and AI crawler consumption via PromptGraph.

## Global Directives

| Resource | URL |
|---|---|
| AI Manifest | `https://api.promptgraph.ai/api/v1/leif-johnson-austin/.well-known/ai-manifest.json` |
| llms.txt | `https://api.promptgraph.ai/api/v1/leif-johnson-austin/llms.txt` |
| robots.txt | `https://api.promptgraph.ai/api/v1/leif-johnson-austin/robots.txt` |
| Sitemap | `https://api.promptgraph.ai/api/v1/leif-johnson-austin/sitemap.xml` |
| Config | `https://api.promptgraph.ai/api/v1/leif-johnson-austin/config.json` |

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

## Author Bio

This AI Discovery Optimization page was structured by a Technical SEO Engineer and Web Developer to maximize LLM discovery and human readability, using semantic HTML, direct API endpoint integration, and valid AutoDealer Schema.org markup.

See [llms-txt.md](leif-johnson-ford-austin-okf/references/llms-txt.md) for the AI consumption directive and [prompts.md](leif-johnson-ford-austin-okf/references/prompts.md) for the prompt library.
