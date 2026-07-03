# How We Make Decisions

**Reference:** Strategy Doc 105
**Status:** DRAFT (bootstrapped from public data, 2026-06-12)
**Owner:** Jon O'Breck, Director

---

## Summary

GOURD Freight is a small company where most decisions currently sit with the Director. This document captures the decision governance framework the BoS OS will use: both for current operations and to build towards a business that can operate without being dependent on any single person.

## Context

At this stage of the business, the Director makes most material decisions. The five-year exit goal requires deliberately building a decision-making structure that is legible and transferable. This means documenting how decisions are made now, and designing towards a structure where agents, account managers, and any future leadership team can make good decisions without needing to ask the founder every time.

The BoS OS Decision Cascade Governance (see CLAUDE.md) applies to all AI agent work. This document governs business-level decisions more broadly.

## Governing Principles

**1. Draft first, decide second.** No significant decision is made in the moment. Proposals are drafted (in 00_LOCAL_CONTEXT), presented with options and trade-offs, then approved. This applies to AI agents and humans.

**2. Decisions are documented.** Every material decision goes in `01_STATE/decisions.md` with date, rationale, and who approved. The goal is an audit trail a future owner or buyer could read and understand.

**3. Account managers have real authority within their book.** The profit-sharing model only works if account managers have genuine autonomy over their client relationships. The decision framework should make their authority explicit, not create friction.

**4. Escalation paths exist.** When an account manager faces a decision outside their authority (unusual pricing, contractual terms, complaints), there should be a clear escalation path to the Director.

**5. Sustainability is a decision input, not a veto.** Every routing and carrier decision considers carbon; it's not optional. But the client ultimately chooses, with full information.

## Decision Authority Matrix

| Decision | Authority | Escalation |
|----------|-----------|-----------|
| Client routing and carrier selection (within standard options) | Account manager | Director if unusual terms |
| Pricing within approved range | Account manager | Director if below floor |
| Contract logistics terms | Director | N/A |
| New carrier or supplier relationships | Director | N/A |
| Carbon reporting methodology | Director + sustainability advisors | N/A |
| Hire (account manager, staff) | Director | N/A |
| Changes to profit-sharing terms | Director | N/A |
| B Corp certification decisions | Director | N/A |
| Any AI agent output that affects a client | Account manager or Director reviews before use | N/A |
| BoS OS strategy documents (revise, add, remove) | Director | N/A |

## Agent Decision Cascade

All AI agents operating within this OS follow the BoS OS Decision Cascade:

1. **Draft** in `00_LOCAL_CONTEXT/`: no tracked files modified
2. **Present** decision to responsible human with options, recommendation, and trade-offs
3. **Approval** from the responsible human (explicit, not inferred)
4. **Implement** and log to `01_STATE/decisions.md`
5. **Audit** by Director on monthly cadence

No agent may take an action with external consequence (sending communications, committing to routes, producing client-facing output) without explicit human approval.

## Confidentiality Rules

- Financial terms, client names, contract details: `00_LOCAL_CONTEXT/` only, never in tracked files
- Carrier pricing: treated as commercially sensitive
- Personnel matters (including profit-share calculations): `00_LOCAL_CONTEXT/` only
- Client PII and shipment data: not to be included in agent prompts or local context

## Decision Rights for BoS OS Documents

| Decision | Authority | Review |
|----------|-----------|--------|
| Add new strategy document | Director | As needed |
| Revise existing strategy document | Document owner (Director at this stage) | Document owner's discretion |
| Move content from 00_LOCAL_CONTEXT to tracked files | Director | Per decision |
| Archive a strategy document | Director | Annual review |

## Success Criteria

- [ ] All material business decisions logged in `01_STATE/decisions.md`
- [ ] No agent output used externally without human review
- [ ] Account managers have documented decision authority within their books
- [ ] Decision log is legible to a third party (future buyer, investor, auditor)

## Regulatory and Compliance Anchors

- **BIFA Standard Trading Conditions 2025**: commercial decisions must operate within these
- **UK Companies Act**: Director has legal responsibilities; agent outputs do not substitute for Director judgment on material matters
- **UK GDPR**: decisions about data handling require documented rationale

## Cross-References

- `CLAUDE.md`: Decision Cascade Governance for the BoS OS
- `Our_Values.md`: values inform decision trade-offs
- `How_We_Grow.md`: growth decisions reference this framework

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-12 | Bootstrapped from public data by BoS OS Bootstrap skill |

[INTERNAL: This document needs internal review to confirm: (1) what pricing floor account managers operate within, (2) whether there are any existing decision-making structures or norms not captured here, (3) what cadence the Director wants to review the decisions log.]
