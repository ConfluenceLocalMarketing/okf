---
type: APIs
title: AI Discovery Page - Ron Marhofer Hyundai of Cuyahoga Falls
description: AI-optimized discovery page with structured JSON-LD endpoints for LLM consumption including business profile, vehicle inventory, prompts, and site directives.
resource: https://www.hyundaiofakron.com/ai-discovery-page.htm
tags:
  - ai-discovery
  - promptgraph
  - llm
  - semantic-web
  - api
timestamp: 2026-07-01
---

# AI Discovery Page - Ron Marhofer Hyundai of Cuyahoga Falls

Ron Marhofer Hyundai of Cuyahoga Falls maintains an [AI Discovery Page](https://www.hyundaiofakron.com/ai-discovery-page.htm) with structured endpoints optimized for LLM and AI crawler consumption via PromptGraph.

## Global Directives

| Resource | URL |
|---|---|
| AI Manifest | `https://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-cuyahoga-falls/.well-known/ai-manifest.json` |
| llms.txt | `https://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-cuyahoga-falls/llms.txt` |
| robots.txt | `https://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-cuyahoga-falls/robots.txt` |
| Sitemap | `https://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-cuyahoga-falls/sitemap.xml` |
| Config | `https://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-cuyahoga-falls/config.json` |

## API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile with address, contact, hours, ratings (JSON-LD) |
| `/vehicles` | Full vehicle inventory with specs, pricing, availability (JSON-LD) |
| `/vehicles/{vin}` | Single vehicle lookup by VIN (JSON-LD) |
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

See [llms-txt.md](ron-marhofer-hyundai-of-cuyahoga-falls-okf/references/llms-txt.md) for the AI consumption directive and [prompts.md](ron-marhofer-hyundai-of-cuyahoga-falls-okf/references/prompts.md) for the prompt library.
