---
type: APIs
title: AI Discovery Page - Genesis Montgomery
description: Genesis Montgomery exposes AI discovery endpoints through PromptGraph, including business data, inventory, prompts, an AI manifest, llms.txt, and a robots.txt policy that allows AI crawlers.
resource: https://api.promptgraph.ai/api/v1/genesis-montgomery
tags:
  - ai-discovery
  - promptgraph
  - llms-txt
  - ai-manifest
  - api
  - robots-txt
timestamp: 2026-08-08
---

# AI Discovery Page - Genesis Montgomery

## Overview

Genesis Montgomery participates in AI discovery through a PromptGraph account (slug: `genesis-montgomery`). The AI discovery hub is not separately configured; discovery is served through PromptGraph endpoints. A sitemap of the AI-facing resources is published at:

https://api.promptgraph.ai/api/v1/genesis-montgomery/sitemap.xml

## AI Discovery Endpoints

| Endpoint | Resource Type | Status |
|---|---|---|
| /business | Structured business profile (JSON-LD AutoDealer) | Available |
| /prompts | ItemList of 20 AI prompts | Available |
| /.well-known/ai-manifest.json | AI manifest (v1.0) | Available |
| /robots.txt | AI crawler policy | Available |
| /llms.txt | LLMForge v1.0 llms.txt | Available |
| /gbp-context | Google Business Profile context | Available |
| /vehicles | Vehicle inventory (ItemList of Car) | Available (empty) |
| /offers | Special offers (ItemList) | Available (empty) |
| /testimonials | Customer testimonials | Available (empty) |
| /site-content | Crawled site content | Available (empty) |
| /openapi.json | OpenAPI spec for discovery + data endpoints | Available |
| /sitemap-inventory.xml | Inventory sitemap | Listed in OpenAPI |
| /vehicles/{vin} | Single-vehicle detail by VIN | Listed in OpenAPI |
| /config.json | Configuration | Listed in OpenAPI |
| /ai-plugin.json | AI plugin manifest | Listed in OpenAPI |

## AI Manifest

The AI manifest (version 1.0) declares schema types: LocalBusiness, AutoDealer, Car, ItemList. Endpoints declared include llms_txt, business, vehicles, prompts, testimonials, sitemap, robots, and config.

## robots.txt Policy

The robots.txt explicitly allows major AI crawlers, including: GPTBot, Claude-Web, GoogleOther, PerplexityBot, anthropic-ai, Grok-Bot, and Applebot.

## llms.txt

A formatted llms.txt is served at /llms.txt using the LLMForge v1.0 format, last updated 2026-08-07. See [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/references/llms-txt.md).

## Related Concepts

- See [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/references/prompts.md) for the published prompt set.
- See [dealership.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/datasets/dealership.md) for the business profile data served through these endpoints.
