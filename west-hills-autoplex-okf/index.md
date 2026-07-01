---
okf_version: "0.1"
---

# West Hills Autoplex OKF Bundle

## Datasets

- [autoplex.md](datasets/autoplex.md) - Group profile, history, leadership, member dealerships, locations, and community involvement for the West Hills Auto Plex in Bremerton, WA
- [west-hills-honda.md](datasets/west-hills-honda.md) - Business profile, hours, contact, services, location, and Honda models for West Hills Honda in Bremerton, WA
- [west-hills-chrysler-jeep-dodge-ram.md](datasets/west-hills-chrysler-jeep-dodge-ram.md) - Business profile, hours, contact, services, location, and Chrysler/Jeep/Dodge/Ram models for West Hills Chrysler Jeep Dodge RAM in Bremerton, WA
- [west-hills-ford.md](datasets/west-hills-ford.md) - Business profile, hours, contact, services, location, and Ford models for West Hills Ford in Bremerton, WA
- [west-hills-kia.md](datasets/west-hills-kia.md) - Business profile, hours, contact, services, location, and Kia models for West Hills Kia in Bremerton, WA
- [west-hills-mazda.md](datasets/west-hills-mazda.md) - Business profile, hours, contact, services, location, and Mazda models for West Hills Mazda in Bremerton, WA
- [faq.md](datasets/faq.md) - Frequently asked questions about the West Hills Auto Plex group, member dealerships, inventory, financing, and service

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - Structured semantic endpoints, PromptGraph API, business profiles, vehicle inventory, and LLM actions for the West Hills Autoplex group
- [llms-txt.md](references/llms-txt.md) - Full llms.txt directive content including PromptGraph API endpoints, site pages, and featured AI prompts
- [prompts.md](references/prompts.md) - Complete PromptGraph library of structured Q&A prompts covering vehicles, financing, service, and dealership info

## Tables

- [dealership-comparison.md](tables/dealership-comparison.md) - Side-by-side comparison of all member dealerships including franchise, address, phone, service hours, and available models

## Relationships

- **autoplex** operates **west-hills-honda**, **west-hills-chrysler-jeep-dodge-ram**, **west-hills-ford**, **west-hills-kia**, and **west-hills-mazda** as member dealerships
- **autoplex** is part of the **Haselwood Auto Group**
- All member dealerships offer **new-vehicle sales**, **pre-owned inventory**, **service centers**, and **financing**
- **ai-discovery-page** exposes structured data for the group business profile and all member dealerships
- **llms-txt** provides top-level agent guidance for the group
- **faq** answers common questions about the group, member dealerships, inventory, financing, and service
- **dealership-comparison** provides structured comparison data for all member dealerships
- **prompts** provides AI-consumable Q&A covering all **datasets** concepts
