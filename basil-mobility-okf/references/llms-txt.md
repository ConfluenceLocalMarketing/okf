---
type: APIs
title: llms.txt — Basil Mobility
description: Full llms.txt directive content for AI agent guidance, sourced from the PromptGraph API at api.promptgraph.ai/api/v1/basil-mobility/llms.txt.
resource: https://api.promptgraph.ai/api/v1/basil-mobility/llms.txt
tags:
  - llms-txt
  - ai-directives
  - agent-guidance
  - promptgraph
  - llm-forge
  - mobility
timestamp: 2026-06-24
---

# llms.txt — Basil Mobility

The PromptGraph API at `https://api.promptgraph.ai/api/v1/basil-mobility/llms.txt` provides a comprehensive LLMForge v1.0 directive:

```
# Basil Mobility
# Format: LLMForge v1.0
# Last Updated: 2026-06-24T12:37:23.228Z
# Schema: JSON-LD (Schema.org)
# Primary Discovery: http://api.promptgraph.ai/api/v1/basil-mobility/.well-known/ai-manifest.json
```

### Description

Basil Mobility is an authorized BraunAbility dealer providing comprehensive maintenance, mechanical and body repair services for wheelchair-accessible vehicles, adaptive driving equipment, lifts, and mobility solutions.

### Discovery

- Primary endpoint: `/api/v1/basil-mobility/.well-known/ai-manifest.json`
- Format: JSON-LD following Schema.org standards
- Update frequency: Real-time
- CORS: Enabled for all origins
- API Base: `http://api.promptgraph.ai/api/v1/basil-mobility`

### API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile (address, contact, hours, location, Schema.org LocalBusiness) |
| `/vehicles` | Complete inventory of 1,158 vehicles with specifications, pricing, and availability |
| `/prompts` | 74 structured Q&A prompts for consistent AI responses |
| `/testimonials` | Customer reviews and ratings in JSON-LD format |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/.well-known/ai-manifest.json` | Machine-readable directory of all available AI resources |
| `/llms.txt` | This file |
| `/sitemap.xml` | XML sitemap for search engine and AI crawler discovery |
| `/config.json` | System configuration and metadata |
| `/robots.txt` | Robots exclusion rules |

### Available Schema Types

- LocalBusiness / AutoDealer
- Car (for vehicle inventory)
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

### Featured Vehicles

| Vehicle | VIN | Price |
|---|---|---|
| 2026 Chrysler Pacifica (BraunAbility) | 2C4RC1FGXRR191633 | $55,980 |
| 2026 Toyota Sienna (BraunAbility XT) | 5TDYRKEC2SS281922 | $88,150 |

### Prompt Library (74 Questions)

The PromptGraph API exposes 74 structured prompt/response pairs covering:

- **Vehicle Shopping:** Side-entry vans, rear-entry vans, lowered-floor vehicles, hybrid accessible vans, Chrysler Pacifica conversions, Toyota hybrid minivans, custom conversions
- **Adaptive Equipment:** Hand controls, steering aids, transfer seats, wheelchair lifts, power ramp installation, tie-down systems, custom interior modifications
- **Service & Repair:** Ramp and lift repair, power door troubleshooting, hydraulic lift repair, electronic diagnostics, brake repairs, powertrain repairs, air filter replacement, oil changes
- **Financing:** BraunAbility financing, low-income approvals, trade-in appraisals, grant navigation, veteran programs
- **Rentals:** Short and long-term accessible van rentals
- **Dealership:** Customer service, family-oriented support, first-time buyer assistance, shuttle service, reviews

See [ai-discovery-page.md](ai-discovery-page.md) for structured semantic endpoints and AI manifest details.
See [prompts.md](prompts.md) for the complete PromptGraph prompt library.
