---
okf_version: "0.1"
---

# Car-X Tire & Auto Arnold OKF Bundle

## Datasets

- [location.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/car-x-arnold-mo-okf/datasets/location.md) - Car-X Arnold location profile: address, hours, contact, rating, and services
- [services.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/car-x-arnold-mo-okf/datasets/services.md) - Full service menu including brakes, tires, maintenance, diagnostics, steering/suspension, and pre-owned inspections

## References

- [prompts.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/car-x-arnold-mo-okf/references/prompts.md) - Complete PromptGraph library of 105 structured Q&A prompts covering all auto repair and maintenance topics
- [ai-discovery.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/car-x-arnold-mo-okf/references/ai-discovery.md) - AI Discovery Page with 16 ReadAction service endpoints and JSON-LD schema.org AutoDealer data


## Tables

- [coupons.md](https://github.com/ConfluenceLocalMarketing/okf/blob/main/car-x-arnold-mo-okf/tables/coupons.md) - Current promotional offers, coupons, and financing options

## Relationships

- **location** operates as a Car-X franchise in Arnold, MO
- **services** lists all repair and maintenance categories offered at the **location**
- **prompts** provides AI-consumable Q&A covering all **services** and general auto care topics
- **ai-discovery** exposes structured ReadAction endpoints and JSON-LD schema for the corporate umbrella
