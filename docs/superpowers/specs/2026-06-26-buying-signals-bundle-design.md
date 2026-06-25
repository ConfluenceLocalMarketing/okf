# Buying Signals OKF Bundle — Design Spec

## Overview

Create an OKF v0.1 bundle for **Buying Signals**, a marketing technology and data services company based in San Leandro, CA and Grapevine, TX. The bundle provides structured, AI-consumable knowledge about the company, its full product catalog, and its machine-readable PromptGraph API surface.

## Bundle Name

`buying-signals-okf/`

## Source URLs

- https://buyingsignals.com/ — main company site
- https://buyingsignals.com/ai-discovery-page/ — AI discovery surface
- https://api.promptgraph.ai/api/v1/buying-signals/sitemap.xml — PromptGraph sitemap
- https://api.promptgraph.ai/api/v1/buying-signals/.well-known/ai-manifest.json — AI Manifest
- https://api.promptgraph.ai/api/v1/buying-signals/business — Business profile (JSON-LD)
- https://api.promptgraph.ai/api/v1/buying-signals/prompts — Q&A prompt library
- https://api.promptgraph.ai/api/v1/buying-signals/llms.txt — LLMForge directive
- Web search for broader company context

## Bundle Structure

```
buying-signals-okf/
├── index.md                               # Bundle entry point
├── datasets/
│   ├── index.md                           # Dataset index
│   ├── company.md                         # Organization profile
│   ├── buying-signals-ai.md               # Conversational AI agents
│   ├── connect-suite.md                   # Cross-platform connectivity
│   ├── consumer-intelligence.md           # Buyer behavior analytics
│   ├── data-hygiene.md                    # Data hygiene, enrichment & DMS Sync
│   ├── geo-signals.md                     # Location-based targeting
│   ├── insight-pixel.md                   # Website visitor identification
│   ├── smart-conquest.md                  # Competitor conquesting
│   ├── marketing-suite.md                 # Omnichannel programmatic advertising
│   ├── business-intelligence.md           # Analytics & BI platform
│   ├── ai-seo.md                          # AI SEO for ChatGPT, Claude, Gemini, Grok
│   └── strategic-consulting.md            # Executive consulting
├── references/
│   ├── index.md                           # Reference index
│   ├── ai-discovery-page.md               # Machine-readable AI surface + PromptGraph
│   ├── llms-txt.md                        # LLMForge directive
│   └── prompts.md                         # PromptGraph Q&A library
└── tables/
    ├── index.md                           # Tables index
    └── product-comparison.md              # All services side-by-side
```

## Concepts

### Datasets

| File | Type | Description |
|---|---|---|
| `company.md` | Organization | Company profile with address, contact, leadership, history, industries served |
| `buying-signals-ai.md` | Product | Conversational AI agent platform for lead conversion |
| `connect-suite.md` | Product | Cross-platform integration hub for social, data, campaigns, CRM |
| `consumer-intelligence.md` | Product | Buyer behavior analytics and audience insights |
| `data-hygiene.md` | Product | Data cleansing, enrichment, DMS sync services |
| `geo-signals.md` | Product | Location-based consumer targeting (geo-framing, location IQ) |
| `insight-pixel.md` | Product | Anonymous website visitor identification and identity resolution |
| `smart-conquest.md` | Product | Competitive conquesting and competitor audience targeting |
| `marketing-suite.md` | Product | Omnichannel programmatic advertising (Display, CTV, OTT, Radio, SEM, Social) |
| `business-intelligence.md` | Product | Analytics and BI platform for marketing measurement |
| `ai-seo.md` | Product | AI-ready SEO services for ChatGPT, Claude, Gemini, Grok |
| `strategic-consulting.md` | Product | Executive-level marketing and data strategy consulting |

### References

| File | Type | Description |
|---|---|---|
| `ai-discovery-page.md` | AI-Discovery-Page | Structured semantic endpoints, AI Manifest, PromptGraph API |
| `llms-txt.md` | Directive | LLMForge v1.0 directive with API endpoints and schema types |
| `prompts.md` | Prompt-Library | Complete PromptGraph Q&A prompt library |

### Tables

| File | Type | Description |
|---|---|---|
| `product-comparison.md` | Comparison-Matrix | Side-by-side comparison of all Buying Signals products |

## Relationships

- **company** develops all **product** concepts and operates the **ai-discovery-page**
- **ai-discovery-page** exposes structured data for the **company**, all **products**, and **prompts**
- **llms-txt** provides top-level agent guidance
- **prompts** provides AI-consumable Q&A covering all concepts
- **product-comparison** provides structured comparison data across all products

## Key Data Points

- **Legal name:** Buying Signals
- **Type:** LocalBusiness (Marketing Data & Analytics, Business Intelligence Platform, Advertising Services)
- **Addresses:** 151 Callan Ave, Suite 301, San Leandro, CA 94577; 601 W. Northwest Hwy, Suite 100, Grapevine, TX 76051
- **Phone:** (510) 343-5555 / (817) 527-1932
- **Emails:** info@buyingsignals.com, sales@buyingsignals.com
- **Social:** Facebook, Instagram, LinkedIn
- **Industries:** Auto, retail, home services, 2A/FFL
- **Years in business:** 15+
- **PromptGraph API base:** `https://api.promptgraph.ai/api/v1/buying-signals/`
- **Schema types:** LocalBusiness, ItemList, Review/AggregateRating, Offer, CreativeWork

## Exclusions

- No vehicle/dealership content (PromptGraph's `AutoDealer`/`Car` schema types are template artifacts)
- No pricing table (no public pricing available)
- DMS Sync merged into `data-hygiene.md` (same data quality workflow)
- Four AI SEO sub-services merged into one `ai-seo.md`
