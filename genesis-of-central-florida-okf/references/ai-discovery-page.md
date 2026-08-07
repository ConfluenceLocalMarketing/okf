---
type: APIs
title: AI Discovery - Genesis of Central Florida
description: Machine-readable AI discovery endpoints for Genesis of Central Florida including a PromptGraph sitemap, business profile, prompt library, AI manifest, and llms.txt for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/genesis-of-central-florida/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - api
  - llm
  - ai-manifest
  - sitemap
timestamp: 2026-08-08
---

# AI Discovery - Genesis of Central Florida

## Overview

Genesis of Central Florida does not publish a separate AI Discovery Hub page on its website. AI discovery is instead served by the PromptGraph platform, which exposes structured JSON-LD endpoints for the business profile, a 20-item prompt library, an AI manifest, llms.txt, and inventory/testimonial feeds for LLM and AI-agent consumption.

## Base URL

- API base: `https://api.promptgraph.ai/api/v1/genesis-of-central-florida`
- Alternate server: `https://app.promptgraph.ai/api/v1/genesis-of-central-florida` (per OpenAPI spec)

## Endpoints

| Endpoint | Status | Description |
|---|---|---|
| `/sitemap.xml` | Available | PromptGraph sitemap listing the discovery endpoints |
| `/business` | Available | Structured business profile (name, address, phone, geo, hours, rating) |
| `/prompts` | Available | 20 question/answer prompts for consistent AI responses |
| `/.well-known/ai-manifest.json` | Available | AI manifest declaring endpoint capabilities |
| `/robots.txt` | Available | Crawler allowances for GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot |
| `/llms.txt` | Available | LLM consumption directive (LLMForge v1.0 format) |
| `/.well-known/llms.txt` | Available | Alias of `/llms.txt` (302 redirect) |
| `/openapi.json` | Available | OpenAPI 3.0 specification of the discovery API |
| `/ai-plugin.json` | Available | ChatGPT plugin manifest |
| `/config.json` | Available | Platform configuration (contains a private API key - excluded from this bundle) |
| `/gbp-context` | Available | Flattened Google Business Profile data (business info, 5 latest posts) |
| `/vehicles` | Available (empty) | Vehicle inventory feed; returns an empty array as of 2026-08-08 |
| `/vehicles/{vin}` | Listed | Per-VIN vehicle detail (OpenAPI spec) |
| `/offers` | Available (empty) | Current offers feed; returns an empty array as of 2026-08-08 |
| `/testimonials` | Available (empty) | Customer testimonial feed; returns an empty array as of 2026-08-08 |
| `/site-content` | Available (empty) | Plain-text site mirror; returns zero pages as of 2026-08-08 |
| `/sitemap-inventory.xml` | Available (empty) | Inventory sitemap; contains an empty urlset as of 2026-08-08 |

## Crawler Allowance (robots.txt)

The following bots are explicitly allowed across all endpoints:

- GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot

## Availability Notes

- `/vehicles`, `/offers`, and `/testimonials` currently return empty arrays, and `/site-content` and `/sitemap-inventory.xml` are empty. Inventory counts in this bundle were therefore sourced from the dealership's public inventory API (Algolia/RideMotive) rather than the PromptGraph feed.
- The AI manifest declares more endpoints than the sitemap lists; the manifest includes vehicles, offers, prompts, testimonials, and gbp-context.
- The `/config.json` response contains an API key; it is intentionally **not** reproduced in this bundle.

## Related Concepts

- See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/references/llms-txt.md) for the LLM consumption directive.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/references/prompts.md) for the prompt library.
- See [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/references/testimonials.md) for the reviews endpoint and aggregate rating.
- See [genesis-of-central-florida.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/datasets/genesis-of-central-florida.md) for the dealership profile.
