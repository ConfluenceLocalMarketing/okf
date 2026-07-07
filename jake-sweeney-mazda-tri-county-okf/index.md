---
okf_version: "0.1"
---

# Jake Sweeney Mazda Tri-County OKF Bundle

## Datasets

- [dealership.md](jake-sweeney-mazda-tri-county-okf/datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs
- [new-vehicles.md](jake-sweeney-mazda-tri-county-okf/datasets/new-vehicles.md) - New Mazda model lineup including CX-30, CX-5, CX-50, CX-70, CX-90, MX-5 Miata, and Mazda3
- [used-vehicles.md](jake-sweeney-mazda-tri-county-okf/datasets/used-vehicles.md) - Pre-owned and Mazda certified pre-owned inventory with multi-make selection
- [staff.md](jake-sweeney-mazda-tri-county-okf/datasets/staff.md) - Staff directory including sales consultants, service advisors, and finance team compiled from customer reviews
- [service-center.md](jake-sweeney-mazda-tri-county-okf/datasets/service-center.md) - Service center details, routine maintenance, diagnostics, major repairs, and parts department
- [faq.md](jake-sweeney-mazda-tri-county-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](jake-sweeney-mazda-tri-county-okf/datasets/financing.md) - Vehicle financing and leasing options including online applications, trade-in valuation, and payment calculators

## References

- [ai-discovery-page.md](jake-sweeney-mazda-tri-county-okf/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](jake-sweeney-mazda-tri-county-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](jake-sweeney-mazda-tri-county-okf/references/testimonials.md) - Customer reviews with all 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](jake-sweeney-mazda-tri-county-okf/references/prompts.md) - Complete PromptGraph library of 10 structured Q&A prompts covering vehicles, financing, service, and dealership info

## Tables

- [model-comparison.md](jake-sweeney-mazda-tri-county-okf/tables/model-comparison.md) - Side-by-side comparison of all new Mazda models including body type, drivetrain, seating, features, trims, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
