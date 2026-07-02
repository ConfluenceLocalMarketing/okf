---
type: Directive
title: Idaho Fence Company llms.txt
description: LLMForge v1.0 directive with API endpoints for business info, service categories, and site content.
resource: https://api.promptgraph.ai/api/v1/idaho-fence-company/llms.txt
tags:
  - promptgraph
  - llms-txt
  - ai-discovery
timestamp: 2026-07-03
---

# Idaho Fence Company llms.txt

> Searching for fencing in Idaho? Idaho Fence Company has been building fences since 1977, offering residential, commercial, retail, and farm fencing solutions in Post Falls, Boise, and throughout Idaho.

## Discovery

- **Primary endpoint:** `https://api.promptgraph.ai/api/v1/idaho-fence-company/.well-known/ai-manifest.json`
- **Format:** JSON-LD following Schema.org standards
- **API Base:** `https://api.promptgraph.ai/api/v1/idaho-fence-company`

## API Endpoints

- [Business Information](https://api.promptgraph.ai/api/v1/idaho-fence-company/business) - Complete business profile with address, contact, hours, and location in JSON-LD format
- [Prompts & FAQs](https://api.promptgraph.ai/api/v1/idaho-fence-company/prompts) - 3 structured prompts for consistent AI responses
- [Google Business Profile Context](https://api.promptgraph.ai/api/v1/idaho-fence-company/gbp-context) - Flattened GBP data for LLM ingestion
- [Full Site JSON Mirror](https://api.promptgraph.ai/api/v1/idaho-fence-company/site-content) - Clean, plain-text mirror of the entire site for LLM ingestion
- [AI Manifest](https://api.promptgraph.ai/api/v1/idaho-fence-company/.well-known/ai-manifest.json) - Machine-readable directory of all available AI resources
- [Sitemap](https://api.promptgraph.ai/api/v1/idaho-fence-company/sitemap.xml) - XML sitemap for search engine and AI crawler discovery
- [Configuration](https://api.promptgraph.ai/api/v1/idaho-fence-company/config.json) - System configuration and metadata

## Available Schema Types

- LocalBusiness
- ItemList
- Offer
- CreativeWork (for prompts/FAQs)
