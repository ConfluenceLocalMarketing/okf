---
okf_version: "0.1"
---

# Haselwood GMC OKF Bundle

## Datasets

- [dealership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/dealership.md) - Business profile, hours, contact, services, location, and special programs for Haselwood GMC in Bremerton, WA
- [financing.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/financing.md) - Vehicle financing and leasing options at Haselwood GMC including online applications, trade-in valuation, and payment calculators
- [new-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/new-vehicles.md) - New GMC model lineup including Acadia, Terrain, Yukon, Yukon XL, Canyon, Sierra 1500, Sierra 2500 HD, Sierra 3500 HD, HUMMER EV SUV, HUMMER EV Pickup, and Sierra EV
- [used-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory with multi-make selection, competitive pricing, and online buying tools
- [staff.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/staff.md) - Staff directory including management, sales consultants, service advisors, finance team, and parts team
- [service-center.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/service-center.md) - GMC-certified service center details, routine maintenance, diagnostics, major repairs, and genuine GMC parts department
- [faq.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership

## References

- [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/references/testimonials.md) - Customer reviews from Google Business Profile and PromptGraph platform
- [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/references/prompts.md) - Complete PromptGraph library of 40 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-gmc-okf/tables/model-comparison.md) - Side-by-side comparison of all new GMC models including body type, drivetrain, seating, features, trims, towing, and warranty

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
