---
okf_version: "0.1"
---

# Texan Title — OKF Bundle

Knowledge bundle for [Texan Title](https://texantitle.com/), an independent Texas title insurance company with 27 offices across 5 regions.

## Datasets

| File | Type | Description |
|------|------|-------------|
| [company.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/company.md) | Organization | Full business profile — founding, acquisitions, underwriters, services, credentials |
| [leadership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/leadership.md) | Entities | 24-person leadership team across executive, escrow, and title plant operations |
| [locations.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/locations.md) | Entities | 27 offices in South, West, Williamson County, Hill Country, and Commercial regions |
| [services.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/services.md) | Entities | Title insurance, escrow, 1031 exchange, realtor tools, commercial division |
| [1031-exchange.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/1031-exchange.md) | Entities | Qualified Intermediary services with Exchange Manager Pro and $50M fidelity bond |
| [community-involvement.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/community-involvement.md) | Entities | $2M+ in charitable giving across 80+ Texas organizations |
| [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/testimonials.md) | Entities | Client and realtor reviews highlighting trusted closings and professionalism |
| [faq.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/datasets/faq.md) | Entities | FAQ covering services, closing costs, first-time buyers, and 1031 exchanges |

## References

| File | Type | Description |
|------|------|-------------|
| [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/references/ai-discovery-page.md) | APIs | PromptGraph AI manifest with 10 API endpoints |
| [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/references/llms-txt.md) | APIs | LLMs.txt directive for AI-discoverable endpoints |
| [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/references/prompts.md) | APIs | 20 PromptGraph prompts organized by category |
| [sitemap.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/references/sitemap.md) | Reference | 46-page website structure from Strapi CMS |

## Tables

| File | Type | Description |
|------|------|-------------|
| [locations-matrix.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/tables/locations-matrix.md) | Tables and Datasets | 27-office comparison matrix by region |
| [underwriters.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/texantitle-okf/tables/underwriters.md) | Tables and Datasets | 9 underwriter partners comparison |

## Relationships

- **company.md** is the central hub linking to all other datasets
- **leadership.md** provides personnel context for **locations.md** regional presidents
- **locations.md** feeds into **locations-matrix.md** table and individual office pages
- **services.md** references **1031-exchange.md** for detailed exchange services
- **ai-discovery-page.md** indexes all PromptGraph endpoints including **prompts.md**
- **llms-txt.md** mirrors the AI discovery structure
- **sitemap.md** maps the Strapi CMS architecture that serves all content
- **underwriters.md** expands the underwriter list from **company.md**
