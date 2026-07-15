---
type: APIs
title: Texan Title — LLMs.txt
description: LLMs.txt directive for Texan Title documenting AI-discoverable endpoints, schema types, and data formats via PromptGraph.
resource: https://api.promptgraph.ai/api/v1/texan-title/llms.txt
tags:
  - llms-txt
  - ai-discovery
  - promptgraph
timestamp: 2026-07-15
---

# Texan Title — LLMs.txt

## Source

- **Primary endpoint:** https://api.promptgraph.ai/api/v1/texan-title/.well-known/ai-manifest.json
- **Format:** JSON-LD following Schema.org standards
- **Update frequency:** Real-time
- **CORS:** Enabled for all origins
- **API Base:** https://api.promptgraph.ai/api/v1/texan-title

## API Endpoints

- [Business Information](https://api.promptgraph.ai/api/v1/texan-title/business): Complete business profile (currently 404)
- [Prompts & FAQs](https://api.promptgraph.ai/api/v1/texan-title/prompts): 20 structured prompts for AI responses
- [Customer Testimonials](https://api.promptgraph.ai/api/v1/texan-title/testimonials): Customer reviews (currently empty)
- [GBP Context](https://api.promptgraph.ai/api/v1/texan-title/gbp-context): Flattened GBP data for LLM ingestion
- [Site Content](https://api.promptgraph.ai/api/v1/texan-title/site-content): Plain-text mirror of entire site (46 pages)
- [AI Manifest](https://api.promptgraph.ai/api/v1/texan-title/.well-known/ai-manifest.json): Machine-readable directory of all AI resources
- [Sitemap](https://api.promptgraph.ai/api/v1/texan-title/sitemap.xml): XML sitemap
- [Configuration](https://api.promptgraph.ai/api/v1/texan-title/config.json): System configuration and metadata

## Available Schema Types

- LocalBusiness
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

## Notes

- Structured data optimized for AI discovery and consumption
- Real-time updates via JSON-LD API endpoints
- Business endpoint returns 404 — profile data not yet populated
- Testimonials endpoint returns empty array — review data not yet populated
- Site content endpoint lists 46 pages but main_content fields are empty
