---
type: APIs
title: Friendly Lincoln AI Discovery
description: Machine-readable AI discovery endpoints for Friendly Lincoln published by PromptGraph, including a business profile, vehicle inventory, offers, prompts, AI manifest, llms.txt, and robots.txt policy for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/friendly-lincoln/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - llms-txt
  - ai-manifest
  - json-ld
  - schema-org
timestamp: 2026-08-18
---

# Friendly Lincoln AI Discovery

Friendly Lincoln exposes machine-readable AI discovery endpoints through PromptGraph. The sitemap at `https://api.promptgraph.ai/api/v1/friendly-lincoln/sitemap.xml` enumerates the available endpoints.

## Endpoints

| Endpoint | Status | Notes |
|---|---|---|
| `/business` | Populated | AutoDealer JSON-LD with address, phone, hours, rating |
| `/prompts` | Populated | 102 items; 15 featured Monroe MI prompts |
| `/offers` | Populated | 7 current offers |
| `/vehicles` | Populated | 99 vehicles, paginated (20 per page) |
| `/testimonials` | Empty | Returns empty array |
| `/gbp-context` | Populated | 4.7/5 rating, 13 reviews, 5 recent reviews |
| `/site-content` | Broken | 107 friendlylincoln.com URLs returned with empty content; bundled unrelated site content |
| `/.well-known/ai-manifest.json` | Populated | Machine-readable resource directory |
| `/robots.txt` | Populated | Allows all AI bots |
| `/llms.txt` | Populated | LLMForge v1.0 directive |
| `/config.json` | Present | Contains a private API key; excluded from bundle |

## robots.txt Policy

The robots.txt allows all user agents and explicitly allows GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, and Applebot.

## Notable Findings

- The `/site-content` mirror is broken as of 2026-08-18: every one of the 107 `friendlylincoln.com` page URLs returned empty `main_content`, and the response bundled full content from an unrelated site (Memorial Hospital of Converse County). Site data was therefore sourced via direct browser crawl instead.
- The `/vehicles` endpoint reports 99 total vehicles but is paginated (20 per page); only page 1 was sampled.

See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/friendly-lincoln/references/llms-txt.md) for the LLMForge directive.
See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/friendly-lincoln/references/prompts.md) for the prompt library.
