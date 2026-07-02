---
type: APIs
title: AI Discovery Page - Nick Mayer Ford
description: Machine-readable knowledge surface for Nick Mayer Ford providing AI agents structured access to business info, inventory, and site content.
resource: https://www.nickmayerford.com/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - machine-readable
  - structured-data
  - json-ld
  - mayfield-heights
timestamp: 2026-07-02
---

# AI Discovery Page - Nick Mayer Ford

## Overview

Nick Mayer Ford's website is built on the DealerOn platform, a common dealership website provider. An analysis was performed to identify machine-readable knowledge surfaces for AI agents.

## PromptGraph API

No PromptGraph API endpoint was detected on the dealership website. The site does not appear to expose a `/.well-known/promptgraph` or similar AI-specific discovery endpoint.

## Available Structured Data

The site includes standard automotive dealership structured data patterns typical of the DealerOn platform.

## Site Structure

The following key site areas are available for programmatic access:

| Section | URL | Content |
|---|---|---|
| Home | https://www.nickmayerford.com/ | Business info, featured inventory |
| New Inventory | https://www.nickmayerford.com/searchnew.aspx | New Ford vehicle listings |
| Used Inventory | https://www.nickmayerford.com/searchused.aspx | Pre-owned vehicle listings |
| Service | https://www.nickmayerford.com/service.aspx | Service center info, scheduling |
| Parts | https://www.nickmayerford.com/parts.aspx | Parts department |
| Financing | https://www.nickmayerford.com/finance.aspx | Financing options, credit app |
| Staff | https://www.nickmayerford.com/staff.aspx | Staff directory |

## AI Accessibility

The site does not currently expose dedicated AI/LLM endpoints. AI agents should rely on standard web scraping of the visible site structure. See [llms-txt.md](llms-txt.md) for additional guidance.

## Related Concepts

- [llms-txt.md](llms-txt.md) - LLMs.txt guidance
- [prompts.md](prompts.md) - Prompt library
- [dealership.md](/datasets/dealership.md) - Dealership overview
