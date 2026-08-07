---
type: APIs
title: llms.txt - Genesis of Central Florida
description: AI consumption directive for Genesis of Central Florida providing structured API endpoints, schema types, and business context to LLM crawlers and AI agents.
resource: https://api.promptgraph.ai/api/v1/genesis-of-central-florida/llms.txt
tags:
  - llms-txt
  - ai-discovery
  - promptgraph
  - llm
  - json-ld
timestamp: 2026-08-08
---

# llms.txt - Genesis of Central Florida

## Overview

An `llms.txt` file is published at the PromptGraph API base to guide LLMs on how to consume Genesis of Central Florida data. It uses the LLMForge v1.0 format and references JSON-LD Schema.org types.

## Key Facts

- **Format**: LLMForge v1.0
- **Schema type**: JSON-LD (Schema.org)
- **Last updated**: 2026-08-07T16:03:50.778Z
- **API base URL**: `http://api.promptgraph.ai/api/v1/genesis-of-central-florida`
- **Primary discovery**: `http://api.promptgraph.ai/api/v1/genesis-of-central-florida/.well-known/ai-manifest.json`

## Endpoints Referenced

- `/business` - business profile
- `/vehicles` - vehicle inventory feed
- `/prompts` - Q&A prompt library
- `/testimonials` - customer testimonials
- `/gbp-context` - Google Business Profile context
- `/site-content` - full site plain-text mirror
- `/.well-known/ai-manifest.json` - AI manifest
- `/sitemap.xml` - XML sitemap

## Available Schema Types

- LocalBusiness / AutoDealer
- Car (for vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

## Business Context Provided

The file supplies Schema.org-style context about the dealership: name, address (4500 Collina Terrace, Clermont, FL 34711), phone (407) 544-5196, and link to the dealership website (https://genesiscfl.com).

## How to Consume

1. Read this file to discover the available endpoints and schema types.
2. Fetch `/business` for the authoritative business profile.
3. Fetch `/prompts` for canonical Q&A answers.
4. Fetch `/vehicles` and `/testimonials` for inventory and reviews (currently empty; use the dealership website inventory API for current stock).

## Related Concepts

- See [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/references/ai-discovery-page.md) for the full endpoint inventory.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/references/prompts.md) for the prompt library.
- See [genesis-of-central-florida.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-of-central-florida/datasets/genesis-of-central-florida.md) for the dealership profile.
