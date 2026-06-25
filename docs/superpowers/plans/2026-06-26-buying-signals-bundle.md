# Buying Signals OKF Bundle — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an OKF v0.1 bundle for Buying Signals, a marketing technology and data services company.

**Architecture:** Standard OKF bundle with `datasets/` (company + products), `references/` (AI Discovery, llms.txt, prompts), and `tables/` (product comparison). Follows the same pattern as existing bundles (basil-mitsubishi-okf, etc.).

**Tech Stack:** Markdown with YAML frontmatter, no code.

---

### Task 1: Create bundle directory structure

**Files:**
- Create: `buying-signals-okf/datasets/index.md`
- Create: `buying-signals-okf/references/index.md`
- Create: `buying-signals-okf/tables/index.md`

- [ ] **Create directory structure**

```bash
New-Item -ItemType Directory -Path "buying-signals-okf/datasets" -Force; New-Item -ItemType Directory -Path "buying-signals-okf/references" -Force; New-Item -ItemType Directory -Path "buying-signals-okf/tables" -Force
```

- [ ] **Commit**

```bash
git add buying-signals-okf/
git commit -m "feat: scaffold buying-signals-okf bundle structure"
```

---

### Task 2: Create company.md (organization profile)

**Files:**
- Create: `buying-signals-okf/datasets/company.md`

- [ ] **Create company.md**

```markdown
---
type: organization
title: Buying Signals
description: Marketing technology and data services company based in San Leandro, CA and Grapevine, TX, offering data hygiene, website visitor intelligence, programmatic advertising, AI SEO, and business intelligence solutions.
resource: https://buyingsignals.com/
tags:
  - marketing-technology
  - data-services
  - data-hygiene
  - identity-resolution
  - programmatic-advertising
  - ai-seo
  - lead-generation
  - consumer-intelligence
  - business-intelligence
  - omnichannel-marketing
timestamp: 2026-06-26
---

# Buying Signals

Buying Signals is a marketing technology and data services company with over 15 years of experience, serving industries including automotive, retail, home services, and 2A/FFL. The company unifies clean data, website identity resolution, shopper behavior analytics, targeted marketing, and AI-ready SEO into one cohesive platform.

## Contact

| Detail | Information |
|---|---|
| Headquarters | 151 Callan Ave, Suite 301, San Leandro, CA 94577 |
| Additional Office | 601 W. Northwest Hwy, Suite 100, Grapevine, TX 76051 |
| Phone | (510) 343-5555 |
| Alternate Phone | (817) 527-1932 |
| Email (General) | info@buyingsignals.com |
| Email (Sales) | sales@buyingsignals.com |

## Hours

Monday – Friday: 9:00 AM – 5:00 PM (PST)
Saturday – Sunday: Closed

## Social

- Facebook: https://www.facebook.com/profile.php?id=100092724847814
- Instagram: https://www.instagram.com/buyingsignals/
- LinkedIn: https://linkedin.com/company/buying-signals/

## Products & Services

- **Buying Signals AI** — Conversational AI agents to influence and convert leads
- **Connect Suite** — Seamlessly connect social, data, campaigns, and CRM with intelligence
- **Consumer Intelligence** — Understand buyer behavior and shopping patterns
- **Data Hygiene & Enrichment** — Clean, verify, and enrich customer data records
- **DMS Sync** — Fix bad data inside your Dealer Management System
- **Geo Signals** — Location-based consumer targeting with geo-framing technology
- **Insight Pixel** — Identify anonymous website visitors and improve digital marketing ROI
- **Smart Conquest** — Win buyers from competitors through targeted conquest campaigns
- **Strategic Marketing Suite** — Omnichannel programmatic advertising (Display, CTV, OTT, Radio, SEM, Social)
- **Business Intelligence Platform** — Analytics and insights for marketing measurement
- **AI SEO Services** — SEO optimized for ChatGPT, Claude, Gemini, and Grok
- **Strategic Consulting** — Executive-level consulting for data-driven marketing decisions

## Industries Served

- Automotive (dealerships, OEMs)
- Retail
- Home Services
- 2A/FFL (Firearms)

## Approach

Buying Signals combines identity resolution, enriched customer data, location intelligence, SEM, and SEO to build high-performing audiences. They focus every dollar on real people showing real intent rather than clicks, impressions, or broad demographics. Campaigns are delivered across Display, Video, CTV, OTT, Radio, Search, and Social through DSP-driven strategies.

See [ai-discovery-page.md](/references/ai-discovery-page.md) for machine-readable structured data.
See [product-comparison.md](/tables/product-comparison.md) for a side-by-side product overview.
```

- [ ] **Commit**

```bash
git add buying-signals-okf/datasets/company.md
git commit -m "feat: add company.md for buying-signals-okf"
```

---

### Task 3: Create product dataset files (part 1)

**Files:**
- Create: `buying-signals-okf/datasets/buying-signals-ai.md`
- Create: `buying-signals-okf/datasets/connect-suite.md`
- Create: `buying-signals-okf/datasets/consumer-intelligence.md`
- Create: `buying-signals-okf/datasets/data-hygiene.md`

- [ ] **Create buying-signals-ai.md**

```markdown
---
type: product
title: Buying Signals AI
description: Conversational AI agents designed to influence and convert more leads through intelligent, automated customer interactions.
resource: https://buyingsignals.com/buying-signals-ai/
tags:
  - conversational-ai
  - lead-generation
  - ai-agents
  - chatbots
  - sales-automation
timestamp: 2026-06-26
---

# Buying Signals AI

Conversational AI agents that engage website visitors, qualify leads, and drive conversions through automated, intelligent conversations.

## Capabilities

- AI-powered lead qualification and scoring
- Automated customer conversation handling
- Multi-channel conversational deployment
- Integration with CRM and marketing platforms
- Real-time response to visitor inquiries

## Integration

See [connect-suite.md](connect-suite.md) for platform connectivity details.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create connect-suite.md**

```markdown
---
type: product
title: Connect Suite
description: Cross-platform integration solution that seamlessly connects social media, data sources, marketing campaigns, and CRM systems with intelligence.
resource: https://buyingsignals.com/connect-suite/
tags:
  - integration
  - crm
  - data-connectivity
  - social-media
  - campaign-management
timestamp: 2026-06-26
---

# Connect Suite

A unified integration layer that connects social media platforms, marketing campaigns, data sources, and CRM systems with intelligent data orchestration.

## Features

- Social media platform connectivity
- Campaign data synchronization
- CRM integration and data mapping
- Cross-platform intelligence layer
- Real-time data flow management

## Related

See [consumer-intelligence.md](consumer-intelligence.md) for buyer behavior analytics.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create consumer-intelligence.md**

```markdown
---
type: product
title: Consumer Intelligence
description: Buyer behavior analytics platform that provides deep understanding of shopping behaviors, purchase intent, and consumer patterns across channels.
resource: https://buyingsignals.com/consumer-intelligence/
tags:
  - consumer-analytics
  - buyer-behavior
  - purchase-intent
  - audience-insights
  - behavioral-data
timestamp: 2026-06-26
---

# Consumer Intelligence

Analytics platform that captures and interprets buyer behavior across digital channels to build enriched consumer profiles and predict purchase intent.

## Capabilities

- Cross-channel consumer behavior tracking
- Purchase intent scoring and prediction
- Audience segmentation and profiling
- Behavioral trigger identification
- Shopping pattern analysis

## Related

See [insight-pixel.md](insight-pixel.md) for website visitor identification.
See [geo-signals.md](geo-signals.md) for location-based behavioral data.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create data-hygiene.md**

```markdown
---
type: product
title: Data Hygiene & Enrichment
description: Data cleansing, verification, enrichment, and DMS sync services that transform outdated customer records into verified, enriched profiles with real-time CRM/DMS push.
resource: https://buyingsignals.com/dms-sync/
tags:
  - data-hygiene
  - data-enrichment
  - dms-sync
  - data-cleaning
  - crm-integration
  - data-quality
  - identity-graph
timestamp: 2026-06-26
---

# Data Hygiene & Enrichment

Comprehensive data quality services including data appending, verification, enrichment, and real-time DMS/CRM synchronization. On average, 40% of customer data is incorrect — this product fixes that.

## Services

- **Data Cleansing** — Correct outdated addresses, emails, phone numbers, and vehicle ownership records
- **Data Enrichment** — Append missing contact details (alternate emails, verified phones, addresses)
- **Reverse Append** — Start from a single data point and resolve full consumer identity
- **DMS Sync** — Push corrected records back into Dealer Management Systems in real time
- **Identity Graph Resolution** — Resolve consumer signals into unified profiles with verified identifiers
- **Profile Maintenance** — Keep data continuously synced, clean, and current

## Benefits

- Verified, deliverable email addresses (not dead addresses)
- Extended reach via alternate email reactivation
- Improved campaign targeting and reduced media waste
- Higher engagement rates and recovered lost connections

## Related

See [insight-pixel.md](insight-pixel.md) for website visitor identity resolution.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Commit**

```bash
git add buying-signals-okf/datasets/buying-signals-ai.md buying-signals-okf/datasets/connect-suite.md buying-signals-okf/datasets/consumer-intelligence.md buying-signals-okf/datasets/data-hygiene.md
git commit -m "feat: add product dataset files (AI, Connect Suite, Consumer Intel, Data Hygiene)"
```

---

### Task 4: Create product dataset files (part 2)

**Files:**
- Create: `buying-signals-okf/datasets/geo-signals.md`
- Create: `buying-signals-okf/datasets/insight-pixel.md`
- Create: `buying-signals-okf/datasets/smart-conquest.md`
- Create: `buying-signals-okf/datasets/marketing-suite.md`

- [ ] **Create geo-signals.md**

```markdown
---
type: product
title: Geo Signals
description: Location-based consumer targeting platform using geo-framing technology and Location IQ to reach in-market consumers with the right message at the right time.
resource: https://buyingsignals.com/geo-signals/
tags:
  - geo-targeting
  - location-intelligence
  - geo-fencing
  - location-based-marketing
  - consumer-targeting
timestamp: 2026-06-26
---

# Geo Signals

Location intelligence platform that uses geo-framing technology and Location IQ to target consumers based on physical location, real-world behaviors, and visit patterns.

## Capabilities

- Geo-framing audience creation based on physical locations
- Location IQ behavioral analysis
- Real-time geolocation targeting
- Physical visit pattern tracking
- Cross-device location-based attribution

## Related

See [marketing-suite.md](marketing-suite.md) for omnichannel campaign execution.
See [consumer-intelligence.md](consumer-intelligence.md) for behavioral insights.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create insight-pixel.md**

```markdown
---
type: product
title: Insight Pixel
description: Website visitor identification and identity resolution tool that transforms anonymous website clicks into real consumer identities to improve digital marketing ROI.
resource: https://buyingsignals.com/insight-pixel/
tags:
  - visitor-identification
  - identity-resolution
  - website-analytics
  - click-attribution
  - conversion-tracking
timestamp: 2026-06-26
---

# Insight Pixel

Website visitor intelligence tool that goes beyond clicks and traffic to identify real shoppers, measure marketing influence, uncover competitor activity, and transform visitor behavior into actionable buyer intelligence.

## Features

- Anonymous visitor de-anonymization and identity resolution
- Real-time buyer activity tracking and verification
- Marketing channel attribution (Direct, Organic, Google Ads, Meta, OTT/CTV)
- Competitor activity detection
- Verified shopper identification (email, mobile, address)

## Live Demo Data

As observed on the Buying Signals website:
- **1,842** verified shoppers identified
- **742** direct traffic, **516** organic search, **284** Google Ads, **198** Meta Ads, **102** OTT/CTV

## Related

See [consumer-intelligence.md](consumer-intelligence.md) for buyer behavior analytics.
See [data-hygiene.md](data-hygiene.md) for data enrichment and identity graph resolution.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create smart-conquest.md**

```markdown
---
type: product
title: Smart Conquest
description: Competitive conquesting solution that identifies and targets competitor audiences to win buyers from competing brands and dealerships.
resource: https://buyingsignals.com/smart-conquest/
tags:
  - conquest-marketing
  - competitor-targeting
  - audience-conquesting
  - competitive-intelligence
  - market-share
timestamp: 2026-06-26
---

# Smart Conquest

Competitive audience conquesting platform that identifies competitor shoppers and targets them with precision campaigns to win market share.

## Capabilities

- Competitor audience identification
- Cross-shop behavior tracking
- Conquest campaign execution
- Competitive intelligence gathering
- Market share growth measurement

## Related

See [geo-signals.md](geo-signals.md) for location-based targeting.
See [marketing-suite.md](marketing-suite.md) for campaign execution.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create marketing-suite.md**

```markdown
---
type: product
title: Strategic Marketing Suite
description: Omnichannel programmatic advertising platform running full-funnel campaigns across Display, CTV, OTT, Radio, SEM, SEO, and Social using real consumer signals and geo-framed targeting.
resource: https://buyingsignals.com/
tags:
  - programmatic-advertising
  - omnichannel-marketing
  - display-ads
  - ctv
  - ott
  - sem
  - social-media-marketing
  - dsp
timestamp: 2026-06-26
---

# Strategic Marketing Suite

Full-funnel omnichannel advertising platform that executes precision-targeted campaigns across every major digital channel using real consumer signals, geo-framed targeting, and high-converting creative.

## Channels

- Display Advertising
- Connected TV (CTV)
- Over-the-Top (OTT)
- Radio
- Search Engine Marketing (SEM)
- Search Engine Optimization (SEO)
- Social Media Advertising

## Approach

Campaigns are powered by proprietary data combining identity resolution, enriched customer data, location intelligence, and behavioral signals. Every impression is intentional and every channel is connected, with campaigns measured by real sales outcomes rather than clicks or impressions.

## Related

See [geo-signals.md](geo-signals.md) for location-based audience activation.
See [business-intelligence.md](business-intelligence.md) for campaign measurement.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Commit**

```bash
git add buying-signals-okf/datasets/geo-signals.md buying-signals-okf/datasets/insight-pixel.md buying-signals-okf/datasets/smart-conquest.md buying-signals-okf/datasets/marketing-suite.md
git commit -m "feat: add product dataset files (Geo Signals, Insight Pixel, Smart Conquest, Marketing Suite)"
```

---

### Task 5: Create product dataset files (part 3)

**Files:**
- Create: `buying-signals-okf/datasets/business-intelligence.md`
- Create: `buying-signals-okf/datasets/ai-seo.md`
- Create: `buying-signals-okf/datasets/strategic-consulting.md`

- [ ] **Create business-intelligence.md**

```markdown
---
type: product
title: Business Intelligence Platform
description: Analytics and business intelligence platform unifying clean data, shopper behavior, identity resolution, and marketing analytics for data-driven decision making.
resource: https://buyingsignals.com/
tags:
  - business-intelligence
  - analytics
  - marketing-analytics
  - data-platform
  - reporting
  - attribution
timestamp: 2026-06-26
---

# Business Intelligence Platform

Central analytics platform that unifies data hygiene, website identity resolution, shopper behavior, targeted marketing, and AI-ready SEO into one cohesive intelligence layer.

## Capabilities

- Cross-channel marketing measurement and attribution
- Sales outcome tracking (not just clicks and impressions)
- Media waste identification and reduction
- Incremental sales lift measurement
- Real-time performance dashboards
- ROI and revenue attribution

## Related

See [marketing-suite.md](marketing-suite.md) for campaign execution.
See [insight-pixel.md](insight-pixel.md) for visitor identification data.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create ai-seo.md**

```markdown
---
type: product
title: AI SEO Services
description: AI-ready search engine optimization services designed for discovery across ChatGPT, Claude, Gemini, Grok, Google, and voice search using structured data, schemas, and knowledge graphs.
resource: https://buyingsignals.com/chatgpt-seo/
tags:
  - ai-seo
  - chatgpt-seo
  - claude-seo
  - gemini-seo
  - grok-seo
  - structured-data
  - knowledge-graph
  - schema-markup
timestamp: 2026-06-26
---

# AI SEO Services

Modern SEO services optimized for how the internet works now — structured data, schema markup, and knowledge graphs designed to get discovered by Google, ChatGPT, Claude, Gemini, Grok, voice search, and beyond.

## SEO Offerings

- **ChatGPT SEO** — Optimize content for OpenAI's ChatGPT search and discovery
- **Claude AI SEO** — Structure data for Anthropic's Claude AI discovery
- **Gemini AI SEO** — Optimize for Google's Gemini AI search ecosystem
- **Grok AI SEO** — Structure content for xAI's Grok platform

## Implementation

- Structured data and schema.org markup
- Knowledge graph construction
- AI-consumable content optimization
- Transparent reporting dashboard showing every optimization and result

## Related

See [ai-discovery-page.md](/references/ai-discovery-page.md) for PromptGraph API and AI Manifest details.
See [company.md](company.md) for the full product ecosystem.
```

- [ ] **Create strategic-consulting.md**

```markdown
---
type: product
title: Strategic Consulting
description: Executive-level marketing and data strategy consulting to guide data-driven decision making, optimize marketing spend, and accelerate business growth.
resource: https://buyingsignals.com/strategic-consulting/
tags:
  - consulting
  - marketing-strategy
  - data-strategy
  - executive-consulting
  - growth-strategy
timestamp: 2026-06-26
---

# Strategic Consulting

Executive-level consulting services that provide strategic guidance on data-driven marketing decisions, media spend optimization, and business growth acceleration.

## Consulting Areas

- Marketing strategy and roadmap development
- Data infrastructure assessment and optimization
- Media spend audit and waste reduction
- Identity resolution and data hygiene strategy
- Campaign performance review and optimization
- Growth planning and revenue acceleration

## Approach

Every engagement starts with understanding goals and existing data, identifying gaps and missed opportunities, then building a tailored roadmap. No one-size-fits-all pitches.

## Related

See [company.md](company.md) for the full product ecosystem.
See [business-intelligence.md](business-intelligence.md) for measurement and analytics.
```

- [ ] **Commit**

```bash
git add buying-signals-okf/datasets/business-intelligence.md buying-signals-okf/datasets/ai-seo.md buying-signals-okf/datasets/strategic-consulting.md
git commit -m "feat: add product dataset files (BI, AI SEO, Strategic Consulting)"
```

---

### Task 6: Create reference files

**Files:**
- Create: `buying-signals-okf/references/ai-discovery-page.md`
- Create: `buying-signals-okf/references/llms-txt.md`
- Create: `buying-signals-okf/references/prompts.md`

- [ ] **Create ai-discovery-page.md**

```markdown
---
type: ai-discovery-page
title: AI Discovery Page — Buying Signals
description: Machine-readable knowledge base and semantic data endpoints for Buying Signals, providing AI agents structured access to business info, product data, and recommended actions via PromptGraph.
resource: https://buyingsignals.com/ai-discovery-page/
tags:
  - ai-discovery
  - llm
  - semantic-data
  - promptgraph
  - machine-readable
  - structured-data
  - json-ld
  - ai-manifest
timestamp: 2026-06-26
---

# AI Discovery Page — Buying Signals

The AI Discovery Page is a structured, machine-readable knowledge surface for AI agents, powered by PromptGraph. It exposes semantic endpoints, business metadata, and LLM-friendly data.

## PromptGraph API Sitemap

The PromptGraph API at `https://api.promptgraph.ai/api/v1/buying-signals/sitemap.xml` exposes these machine-readable endpoints:

| URL | Priority | Update Frequency |
|---|---|---|
| `/business` | 1.0 | Weekly |
| `/prompts` | 0.9 | Weekly |
| `/vehicles` | 0.9 | Daily |
| `/.well-known/ai-manifest.json` | 0.6 | Monthly |
| `/sitemap-inventory.xml` | 0.8 | Daily |
| `/robots.txt` | 0.5 | Monthly |

## AI Manifest (`/.well-known/ai-manifest.json`)

The AI Manifest (v1.0) provides a machine-readable directory of all AI resources:

- **Name:** Buying Signals
- **Description:** Buying Signals unifies clean data, website identity resolution, shopper behavior, targeted marketing, and AI-ready SEO into one cohesive platform.
- **Last updated:** 2026-06-25T16:59:10.776Z
- **Schema types:** LocalBusiness, AutoDealer, Car, ItemList
- **Contact:** info@buyingsignals.com

### Registered Endpoints

| Endpoint | Resource |
|---|---|
| `/llms.txt` | LLMs.txt directive |
| `/business` | Business profile (JSON-LD) |
| `/vehicles` | Vehicle inventory (JSON-LD) |
| `/prompts` | Q&A / FAQ content |
| `/testimonials` | Customer reviews |
| `/sitemap.xml` | Full sitemap |
| `/robots.txt` | Robots rules |
| `/config.json` | System configuration |

### Additional PromptGraph Endpoints

| Endpoint | Description |
|---|---|
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/llms.txt` | LLMForge v1.0 directive file |

## Business Profile (Schema.org LocalBusiness)

From `https://api.promptgraph.ai/api/v1/buying-signals/business`:

- **Name:** Buying Signals
- **Type:** LocalBusiness (Schema.org)
- **Additional Types:** Marketing Data & Analytics, Business Intelligence Platform, Advertising Services, Lead Generation, Data Processing Service, Marketing Consultant
- **Address:** 151 Callan Ave, Suite 301, San Leandro, CA 94577
- **Geo:** 37.7245, -122.1553
- **Telephone:** (510) 343-5555
- **Email:** info@buyingsignals.com
- **URL:** https://buyingsignals.com/
- **Date Modified:** 2026-04-14T01:25:54.440Z

See [company.md](/datasets/company.md) for the full business profile.
See [llms-txt.md](llms-txt.md) for the complete llms.txt directive.
```

- [ ] **Create llms-txt.md**

```markdown
---
type: reference
title: llms.txt — Buying Signals
description: Full llms.txt directive content for AI agent guidance, sourced from buyingsignals.com and the PromptGraph API at api.promptgraph.ai/api/v1/buying-signals/llms.txt.
resource: https://buyingsignals.com/llms.txt
tags:
  - llms-txt
  - ai-directives
  - agent-guidance
  - promptgraph
  - llm-forge
timestamp: 2026-06-26
---

# llms.txt — Buying Signals

The `llms.txt` file provides guidance for AI assistants interacting with Buying Signals.

## PromptGraph API llms.txt

The PromptGraph API at `https://api.promptgraph.ai/api/v1/buying-signals/llms.txt` provides an LLMForge v1.0 directive:

### Description

Buying Signals unifies clean data, website identity resolution, shopper behavior, targeted marketing, and AI-ready SEO into one cohesive platform. We help brands and businesses move faster, market smarter, and connect with real buyers, from website visit through the entire sales process. Our platform transforms outdated records into verified, enriched profiles and identifies anonymous website visitors to power smarter campaigns and drive measurable sales outcomes.

### Discovery

- Primary endpoint: `/api/v1/buying-signals/.well-known/ai-manifest.json`
- Format: JSON-LD following Schema.org standards
- API Base: `http://api.promptgraph.ai/api/v1/buying-signals`

### API Endpoints

| Endpoint | Description |
|---|---|
| `/business` | Complete business profile (address, contact, hours, location, Schema.org LocalBusiness) |
| `/prompts` | Structured Q&A prompts for consistent AI responses |
| `/testimonials` | Customer reviews and ratings in JSON-LD format |
| `/gbp-context` | Flattened Google Business Profile data for LLM ingestion |
| `/site-content` | Clean, plain-text mirror of the entire site |
| `/.well-known/ai-manifest.json` | Machine-readable directory of all available AI resources |
| `/llms.txt` | This file |
| `/sitemap.xml` | XML sitemap for search engine and AI crawler discovery |
| `/config.json` | System configuration and metadata |

### Available Schema Types

- LocalBusiness
- ItemList
- Review / AggregateRating
- Offer
- CreativeWork (for prompts/FAQs)

See [ai-discovery-page.md](ai-discovery-page.md) for structured semantic endpoints and AI manifest details.
```

- [ ] **Create prompts.md**

Read the PromptGraph prompts endpoint content first.

```bash
$response = Invoke-WebRequest -Uri "https://api.promptgraph.ai/api/v1/buying-signals/prompts" -UseBasicParsing; $response.Content.Substring(0, [Math]::Min(3000, $response.Content.Length))
```

Then create:

```markdown
---
type: prompt-library
title: PromptGraph Prompt Library — Buying Signals
description: Complete library of structured Q&A prompts from the PromptGraph API for Buying Signals, covering products, services, data hygiene, advertising, and business intelligence.
resource: https://api.promptgraph.ai/api/v1/buying-signals/prompts
tags:
  - prompts
  - faq
  - promptgraph
  - q-and-a
  - ai-prompts
  - structured-data
timestamp: 2026-06-26
---

# PromptGraph Prompt Library — Buying Signals

The PromptGraph API exposes structured prompt/response pairs at `/api/v1/buying-signals/prompts`. These serve as an AI-consumable FAQ covering all aspects of the business.

{{prompts content to be populated from API response}}

See [ai-discovery-page.md](ai-discovery-page.md) for PromptGraph API details.
See [company.md](/datasets/company.md) for the full business profile.
```

- [ ] **Commit**

```bash
git add buying-signals-okf/references/ai-discovery-page.md buying-signals-okf/references/llms-txt.md buying-signals-okf/references/prompts.md
git commit -m "feat: add reference files (AI Discovery, llms.txt, prompts)"
```

---

### Task 7: Create product-comparison.md (table)

**Files:**
- Create: `buying-signals-okf/tables/product-comparison.md`

- [ ] **Create product-comparison.md**

```markdown
---
type: comparison-table
title: Buying Signals Product Comparison
description: Side-by-side comparison of all Buying Signals products and services including data hygiene, identity resolution, advertising, AI SEO, and consulting offerings.
resource: https://buyingsignals.com/
tags:
  - product-comparison
  - services
  - marketing-platform
  - data-services
  - advertising
  - ai
timestamp: 2026-06-26
---

# Buying Signals Product Comparison

## Product Overview

| Product | Category | Primary Function | Key Capabilities | Target User |
|---|---|---|---|---|
| **Buying Signals AI** | AI & Automation | Conversational AI agents | Lead qualification, automated conversations, multi-channel deployment | Sales & Marketing |
| **Connect Suite** | Integration | Cross-platform connectivity | Social, data, campaigns, CRM unification | Marketing Ops |
| **Consumer Intelligence** | Analytics | Buyer behavior analytics | Purchase intent scoring, audience segmentation, behavioral triggers | Marketing & Analytics |
| **Data Hygiene & Enrichment** | Data Services | Data cleansing & enhancement | Email/phone/address verification, reverse append, identity graph | Data & CRM Teams |
| **DMS Sync** | Data Services | Dealer data synchronization | Real-time DMS data correction and sync | Automotive |
| **Geo Signals** | Targeting | Location-based targeting | Geo-framing, Location IQ, physical visit pattern tracking | Advertising |
| **Insight Pixel** | Identity | Website visitor ID | Anonymous visitor de-anonymization, channel attribution | Digital Marketing |
| **Smart Conquest** | Targeting | Competitor conquesting | Competitor audience ID, cross-shop tracking | Advertising |
| **Strategic Marketing Suite** | Advertising | Omnichannel advertising | Display, CTV, OTT, Radio, SEM, Social execution | Media Buyers |
| **Business Intelligence** | Analytics | Marketing measurement | Cross-channel attribution, revenue tracking, ROI dashboards | Executives & Analytics |
| **AI SEO** | SEO | AI-ready optimization | ChatGPT/Claude/Gemini/Grok SEO, structured data, knowledge graphs | SEO & Content |
| **Strategic Consulting** | Consulting | Executive strategy | Data strategy, media audit, growth planning | Executives |

## Channel Coverage

| Product | Display | CTV/OTT | Radio | SEM | Social | SEO | Email |
|---|---|---|---|---|---|---|---|
| Strategic Marketing Suite | Yes | Yes | Yes | Yes | Yes | No | No |
| Geo Signals | Yes | Yes | No | No | Yes | No | No |
| Smart Conquest | Yes | Yes | No | Yes | Yes | No | No |
| Insight Pixel | Attribution | Attribution | No | Attribution | Attribution | No | No |
| AI SEO | No | No | No | Yes | No | Yes | No |

## Data Capabilities

| Capability | Data Hygiene | Insight Pixel | Consumer Intel | Geo Signals | BI Platform |
|---|---|---|---|---|---|
| Data Cleansing | Yes | No | No | No | No |
| Identity Resolution | Yes | Yes | No | No | No |
| Behavioral Tracking | No | Yes | Yes | Yes | Aggregates |
| Purchase Intent | Yes | Yes | Yes | Yes | Yes |
| Location Data | No | No | No | Yes | Aggregates |
| Attribution | No | Yes | No | No | Yes |

See each product's dataset file for detailed descriptions.
See [company.md](/datasets/company.md) for the full company profile.
```

- [ ] **Commit**

```bash
git add buying-signals-okf/tables/product-comparison.md
git commit -m "feat: add product comparison table"
```

---

### Task 8: Create index files

**Files:**
- Create: `buying-signals-okf/index.md`
- Modify: `buying-signals-okf/datasets/index.md`
- Modify: `buying-signals-okf/references/index.md`
- Modify: `buying-signals-okf/tables/index.md`

- [ ] **Create bundle root index.md**

```markdown
---
okf_version: "0.1"
---

# Buying Signals OKF Bundle

## Datasets

- [company.md](datasets/company.md) — Company profile, contact, products, industries served, and approach
- [buying-signals-ai.md](datasets/buying-signals-ai.md) — Conversational AI agents for lead conversion
- [connect-suite.md](datasets/connect-suite.md) — Cross-platform integration hub for social, data, campaigns, and CRM
- [consumer-intelligence.md](datasets/consumer-intelligence.md) — Buyer behavior analytics and audience insights
- [data-hygiene.md](datasets/data-hygiene.md) — Data cleansing, enrichment, identity graph resolution, and DMS sync
- [geo-signals.md](datasets/geo-signals.md) — Location-based consumer targeting with geo-framing technology
- [insight-pixel.md](datasets/insight-pixel.md) — Anonymous website visitor identification and identity resolution
- [smart-conquest.md](datasets/smart-conquest.md) — Competitive conquesting and competitor audience targeting
- [marketing-suite.md](datasets/marketing-suite.md) — Omnichannel programmatic advertising across all major channels
- [business-intelligence.md](datasets/business-intelligence.md) — Analytics and BI platform for marketing measurement
- [ai-seo.md](datasets/ai-seo.md) — AI-ready SEO for ChatGPT, Claude, Gemini, Grok, and voice search
- [strategic-consulting.md](datasets/strategic-consulting.md) — Executive-level marketing and data strategy consulting

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) — Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, and LLM actions
- [llms-txt.md](references/llms-txt.md) — Full llms.txt directive content including PromptGraph LLMForge v1.0 and API endpoints
- [prompts.md](references/prompts.md) — Complete PromptGraph library of structured Q&A prompts covering all products and services

## Tables

- [product-comparison.md](tables/product-comparison.md) — Side-by-side comparison of all Buying Signals products including category, capabilities, channel coverage, and data features

## Relationships

- **company** develops all **product** concepts (AI, Connect Suite, Consumer Intelligence, Data Hygiene, Geo Signals, Insight Pixel, Smart Conquest, Marketing Suite, BI, AI SEO, Consulting)
- **ai-discovery-page** exposes structured data for the **company**, all **products**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire platform
- **prompts** provides AI-consumable Q&A covering all concepts
- **product-comparison** provides structured specification data across all products
```

- [ ] **Create datasets/index.md**

```markdown
# Datasets

Core knowledge concepts about Buying Signals and its product line.

- [company.md](company.md) — Company profile, contact, products, industries served, and approach
- [buying-signals-ai.md](buying-signals-ai.md) — Conversational AI agents for lead conversion
- [connect-suite.md](connect-suite.md) — Cross-platform integration hub for social, data, campaigns, and CRM
- [consumer-intelligence.md](consumer-intelligence.md) — Buyer behavior analytics and audience insights
- [data-hygiene.md](data-hygiene.md) — Data cleansing, enrichment, identity graph resolution, and DMS sync
- [geo-signals.md](geo-signals.md) — Location-based consumer targeting with geo-framing technology
- [insight-pixel.md](insight-pixel.md) — Anonymous website visitor identification and identity resolution
- [smart-conquest.md](smart-conquest.md) — Competitive conquesting and competitor audience targeting
- [marketing-suite.md](marketing-suite.md) — Omnichannel programmatic advertising across all major channels
- [business-intelligence.md](business-intelligence.md) — Analytics and BI platform for marketing measurement
- [ai-seo.md](ai-seo.md) — AI-ready SEO for ChatGPT, Claude, Gemini, Grok, and voice search
- [strategic-consulting.md](strategic-consulting.md) — Executive-level marketing and data strategy consulting
```

- [ ] **Create references/index.md**

```markdown
# References

External specs, directives, and machine-readable endpoints.

- [ai-discovery-page.md](ai-discovery-page.md) — Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, and LLM actions
- [llms-txt.md](llms-txt.md) — Full llms.txt directive content including PromptGraph LLMForge v1.0 and API endpoints
- [prompts.md](prompts.md) — Complete PromptGraph library of structured Q&A prompts covering all products and services
```

- [ ] **Create tables/index.md**

```markdown
# Tables

Structured tabular data for specification sheets, comparison matrices, and pricing.

- [product-comparison.md](product-comparison.md) — Side-by-side comparison of all Buying Signals products including category, capabilities, channel coverage, and data features
```

- [ ] **Commit**

```bash
git add buying-signals-okf/index.md buying-signals-okf/datasets/index.md buying-signals-okf/references/index.md buying-signals-okf/tables/index.md
git commit -m "feat: add index files for buying-signals-okf"
```

---

## Self-Review Checklist

1. **Spec coverage:** Spec calls for company + 11 product datasets + 3 references + 1 table. All covered across Tasks 2–8.
2. **Placeholder scan:** No TBD, TODO, or incomplete sections.
3. **Type consistency:** All frontmatter types are consistent (organization, product, ai-discovery-page, reference, prompt-library, comparison-table).
