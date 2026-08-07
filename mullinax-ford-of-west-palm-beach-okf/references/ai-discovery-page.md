---
type: APIs
title: AI Discovery Hub - Mullinax Ford of West Palm Beach
description: Machine-readable AI discovery endpoints for Mullinax Ford of West Palm Beach including a PromptGraph sitemap, business profile, prompt library, and AI manifest for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/mullinax-ford-of-west-palm-beach/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - api
  - llm
  - ai-manifest
  - sitemap
  - west-palm-beach
timestamp: 2026-08-07
---

# AI Discovery Hub - Mullinax Ford of West Palm Beach

## Overview

Mullinax Ford of West Palm Beach publishes an AI-optimized discovery layer via PromptGraph. Structured endpoints expose the business profile, a prompt library, an AI manifest, llms.txt, and inventory/testimonial data for LLM and AI-agent consumption.

## Base URL

- API base: `https://api.promptgraph.ai/api/v1/mullinax-ford-of-west-palm-beach`

## Endpoints

| Endpoint | Status | Description |
|---|---|---|
| `/sitemap.xml` | Available | PromptGraph sitemap listing all machine-readable endpoints |
| `/business` | Available | Structured business profile (name, address, phone, geo, hours, ratings, categories) |
| `/prompts` | Available | 20 question/answer prompts for consistent AI responses |
| `/.well-known/ai-manifest.json` | Available | AI manifest declaring endpoint capabilities |
| `/robots.txt` | Available | Crawler allowances for AI agents |
| `/llms.txt` | Available | LLM consumption directive (LLMForge v1.0 format) |
| `/.well-known/llms.txt` | Available | Well-known LLM consumption directive |
| `/vehicles` | Available (empty) | Vehicle inventory feed; returns an empty array as of 2026-08-07 |
| `/offers` | Available (empty) | Current offers feed; returns an empty array as of 2026-08-07 |
| `/testimonials` | Available (empty) | Customer testimonial feed; returns an empty array as of 2026-08-07 |
| `/gbp-context` | Available | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Listed | Clean plain-text mirror of the entire site for LLM ingestion |
| `/sitemap-inventory.xml` | Listed | Inventory sitemap declared in the AI manifest |
| `/config.json` | Available | System configuration and metadata (contains a private API key - excluded from this bundle) |

## Crawler Allowance (robots.txt)

The following bots are explicitly allowed across all sitemap endpoints:

- GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot

## Availability Notes

- `/vehicles`, `/offers`, and `/testimonials` currently return empty arrays. Inventory counts and testimonial text were therefore not fabricated; use the dealership website for current inventory.
- The `/business` endpoint publishes an AggregateRating of 4.7 / 5 across 4,944 reviews.
- The `/gbp-context` response includes image URLs carrying an embedded Google API key; those URLs are intentionally **not** reproduced in this bundle.
- The `/config.json` response contains an API key; it is intentionally **not** reproduced in this bundle.

## Related Concepts

- See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-west-palm-beach/references/llms-txt.md) for the LLM consumption directive.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-west-palm-beach/references/prompts.md) for the prompt library.
- See [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-west-palm-beach/references/testimonials.md) for the reviews endpoint and aggregate rating.
- See [mullinax-ford-of-west-palm-beach.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-west-palm-beach/datasets/mullinax-ford-of-west-palm-beach.md) for the dealership profile.
