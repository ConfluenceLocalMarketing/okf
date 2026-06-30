---
okf_version: "0.1"
---

# Ron Marhofer Hyundai of Green

OKF v0.1 knowledge bundle for Ron Marhofer Hyundai of Green, a Hyundai dealership located in Akron, Ohio.

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, contact, hours, location, and services of Ron Marhofer Hyundai of Green.
- [new-vehicles.md](datasets/new-vehicles.md) - Hyundai model lineup including sedans, SUVs, hybrids, and EVs available at the dealership.
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned inventory of used cars, SUVs, and trucks.
- [staff.md](datasets/staff.md) - Sales and service staff directory.
- [service-center.md](datasets/service-center.md) - Service department with factory-trained technicians and genuine parts.
- [faq.md](datasets/faq.md) - Frequently asked questions about dealership services, financing, and policies.

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - AI Discovery Page documentation and PromptGraph API endpoints for structured data access.
- [llms-txt.md](references/llms-txt.md) - LLM directives and AI consumption guidelines from the PromptGraph API.
- [testimonials.md](references/testimonials.md) - Customer reviews and testimonials.
- [prompts.md](references/prompts.md) - Curated Q&A prompt library for consistent AI responses about the dealership.

## Tables

- [model-comparison.md](tables/model-comparison.md) - Comparison table of Hyundai models available at the dealership.

## Relationships

- [dealership.md](datasets/dealership.md) is the parent entity for all other concepts.
- [new-vehicles.md](datasets/new-vehicles.md) and [used-vehicles.md](datasets/used-vehicles.md) represent inventory offered at [dealership.md](datasets/dealership.md).
- [service-center.md](datasets/service-center.md) represents the service department operated by [dealership.md](datasets/dealership.md).
- [staff.md](datasets/staff.md) lists personnel employed by [dealership.md](datasets/dealership.md).
- [model-comparison.md](tables/model-comparison.md) provides structured comparison data for [new-vehicles.md](datasets/new-vehicles.md).
- [testimonials.md](references/testimonials.md) captures customer feedback about [dealership.md](datasets/dealership.md) and [service-center.md](datasets/service-center.md).
- [prompts.md](references/prompts.md) provides AI-facing Q&A content referencing all other concepts.
