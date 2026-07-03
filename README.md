# GOURD Freight: A Worked BoS OS Example

GOURD Freight Ltd is a fictional company. Its BoS OS was built by running the real Bootstrap, Workshop, and Run skills end to end, then developed to a realistic "month three" state: not perfect, but lived-in.

## Why this exists

Most people building a BoS OS ask the same question early on: is what I've got any good, or is it broken? Without something to compare against, it's hard to tell. This repo is that comparison point.

## What's here

- Full folder structure matching the BoS OS: strategy documents, a role stub, a decision log, session state, and a first mission (`04_MISSIONS/M01_Pricing_Exception_Agent/`)
- Strategy documents at different stages of maturity. Some are just bootstrapped from public information, others were worked through in a Workshop session with the founder. That mix is intentional: a real OS is never uniformly finished.
- A first mission taken from idea to spec: a Pricing Exception Agent that learns the founder's routing judgment from an email workflow
- A decision log (`01_STATE/decisions.md`) and session summary showing what a lived-in operating rhythm looks like

## How to use it

Start with `CLAUDE.md`. It's GOURD Freight's own governing document, and it explains the constraints its agents operate under. Then read `01_STATE/session_summary.md` for where things currently stand, and `04_MISSIONS/M01_Pricing_Exception_Agent/MISSION.md` to see what a mission looks like once it's been shaped from a vague idea into something specific.

## Get hands-on with it

Reading the files only gets you so far. Clone this repo to its own folder on your computer, separate from any BoS OS you're building for your own company, and open it in Claude or any editor. Then follow the thread through a few files instead of reading them in isolation:

1. Open `CLAUDE.md` first. It's the rulebook: what agents can and can't do, who approves what, where confidential material goes.
2. Open `01_STATE/decisions.md` and pick a recent entry. Notice it names the files that changed as a result.
3. Follow one of those files back to `04_MISSIONS/M01_Pricing_Exception_Agent/MISSION.md` and see how a vague idea became a scoped mission with a named owner and a decision boundary.
4. Open `01_STATE/session_summary.md` and compare it to the decision log. That's what "current state" looks like day to day, not a one-time snapshot.

None of this is precious. Rename files, delete a mission, add a fake strategy document, break something on purpose. It's a fictional company. There's nothing here to protect.

```
git clone https://github.com/BoSMark/GourdFreightOS.git
```

## This isn't a template to copy

Your strategy documents, decision boundaries, and missions should come from your own business, built with [Bootstrap, Workshop, and Run](https://github.com/BoSMark/BoS_OS_Start). GOURD Freight exists so you have something real to measure your own OS against, and something safe to break, once you've built one.

## What's fictional, and why

GOURD Freight Ltd does not exist. Its founder, financials, and clients are invented. The pricing thresholds, growth targets, and decision boundaries throughout are illustrative: specific enough to be instructive, not drawn from any real company's numbers.

---

Built with the [BoS OS](https://github.com/BoSMark/BoS_OS_Start), Business of Software's operating system for founders who want AI to have a governed place inside how they actually run their company.
