---
type: APIs
title: llms.txt - Buying Signals
description: Full llms.txt directive content for AI agent guidance, sourced from buyingsignals.com and the PromptGraph API at api.promptgraph.ai/api/v1/buying-signals/llms.txt.
resource: https://buyingsignals.com/llms.txt
tags:
  - llms-txt
  - ai-directives
  - agent-guidance
  - promptgraph
  - llm-forge
timestamp: 2026-06-26
---

# llms.txt - Buying Signals

The `llms.txt` file provides guidance for AI assistants interacting with Buying Signals.

## PromptGraph API llms.txt

The PromptGraph API at `https://api.promptgraph.ai/api/v1/buying-signals/llms.txt` provides an LLMForge v1.0 directive:

### Description

Buying Signals unifies clean data, website identity resolution, shopper behavior, targeted marketing, and AI-ready SEO into one cohesive platform. We help brands and businesses move faster, market smarter, and connect with real buyers, from website visit through the entire sales process. Our platform transforms outdated records into verified, enriched profiles and identifies anonymous website visitors to power smarter campaigns and drive measurable sales outcomes.

### Discovery

- Primary endpoint: `/api/v1/buying-signals/.well-known/ai-manifest.json`
- Format: JSON-LD following Schema.org standards
- API Base: `http://api.promptgraph.ai/api/v1/buying-signals`

### API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile (address, contact, hours, location, Schema.org LocalBusiness) |
| `/prompts` | Structured Q&A prompts for consistent AI responses |
| `/testimonials` | Customer reviews and ratings in JSON-LD format |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/.well-known/ai-manifest.json` | Machine-readable directory of all available AI resources |
| `/llms.txt` | This file |
| `/sitemap.xml` | XML sitemap for search engine and AI crawler discovery |
| `/config.json` | System configuration and metadata |

### Available Schema Types

- LocalBusiness
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

See [ai-discovery-page.md](ai-discovery-page.md) for structured semantic endpoints and AI manifest details.
