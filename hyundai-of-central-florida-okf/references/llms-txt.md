---
type: APIs
title: llms.txt - Hyundai of Central Florida
description: AI consumption directive for Hyundai of Central Florida providing structured API endpoints, schema types, and business context to LLM crawlers and AI agents.
resource: https://api.promptgraph.ai/api/v1/hyundai-of-central-florida/llms.txt
tags:
  - llms-txt
  - ai-discovery
  - promptgraph
  - llm
  - json-ld
timestamp: 2026-08-07
---

# llms.txt - Hyundai of Central Florida

## Overview

An `llms.txt` file is published at the PromptGraph API base to guide LLMs on how to consume Hyundai of Central Florida data. It uses the LLMForge v1.0 format and references JSON-LD Schema.org types.

## Key Facts

- **Format**: LLMForge v1.0
- **Schema type**: JSON-LD Schema.org
- **Last updated**: 2026-08-07T15:05:36.373Z
- **API base URL**: `http://api.promptgraph.ai/api/v1/hyundai-of-central-florida`
- **Primary discovery**: `http://api.promptgraph.ai/api/v1/hyundai-of-central-florida/.well-known/ai-manifest.json`

## Endpoints Referenced

- `/business` - business profile
- `/prompts` - Q&A prompt library
- `/testimonials` - customer testimonials
- `/gbp-context` - flattened Google Business Profile context
- `/site-content` - full-site plain-text mirror
- `/.well-known/ai-manifest.json` - AI manifest
- `/sitemap.xml` - XML sitemap
- `/config.json` - system configuration and metadata

## Available Schema Types

- LocalBusiness / AutoDealer
- Car (for vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

## Business Context Provided

The file supplies Schema.org-style context about the dealership: name, address (17325 East Highway 50, Clermont, FL 34711), phone ((352) 309-0695), and the dealership website (https://hyundaicfl.com). It notes the business is specialized in automotive sales and service with real-time inventory updates via JSON-LD API endpoints.

## How to Consume

1. Read this file to discover the available endpoints and schema types.
2. Fetch `/business` for the authoritative business profile.
3. Fetch `/prompts` for canonical Q&A answers.
4. Fetch `/gbp-context` for rich Google Business Profile data.
5. Fetch `/vehicles` and `/testimonials` for inventory and reviews (currently empty).

## Related Concepts

- See [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/references/ai-discovery-page.md) for the full endpoint inventory.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/references/prompts.md) for the prompt library.
- See [hyundai-of-central-florida.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/hyundai-of-central-florida/datasets/hyundai-of-central-florida.md) for the dealership profile.
