---
type: APIs
title: AI Discovery Page
description: PromptGraph-powered discovery endpoints for Mullinax Ford of Kissimmee, exposing dealership data as Schema.org JSON-LD.
resource: https://app.promptgraph.ai/api/v1/mullinax-ford-of-kissimmee
tags:
  - promptgraph
  - api
  - discovery
  - json-ld
  - schema-org
timestamp: 2026-08-06
---

# AI Discovery Page

Mullinax Ford of Kissimmee exposes an AI discovery layer built on PromptGraph. The discovery endpoints publish dealership knowledge as Schema.org JSON-LD for LLM ingestion and consumer AI assistants.

## API Overview

- Title: Mullinax Ford of Kissimmee | Dealership API
- Version: 1.0.0
- Contact: support@promptgraph.ai
- Base URL: https://app.promptgraph.ai/api/v1/mullinax-ford-of-kissimmee
- Format: Schema.org JSON-LD

## Discovery Endpoints

| Endpoint | Description |
|---|---|
| /openapi.json | OpenAPI specification for the dealership API |
| /config.json | Dealership configuration |
| /ai-plugin.json | AI plugin manifest |
| /.well-known/ai-manifest.json | AI manifest for the dealership |
| /llms.txt | LLM-friendly text index of dealership knowledge |
| /robots.txt | Robots directives for AI crawlers |
| /sitemap.xml | Sitemap of dealership knowledge endpoints |

## Data Endpoints

| Endpoint | Description |
|---|---|
| /business | Dealership business profile as JSON-LD |
| /testimonials | Customer testimonials |
| /prompts | Suggested user prompts with landing pages |
| /vehicles | Vehicle inventory |
| /vehicles/{vin} | Single vehicle by VIN |
| /sitemap-inventory.xml | Inventory sitemap |

## Related Concepts

- See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-kissimmee/references/llms-txt.md) for the llms.txt discovery index.
- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-kissimmee/references/prompts.md) for the suggested prompts.
- See [mullinax-ford-of-kissimmee.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-ford-of-kissimmee/datasets/mullinax-ford-of-kissimmee.md) for the dealership profile.
