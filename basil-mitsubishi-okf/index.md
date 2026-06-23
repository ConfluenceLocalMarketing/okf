---
type: bundle
title: Basil Mitsubishi OKF Bundle
description: Open Knowledge Format bundle for Basil Mitsubishi — a full-service Mitsubishi dealership in Buffalo, NY. Covers the dealership, AI discovery endpoints, vehicle inventory, and machine-readable directives.
resource: https://www.basilmitsubishi.com/
tags:
  - okf-bundle
  - basil-mitsubishi
  - dealership
  - buffalo-ny
timestamp: 2026-06-24
---

# Basil Mitsubishi OKF Bundle

## datasets/

| File | Type | Description |
|---|---|---|
| [dealership.md](datasets/dealership.md) | `organization` | Business profile, hours, contact, services, location |
| [new-vehicles.md](datasets/new-vehicles.md) | `product-line` | New Mitsubishi model lineup, features, promotions |
| [used-vehicles.md](datasets/used-vehicles.md) | `product-line` | Pre-owned and certified pre-owned inventory, trade-in |

## references/

| File | Type | Description |
|---|---|---|
| [llms-txt.md](references/llms-txt.md) | `reference` | llms.txt directive content for AI agent guidance |
| [ai-discovery-page.md](references/ai-discovery-page.md) | `ai-discovery-page` | Structured semantic endpoints, LLM actions, machine-readable data |

## tables/

*(empty — add tabular data extracts here)*

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **ai-discovery-page** exposes structured data for the **dealership** and both vehicle lines
- **llms-txt** provides top-level agent guidance for the entire site
