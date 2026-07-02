---
okf_version: "0.1"
---

# West Hills Honda OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for West Hills Honda in Bremerton, WA
- [new-vehicles.md](datasets/new-vehicles.md) - New Honda model lineup including Civic, Accord, CR-V, Pilot, Odyssey, HR-V, Passport, Ridgeline, Prologue, and hybrid/electric variants
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned and HondaTrue Certified Pre-Owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](datasets/staff.md) - Staff directory including management, sales consultants, service advisors, finance team, and parts team
- [service-center.md](datasets/service-center.md) - Honda-certified service center details, routine maintenance, diagnostics, major repairs, genuine Honda parts, and Honda Express Service
- [faq.md](datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](datasets/financing.md) - Financing and leasing options, trade-in valuation, and online payment calculators.

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](references/prompts.md) - Complete PromptGraph library of 29 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of all new Honda models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
