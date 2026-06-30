---
okf_version: "0.1"
---

# Jake Sweeney Used Car Superstore OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, hours, contact, services, location, programs, and staff overview for the original used car superstore
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned inventory of over 900 vehicles with multi-make selection spanning luxury to budget and 100% online buying
- [staff.md](datasets/staff.md) - Staff directory including sales consultants, service advisors, and finance team compiled from customer reviews
- [service-center.md](datasets/service-center.md) - Service center details, routine maintenance, diagnostics, major repairs, and parts department
- [faq.md](datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - PromptGraph API endpoints overview; no dedicated AI Discovery Page found on this site
- [llms-txt.md](references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints and 10 featured AI prompts
- [testimonials.md](references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](references/prompts.md) - PromptGraph library of 10 structured Q&A prompts covering vehicles, financing, service, and dealership info

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of popular used vehicle body types and brands available at the superstore

## Relationships

- **dealership** offers **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, vehicles, **testimonials**, and **prompts** via PromptGraph
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership
- **model-comparison** provides structured specification data for popular vehicle segments
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and vehicle purchases
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
