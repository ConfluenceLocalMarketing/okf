# Basil Mitsubishi OKF Bundle

## Datasets

- [dealership.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/dealership.md) - Business profile, hours, contact, services, location, staff leadership, perks
- [new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/new-vehicles.md) - New Mitsubishi model lineup, features, trims, promotions
- [used-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory, trade-in, quality assurance
- [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/financing.md) - Vehicle financing, leasing, trade-in, and payment calculator information at Basil Mitsubishi
- [staff.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/staff.md) - Full staff directory including management, sales, service, and parts teams
- [service-center.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/datasets/service-center.md) - Service center details, routine maintenance, diagnostics, collision repair, parts department

## References

- [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/references/llms-txt.md) - Full llms.txt directive content including PromptGraph LLMForge v1.0, API endpoints, and 10 featured AI prompts
- [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/references/testimonials.md) - 245 customer reviews with 5.0 rating, most-praised staff, and notable excerpts
- [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/references/prompts.md) - Complete PromptGraph library of 64 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mitsubishi/tables/model-comparison.md) - Side-by-side comparison of all new Mitsubishi models including body type, drivetrain, seating, features, trims, and warranty

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
