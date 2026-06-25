---
type: ai-discovery-page
title: AI Discovery Page — Buying Signals
description: Machine-readable knowledge base and semantic data endpoints for Buying Signals, providing AI agents structured access to business info, product data, and recommended actions via PromptGraph.
resource: https://buyingsignals.com/ai-discovery-page/
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

# AI Discovery Page — Buying Signals

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by PromptGraph. It exposes semantic endpoints, business metadata, and LLM-friendly data.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/buying-signals/sitemap.xml` exposes these machine-readable endpoints:

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

- **Name:** Buying Signals
- **Description:** Buying Signals unifies clean data, website identity resolution, shopper behavior, targeted marketing, and AI-ready SEO into one cohesive platform.
- **Last updated:** 2026-06-25T16:59:10.776Z
- **Schema types:** LocalBusiness, AutoDealer, Car, ItemList
- **Contact:** info@buyingsignals.com

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

## Business Profile (Schema.org LocalBusiness)

From `https://api.promptgraph.ai/api/v1/buying-signals/business`:

- **Name:** Buying Signals
- **Type:** LocalBusiness (Schema.org)
- **Additional Types:** Marketing Data & Analytics, Business Intelligence Platform, Advertising Services, Lead Generation, Data Processing Service, Marketing Consultant
- **Address:** 151 Callan Ave, Suite 301, San Leandro, CA 94577
- **Geo:** 37.7245, -122.1553
- **Telephone:** (510) 343-5555
- **Email:** info@buyingsignals.com
- **URL:** https://buyingsignals.com/
- **Date Modified:** 2026-04-14T01:25:54.440Z

See [company.md](/datasets/company.md) for the full business profile.
See [llms-txt.md](llms-txt.md) for the complete llms.txt directive.
