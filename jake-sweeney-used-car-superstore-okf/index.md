---
okf_version: "0.1"
---

# Jake Sweeney Used Car Superstore OKF Bundle

## Datasets

- [dealership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/dealership.md) - Business profile, hours, contact, services, location, programs, and staff overview for the original used car superstore
- [used-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/used-vehicles.md) - Pre-owned inventory of over 900 vehicles with multi-make selection spanning luxury to budget and 100% online buying
- [staff.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/staff.md) - Staff directory including sales consultants, service advisors, and finance team compiled from customer reviews
- [service-center.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/service-center.md) - Service center details, routine maintenance, diagnostics, major repairs, and parts department
- [faq.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [new-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/new-vehicles.md) - New vehicle access through the Jake Sweeney Automotive group of dealerships
- [financing.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/datasets/financing.md) - Vehicle financing options including online applications, buy-here-pay-here programs, and trade-in valuation

## References

- [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/ai-discovery-page.md) - PromptGraph API endpoints overview; no dedicated AI Discovery Page found on this site
- [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints and 10 featured AI prompts
- [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/references/prompts.md) - PromptGraph library of 10 structured Q&A prompts covering vehicles, financing, service, and dealership info

## Tables

- [model-comparison.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/jake-sweeney-used-car-superstore-okf/tables/model-comparison.md) - Side-by-side comparison of popular used vehicle body types and brands available at the superstore

## Relationships

- **dealership** offers **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, vehicles, **testimonials**, and **prompts** via PromptGraph
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership
- **model-comparison** provides structured specification data for popular vehicle segments
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and vehicle purchases
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
