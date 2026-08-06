---
okf_version: "0.1"
---

# West Hills Mazda OKF Bundle

## Datasets

- [dealership.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for West Hills Mazda in Bremerton, WA
- [new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/new-vehicles.md) - New Mazda model lineup including CX-30, CX-5, CX-50, CX-70, CX-90, Mazda3, MX-5 Miata, and hybrid/electric options
- [used-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/staff.md) - Staff directory including management, sales consultants, service advisors, finance team, and parts team
- [service-center.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/service-center.md) - Mazda-certified service center details, routine maintenance, diagnostics, major repairs, and genuine Mazda parts department
- [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/datasets/financing.md) - Financing and leasing options, trade-in valuation, and online payment calculators

## References

- [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/references/prompts.md) - Complete PromptGraph library of 10 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/west-hills-mazda/tables/model-comparison.md) - Side-by-side comparison of all new Mazda models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
- **financing** details loan and lease options available through the **dealership**'s finance center
