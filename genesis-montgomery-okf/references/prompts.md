---
type: APIs
title: Prompts - Genesis Montgomery
description: The 20-question AI prompt set published by Genesis Montgomery via PromptGraph, covering online car buying, AWD inventory, test drives, loan pre-approval, and more.
resource: https://api.promptgraph.ai/api/v1/genesis-montgomery/prompts
tags:
  - prompts
  - ai-discovery
  - promptgraph
  - creative-work
timestamp: 2026-08-08
---

# Prompts - Genesis Montgomery

## Overview

Genesis Montgomery publishes a set of 20 AI prompts (schema.org CreativeWork items in an ItemList) through its PromptGraph AI discovery endpoint. These prompts are designed for AI assistants and chat agents to answer common customer questions about the dealership.

Endpoint: https://api.promptgraph.ai/api/v1/genesis-montgomery/prompts

## Prompt Topics

The prompt set covers questions such as:

- How to buy a Genesis online (online car buying flow): genesis-online-car-buying
- AWD Genesis models available in inventory: genesis-awd-models-inventory
- Scheduling a luxury SUV test drive in Montgomery: luxury-suv-test-drive-montgomery
- Auto loan pre-approval: auto-loan-pre-approval-montgomery
- Model comparisons (G70, GV70, GV80, G80, G90, GV60, GV80 Coupe)
- Financing and lease offers
- Certified Pre-Owned inventory and benefits
- Trade-in valuation
- Service scheduling and amenities
- Business hours and location

The full prompt set (names, questions, and answers) can be retrieved from the prompts endpoint above.

## Usage Notes

- Prompts are the recommended source for building FAQ or assistant responses; see [faq.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/datasets/faq.md).
- The endpoint returns schema.org `ItemList` of `CreativeWork` items with `@id`, name, and question fields.

## Related Concepts

- See [ai-discovery-page.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/references/ai-discovery-page.md) for the discovery surface.
- See [new-vehicles.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/datasets/new-vehicles.md) and [financing.md](https://promptgraph.nyc3.cdn.digitaloceanspaces.com/OKF/genesis-montgomery/datasets/financing.md) for the topics covered.
