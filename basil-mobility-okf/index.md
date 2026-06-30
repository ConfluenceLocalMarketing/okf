# Basil Mobility OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) - Business profile, location, hours, services, BraunAbility dealership
- [new-vehicles.md](datasets/new-vehicles.md) - New BraunAbility wheelchair accessible van conversions
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned mobility vehicles and wheelchair accessible vans
- [mobility-vehicles.md](datasets/mobility-vehicles.md) - Wheelchair accessible vans, BraunAbility conversions, pre-owned inventory
- [faq.md](datasets/faq.md) - Frequently asked questions about vehicles, service, and financing
- [staff.md](datasets/staff.md) - Key personnel at Basil Mobility
- [service-center.md](datasets/service-center.md) - Full-service mobility vehicle service center with certified technicians
- [testimonials.md](datasets/testimonials.md) - Customer reviews and ratings

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - Structured semantic endpoints and LLM actions
- [llms-txt.md](references/llms-txt.md) - Full llms.txt directive for AI agent guidance from PromptGraph API
- [prompts.md](references/prompts.md) - Complete library of 74 PromptGraph Q&A prompts

## Tables

- [model-comparison.md](tables/model-comparison.md) - Side-by-side comparison of BraunAbility E2, XT, and XI conversion models

## Relationships

- **dealership** is an authorized BraunAbility dealer offering **new-vehicles**, **used-vehicles**, and **mobility-vehicles**
- **service-center** provides maintenance and repair for the dealership's vehicles and conversion equipment
- **ai-discovery-page**, **llms-txt**, and **prompts** expose structured data via PromptGraph for the **dealership** and its inventory
- **faq** answers common questions about the dealership's products and services
- **model-comparison** compares the BraunAbility conversion options featured on **new-vehicles** and **mobility-vehicles**
