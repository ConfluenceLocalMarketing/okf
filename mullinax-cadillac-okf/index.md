---
okf_version: "0.1"
---

# Mullinax Cadillac

An Open Knowledge Format (OKF) v0.1 bundle describing Mullinax Cadillac, a Cadillac dealership at 833 Eastern Blvd, Montgomery, AL 36117 serving the Montgomery River Region and Central Alabama. It covers the dealership profile, new and used vehicle sales, service, parts, financing, staff, reviews, and AI-optimized discovery endpoints.

## Datasets

- [mullinax-cadillac.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/mullinax-cadillac.md) - Cadillac dealership in Montgomery, AL serving Central Alabama with new and used vehicle sales, Up Front Pricing, financing, service, and parts at 833 Eastern Blvd.
- [new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/new-vehicles.md) - New Cadillac vehicle inventory covering sedans, SUVs, and electric vehicles including CT4, CT5, XT4, XT5, XT6, LYRIQ, OPTIQ, VISTIQ, and Escalade.
- [used-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/used-vehicles.md) - Pre-owned vehicle inventory including Certified Pre-Owned Cadillac, courtesy and demo units, Up Front Pricing with zero dealer fees, and trade-in valuation.
- [service-center.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/service-center.md) - Cadillac service center in Montgomery, AL offering factory-trained maintenance and repair with OEM parts, online appointment scheduling, and a parts department.
- [staff.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/staff.md) - Staff directory covering management, sales, finance, service, parts, and office departments with contact details.
- [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/faq.md) - Common questions and answers about financing, no-dealer-fee pricing, and dealership operations.
- [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/financing.md) - Vehicle financing options including online credit application, leasing, trade-in valuation, and a payment calculator.

## References

- [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/ai-discovery-page.md) - Machine-readable AI discovery endpoints including a PromptGraph sitemap, business profile, prompt library, and AI manifest for LLM consumption.
- [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/llms-txt.md) - AI consumption directive providing structured API endpoints, schema types, and business context to LLM crawlers and AI agents.
- [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/prompts.md) - Twenty curated Q&A prompts for consistent AI responses covering inventory, financing, service, and luxury-vehicle shopping.
- [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/testimonials.md) - Customer ratings including a 3.9-star Google rating across 208 reviews, with an empty PromptGraph testimonials feed as of August 2026.

## Tables

- [contact.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/tables/contact.md) - Consolidated phone directory and address for sales, service, parts, financing, and general inquiries.
- [hours.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/tables/hours.md) - Sales, service, and parts operating hours.
- [model-comparison.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/tables/model-comparison.md) - Side-by-side comparison of key Cadillac models by body type, powertrain, seating, and typical buyer.

## Relationships

- The dealership **operates** new vehicle sales ([new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/new-vehicles.md)) and pre-owned sales ([used-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/used-vehicles.md)).
- New and used vehicle purchases **are financed** through [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/financing.md).
- [service-center.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/service-center.md) **supports** vehicle ownership with maintenance, repair, and parts.
- [staff.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/staff.md) **comprises** the management, sales, finance, service, parts, and office teams that serve customers.
- [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/datasets/faq.md) **answers** common questions about sales, financing, and service.
- The dealership **exposes** AI discovery endpoints described in [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/ai-discovery-page.md) and [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/llms-txt.md).
- The prompt library ([prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/prompts.md)) **targets** the dealership's inventory, financing, and luxury-vehicle pages.
- Customer reputation **is measured** by aggregate ratings in [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/references/testimonials.md).
- [contact.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/tables/contact.md) and [hours.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/tables/hours.md) **describe** how to reach and visit the dealership.
- [model-comparison.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/mullinax-cadillac/tables/model-comparison.md) **compares** the Cadillac models sold at the dealership.
