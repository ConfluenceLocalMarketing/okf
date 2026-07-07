---
okf_version: "0.1"
---

# Varsity Lincoln — OKF Bundle

OKF v0.1 bundle for Varsity Lincoln, the #1 Volume Lincoln Dealer in the World for 22 consecutive years, located in Novi, MI and serving Ann Arbor, Wixom, Farmington Hills, and Metro Detroit with new and pre-owned Lincoln vehicles, certified service, genuine OEM parts, Lincoln Pickup & Delivery, Lincoln Mobile Service, Black Label experience, and luxury vehicle financing. Part of Varsity Automotive Group (family-owned, 30+ years).

## Datasets

- [dealership.md](varsity-lincoln-okf/datasets/dealership.md) - Full dealership profile with contact, hours, awards, and service area.
- [new-vehicles.md](varsity-lincoln-okf/datasets/new-vehicles.md) - Full new Lincoln luxury SUV lineup including Corsair, Nautilus, Aviator, Navigator, and Lincoln Black Label.
- [used-vehicles.md](varsity-lincoln-okf/datasets/used-vehicles.md) - Pre-owned inventory with Lincoln Certified Pre-Owned program and multi-brand luxury selection.
- [vehicles.md](varsity-lincoln-okf/datasets/vehicles.md) - Combined new and pre-owned Lincoln vehicle inventory overview.
- [service-center.md](varsity-lincoln-okf/datasets/service-center.md) - Lincoln factory-trained service center with OEM parts, mobile service, and complimentary loaners.
- [staff.md](varsity-lincoln-okf/datasets/staff.md) - Team members across management, sales, service, and parts departments.
- [faq.md](varsity-lincoln-okf/datasets/faq.md) - Common customer questions about vehicles, financing, service, and operations.
- [financing.md](varsity-lincoln-okf/datasets/financing.md) - Purchase financing, luxury leasing, pre-approval, trade-in valuation, and payment calculators.

## References

- [website.md](varsity-lincoln-okf/references/website.md) - Varsity Lincoln website reference.
- [ai-discovery-page.md](varsity-lincoln-okf/references/ai-discovery-page.md) - AI Discovery Hub with structured JSON-LD endpoints for LLM consumption.
- [llms-txt.md](varsity-lincoln-okf/references/llms-txt.md) - AI discovery directive with API endpoints and schema types.
- [prompts.md](varsity-lincoln-okf/references/prompts.md) - Structured Q&A prompts covering vehicles, financing, service, and operations.

## Tables

- [model-comparison.md](varsity-lincoln-okf/tables/model-comparison.md) - Lincoln model comparison across class, passengers, drivetrain, MSRP, and key features.

## Relationships

- [dealership.md](varsity-lincoln-okf/datasets/dealership.md) sells [new-vehicles.md](varsity-lincoln-okf/datasets/new-vehicles.md) and [used-vehicles.md](varsity-lincoln-okf/datasets/used-vehicles.md)
- [dealership.md](varsity-lincoln-okf/datasets/dealership.md) operates [service-center.md](varsity-lincoln-okf/datasets/service-center.md)
- [dealership.md](varsity-lincoln-okf/datasets/dealership.md) offers [financing.md](varsity-lincoln-okf/datasets/financing.md)
- [staff.md](varsity-lincoln-okf/datasets/staff.md) works at [dealership.md](varsity-lincoln-okf/datasets/dealership.md)
- [dealership.md](varsity-lincoln-okf/datasets/dealership.md) references [model-comparison.md](varsity-lincoln-okf/tables/model-comparison.md) for vehicle specifications
