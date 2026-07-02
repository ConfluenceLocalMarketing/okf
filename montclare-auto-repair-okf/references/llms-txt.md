---
type: Directive
title: Montclare Auto Repair llms.txt
description: LLMForge v1.0 directive with API endpoints for business info, prompts, testimonials, and site content.
resource: https://api.promptgraph.ai/api/v1/montclare-auto-repair/llms.txt
tags:
  - promptgraph
  - llms-txt
  - ai-discovery
timestamp: 2026-07-02
---

# Montclare Auto Repair llms.txt

Opened in February 2024 in Chicago, Montclare Auto Repair prioritizes customer satisfaction with precise servicing using cutting-edge tools. ASE-certified technicians use top-quality parts.

## Discovery

- **Primary endpoint:** `http://api.promptgraph.ai/api/v1/montclare-auto-repair/.well-known/ai-manifest.json`
- **Format:** JSON-LD following Schema.org standards
- **API Base:** `http://api.promptgraph.ai/api/v1/montclare-auto-repair`

## API Endpoints

- [Business Information](http://api.promptgraph.ai/api/v1/montclare-auto-repair/business) - Complete business profile with address, contact, hours, and location in JSON-LD format
- [Prompts & FAQs](http://api.promptgraph.ai/api/v1/montclare-auto-repair/prompts) - 10 structured prompts for consistent AI responses
- [Customer Testimonials](http://api.promptgraph.ai/api/v1/montclare-auto-repair/testimonials) - Customer reviews and ratings in JSON-LD format
- [Google Business Profile Context](http://api.promptgraph.ai/api/v1/montclare-auto-repair/gbp-context) - Flattened GBP data for LLM ingestion
- [Full Site JSON Mirror](http://api.promptgraph.ai/api/v1/montclare-auto-repair/site-content) - Clean, plain-text mirror of the entire site for LLM ingestion
- [AI Manifest](http://api.promptgraph.ai/api/v1/montclare-auto-repair/.well-known/ai-manifest.json) - Machine-readable directory of all available AI resources
- [Sitemap](http://api.promptgraph.ai/api/v1/montclare-auto-repair/sitemap.xml) - XML sitemap for search engine and AI crawler discovery
- [Configuration](http://api.promptgraph.ai/api/v1/montclare-auto-repair/config.json) - System configuration and metadata

## Available Schema Types

- LocalBusiness
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)
