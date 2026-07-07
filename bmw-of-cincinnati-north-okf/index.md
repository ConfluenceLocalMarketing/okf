---
okf_version: "0.1"
---

# BMW of Cincinnati North OKF Bundle

## Datasets

- [dealership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/dealership.md) - Business profile, hours, contact, services, location, special programs, and staff overview
- [new-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/new-vehicles.md) - New BMW model lineup including sedans, SUVs, coupes, convertibles, electric i4/i5/i7/iX, and M performance variants
- [used-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/used-vehicles.md) - Pre-owned and BMW Certified Pre-Owned inventory with multi-make selection and BMW Certified program details
- [staff.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/staff.md) - Staff directory including sales consultants, service advisors, and BMW M Certified specialists
- [service-center.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/service-center.md) - BMW-certified service center details, routine maintenance, diagnostics, major repairs, and OEM parts
- [faq.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and dealership
- [financing.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/datasets/financing.md) - BMW Financial Services financing, leasing, trade-in, and special programs at BMW of Cincinnati North

## References

- [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/references/ai-discovery-page.md) - PromptGraph AI endpoints, AI Manifest, business profile, vehicle inventory, and LLM actions for BMW of Cincinnati North
- [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/references/testimonials.md) - Customer reviews with predominantly 5-star ratings and notable themes
- [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/references/prompts.md) - Complete PromptGraph library of 16 structured Q&A prompts covering vehicles, financing, service, parts, and dealership info

## Tables

- [model-comparison.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/bmw-of-cincinnati-north-okf/tables/model-comparison.md) - Side-by-side comparison of all new BMW models including body type, drivetrain, seating, features, trims, and starting MSRP

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
