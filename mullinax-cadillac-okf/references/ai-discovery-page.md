---
type: APIs
title: AI Discovery Layer - Mullinax Cadillac
description: Machine-readable AI discovery endpoints for Mullinax Cadillac including a PromptGraph sitemap, business profile, prompt library, and AI manifest for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/mullinax-cadillac/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - api
  - llm
  - ai-manifest
  - sitemap
timestamp: 2026-08-08
---

# AI Discovery Layer - Mullinax Cadillac

## Overview

Mullinax Cadillac publishes an AI-optimized discovery layer via PromptGraph. Structured endpoints expose the business profile, a prompt library, an AI manifest, llms.txt, and empty inventory/testimonial feeds for LLM and AI-agent consumption.

## Base URL

- API base: `https://api.promptgraph.ai/api/v1/mullinax-cadillac`
- AI Discovery Hub: not published; endpoint availability is documented in this bundle instead

## Endpoints

| Endpoint | Status | Description |
|---|---|---|
| `/sitemap.xml` | Available | PromptGraph sitemap listing all machine-readable endpoints |
| `/business` | Available | Structured business profile (name, address, phone, geo, hours, categories, rating) |
| `/prompts` | Available | 20 question/answer prompts for consistent AI responses |
| `/.well-known/ai-manifest.json` | Available | AI manifest declaring endpoint capabilities |
| `/robots.txt` | Available | Crawler allowances for GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot |
| `/llms.txt` | Available | LLM consumption directive (LLMForge v1.0 format) |
| `/vehicles` | Available (empty) | Vehicle inventory feed; returns zero items as of 2026-08-08 |
| `/testimonials` | Available (empty) | Customer testimonial feed; returns zero items as of 2026-08-08 |
| `/offers` | Available (empty) | Offer feed; returns zero items as of 2026-08-08 |
| `/gbp-context` | Available | Google Business Profile context and service labels |
| `/site-content` | Available (0 pages) | Indexed site content feed; returns zero pages as of 2026-08-08 |
| `/config.json` | Referenced | Platform configuration referenced by the AI manifest (contains a private API key - excluded from this bundle) |

## Crawler Allowance (robots.txt)

The following bots are explicitly allowed across the API endpoints:

- GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, Applebot

Note: the robots.txt sitemap directive has a doubled-slash typo (`https://api.promptgraph.ai//api/v1/mullinax-cadillac/sitemap.xml`).

## AI Manifest Schema Types

The AI manifest (version 1.0, last updated 2026-08-07T17:49:39.762Z) declares these schema.org types: `LocalBusiness`, `AutoDealer`, `Car`, `ItemList`. Additional discovery is exposed at `/.well-known/llms.txt`.

## Availability Notes

- `/vehicles`, `/testimonials`, and `/offers` currently return empty results. Inventory counts and testimonial text were therefore not fabricated from the API; use the dealership website for current inventory.
- The AI manifest and sitemap declare additional endpoints beyond those returning data today.
- The `/config.json` response contains an API key; it is intentionally **not** reproduced in this bundle.

## Related Concepts

- See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/llms-txt.md) for the LLM consumption directive.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/prompts.md) for the prompt library.
- See [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/testimonials.md) for the reviews endpoint and aggregate rating.
- See [mullinax-cadillac.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/mullinax-cadillac.md) for the dealership profile.
