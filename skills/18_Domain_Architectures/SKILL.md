---
name: domain-reference-architectures
description: Worked end-to-end reference architectures per product category — SaaS/B2B, marketplace/e-commerce, and AI/IoT/robotics products — showing how the rest of the knowledge base's domain-level decisions compose into a coherent whole system.
---

# 18 — Domain Reference Architectures (L4)

**Level:** L4 — Principal Engineering (synthesis across all other domains).

## Goal

Every other skill domain in this knowledge base addresses one slice of a system (database, API, cloud, security...). This domain exists to show how those slices compose into a coherent, end-to-end architecture for specific, common product categories — because the hardest part of applying architectural knowledge is often not any single decision, but integrating many simultaneous decisions into one consistent system.

## How to Use These References

Each reference file in this domain walks through a representative product category (building on the category deep dives already established in `skills/02_Product/reference/product-discovery-requirements.md`) and shows a concrete, justified reference architecture: which data stores, which API style, which deployment topology, which specific trade-offs were made and why — in the same Output Standard format used by `/archon-principal` mode. These are *reference points to reason from and adapt*, not templates to copy verbatim — the actual right architecture for any real product still depends on its specific constraints (team size, stage, compliance needs).

## Reference Files

- `reference/saas-b2b-architecture.md` — a reference architecture for a typical multi-tenant B2B SaaS product.
- `reference/marketplace-ecommerce-architecture.md` — a reference architecture for marketplace and e-commerce products.
- `reference/ai-iot-robotics-product-architecture.md` — a reference architecture spanning AI-enabled products, IoT products, and robotics products, reflecting their shared cloud-to-edge-to-device structure.
