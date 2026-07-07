---
type: APIs
title: llms.txt
description: LLM directives file for Ron Marhofer Chevrolet providing structured data endpoints, schema types, and AI-consumable content.
resource: https://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet/llms.txt
tags:
  - llms-txt
  - ai-discovery
  - structured-data
  - json-ld
  - promptgraph
timestamp: 2026-07-01
---

# llms.txt

## Overview

The llms.txt file is available at:
`https://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet/llms.txt`

It provides a structured, AI-optimized directory of all available data endpoints for the Ron Marhofer Chevrolet dealership, following the LLMForge v1.0 format.

## Key Sections

### Discovery
- Primary endpoint: `http://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet/.well-known/ai-manifest.json`
- Format: JSON-LD following Schema.org standards
- Update frequency: Real-time
- CORS: Enabled for all origins
- API Base: `http://api.promptgraph.ai/api/v1/ron-marhofer-chevrolet`

### API Endpoints

| Resource | URL | Description |
|---|---|---|
| Business Information | `/business` | Complete business profile with address, contact, hours |
| Vehicle Inventory | `/vehicles` | Complete inventory with specs, pricing, availability |
| Prompts and FAQs | `/prompts` | 61 structured prompts for consistent AI responses |
| Customer Testimonials | `/testimonials` | Customer reviews and ratings |
| GBP Context | `/gbp-context` | Google Business Profile data for LLM ingestion |
| Site Content | `/site-content` | Clean plain-text site mirror |
| AI Manifest | `/.well-known/ai-manifest.json` | Machine-readable resource directory |

### Schema Types

- LocalBusiness / AutoDealer
- Car
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork

## Content

Ron Marhofer Chevrolet proudly services Stow, OH, and the surrounding communities including Akron and Kent. The Chevrolet lineup includes iconic new Chevrolet models such as the Camaro and Corvette, Colorado and Silverado, and the Equinox and Traverse. The dealership offers certified Chevrolet service for all vehicle maintenance and repair needs.

See [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/ron-marhofer-chevrolet-okf/references/ai-discovery-page.md) for the AI manifest details.
