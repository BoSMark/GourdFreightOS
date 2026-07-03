# GOURD Freight: A Worked BoS OS Example

GOURD Freight Ltd is a fictional company. Its BoS OS was built by running the real Bootstrap, Workshop, and Run skills end to end: about twenty minutes of bootstrapping, an hour of Workshop, and a first mission through Run. Call it two hours of work in total. A founder doing the same thing around a normal week might spread that across two or three days, but the effort behind it is closer to an afternoon than a quarter. This is what's in hand after a first real pass through the OS, not a polished archive of months of use.

> **This is a sandbox, not a template. It isn't connected to your company or your BoS OS in any way.** Explore it, go down rabbit holes, break things on purpose. **When you build your own BoS OS, start from scratch with [Bootstrap, Workshop, and Run](https://github.com/BoSMark/BoS_OS_Start), in a new Claude Cowork project and a new folder, separate from wherever you cloned this one. Don't copy or adapt anything from this repo into it.** Your OS needs to come from your business, not from GOURD Freight's.

## Why this exists

A BoS OS is abstract until you've seen one running: what the folders actually hold, how a decision in `decisions.md` ties back to a mission, what `session_summary.md` looks like after a founder's first real session. This repo is that: a fictional company's OS, built the same way yours would be, so you can see the pieces in place and play with them before you build your own.

## What's here

- Full folder structure matching the BoS OS: strategy documents, a role stub, a decision log, session state, and a first mission (`04_MISSIONS/M01_Pricing_Exception_Agent/`)
- Strategy documents at different stages of maturity. Some are just bootstrapped from public information, others were worked through in a Workshop session with the founder. That mix is intentional: a real OS is never uniformly finished.
- A first mission taken from idea to spec: a Pricing Exception Agent that learns the founder's routing judgment from an email workflow
- A decision log (`01_STATE/decisions.md`) and session summary showing what a lived-in operating rhythm looks like

## How to use it

Start with `CLAUDE.md`. It's GOURD Freight's own governing document, and it explains the constraints its agents operate under. Then read `01_STATE/session_summary.md` for where things currently stand, and `04_MISSIONS/M01_Pricing_Exception_Agent/MISSION.md` to see what a mission looks like once it's been shaped from a vague idea into something specific.

## Get hands-on with it

Reading the files only gets you so far. Clone this repo to its own folder on your computer, separate from any BoS OS you're building for your own company, and open it in Claude or any editor. Go down rabbit holes. Follow the thread through a few files instead of reading them in isolation:

1. Open `CLAUDE.md` first. It's the rulebook: what agents can and can't do, who approves what, where confidential material goes.
2. Open `01_STATE/decisions.md` and pick a recent entry. Notice it names the files that changed as a result.
3. Follow one of those files back to `04_MISSIONS/M01_Pricing_Exception_Agent/MISSION.md` and see how a vague idea became a scoped mission with a named owner and a decision boundary.
4. Open `01_STATE/session_summary.md` and compare it to the decision log. That's what "current state" looks like day to day, not a one-time snapshot.

None of this is precious. Rename files, delete a mission, add a fake strategy document, break something on purpose. It's a fictional company, not connected to anything real. There's nothing here to protect.

```
git clone https://github.com/BoSMark/GourdFreightOS.git
```

## What's fictional, and why

GOURD Freight Ltd does not exist. Its founder, financials, and clients are invented. The pricing thresholds, growth targets, and decision boundaries throughout are illustrative: specific enough to be instructive, not drawn from any real company's numbers.

## Where to go next

Once you've explored GOURD Freight, the natural next step is your own. Clone [Bootstrap, Workshop, and Run](https://github.com/BoSMark/BoS_OS_Start) and start with your own business, not this one, in a new Claude Cowork project and a new folder.

```
git clone https://github.com/BoSMark/BoS_OS_Start.git
```

---

Built with the [BoS OS](https://github.com/BoSMark/BoS_OS_Start), Business of Software's operating system for founders who want AI to have a governed place inside how they run their company.
