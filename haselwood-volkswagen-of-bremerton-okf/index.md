---
okf_version: "0.1"
---

# Haselwood Volkswagen of Bremerton OKF Bundle

## Datasets

- [dealership.md](haselwood-volkswagen-of-bremerton-okf/datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for Haselwood Volkswagen of Bremerton in Bremerton, WA
- [financing.md](haselwood-volkswagen-of-bremerton-okf/datasets/financing.md) - Vehicle financing and leasing options at Haselwood Volkswagen of Bremerton including online applications, trade-in valuation, and payment calculators
- [new-vehicles.md](haselwood-volkswagen-of-bremerton-okf/datasets/new-vehicles.md) - New Volkswagen model lineup including Atlas, Taos, Tiguan, ID.4, Jetta, Golf GTI, Golf R, ID. Buzz, and Arteon
- [used-vehicles.md](haselwood-volkswagen-of-bremerton-okf/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](haselwood-volkswagen-of-bremerton-okf/datasets/staff.md) - Staff directory including management, sales consultants, service advisors, and finance team
- [service-center.md](haselwood-volkswagen-of-bremerton-okf/datasets/service-center.md) - Volkswagen-certified service center details, routine maintenance, diagnostics, major repairs, and genuine VW parts department
- [faq.md](haselwood-volkswagen-of-bremerton-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership

## References

- [ai-discovery-page.md](haselwood-volkswagen-of-bremerton-okf/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](haselwood-volkswagen-of-bremerton-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](haselwood-volkswagen-of-bremerton-okf/references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](haselwood-volkswagen-of-bremerton-okf/references/prompts.md) - Complete PromptGraph library of 39 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](haselwood-volkswagen-of-bremerton-okf/tables/model-comparison.md) - Side-by-side comparison of all new Volkswagen models including body type, drivetrain, seating, features, trims, and towing

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
