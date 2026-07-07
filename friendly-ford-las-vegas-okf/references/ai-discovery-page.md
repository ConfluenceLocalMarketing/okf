---
type: API
title: AI Discovery Hub - Friendly Ford Las Vegas
description: AI-optimized discovery page with structured endpoints for LLM consumption, including business profile, vehicle inventory, prompts, and site directives.
resource: https://www.friendlyfordlasvegas.com/
tags:
  - ai-discovery
  - promptgraph
  - llm
  - semantic-web
  - api
timestamp: 2026-07-03
---

# AI Discovery Hub

Friendly Ford Las Vegas maintains structured endpoints optimized for LLM and AI crawler consumption.

## Global Directives

| Resource | URL |
|---|---|
| llms.txt | `https://www.friendlyfordlasvegas.com/llms.txt` |
| robots.txt | `https://www.friendlyfordlasvegas.com/robots.txt` |
| Sitemap | `https://www.friendlyfordlasvegas.com/sitemap.xml` |

## API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile with address, contact, hours, ratings (JSON-LD) |
| `/vehicles` | Full vehicle inventory with specs, pricing, availability (JSON-LD) |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts for consistent AI responses |
| `/site-content` | Clean, plain-text site mirror for LLM ingestion |
| `/llms.txt` | AI discovery and consumption directives |

## Schema Types

- AutoDealer (LocalBusiness)
- Car (vehicle inventory)
- ItemList
- Offer
- CreativeWork (prompts/FAQs)

See [llms-txt.md](friendly-ford-las-vegas-okf/references/llms-txt.md) for the AI consumption directive and [prompts.md](friendly-ford-las-vegas-okf/references/prompts.md) for the prompt library.
