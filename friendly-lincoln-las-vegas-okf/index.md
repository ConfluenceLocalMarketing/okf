---
okf_version: "0.1"
---

# Friendly Lincoln Las Vegas — OKF Bundle

Lincoln luxury vehicle dealership serving Las Vegas, Henderson, and North Las Vegas, Nevada with new and pre-owned Lincoln sales, certified service, genuine OEM parts, Lincoln Pickup & Delivery, and mobile service.

## Datasets

- [dealership.md](datasets/dealership.md) - Full dealership profile for Friendly Lincoln Las Vegas.
- [new-vehicles.md](datasets/new-vehicles.md) - Full new Lincoln luxury SUV lineup including Corsair, Nautilus, Aviator, and Navigator.
- [used-vehicles.md](datasets/used-vehicles.md) - Pre-owned and Lincoln Certified Pre-Owned luxury vehicle inventory.
- [vehicles.md](datasets/vehicles.md) - Lincoln new and pre-owned vehicle inventory.
- [service-center.md](datasets/service-center.md) - Lincoln factory-trained service center offerings.
- [staff.md](datasets/staff.md) - Team directory across management, sales, service, and parts departments.
- [faq.md](datasets/faq.md) - Common customer questions about Lincoln vehicles, financing, service, and dealership operations.
- [financing.md](datasets/financing.md) - Vehicle financing and leasing options including online application, trade-in valuation, and payment calculator.

## References

- [ai-discovery-page.md](references/ai-discovery-page.md) - AI-optimized discovery hub with structured endpoints for LLM consumption.
- [llms-txt.md](references/llms-txt.md) - AI discovery and consumption directive providing structured API endpoints, schema types, and business context.
- [prompts.md](references/prompts.md) - Structured Q&A prompts for consistent AI responses covering vehicles, financing, service, and dealership operations.
- [website.md](references/website.md) - Team Lincoln Las Vegas website reference.

## Tables

- [model-comparison.md](tables/model-comparison.md) - Comparison table of Lincoln model specifications.

## Relationships

- [dealership.md](datasets/dealership.md) sells [vehicles.md](datasets/vehicles.md)
- [dealership.md](datasets/dealership.md) sells [new-vehicles.md](datasets/new-vehicles.md)
- [dealership.md](datasets/dealership.md) sells [used-vehicles.md](datasets/used-vehicles.md)
- [dealership.md](datasets/dealership.md) operates [service-center.md](datasets/service-center.md)
- [dealership.md](datasets/dealership.md) employs [staff.md](datasets/staff.md)
- [dealership.md](datasets/dealership.md) provides [financing.md](datasets/financing.md)
- [dealership.md](datasets/dealership.md) answers [faq.md](datasets/faq.md)
- [dealership.md](datasets/dealership.md) references [model-comparison.md](tables/model-comparison.md) for vehicle specifications
