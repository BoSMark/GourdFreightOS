"""
Calibration Session for GOURD Freight M01 Pricing Exception Agent

Run this when 10-15 decisions have accumulated in exceptions_log.csv.
Walks through unreviewed decisions one at a time, captures Jon's
reasoning and decision, writes back to the log.

Usage: python calibration_session.py
"""

import csv
import os
import tempfile
import shutil

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exceptions_log.csv")

def run_calibration():
    if not os.path.exists(LOG_FILE):
        print("No log file found. Nothing to review.")
        return

    with open(LOG_FILE, newline="") as f:
        rows = list(csv.DictReader(f))

    unreviewed = [r for r in rows if not r.get("jon_decision")]

    if not unreviewed:
        print("Nothing to review: all logged decisions already have Jon's input.")
        return

    print(f"\n=== Calibration Session ===")
    print(f"{len(unreviewed)} decision(s) to review.\n")
    print("For each one, enter Jon's decision and reasoning.")
    print("Press Enter to skip any you can't recall. Type 'quit' to stop and save.\n")

    updated = 0

    for i, row in enumerate(rows):
        if row.get("jon_decision"):
            continue  # already reviewed

        print(f"--- Exception {i+1} of {len(rows)} ---")
        print(f"  Date:       {row.get('date', '')}")
        print(f"  Client:     {row.get('client', '')}")
        print(f"  Route:      {row.get('route', '')}")
        print(f"  Carrier:    {row.get('carrier', '')}")
        print(f"  Deal size:  £{row.get('deal_size_gbp', '')}")
        print(f"  Margin:     {row.get('margin_pct', '')}%")
        print(f"  Agent said: {row.get('agent_prediction', '')}: {row.get('agent_reasoning', '')}")
        print()

        decision = input("  Jon's decision (approve / reject / modify / skip / quit): ").strip().lower()

        if decision == "quit":
            break
        if decision == "skip" or decision == "":
            print("  Skipped.\n")
            continue

        reasoning = input("  Jon's reasoning (one sentence): ").strip()
        outcome = input("  Outcome (if known: leave blank for now): ").strip()

        match = "yes" if decision == row.get("agent_prediction", "").lower() else "no"

        row["jon_decision"] = decision
        row["jon_reasoning"] = reasoning
        row["match"] = match
        row["outcome"] = outcome

        updated += 1
        print(f"  Logged. Match: {match}\n")

    # Write updated rows back to CSV
    if updated > 0:
        fieldnames = list(rows[0].keys())
        tmp = LOG_FILE + ".tmp"
        with open(tmp, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        shutil.move(tmp, LOG_FILE)
        print(f"=== Session complete. {updated} decision(s) updated. ===")
    else:
        print("=== No changes made. ===")

    # Summary
    with open(LOG_FILE, newline="") as f:
        all_rows = list(csv.DictReader(f))

    reviewed = [r for r in all_rows if r.get("jon_decision")]
    if reviewed:
        matches = sum(1 for r in reviewed if r.get("match") == "yes")
        match_rate = round(matches / len(reviewed) * 100)
        print(f"\nCurrent match rate: {matches}/{len(reviewed)} ({match_rate}%)")
        if match_rate >= 80:
            print("Match rate is at or above 80%: ready to consider Phase 3 (blind test).")
        else:
            print(f"Need more decisions before Phase 3. Keep logging.")

if __name__ == "__main__":
    run_calibration()
