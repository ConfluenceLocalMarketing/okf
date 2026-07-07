---
okf_version: "0.1"
---

# Haselwood Auto Group OKF Bundle

## Datasets

- [dealership.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/dealership.md) - Multi-franchise auto group business profile, history by Chuck Haselwood, member dealerships, hours, contact, services, community involvement, and awards for Haselwood Auto Group in Bremerton, WA
- [new-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/new-vehicles.md) - New vehicle lineup across member franchises representing Chevrolet, Buick, GMC, Hyundai, Volkswagen, Toyota, Ford, Honda, Kia, Mazda, Chrysler, Jeep, Dodge, and Ram brands
- [used-vehicles.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/used-vehicles.md) - Pre-owned and certified pre-owned inventory across the West Hills Autoplex with multi-brand selection, West Hills warranty, and online buying tools
- [staff.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/staff.md) - Staff directory including executive leadership, management, sales consultants, and service team compiled from the group website and customer reviews
- [service-center.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/service-center.md) - Multi-brand service centers across the West Hills Autoplex offering routine maintenance, diagnostics, major repairs, and genuine OEM parts
- [faq.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/faq.md) - Frequently asked questions about inventory, financing, service, and auto group operations
- [financing.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/datasets/financing.md) - Vehicle financing and leasing options across the West Hills Autoplex including online credit application and trade-in valuation

## References

- [ai-discovery-page.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/references/ai-discovery-page.md) - Structured semantic endpoints, AI Manifest, PromptGraph API, MCP server, business profile, vehicle inventory, and LLM actions
- [llms-txt.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [testimonials.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/references/testimonials.md) - Customer reviews with predominantly 5-star ratings, praised staff, and notable excerpts from PromptGraph
- [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/references/prompts.md) - Complete PromptGraph prompt library covering vehicles, financing, service, parts, and auto group info

## Tables

- [model-comparison.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/haselwood-auto-group-okf/tables/model-comparison.md) - Side-by-side comparison of popular vehicle models across member brands including body type, seating, drivetrain, features, and warranty

## Relationships

- **dealership** operates member franchises offering **new-vehicles** and **used-vehicles**
- **dealership** employs **staff** and operates **service-center** across multiple locations
- **ai-discovery-page** exposes structured data for the **dealership**, both vehicle lines, **testimonials**, and **prompts** via PromptGraph
- **llms-txt** provides top-level agent guidance for the entire group site
- **faq** answers common questions about inventory, financing, service, and auto group programs
- **model-comparison** provides structured specification data for popular brand models across **new-vehicles**
- **testimonials** reflect customer experiences with **dealership** services, **staff**, and member locations
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
- **financing** details loan and lease options available through the **dealership**'s finance center
