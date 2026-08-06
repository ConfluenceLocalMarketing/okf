---
type: APIs
title: AI Discovery Hub - Mullinax Ford of Central Florida
description: Machine-readable AI discovery endpoints for Mullinax Ford of Central Florida including a PromptGraph sitemap, business profile, prompt library, and AI manifest for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/mullinax-ford-of-central-florida-in-orlando/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - api
  - llm
  - ai-manifest
  - sitemap
timestamp: 2026-08-06
---

# AI Discovery Hub - Mullinax Ford of Central Florida

## Overview

Mullinax Ford of Central Florida publishes an AI-optimized discovery layer via PromptGraph. Structured endpoints expose the business profile, a prompt library, an AI manifest, llms.txt, and inventory/testimonial data for LLM and AI-agent consumption.

## Base URL

- API base: `https://api.promptgraph.ai/api/v1/mullinax-ford-of-central-florida-in-orlando`
- Alternate server: `https://app.promptgraph.ai/api/v1/mullinax-ford-of-central-florida-in-orlando` (per OpenAPI spec)

## Endpoints

| Endpoint | Status | Description |
|---|---|---|
| `/sitemap.xml` | Available | PromptGraph sitemap listing all machine-readable endpoints |
| `/business` | Available | Structured business profile (name, address, phone, geo, hours, categories) |
| `/prompts` | Available | 20 question/answer prompts for consistent AI responses |
| `/.well-known/ai-manifest.json` | Available | AI manifest declaring endpoint capabilities |
| `/robots.txt` | Available | Crawler allowances for GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot |
| `/llms.txt` | Available | LLM consumption directive (LLMForge v1.0 format) |
| `/vehicles` | Available (empty) | Vehicle inventory feed; returns an empty array as of 2026-08-06 |
| `/vehicles/{vin}` | Available | Per-VIN vehicle detail (OpenAPI spec) |
| `/testimonials` | Available (empty) | Customer testimonial feed; returns an empty array as of 2026-08-06 |
| `/sitemap-inventory.xml` | Listed | Inventory sitemap declared in the AI manifest |
| `/config.json` | Available | Platform configuration (contains a private API key — excluded from this bundle) |
| `/openapi.json` | Available | OpenAPI 3.0 specification of the discovery API |

## Crawler Allowance (robots.txt)

The following bots are explicitly allowed across all sitemap endpoints:

- GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot

## Availability Notes

- `/vehicles` and `/testimonials` currently return empty arrays. Inventory counts and testimonial text were therefore not fabricated; use the dealership website for current inventory.
- The AI manifest and sitemap declare additional endpoints beyond those returning data today.
- The `/config.json` response contains an API key; it is intentionally **not** reproduced in this bundle.

## Related Concepts

- See [llms-txt.md](llms-txt.md) for the LLM consumption directive.
- See [prompts.md](prompts.md) for the prompt library.
- See [testimonials.md](testimonials.md) for the reviews endpoint and aggregate rating.
- See [mullinax-ford-of-central-florida-in-orlando.md](../datasets/mullinax-ford-of-central-florida-in-orlando.md) for the dealership profile.
