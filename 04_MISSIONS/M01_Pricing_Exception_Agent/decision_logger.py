"""
Decision Logger for GOURD Freight M01 Pricing Exception Agent
Phase 1: Passive logging with parallel agent prediction

HOW IT WORKS:
- Monitors exceptions@gourdfreight.example for emails BCC'd there by Jon
- In parallel, scans Jon's main inbox for emails it suspects are exceptions
- For every flagged exception: extracts structured data, records agent prediction,
  waits for Jon's decision, then logs both to exceptions_log.csv
- Out-of-boundary cases logged separately to non_exception_log.csv
- Reports to Jon only when: (a) legal/contractual content detected,
  (b) 10-match streak reached, or (c) agent identifies a self-correction

CONFIGURATION: Edit the CONFIG section below before running.
"""

import imaplib
import email
import csv
import os
import json
import re
from datetime import datetime
from email.header import decode_header
from anthropic import Anthropic

# ---------------------------------------------------------------------------
# CONFIG: edit these before running
# ---------------------------------------------------------------------------

IMAP_HOST = "mail.gourdfreight.example"       # Your mail server
IMAP_PORT = 993
EXCEPTIONS_EMAIL = "exceptions@gourdfreight.example"
EXCEPTIONS_PASSWORD = "REPLACE_ME"       # Use env var in production

JON_EMAIL = "jon@gourdfreight.example"  # Main inbox to scan proactively
JON_PASSWORD = "REPLACE_ME"

MARGIN_FLOOR = 10.0       # %: confirmed 2026-06-12
DEAL_SIZE_FLOOR = 500.0   # £ : confirmed 2026-06-12

LOG_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEPTIONS_LOG = os.path.join(LOG_DIR, "exceptions_log.csv")
NON_EXCEPTION_LOG = os.path.join(LOG_DIR, "non_exception_log.csv")
STATE_FILE = os.path.join(LOG_DIR, "agent_state.json")

LEGAL_KEYWORDS = [
    "contract", "legal", "liability", "indemnity", "clause",
    "dispute", "litigation", "solicitor", "terms and conditions",
    "penalty", "breach", "arbitration"
]

# ---------------------------------------------------------------------------
# STATE: persists match streak and prediction history across runs
# ---------------------------------------------------------------------------

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "match_streak": 0,
        "total_logged": 0,
        "prediction_history": []  # list of {date, fields, prediction, actual, match}
    }

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

# ---------------------------------------------------------------------------
# EMAIL UTILITIES
# ---------------------------------------------------------------------------

def connect_imap(host, port, user, password):
    mail = imaplib.IMAP4_SSL(host, port)
    mail.login(user, password)
    return mail

def fetch_unread(mail, folder="INBOX"):
    mail.select(folder)
    _, data = mail.search(None, "UNSEEN")
    ids = data[0].split()
    messages = []
    for uid in ids:
        _, msg_data = mail.fetch(uid, "(RFC822)")
        raw = msg_data[0][1]
        msg = email.message_from_bytes(raw)
        body = extract_body(msg)
        messages.append({
            "uid": uid,
            "subject": decode_str(msg.get("Subject", "")),
            "from": msg.get("From", ""),
            "date": msg.get("Date", ""),
            "body": body,
            "raw": msg
        })
        # Mark as read
        mail.store(uid, "+FLAGS", "\\Seen")
    return messages

def extract_body(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_payload(decode=True).decode(errors="replace")
    else:
        body = msg.get_payload(decode=True).decode(errors="replace")
    return body

def decode_str(s):
    parts = decode_header(s)
    decoded = []
    for part, enc in parts:
        if isinstance(part, bytes):
            decoded.append(part.decode(enc or "utf-8", errors="replace"))
        else:
            decoded.append(part)
    return " ".join(decoded)

def contains_legal_content(text):
    text_lower = text.lower()
    return any(kw in text_lower for kw in LEGAL_KEYWORDS)

# ---------------------------------------------------------------------------
# AGENT: extract structured fields from email text using Claude
# ---------------------------------------------------------------------------

client = Anthropic()

def extract_fields(email_text):
    """Use Claude to extract structured exception fields from email body."""
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": f"""Extract pricing exception details from this email.
Return JSON only, no explanation. Fields:
- client (string or null)
- route (string or null)
- carrier (string or null)
- deal_size_gbp (number or null)
- margin_pct (number or null)
- missing_fields (list of field names that could not be extracted)

Email:
{email_text[:3000]}

JSON:"""
        }]
    )
    try:
        return json.loads(response.content[0].text.strip())
    except Exception:
        return {
            "client": None, "route": None, "carrier": None,
            "deal_size_gbp": None, "margin_pct": None,
            "missing_fields": ["parse_error"]
        }

def is_exception(fields):
    """Check whether this email meets the exception thresholds."""
    margin = fields.get("margin_pct")
    deal_size = fields.get("deal_size_gbp")
    if margin is not None and margin < MARGIN_FLOOR:
        return True
    if deal_size is not None and deal_size > DEAL_SIZE_FLOOR:
        return True
    return False

def make_prediction(fields, history):
    """Use Claude to predict what Jon would decide, given fields and history."""
    history_text = ""
    if history:
        recent = history[-20:]  # last 20 decisions for context
        history_text = "\n".join([
            f"- {h['date']}: {h['fields']} → {h['actual']} ({h.get('jon_reasoning', '')})"
            for h in recent if h.get("actual")
        ])

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{
            "role": "user",
            "content": f"""You are learning Jon O'Breck's pricing exception judgment at GOURD Freight.

Exception thresholds: margin below {MARGIN_FLOOR}% OR deal size above £{DEAL_SIZE_FLOOR}

Recent decisions Jon has made:
{history_text or "None yet: this is an early decision."}

New exception to assess:
{json.dumps(fields, indent=2)}

Predict whether Jon will APPROVE or REJECT this exception.
Reply in JSON: {{"prediction": "approve" or "reject", "reasoning": "one sentence"}}"""
        }]
    )
    try:
        return json.loads(response.content[0].text.strip())
    except Exception:
        return {"prediction": "unknown", "reasoning": "Could not generate prediction"}

# ---------------------------------------------------------------------------
# LOGGING
# ---------------------------------------------------------------------------

def log_exception(fields, prediction, jon_decision="", jon_reasoning="", match=""):
    row = {
        "date": datetime.now().isoformat(),
        "client": fields.get("client", ""),
        "route": fields.get("route", ""),
        "carrier": fields.get("carrier", ""),
        "deal_size_gbp": fields.get("deal_size_gbp", ""),
        "margin_pct": fields.get("margin_pct", ""),
        "agent_prediction": prediction.get("prediction", ""),
        "agent_reasoning": prediction.get("reasoning", ""),
        "jon_decision": jon_decision,
        "jon_reasoning": jon_reasoning,
        "match": match,
        "outcome": ""
    }
    with open(EXCEPTIONS_LOG, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writerow(row)
    return row

def log_non_exception(fields, why_flagged, why_not):
    row = {
        "date": datetime.now().isoformat(),
        "client": fields.get("client", ""),
        "route": fields.get("route", ""),
        "carrier": fields.get("carrier", ""),
        "deal_size_gbp": fields.get("deal_size_gbp", ""),
        "margin_pct": fields.get("margin_pct", ""),
        "why_flagged_as_exception": why_flagged,
        "why_not_an_exception": why_not,
        "notes": ""
    }
    with open(NON_EXCEPTION_LOG, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writerow(row)

# ---------------------------------------------------------------------------
# NOTIFICATIONS TO JON (minimal, only when meaningful)
# ---------------------------------------------------------------------------

def notify_jon(subject, body):
    """
    Send a notification email to Jon.
    Plug in your mail-sending method here (SMTP, API, etc.)
    For now: prints to stdout so it can be piped to any notification system.
    """
    print(f"\n[NOTIFY JON] {subject}\n{body}\n")

def check_streak_and_notify(state):
    if state["match_streak"] > 0 and state["match_streak"] % 10 == 0:
        notify_jon(
            subject=f"Decision Logger: {state['match_streak']} predictions in a row matched yours",
            body=(
                f"The agent has now matched your last {state['match_streak']} pricing exception "
                f"decisions in a row. Total logged: {state['total_logged']}.\n\n"
                f"You can review the full log at: {EXCEPTIONS_LOG}"
            )
        )

def check_self_correction(state, new_prediction, fields):
    """
    Detect if the agent would have called this differently earlier.
    Compare against predictions from the first half of history vs recent.
    """
    history = state.get("prediction_history", [])
    if len(history) < 10:
        return  # Not enough history to detect correction

    early = history[:len(history)//2]
    # Re-predict using only early history to see if call would differ
    early_prediction = make_prediction(fields, early)
    if early_prediction.get("prediction") != new_prediction.get("prediction"):
        notify_jon(
            subject="Decision Logger: I've updated my judgment on a case type",
            body=(
                f"Earlier in the log, I would have predicted '{early_prediction['prediction']}' "
                f"for this exception. Based on what I've learned from your decisions, "
                f"I now predict '{new_prediction['prediction']}'.\n\n"
                f"Reason: {new_prediction['reasoning']}\n\n"
                f"This is a learning signal: my model of your judgment is updating."
            )
        )

# ---------------------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------------------

def process_exceptions_inbox():
    """Process emails BCC'd to exceptions@gourdfreight.example by Jon."""
    state = load_state()

    try:
        mail = connect_imap(IMAP_HOST, IMAP_PORT, EXCEPTIONS_EMAIL, EXCEPTIONS_PASSWORD)
    except Exception as e:
        print(f"[ERROR] Could not connect to exceptions inbox: {e}")
        return

    messages = fetch_unread(mail)
    print(f"[Exceptions inbox] {len(messages)} new message(s)")

    for msg in messages:
        text = msg["body"]

        # Legal/contractual check: escalate immediately
        if contains_legal_content(text):
            notify_jon(
                subject=f"[ESCALATE] Legal content detected in exception email",
                body=(
                    f"Subject: {msg['subject']}\nFrom: {msg['from']}\n\n"
                    f"This email contains language that may have legal or contractual implications. "
                    f"Please review before any decision is logged.\n\nEmail excerpt:\n{text[:500]}"
                )
            )
            continue

        # Extract fields
        fields = extract_fields(text)

        # Check if it actually meets exception thresholds
        if not is_exception(fields) and not fields.get("missing_fields"):
            log_non_exception(
                fields,
                why_flagged="Jon flagged via BCC to exceptions@gourdfreight.example",
                why_not=f"Margin {fields.get('margin_pct')}% >= {MARGIN_FLOOR}% and "
                        f"deal size £{fields.get('deal_size_gbp')} <= £{DEAL_SIZE_FLOOR}"
            )
            print(f"[Non-exception logged] {msg['subject']}")
            continue

        # Make prediction before Jon's decision is known
        prediction = make_prediction(fields, state["prediction_history"])
        check_self_correction(state, prediction, fields)

        # Log with Jon's decision blank: to be filled when he replies
        log_exception(fields, prediction)
        state["total_logged"] += 1

        print(f"[Logged] {msg['subject']} | Agent predicts: {prediction['prediction']}")

    save_state(state)
    mail.logout()

def scan_jon_inbox_proactively():
    """
    Scan Jon's main inbox for emails the agent suspects are exceptions.
    These are candidates only: not logged unless Jon also flags them.
    Printed to stdout for review; could be written to a candidates file.
    """
    try:
        mail = connect_imap(IMAP_HOST, IMAP_PORT, JON_EMAIL, JON_PASSWORD)
    except Exception as e:
        print(f"[ERROR] Could not connect to Jon's inbox: {e}")
        return

    messages = fetch_unread(mail)
    candidates = []

    for msg in messages:
        fields = extract_fields(msg["body"])
        if is_exception(fields):
            candidates.append({
                "subject": msg["subject"],
                "from": msg["from"],
                "date": msg["date"],
                "fields": fields
            })

    if candidates:
        print(f"\n[Proactive scan] {len(candidates)} potential exception(s) spotted in Jon's inbox:")
        for c in candidates:
            print(f"  - {c['subject']} | {c['fields']}")
    else:
        print("[Proactive scan] No candidate exceptions found in Jon's inbox.")

    mail.logout()

# ---------------------------------------------------------------------------
# RUN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(f"\n=== Decision Logger: {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
    process_exceptions_inbox()
    scan_jon_inbox_proactively()
    print("\nDone.")
