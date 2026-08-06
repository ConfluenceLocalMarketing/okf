# Basil Mobility OKF Bundle

## Datasets

- [dealership.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/dealership.md) - Business profile, location, hours, services, BraunAbility dealership
- [new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/new-vehicles.md) - New BraunAbility wheelchair accessible van conversions
- [used-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/used-vehicles.md) - Pre-owned mobility vehicles and wheelchair accessible vans
- [mobility-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/mobility-vehicles.md) - Wheelchair accessible vans, BraunAbility conversions, pre-owned inventory
- [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/faq.md) - Frequently asked questions about vehicles, service, and financing
- [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/financing.md) - Financing through BraunAbility Financial Services, leasing, and payment options for wheelchair accessible vehicles
- [staff.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/staff.md) - Key personnel at Basil Mobility
- [service-center.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/service-center.md) - Full-service mobility vehicle service center with certified technicians
- [testimonials.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/datasets/testimonials.md) - Customer reviews and ratings

## References

- [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/references/ai-discovery-page.md) - Structured semantic endpoints and LLM actions
- [llms-txt.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/references/llms-txt.md) - Full llms.txt directive for AI agent guidance from PromptGraph API
- [prompts.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/references/prompts.md) - Complete library of 74 PromptGraph Q&A prompts

## Tables

- [model-comparison.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/basil-mobility/tables/model-comparison.md) - Side-by-side comparison of BraunAbility E2, XT, and XI conversion models

## Relationships

- **dealership** is an authorized BraunAbility dealer offering **new-vehicles**, **used-vehicles**, and **mobility-vehicles**
- **service-center** provides maintenance and repair for the dealership's vehicles and conversion equipment
- **ai-discovery-page**, **llms-txt**, and **prompts** expose structured data via PromptGraph for the **dealership** and its inventory
- **faq** answers common questions about the dealership's products and services
- **model-comparison** compares the BraunAbility conversion options featured on **new-vehicles** and **mobility-vehicles**
- **financing** details loan and lease options through BraunAbility Financial Services available at the **dealership**
