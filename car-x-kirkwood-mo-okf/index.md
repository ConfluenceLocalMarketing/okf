---
okf_version: "0.1"
---

# Car-X Tire & Auto Kirkwood, MO OKF Bundle

## Datasets

- [location.md](datasets/location.md) - Car-X Tire & Auto location in Kirkwood, MO: address, hours, contact, and full auto repair services.
- [services.md](datasets/services.md) - Full service menu including brakes, tires, maintenance, diagnostics, steering/suspension, and pre-owned inspections

## References

- [prompts.md](references/prompts.md) - Complete PromptGraph library of 105 structured Q&A prompts covering all auto repair and maintenance topics
- [ai-discovery.md](references/ai-discovery.md) - AI Discovery Page with 16 ReadAction service endpoints and JSON-LD schema.org AutoDealer data


## Tables

- [coupons.md](tables/coupons.md) - Current promotional offers, coupons, and financing options

## Relationships

- **location** operates as a Car-X franchise in Kirkwood, MO
- **services** lists all repair and maintenance categories offered at the **location**
- **prompts** provides AI-consumable Q&A covering all **services** and general auto care topics
- **ai-discovery** exposes structured ReadAction endpoints and JSON-LD schema for the corporate umbrella
