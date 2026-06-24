# Basil Mobility OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) — Business profile, location, hours, services, BraunAbility dealership
- [new-vehicles.md](datasets/new-vehicles.md) — New BraunAbility wheelchair accessible van conversions
- [used-vehicles.md](datasets/used-vehicles.md) — Pre-owned mobility vehicles and wheelchair accessible vans
- [mobility-vehicles.md](datasets/mobility-vehicles.md) — Wheelchair accessible vans, BraunAbility conversions, pre-owned inventory
- [faq.md](datasets/faq.md) — Frequently asked questions about vehicles, service, and financing

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) — Structured semantic endpoints and LLM actions

## Tables

*(add tabular data here)*

## Relationships

- **dealership** is an authorized BraunAbility dealer offering **new-vehicles**, **used-vehicles**, and **mobility-vehicles**
- **ai-discovery-page** exposes structured data for the **dealership** and its inventory
- **faq** answers common questions about the dealership's products and services
