---
okf_version: "0.1"
---

# Nick Mayer Ford West Bundle

OKF v0.1 bundle documenting Nick Mayer Ford West, a Ford dealership located in Avon Lake, OH.

## Datasets

- [dealership.md](datasets/dealership.md) - Ford dealership in Avon Lake, OH serving Cleveland, Lorain, and Westlake with new and pre-owned vehicles, financing, service, and parts.
- [new-vehicles.md](datasets/new-vehicles.md) - New Ford model lineup available at Nick Mayer Ford West in Avon Lake, OH including F-150, Explorer, Escape, Expedition, Bronco, Mustang, Edge, Ranger, Maverick, and more.
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned inventory at Nick Mayer Ford West in Avon Lake, OH spanning multiple makes with certified pre-owned Ford Blue Advantage vehicles.
- [staff.md](datasets/staff.md) - Sales and service staff at Nick Mayer Ford West in Avon Lake, OH including management, sales consultants, service technicians, and finance team.
- [service-center.md](datasets/service-center.md) - Ford-certified service center in Avon Lake, OH offering routine maintenance, diagnostics, major repairs, and genuine Ford OEM parts.
- [faq.md](datasets/faq.md) - Common questions about Nick Mayer Ford West's inventory, financing, service, and dealership operations in Avon Lake, OH.
- [financing.md](datasets/financing.md) - Vehicle financing and leasing options including online applications, second-chance financing, and trade-in valuation.

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - Machine-readable knowledge surface for Nick Mayer Ford West providing AI agents structured access to business info, inventory, and site content.
- [llms-txt.md](references/llms-txt.md) - Structured directive for AI agents interacting with Nick Mayer Ford West's web properties in Avon Lake, OH.
- [testimonials.md](references/testimonials.md) - Customer reviews for Nick Mayer Ford West in Avon Lake, OH reflecting sales and service experiences.
- [prompts.md](references/prompts.md) - AI-consumable Q&A prompts covering vehicles, financing, service, parts, and dealership info for Nick Mayer Ford West in Avon Lake, OH.

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of new Ford models available at Nick Mayer Ford West in Avon Lake, OH.

## Relationships

| Source | Target | Relationship |
|---|---|---|
| [dealership.md](datasets/dealership.md) | [new-vehicles.md](datasets/new-vehicles.md) | Dealership sells new vehicles |
| [dealership.md](datasets/dealership.md) | [used-vehicles.md](datasets/used-vehicles.md) | Dealership sells pre-owned vehicles |
| [dealership.md](datasets/dealership.md) | [service-center.md](datasets/service-center.md) | Dealership operates service center |
| [dealership.md](datasets/dealership.md) | [staff.md](datasets/staff.md) | Dealership employs staff |
| [new-vehicles.md](datasets/new-vehicles.md) | [model-comparison.md](tables/model-comparison.md) | Model details compared in table |
| [dealership.md](datasets/dealership.md) | [faq.md](datasets/faq.md) | Dealership answered in FAQ |
| [service-center.md](datasets/service-center.md) | [staff.md](datasets/staff.md) | Service center includes staff |
| [dealership.md](datasets/dealership.md) | [testimonials.md](references/testimonials.md) | Dealership subject of reviews |
| [prompts.md](references/prompts.md) | [faq.md](datasets/faq.md) | Prompt library covers FAQ topics |
