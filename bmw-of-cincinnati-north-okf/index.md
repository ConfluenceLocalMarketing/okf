---
okf_version: "0.1"
---

# BMW of Cincinnati North OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, hours, contact, services, location, special programs, and staff overview
- [new-vehicles.md](datasets/new-vehicles.md) - New BMW model lineup including sedans, SUVs, coupes, convertibles, electric i4/i5/i7/iX, and M performance variants
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned and BMW Certified Pre-Owned inventory with multi-make selection and BMW Certified program details
- [staff.md](datasets/staff.md) - Staff directory including sales consultants, service advisors, and BMW M Certified specialists
- [service-center.md](datasets/service-center.md) - BMW-certified service center details, routine maintenance, diagnostics, major repairs, and OEM parts
- [faq.md](datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](datasets/financing.md) - BMW Financial Services financing, leasing, trade-in, and special programs at BMW of Cincinnati North

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - PromptGraph AI endpoints, AI Manifest, business profile, vehicle inventory, and LLM actions for BMW of Cincinnati North
- [llms-txt.md](references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](references/testimonials.md) - Customer reviews with predominantly 5-star ratings and notable themes
- [prompts.md](references/prompts.md) - Complete PromptGraph library of 16 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of all new BMW models including body type, drivetrain, seating, features, trims, and starting MSRP

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center**
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, and **prompts**
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
- **model-comparison** provides structured specification data for all **new-vehicles** models
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and both vehicle lines
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
- **financing** details BMW Financial Services loan and lease options available through the **dealership**'s finance center
