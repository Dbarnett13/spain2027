"""Build plan/spain2027-deadlines.ics from plan/deadlines.md.

One all-day event per dated item, with reminders 7 days and 1 day before at 09:00.
Import once into Google Calendar (Settings, Import and export) or Apple Calendar.
"""
import re
from datetime import date, timedelta
from pathlib import Path
from uuid import uuid5, NAMESPACE_URL

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "plan" / "spain2027-deadlines.ics"


def md_table(path):
    rows = []
    for line in path.read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows[0], rows[1:]


def parse_due(text):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", text)
    if m:
        return date(*map(int, m.groups())), False
    m = re.match(r"(\d{4})-(\d{2})", text)
    if m:
        return date(int(m.group(1)), int(m.group(2)), 1), True
    return None, False


def esc(s):
    return s.replace("\\", "\\\\").replace(";", "\;").replace(",", "\\,").replace("\n", "\\n")


def main():
    _, rows = md_table(ROOT / "plan" / "deadlines.md")
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//spain2027//plan//EN",
             "X-WR-CALNAME:Spain 2027 deadlines", "CALSCALE:GREGORIAN"]
    n = 0
    for r in rows:
        due_text, item, workstream, typ, conf, source, status = r[:7]
        due, month_only = parse_due(due_text)
        if due is None or status.lower().startswith("past"):
            continue
        n += 1
        title = f"[{workstream}] {item}"
        if month_only:
            title += " (month only, day not set)"
        desc = f"Type: {typ}. Confidence: {conf}. Source: {source}. From plan/deadlines.md in the spain2027 repo."
        uid = uuid5(NAMESPACE_URL, f"spain2027/{due_text}/{item}")
        lines += ["BEGIN:VEVENT", f"UID:{uid}@spain2027",
                  f"DTSTAMP:{date.today().strftime('%Y%m%d')}T000000Z",
                  f"DTSTART;VALUE=DATE:{due.strftime('%Y%m%d')}",
                  f"DTEND;VALUE=DATE:{(due + timedelta(days=1)).strftime('%Y%m%d')}",
                  f"SUMMARY:{esc(title)}", f"DESCRIPTION:{esc(desc)}",
                  f"CATEGORIES:{esc(workstream)}",
                  "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:Due in 7 days", "TRIGGER:-P6DT15H", "END:VALARM",
                  "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:Due tomorrow", "TRIGGER:-PT15H", "END:VALARM",
                  "END:VEVENT"]
    lines.append("END:VCALENDAR")
    OUT.write_text("\r\n".join(lines) + "\r\n")
    print(OUT, n, "events")


if __name__ == "__main__":
    main()
