# Compliance & Regulatory Governance

## Goal

Compliance frameworks (GDPR, HIPAA, SOC 2, PCI-DSS, and similar) translate into concrete, non-negotiable technical requirements — not just paperwork. Treat the relevant framework as an architecture input from the first design pass for any system handling the data category it covers, because retrofitting compliance onto an already-built system is dramatically more expensive than designing for it from the start.

## Framework Decision Matrix

| Framework | Triggered by | Core technical requirements | Common mistake |
|---|---|---|---|
| GDPR | Processing personal data of EU residents, regardless of where the company is based | Lawful basis for processing, data subject access/deletion/portability rights, breach notification within 72 hours, data minimization, privacy-by-design | Treating "we're not based in the EU" as exemption — GDPR applies based on whose data you process, not where you're incorporated |
| HIPAA | Handling Protected Health Information (PHI) in the US, as a covered entity or business associate | Access controls and audit logging on PHI, encryption at rest and in transit, signed Business Associate Agreements (BAAs) with any vendor touching PHI, breach notification rules | Assuming a cloud provider's general security certifications cover HIPAA without confirming the specific services used are covered under a signed BAA |
| SOC 2 | Almost always a sales/trust requirement from enterprise buyers, not a legal mandate | Documented access controls, change management process, vendor risk management, continuous monitoring, an annual third-party audit (Type II covers a period of time, not a point in time) | Starting the audit-readiness process only after a deal is blocked on it — Type II requires evidence collected over months, so the lead time is real |
| PCI-DSS | Storing, processing, or transmitting cardholder data directly | Strong default: don't touch raw card data at all — tokenize through a PCI-compliant processor (Stripe, Adyen, Braintree) so PCI scope stays minimal | Building custom card-storage/payment logic "to save on processor fees" without appreciating the compliance burden and breach liability that comes with expanded PCI scope |

## Designing for Compliance, Not Just Auditing for It

The technical controls these frameworks require — access logging, encryption, data lifecycle management, vendor risk tracking — substantially overlap with `skills/12_Security/reference/data-protection-encryption.md` and `skills/12_Security/reference/authn-authz.md`. Build those controls as standard architecture practice regardless of whether a framework currently requires them; this means the eventual compliance push is a documentation and audit exercise rather than a re-architecture effort.

## Staged Approach

| Stage | Compliance posture |
|---|---|
| Pre-PMF | Know which frameworks your data categories and target customers will eventually require; don't build the full control set before there's a real trigger, but don't make architecture choices that would make later compliance unreasonably hard (e.g., commingling regulated and unregulated data with no separation) |
| Early enterprise sales | SOC 2 Type II readiness typically becomes the first real trigger — start the audit-readiness process (often 6-12 months of evidence collection) as soon as enterprise deals are in the pipeline, not after one stalls on it |
| Regulated data at scale | Dedicated compliance/security headcount, formal risk assessments, and a recurring audit cadence become justified once the regulated-data surface area and customer base are large enough that the cost of a violation or a failed audit clearly outweighs the investment |

## Vendor and Sub-Processor Risk

Every third-party vendor that touches regulated data extends your compliance boundary to include their controls. Maintain an explicit inventory of sub-processors handling regulated data, confirm they carry the relevant certifications/agreements (BAA for HIPAA, a Data Processing Agreement for GDPR), and re-verify this when adding new vendors — a compliance gap introduced by an under-vetted vendor is still your liability.

## Common Mistakes

- Treating compliance as a one-time certification rather than an ongoing operational practice (access reviews, control monitoring, evidence collection don't stop after the audit passes).
- Expanding PCI scope unnecessarily by touching raw card data when a tokenizing processor would keep that scope minimal.
- Signing up enterprise customers requiring SOC 2 before starting the audit-readiness clock, creating an avoidable sales blocker.
- Assuming a cloud provider's own compliance certifications automatically extend to cover how the product uses that provider's services — shared responsibility applies to compliance as much as to security.

## Decision Rule for This Domain

Identify the compliance frameworks triggered by your actual data categories and customer base early, build the underlying technical controls (access control, encryption, audit logging, vendor risk tracking) as standard practice rather than framework-specific add-ons, and start audit-readiness work (especially SOC 2 Type II) well before a deal or regulator forces the timeline.
