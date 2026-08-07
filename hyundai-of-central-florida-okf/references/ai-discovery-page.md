---
type: APIs
title: AI Discovery Hub - Hyundai of Central Florida
description: Machine-readable AI discovery endpoints for Hyundai of Central Florida including a PromptGraph sitemap, business profile, prompt library, AI manifest, and llms.txt for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/hyundai-of-central-florida/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - api
  - llm
  - ai-manifest
  - sitemap
timestamp: 2026-08-07
---

# AI Discovery Hub - Hyundai of Central Florida

## Overview

Hyundai of Central Florida publishes an AI-optimized discovery layer via PromptGraph. Structured endpoints expose the business profile, a 20-item prompt library, an AI manifest, llms.txt, Google Business Profile context, and inventory/testimonial feeds for LLM and AI-agent consumption.

## Base URL

- API base: `https://api.promptgraph.ai/api/v1/hyundai-of-central-florida`
- Business URL: https://hyundaicfl.com (UTM-tagged for Google Business Profile)

## Endpoints

| Endpoint | Status | Description |
|---|---|---|
| `/sitemap.xml` | Available | PromptGraph sitemap listing all machine-readable endpoints |
| `/business` | Available | Structured AutoDealer profile (name, address, phone, geo, hours, categories, rating) |
| `/prompts` | Available | 20 question/answer prompts for consistent AI responses |
| `/.well-known/ai-manifest.json` | Available | AI manifest declaring endpoint capabilities and schema types |
| `/robots.txt` | Available | Crawler allowances for GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot |
| `/llms.txt` | Available | LLM consumption directive (LLMForge v1.0 format) |
| `/gbp-context` | Available | Flattened Google Business Profile data including business info, recent posts, and image URLs |
| `/vehicles` | Available (empty) | Vehicle inventory feed; returns an empty ItemList as of 2026-08-07 |
| `/offers` | Available (empty) | Current offers feed; returns an empty ItemList as of 2026-08-07 |
| `/testimonials` | Available (empty) | Customer testimonial feed; returns an empty array as of 2026-08-07 |
| `/site-content` | Available (empty) | Full-site plain-text mirror; returns 0 pages as of 2026-08-07 |
| `/inventory` | Listed | Inventory endpoint declared in robots.txt |
| `/openapi.json` | Listed | OpenAPI specification of the discovery API (robots.txt) |
| `/ai-plugin.json` | Listed | AI plugin manifest (robots.txt) |
| `/config.json` | Declared | Platform configuration declared in the AI manifest |

## Verified Not Found

The following endpoints return 404 and are not part of the API surface:

- `/vehicles/new`
- `/vehicles/used`
- `/business-hours`

## Crawler Allowance (robots.txt)

The following bots are explicitly allowed across all sitemap endpoints:

- GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot

## Availability Notes

- `/vehicles`, `/offers`, `/testimonials`, and `/site-content` currently return empty feeds. Inventory counts, offers, and testimonial text were therefore not fabricated; use the dealership website for current data.
- The `/gbp-context` endpoint is the richest source, providing business description, categories, hours, service items, latest posts, and image URLs (last synced 2026-08-05).
- The `/config.json` response is excluded from this bundle.

## Related Concepts

- See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/references/llms-txt.md) for the LLM consumption directive.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/references/prompts.md) for the prompt library.
- See [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/references/testimonials.md) for the reviews endpoint and aggregate rating.
- See [hyundai-of-central-florida.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/datasets/hyundai-of-central-florida.md) for the dealership profile.
