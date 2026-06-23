# Agent Registry

ARCHON ships a single agent. This registry exists as the canonical record of that agent's identity and scope, per ADR-001 in `ARCHITECTURE_DECISIONS.md` (single cohesive agent with internal L1-L5 levels, rejecting a separate-agent-per-C-suite-role model).

| Field | Value |
|---|---|
| Name | `archon` |
| File | `agents/archon.md` |
| Persona | Principal Engineer / CTO-level technical decision-maker |
| Levels | L1 Foundations → L2 Software Engineering → L3 Infrastructure & Cloud → L4 Principal Engineering → L5 CTO & Business |
| Tools | Read, Grep, Glob, WebSearch |
| Model | inherit |
| Invocation | Via the 8 slash commands in `COMMAND_REGISTRY.md`, or directly as a subagent |

## Why One Agent, Not Many

The source playbook this project draws structural inspiration from describes a full C-suite roster (CEO/CPO/CTO/CIO/COO/CFO/CRO/CMO/CHRO/CBO agents). ARCHON deliberately implements only the CTO/Principal-Engineer persona as a single agent with internal seniority levels, because the actual need this project serves is a single, consistent engineering decision-making voice — not a simulated executive team. See ADR-001 for the full reasoning.

## How the Agent Uses the Skill Library

The `archon` agent does not hardcode domain knowledge in its own definition. It reasons using the Engineering Decision Principles and the 8 Core Principles defined in `skills/00_Core/`, and pulls domain-specific decision rules from the 20 domain skill modules (`skills/01_Foundations/` through `skills/19_Review_Outputs/`) plus the cross-cutting `skills/99_Decision_Engine/` routing layer, exactly as a Claude Code subagent is expected to compose with the skill library available to it. See `SKILL_REGISTRY.md` for the full skill module list and `MODULE_INDEX.md` for the complete repository map.

## Adding a New Agent

Per `CONTRIBUTING.md`, new agents are out of scope unless they represent a genuinely distinct persona need (not just a new domain of knowledge, which belongs in `skills/` instead). Any proposal to add a second agent should start with an ADR explaining why the single-agent model in ADR-001 no longer fits.
