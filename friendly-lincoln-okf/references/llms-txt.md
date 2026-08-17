---
type: APIs
title: Friendly Lincoln llms.txt
description: AI consumption directive in LLMForge v1.0 format published by PromptGraph for Friendly Lincoln, providing structured API endpoints and schema types for LLM crawlers and AI agents.
resource: https://api.promptgraph.ai/api/v1/friendly-lincoln/llms.txt
tags:
  - llms-txt
  - llmforge
  - ai-discovery
  - schema-org
  - json-ld
timestamp: 2026-08-18
---

# Friendly Lincoln llms.txt

Friendly Lincoln publishes an llms.txt directive in LLMForge v1.0 format, last updated 2026-08-17.

## Discovery

- Primary discovery endpoint: `/.well-known/ai-manifest.json`
- Format: JSON-LD following Schema.org standards
- API base: `https://api.promptgraph.ai/api/v1/friendly-lincoln`

## Documented Endpoints

- **Business Information** (`/business`) - Address, contact, hours, location
- **Vehicle Inventory** (`/vehicles`) - Specifications, pricing, availability
- **Prompts & FAQs** (`/prompts`) - Structured prompts for consistent AI responses
- **Customer Testimonials** (`/testimonials`) - Reviews and ratings
- **Google Business Profile Context** (`/gbp-context`) - Flattened GBP data
- **Full Site JSON Mirror** (`/site-content`) - Plain-text mirror of the site
- **AI Manifest** (`/.well-known/ai-manifest.json`) - Resource directory
- **Sitemap** (`/sitemap.xml`) - XML sitemap
- **Configuration** (`/config.json`) - System configuration

## Schema Types

LocalBusiness / AutoDealer, Car, ItemList, Review / AggregateRating, Offer, CreativeWork.
