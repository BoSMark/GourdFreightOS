# Mission M01: Pricing Exception Agent

**Status:** Planned
**Created:** 2026-06-12
**Owner:** Jon O'Breck, Director
**Phase:** Pre-deployment: ground truth collection
**Thresholds confirmed (2026-06-12):** margin floor 10%, deal size £500

---

## The Problem

Pricing exceptions currently land in Jon's inbox and require his personal judgment every time. Approximately 80% follow predictable patterns and don't genuinely require him, but because there is no documented decision logic, everything escalates to the Director by default. This is a time drain and a single point of failure.

## The Mission

Build an agent that sits in Jon's email workflow, captures pricing exception decisions as they happen, and over time learns to route the predictable 80% without requiring Jon: escalating only the genuinely ambiguous 20%, with context from similar past decisions.

Jon's behaviour does not change. The agent works around him, not through him.

---

## Boundaries

**Within scope:**
- Pricing exception requests arriving by email to Jon's inbox
- Exceptions defined as: margin below 10% OR deal size above £500 (thresholds confirmed 2026-06-12)
- Logging decision, reasoning, and outcome for every exception

**Email system:** Jon's homegrown system. Jon identifies and flags pricing exception emails himself: the agent does not auto-detect. This keeps Jon in control and avoids false positives while trust is being established.

**Out of scope:**
- Routine quotes within boundary (handled by finance, not exceptions)
- Strategic commercial decisions
- New client relationship decisions
- Any decision with contractual or legal implications

**Hard constraints:**
- The agent never approves or rejects an exception autonomously: it routes and presents, Jon decides
- All decisions remain with Jon until the decision library is large enough to validate autonomous routing (minimum 50 logged decisions, 80%+ match rate on test cases)
- No client data leaves GOURD Freight systems

---

## Ground Truth

No historical record of past exceptions exists. Ground truth is built forward from mission start.

**What gets logged for every exception:**
1. What was requested (route, carrier, client type, deal size, margin)
2. What Jon decided (approve / reject / modify)
3. Jon's reasoning (one sentence minimum)
4. Outcome (did the decision play out as expected?)

Logging is automatic: captured by the agent from the email workflow. Jon does not fill in a form.

---

## Phase Structure

### Phase 1: Passive logging (Weeks 1-6)
- Agent monitors Jon's inbox for pricing exception emails
- Presents each exception in structured format for Jon's decision
- Logs decision and reasoning automatically
- Target: 20-30 logged decisions
- Success: clean log exists, no friction added to Jon's workflow

### Phase 2: Pattern calibration (After 10-15 decisions, earlier than originally planned)

**How reasoning is captured:** Not in real time. Jon's reasoning is captured in a dedicated Calibration Session: a structured review of the logged decisions where Jon explains his call on each one. Some will reveal clear patterns; some won't. Both outcomes are useful. The agent updates the log after each session.

### Phase 2 original (After 20-30 decisions)
- Review logged decisions with Jon
- Identify the predictable patterns: what characteristics make an exception obviously approvable or obviously rejectable?
- Codify initial routing rules from observed decisions
- Success: at least 3 clear routing rules identified and agreed

### Phase 3: Blind test (After 30-50 decisions)
- Agent scores new incoming exceptions against routing rules before showing to Jon
- Jon makes his call without seeing the agent's suggestion
- Compare: how often does the agent's routing match Jon's decision?
- Target: 80%+ match rate
- Success: match rate confirmed, rules refined

### Phase 4: Assisted routing (After 80%+ match rate confirmed)
- Agent presents its routing recommendation alongside each exception
- Jon can accept or override
- Every override is logged and used to refine rules
- Success: Jon reports reduced cognitive load on exceptions

### Phase 5: Autonomous routing (future, after extensive validation)
- Predictable exceptions routed without Jon
- Ambiguous exceptions escalated with context: "here are 3 similar past decisions and how you called them"
- Jon reviews a weekly digest rather than individual exceptions
- Success: Jon's time on routine pricing exceptions approaches zero

---

## Success Metrics

- **Phase 1:** 20+ decisions logged with zero additional work from Jon
- **Phase 3:** Agent matches Jon's call on 80%+ of test cases
- **Phase 5:** Jon spends less than 30 minutes per week on pricing exceptions (down from current baseline, to be measured in Phase 1)

---

## What This Proves

If this mission works, it demonstrates that the BoS OS can learn Jon's judgment in a bounded domain and apply it consistently: freeing him to focus on the 20% that genuinely requires him. It is the proof of concept for the broader ambition: a Director who operates at Director level, not dispatcher level.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-06-12 | Created in Workshop Phase 3, by Jon O'Breck, Director |
| 0.2 | 2026-06-12 | Thresholds confirmed (10% margin, £500 deal size); email workflow clarified: Jon flags, agent logs |
