---
okf_version: "0.1"
---

# Kruse Motors OKF Bundle

## Datasets

- [dealership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/dealership.md) - Multi-brand automotive dealership in Marshall, MN serving as certified dealer for Ford, Lincoln, Buick, and GMC with new/used vehicle sales, service, parts, and financing.
- [new-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/new-vehicles.md) - New vehicle lineup across Ford, Lincoln, Buick, and GMC brands including trucks, SUVs, crossovers, sedans, and electric vehicles with custom ordering through Kruse Your Way.
- [used-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory of cars, trucks, and SUVs across multiple brands with KBB trade-in valuation, vehicle protection plans, and we-buy-cars program.
- [service-center.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/service-center.md) - Factory-authorized service centers at Kruse Motors Ford Lincoln and Kruse Motors Buick GMC offering routine maintenance, advanced diagnostics, major repairs, OEM parts, and accessories.
- [financing.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/financing.md) - Auto financing and leasing options including pre-qualification, online credit applications, student savings, lease specials, and flexible loan programs.
- [staff.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/staff.md) - Sales, service, and finance staff at Kruse Motors compiled from customer testimonials and reviews.
- [faq.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/datasets/faq.md) - Common questions and answers about inventory, financing, service, trade-ins, and dealership experience.

## References

- [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/references/ai-discovery-page.md) - Machine-readable knowledge base and semantic data endpoints for Kruse Motors, providing AI agents structured access to business info, vehicle inventory, customer reviews, and recommended actions via PromptGraph.
- [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph LLMForge v1.0 and API endpoints.
- [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/references/testimonials.md) - Collection of 100+ customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts.
- [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/references/prompts.md) - Complete PromptGraph library of 28+ structured Q&A prompts covering dealership, vehicles, financing, service, and customer experience.

## Tables

- [brand-comparison.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/kruse-motors-okf/tables/brand-comparison.md) - Side-by-side comparison of the four automotive brands available at Kruse Motors - Ford, Lincoln, Buick, and GMC - covering positioning, popular models, key features, and target buyer.

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles** across four brands (Ford, Lincoln, Buick, GMC)
- **dealership** employees **staff** and operates two **service-center** locations (Ford Lincoln, Buick GMC)
- **dealership** provides **financing** through its finance department
- **ai-discovery-page** exposes structured data for the **dealership**, **vehicles** (new/used), **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership
- **brand-comparison** provides structured specification data across all four **new-vehicles** brands
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and vehicle purchases
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
