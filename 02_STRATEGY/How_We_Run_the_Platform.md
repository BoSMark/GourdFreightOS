# How We Run the Platform

**Reference:** Strategy Doc 107
**Status:** DRAFT (bootstrapped from public data, 2026-06-12)
**Owner:** Jon O'Breck, Director

---

## Summary

GOURD Freight's technology platform (covering digital booking, ERP/EDI integration, real-time tracking, route optimisation, and AI planning) is a core differentiator. This document governs how the platform is developed, maintained, and governed.

## Context

GOURD Freight describes itself as a "digital-first freight forwarder." The platform capabilities described publicly include:

- Online booking (self-service rate getting across air, sea, road, rail, storage, customs)
- ERP integration (clients can connect their enterprise systems directly)
- EDI (Electronic Data Interchange) for booking submission
- Real-time tracking and shipment monitoring
- Route optimisation using AI and ML (traffic, weather, road restrictions)
- Carbon emissions reporting per shipment and mode
- Rates volatility tracking
- TMS (Transportation Management System) integration

The "admin assistant that never slept" framing on the careers page gives a useful picture of the platform's ambition: rate quoting, routing, monitoring ETAs, filling customs forms, chasing port bookings, all handled digitally, faster than a human can.

## Technology Principles

**1. Speed over paperwork.** Every manual step that can be automated should be. The platform wins if it makes an account manager faster, not if it replaces them.

**2. Transparency as a feature.** Real-time tracking, rate volatility tracking, carbon reporting: the platform's job is to give clients more information than they had before, not to obscure.

**3. AI augments humans.** AI is used for planning speed and accuracy. All client-facing outputs are reviewed by a human (account manager or Director) before use.

**4. Integrations create switching costs.** ERP and EDI integrations are high-value for clients and create genuine lock-in. Prioritise depth of integration over breadth of features.

## Platform Capabilities

| Capability | Description | Status |
|-----------|-------------|--------|
| Multi-modal rate getting | Air, sea, road, rail, storage, customs | Live (website) |
| Online booking | Self-service booking submission | Live |
| ERP integration | Client ERP systems connecting directly | Described as live |
| EDI | Electronic Data Interchange for booking | Described as live |
| Real-time tracking | Shipment status and ETA monitoring | Described as live |
| Route optimisation | AI-powered routing considering traffic, weather, restrictions | Described as live |
| Carbon reporting | Emissions per shipment per mode | Described as live |
| Rates volatility tracking | Market rate monitoring | Described as live |
| TMS integration | Integration with client transport management systems | Described as live |
| GPS / fleet management integration | For road freight | Described as live |

[INTERNAL: The Director should confirm which of the above are actually live and production-ready vs. described capabilities. This matters for client onboarding and for the competitive positioning document.]

## Data and Security Governance

- Client shipment data is commercially sensitive and must not be used in AI training or shared with third parties without consent
- ERP and EDI credentials are treated as restricted access: never stored in git or local context
- Carbon data is aggregated and anonymised before any external reporting
- UK GDPR applies to all personal data processed through the platform

## Third-Party Dependencies

[INTERNAL: The Director should document which third-party services the platform depends on: carrier APIs, tracking data providers, carbon calculation APIs, cloud infrastructure, TMS platforms, etc. These are operational risks and due diligence items for a future buyer.]

## Decision Rights

| Decision | Authority | Review |
|----------|-----------|--------|
| Platform feature prioritisation | Director | Quarterly |
| New carrier or data integration | Director | Per integration |
| Platform security and data handling | Director | Annual minimum |
| AI model selection and use | Director | Per deployment |

## Success Criteria

- [ ] Platform uptime and reliability tracked (target: >99%)
- [ ] ERP/EDI integration available for all new contract logistics clients
- [ ] Carbon reporting available for 100% of shipment modes
- [ ] No data incidents or breaches
- [ ] Platform capabilities documented well enough for a technical due diligence process

## Regulatory and Compliance Anchors

- **UK GDPR**: data minimisation, consent, and breach notification requirements
- **BIFA Standard Trading Conditions**: electronic booking and documentation standards
- **UK Customs**: HMRC customs declaration requirements; CDS (Customs Declaration Service)
- **Air cargo security**: CASP/CASPD requirements if handling air cargo as a known agent

## Cross-References

- `How_We_Make_Decisions.md`: platform decisions follow decision cascade
- `Where_We_Win.md`: platform as competitive moat
- `How_We_Move_Freight_Sustainably.md`: carbon reporting is a platform feature

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-12 | Bootstrapped from public data by BoS OS Bootstrap skill |
