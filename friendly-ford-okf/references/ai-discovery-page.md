---
type: APIs
title: Friendly Ford AI Discovery
description: PromptGraph AI discovery endpoints for the friendly-ford slug in Monroe, MI, documenting a business, vehicle inventory, offers, prompts, AI manifest, llms.txt, and robots.txt policy for LLM consumption.
resource: https://api.promptgraph.ai/api/v1/friendly-ford/sitemap.xml
tags:
  - ai-discovery
  - promptgraph
  - llms-txt
  - ai-manifest
  - json-ld
  - schema-org
timestamp: 2026-08-18
---

# Friendly Ford AI Discovery

Friendly Ford (Monroe, MI) is associated with the PromptGraph slug `friendly-ford`. The sitemap at `https://api.promptgraph.ai/api/v1/friendly-ford/sitemap.xml` enumerates the available endpoints.

## Endpoints

| Endpoint | Status | Notes |
|---|---|---|
| `/business` | Populated | AutoDealer JSON-LD with address, phone, hours, rating |
| `/prompts` | Populated | 15 featured Monroe MI prompts |
| `/offers` | Populated | 8 Ford program offers |
| `/vehicles` | Populated | 134 vehicles, paginated (20 per page) |
| `/testimonials` | Empty | Returns empty array |
| `/gbp-context` | Populated | 4.5/5 rating, 1,201 reviews, 5 recent reviews |
| `/.well-known/ai-manifest.json` | Populated | Machine-readable resource directory |
| `/robots.txt` | Populated | Allows all AI bots |
| `/llms.txt` | Populated | LLMForge v1.0 directive |

## robots.txt Policy

The robots.txt allows all user agents and explicitly allows GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, and Applebot.

## Data Note

The `/vehicles` endpoint reports 134 total vehicles, but its crawl metadata references `friendlyford.com` (a different, unrelated Friendly Ford dealership in Roselle, IL) rather than the Monroe site `yourfriendlyford.com`. Inventory counts should therefore be treated with caution.

See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/friendly-ford/references/llms-txt.md) for the LLMForge directive.
See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/friendly-ford/references/prompts.md) for the prompt library.
