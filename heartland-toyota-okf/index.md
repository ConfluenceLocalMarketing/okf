---
okf_version: "0.1"
---

# Heartland Toyota OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for Heartland Toyota in Bremerton, WA
- [financing.md](datasets/financing.md) - Vehicle financing and leasing options at Heartland Toyota including online applications, trade-in valuation, and payment calculators
- [new-vehicles.md](datasets/new-vehicles.md) - New Toyota model lineup including Camry, Corolla, RAV4, Tacoma, Tundra, Highlander, 4Runner, and more
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](datasets/staff.md) - Staff directory including management, sales consultants, service advisors, finance team, and parts team
- [service-center.md](datasets/service-center.md) - Toyota-certified service center details, routine maintenance, diagnostics, major repairs, and genuine Toyota parts department
- [faq.md](datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](references/prompts.md) - Complete PromptGraph library of 38 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of all new Toyota models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
