---
okf_version: "0.1"
---

# West Hills Chrysler Jeep Dodge RAM OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, hours, contact, services, location, and community programs for West Hills Chrysler Jeep Dodge RAM in Bremerton, WA
- [new-vehicles.md](datasets/new-vehicles.md) - New Chrysler, Jeep, Dodge, and RAM model lineup including Pacifica, Wrangler, Grand Cherokee, Charger, Durango, RAM trucks, and ProMaster vans
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, online buying tools, and trade-in services
- [staff.md](datasets/staff.md) - Staff directory including management, sales managers, finance team, and service/parts managers
- [service-center.md](datasets/service-center.md) - Mopar-certified service center details, routine maintenance, diagnostics, major repairs, and genuine Mopar parts department
- [faq.md](datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - AI-facing infrastructure assessment, tested endpoints, and structured data availability
- [llms-txt.md](references/llms-txt.md) - llms.txt availability assessment and key site pages for AI crawling
- [testimonials.md](references/testimonials.md) - Customer reviews, dealership reputation, and community awards
- [prompts.md](references/prompts.md) - AI prompt patterns for querying dealership knowledge

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of all new Chrysler, Jeep, Dodge, and RAM models including body type, drivetrain, seating, features, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** documents the lack of AI-facing infrastructure for the **dealership**
- **faq** answers common questions about inventory, financing, service, and dealership
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services and **staff**
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
