---
type: APIs
title: AI Discovery Page
description: Machine-readable AI manifest and API endpoint directory for Ron Marhofer Chevrolet's structured data resources.
resource: https://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet/.well-known/ai-manifest.json
tags:
  - ai-discovery
  - api
  - json-ld
  - structured-data
  - manifest
timestamp: 2026-07-01
---

# AI Discovery Page

## AI Manifest

The AI Manifest is available at:
`https://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet/.well-known/ai-manifest.json`

```json
{
  "version": "1.0",
  "name": "Ron Marhofer Chevrolet",
  "schema_types": ["LocalBusiness", "AutoDealer", "Car", "ItemList"],
  "last_updated": "2026-06-30T17:55:28.331Z",
  "contact": {
    "url": "https://www.ronmarhoferchevy.com/?utm_source=gbp&utm_medium=organic&utm_campaign=confluence",
    "email": "cmarhofer@gmail.com"
  }
}
```

## API Endpoints

| Endpoint | URL | Description |
|---|---|---|
| Business | `/api/v1/ron-marhofer-chevrolet/business` | Complete business profile in JSON-LD |
| Vehicles | `/api/v1/ron-marhofer-chevrolet/vehicles` | Full vehicle inventory with specs and pricing |
| Prompts | `/api/v1/ron-marhofer-chevrolet/prompts` | Structured Q&A prompts for AI responses |
| Testimonials | `/api/v1/ron-marhofer-chevrolet/testimonials` | Customer reviews and ratings |
| LLM TXT | `/api/v1/ron-marhofer-chevrolet/llms.txt` | LLM-friendly site directive |
| AI Manifest | `/api/v1/ron-marhofer-chevrolet/.well-known/ai-manifest.json` | Machine-readable resource directory |
| Site Content | `/api/v1/ron-marhofer-chevrolet/site-content` | Clean plain-text site mirror |
| Sitemap | `/api/v1/ron-marhofer-chevrolet/sitemap.xml` | XML sitemap for crawlers |
| Config | `/api/v1/ron-marhofer-chevrolet/config.json` | System configuration |
| GBP Context | `/api/v1/ron-marhofer-chevrolet/gbp-context` | Google Business Profile context for LLM ingestion |

## Schema Types

- LocalBusiness / AutoDealer
- Car (for vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts and FAQs)

## Base URL

`http://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet`

See [llms-txt.md](llms-txt.md) for LLM directives.
