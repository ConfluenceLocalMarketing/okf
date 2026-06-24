# Basil Mitsubishi OKF Bundle

## Datasets

- [dealership.md](datasets/dealership.md) — Business profile, hours, contact, services, location
- [new-vehicles.md](datasets/new-vehicles.md) — New Mitsubishi model lineup, features, promotions
- [used-vehicles.md](datasets/used-vehicles.md) — Pre-owned and certified pre-owned inventory, trade-in
- [faq.md](datasets/faq.md) — Frequently asked questions about inventory, financing, and service

## References

- [llms-txt.md](references/llms-txt.md) — llms.txt directive content for AI agent guidance
- [ai-discovery-page.md](references/ai-discovery-page.md) — Structured semantic endpoints, LLM actions, machine-readable data

## Tables

*(empty — add tabular data extracts here)*

## Relationships

- **dealership** offers **new-vehicles** and **used-vehicles**
- **ai-discovery-page** exposes structured data for the **dealership** and both vehicle lines
- **llms-txt** provides top-level agent guidance for the entire site
- **faq** answers common questions about inventory, financing, service, and dealership perks
