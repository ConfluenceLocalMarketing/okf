---
type: APIs
title: AI Discovery Page — Kruse Motors
description: Machine-readable knowledge base and semantic data endpoints for Kruse Motors, providing AI agents structured access to business info, vehicle inventory, customer reviews, and recommended actions via PromptGraph.
resource: https://krusemotors.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
timestamp: 2026-06-26
---

# AI Discovery Page — Kruse Motors

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by PromptGraph. It exposes semantic endpoints, business metadata, and LLM-friendly data for Kruse Motors.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/kruse-motors/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/sitemap-inventory.xml` | 0.8 | Daily |
| `/robots.txt` | 0.5 | Monthly |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Name:** Kruse Motors
- **Description:** Kruse Motors is proud to serve our customers around the Marshall area and worldwide as your certified dealer for Ford, Lincoln, Buick, and GMC.
- **Last updated:** 2026-06-25T17:27:12.157Z
- **Schema types:** LocalBusiness, AutoDealer, Car, ItemList
- **Contact:** kendallbillman@gmail.com

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/llms.txt` | LLMs.txt directive |
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ content |
| `/testimonials` | Customer reviews |
| `/sitemap.xml` | Full sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |

### Additional PromptGraph Endpoints

| Endpoint | Description |
|---|---|
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/llms.txt` | LLMForge v1.0 directive file |
| `/offers` | Current specials and incentives |

## Business Profile (Schema.org AutoDealer)

From `https://api.promptgraph.ai/api/v1/kruse-motors/business`:

- **Name:** Kruse Motors Auto Group
- **Type:** AutoDealer (Schema.org)
- **Additional Types:** Ford dealer, Car dealer, GMC dealer, Buick dealer, Truck dealer, Used car dealer, Used truck dealer, Car leasing service, Motor vehicle dealer, Lincoln dealer
- **Address:** 1651 East College Drive, Marshall, MN 56258
- **Geo:** 44.4516, -95.7517
- **Telephone:** (507) 337-7500
- **Email:** kendallbillman@gmail.com
- **URL:** https://www.krusemotors.com/
- **Aggregate Rating:** 4.6/5.0 (1,259 reviews)
- **Date Modified:** 2026-02-03T15:05:04.755Z

See [dealership.md](/datasets/dealership.md) for the full business profile.
See [llms-txt.md](llms-txt.md) for the complete llms.txt directive.
See [testimonials.md](testimonials.md) for customer reviews.
