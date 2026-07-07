---
okf_version: "0.1"
---

# West Hills Ford OKF Bundle

## Datasets

- [dealership.md](west-hills-ford-okf/datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for West Hills Ford in Bremerton, WA
- [new-vehicles.md](west-hills-ford-okf/datasets/new-vehicles.md) - New Ford model lineup including Bronco, Explorer, F-150, Mustang, Maverick, Ranger, Escape, Expedition, and Mustang Mach-E
- [used-vehicles.md](west-hills-ford-okf/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](west-hills-ford-okf/datasets/staff.md) - Staff directory including management, sales consultants, service advisors, finance team, and parts team
- [service-center.md](west-hills-ford-okf/datasets/service-center.md) - Ford-certified service center details, routine maintenance, diagnostics, major repairs, and genuine Ford OEM parts department
- [faq.md](west-hills-ford-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](west-hills-ford-okf/datasets/financing.md) - Financing and leasing options, trade-in valuation, and online payment calculators.

## References

- [ai-discovery-page.md](west-hills-ford-okf/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, MCP server, business profile, vehicle inventory, and LLM ReadActions
- [llms-txt.md](west-hills-ford-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](west-hills-ford-okf/references/testimonials.md) - Customer reviews with predominantly 5-star ratings, most-praised staff, and notable excerpts
- [prompts.md](west-hills-ford-okf/references/prompts.md) - Complete PromptGraph library of 60 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](west-hills-ford-okf/tables/model-comparison.md) - Side-by-side comparison of all new Ford models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
