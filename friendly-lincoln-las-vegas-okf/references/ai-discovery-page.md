---
type: API
title: AI Discovery Hub - Friendly Lincoln Las Vegas
description: AI-optimized discovery page with structured endpoints for LLM consumption, including business profile, vehicle inventory, prompts, and site directives.
resource: https://www.teamlincolnlasvegas.com/
tags:
  - ai-discovery
  - llm
  - semantic-web
  - api
  - promptgraph
  - lincoln
timestamp: 2026-07-03
---

# AI Discovery Hub

Friendly Lincoln Las Vegas provides structured endpoints optimized for LLM and AI crawler consumption.

## API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile with address, contact, hours (JSON-LD) |
| `/vehicles` | Full vehicle inventory with specs, pricing, availability (JSON-LD) |
| `/offers` | Current special offers and incentives |
| `/prompts` | Structured Q&A prompts for consistent AI responses |
| `/llms.txt` | AI discovery and consumption directives |
| `/.well-known/ai-manifest.json` | Machine-readable AI resource directory |

## Schema Types

- AutoDealer (LocalBusiness)
- Car (vehicle inventory)
- ItemList
- Offer
- Review / AggregateRating
- CreativeWork (prompts/FAQs)

## Discovery Endpoints

| Resource | URL |
|---|---|
| AI Manifest | `https://www.teamlincolnlasvegas.com/.well-known/ai-manifest.json` |
| llms.txt | `https://www.teamlincolnlasvegas.com/llms.txt` |
| robots.txt | `https://www.teamlincolnlasvegas.com/robots.txt` |

See [llms-txt.md](friendly-lincoln-las-vegas-okf/references/llms-txt.md) for the AI consumption directive and [prompts.md](friendly-lincoln-las-vegas-okf/references/prompts.md) for the prompt library.
