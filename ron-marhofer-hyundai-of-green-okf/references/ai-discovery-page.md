---
type: APIs
title: Ron Marhofer Hyundai of Green - AI Discovery Page
description: AI Discovery Page documentation and PromptGraph API endpoints for structured JSON-LD data access.
resource: https://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-green/.well-known/ai-manifest.json
tags:
  - api
  - promptgraph
  - json-ld
  - ai-discovery
  - structured-data
timestamp: 2026-07-01
---

# Ron Marhofer Hyundai of Green - AI Discovery Page

The AI Discovery Page provides structured JSON-LD data endpoints for AI consumption. The dealership uses the PromptGraph platform to expose business information, vehicle inventory, customer testimonials, and Q&A prompts through standardized schema.org-compliant APIs.

## API Endpoints

| Endpoint | Description | Format |
|----------|-------------|--------|
| `/business` | Complete business profile with address, contact, hours, location | JSON-LD |
| `/vehicles` | Complete inventory with specifications, pricing, availability | JSON-LD |
| `/prompts` | Structured prompts for consistent AI responses | JSON-LD |
| `/testimonials` | Customer reviews and ratings | JSON-LD |
| `/llms.txt` | LLM directives and AI consumption guidelines | Plain text |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion | JSON-LD |
| `/site-content` | Clean plain-text mirror of the entire site | Text |

## API Base

All endpoints are under:
`http://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-green/`

## Schema Types

- LocalBusiness / AutoDealer
- Car (for vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

## AI Manifest

The AI manifest is available at:
`http://api.promptgraph.ai/api/v1/ron-marhofer-hyundai-of-green/.well-known/ai-manifest.json`

This provides a machine-readable directory of all available AI resources for the dealership.

## CORS

CORS is enabled for all origins.

## Update Frequency

Inventory data is updated in real-time.

## Related

- See [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-hyundai-of-green-okf/references/llms-txt.md) for LLM consumption directives.
- See [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-hyundai-of-green-okf/references/prompts.md) for the Q&A prompt library.
- See [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-hyundai-of-green-okf/references/testimonials.md) for customer reviews.
- See [dealership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-hyundai-of-green-okf/datasets/dealership.md) for the business profile.
