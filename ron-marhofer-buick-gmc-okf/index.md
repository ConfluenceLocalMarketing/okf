---
okf_version: "0.1"
---

# Ron Marhofer Buick GMC OKF Bundle

## Datasets

- [dealership.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for Ron Marhofer Buick GMC in North Canton, OH
- [new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/new-vehicles.md) - New Buick and GMC model lineup including Encore GX, Envision, Enclave, Terrain, Acadia, Yukon, Sierra, Canyon, and HUMMER EV
- [used-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/staff.md) - Staff directory including management, sales consultants, service advisors, finance team, and parts team
- [service-center.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/service-center.md) - Buick and GMC certified service center details, routine maintenance, diagnostics, major repairs, and genuine OEM parts department
- [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/datasets/financing.md) - Vehicle financing and leasing options including online applications, trade-in valuation, and payment calculators

## References

- [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/references/prompts.md) - Complete PromptGraph library of 10+ structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/ron-marhofer-buick-gmc/tables/model-comparison.md) - Side-by-side comparison of all new Buick and GMC models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
