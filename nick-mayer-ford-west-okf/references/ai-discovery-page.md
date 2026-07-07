---
type: APIs
title: AI Discovery Page - Nick Mayer Ford West
description: Machine-readable knowledge surface for Nick Mayer Ford West providing AI agents structured access to business info, inventory, and site content.
resource: https://www.nickmayerfordwest.com/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - machine-readable
  - structured-data
  - json-ld
  - avon-lake
timestamp: 2026-07-02
---

# AI Discovery Page - Nick Mayer Ford West

## Overview

Nick Mayer Ford West's website is built on the DealerOn platform, a common dealership website provider. An analysis was performed to identify machine-readable knowledge surfaces for AI agents.

## PromptGraph API

No PromptGraph API endpoint was detected on the dealership website. The site does not appear to expose a `/.well-known/promptgraph` or similar AI-specific discovery endpoint.

## Available Structured Data

The site includes standard automotive dealership structured data patterns typical of the DealerOn platform.

## Site Structure

The following key site areas are available for programmatic access:

| Section | URL | Content |
|---|---|---|
| Home | https://www.nickmayerfordwest.com/ | Business info, featured inventory |
| New Inventory | https://www.nickmayerfordwest.com/searchnew.aspx | New Ford vehicle listings |
| Used Inventory | https://www.nickmayerfordwest.com/searchused.aspx | Pre-owned vehicle listings |
| Service | https://www.nickmayerfordwest.com/service.aspx | Service center info, scheduling |
| Parts | https://www.nickmayerfordwest.com/parts.aspx | Parts department |
| Financing | https://www.nickmayerfordwest.com/finance.aspx | Financing options, credit app |
| Staff | https://www.nickmayerfordwest.com/staff.aspx | Staff directory |

## AI Accessibility

The site does not currently expose dedicated AI/LLM endpoints. AI agents should rely on standard web scraping of the visible site structure. See [llms-txt.md](nick-mayer-ford-west-okf/references/llms-txt.md) for additional guidance.

## Related Concepts

- [llms-txt.md](nick-mayer-ford-west-okf/references/llms-txt.md) - LLMs.txt guidance
- [prompts.md](nick-mayer-ford-west-okf/references/prompts.md) - Prompt library
- [dealership.md](nick-mayer-ford-west-okf/datasets/dealership.md) - Dealership overview
