---
type: APIs
title: AI Discovery Page - West Hills Chrysler Jeep Dodge RAM
description: Assessment of AI-facing infrastructure for West Hills CJDR. The Dealer.com-powered site does not host an AI Discovery Page, llms.txt, or PromptGraph API endpoints as of July 2026. (synthesized)
resource: https://www.westhillscjd.com/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - machine-readable
  - structured-data
  - json-ld
  - bremerton
  - chrysler
  - jeep
  - dodge
  - ram
timestamp: 2026-07-01
---

# AI Discovery Page - West Hills Chrysler Jeep Dodge RAM

As of July 2026, West Hills Chrysler Jeep Dodge RAM does **not** host an AI Discovery Page, `llms.txt`, or PromptGraph API. The site is built on the **Dealer.com** platform but lacks the optional AI-facing infrastructure that some Dealer.com sites have enabled.

## Tested Endpoints

The following were checked and returned errors or 404:

| Resource | URL | Status |
|---|---|---|
| AI Discovery Page | `/ai-discovery-page.htm` | 404 Not Found |
| LLMs.txt | `/llms.txt` | Served sitemap-style TXT content, not llms.txt |
| AI Manifest | `/.well-known/ai-manifest.json` | 404 Not Found |
| PromptGraph API | `https://api.promptgraph.ai/api/v1/westhillscjd/business` | Not Found |
| PromptGraph API | `https://api.promptgraph.ai/api/v1/west-hills-chrysler-jeep-dodge-ram/business` | Not Found |

## Available Structured Data

While no dedicated AI surface exists, the site provides:

- **Schema.org JSON-LD** embedded in pages (auto dealer, vehicle, local business markup via Dealer.com platform)
- **Standard sitemap** at `/sitemap.xml`
- **Robots.txt** at `/robots.txt`
- **Standard HTML metadata** including Open Graph and meta descriptions

## Recommendation

To enable AI agent discovery, the dealership could enable a PromptGraph integration (available on Dealer.com), add an `llms.txt` file, or create an AI Discovery Page at `/ai-discovery-page.htm` — all supported by the Dealer.com platform but not currently activated.

See [llms-txt.md](west-hills-chrysler-jeep-dodge-ram-okf/references/llms-txt.md) for the llms.txt assessment.
