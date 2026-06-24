---
okf_version: "0.1"
---

# Jake Sweeney Chevrolet OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) — Business profile, hours, contact, services, location, special programs, and staff overview
- [new-vehicles.md](datasets/new-vehicles.md) — New Chevrolet model lineup including Silverado, Equinox, Trax, Trailblazer, Traverse, Blazer, Colorado, Tahoe, Corvette, and EV models
- [used-vehicles.md](datasets/used-vehicles.md) — Pre-owned and certified pre-owned inventory of over 4,000 vehicles with multi-make selection and Jake Sweeney Express online purchasing
- [staff.md](datasets/staff.md) — Staff directory including sales consultants, service advisors, and finance team compiled from customer reviews
- [service-center.md](datasets/service-center.md) — Service center details, routine maintenance, diagnostics, major repairs, and parts department
- [faq.md](datasets/faq.md) — Frequently asked questions about inventory, financing, service, and dealership

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) — Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](references/llms-txt.md) — Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](references/testimonials.md) — Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](references/prompts.md) — Complete PromptGraph library of 119 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](tables/model-comparison.md) — Side-by-side comparison of all new Chevrolet models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
