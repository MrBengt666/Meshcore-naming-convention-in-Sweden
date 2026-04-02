import re, base64, datetime
from weasyprint import HTML, CSS

# ── CONFIG ────────────────────────────────────────────────────────────────────
INPUT_MD   = "appendix_-_kommuner_med_flygplatser_och_förkortningar_2026-04-02.md"
OUTPUT_PDF = f"output/appendix_filtered_{datetime.date.today()}.pdf"

# Columns to keep (exact header names as they appear in the MD table)
KEEP = ['Storleks- ordning', 'Kommun', 'Kommun- förkortning',
        'Centralort', 'IATA', 'ICAO', 'Folkmängd']

# ── READ & PARSE ──────────────────────────────────────────────────────────────
with open(INPUT_MD, encoding='utf-8') as f:
    lines = f.readlines()

# Split into intro (before table) and table lines
intro, table_lines = [], []
in_table = False
for line in lines:
    if line.startswith('|') and not in_table:
        in_table = True
    if in_table:
        table_lines.append(line.rstrip())
    else:
        intro.append(line.rstrip())

# Parse header and find indices to keep
headers = [h.strip() for h in table_lines[0].split('|')[1:-1]]
keep_idx = [i for i, h in enumerate(headers) if h in KEEP]
kept_headers = [headers[i] for i in keep_idx]

# ── BUILD FILTERED HTML TABLE ─────────────────────────────────────────────────
rows_html = []
for line in table_lines[2:]:   # skip header and separator rows
    cells = [c.strip() for c in line.split('|')[1:-1]]
    kept = [cells[i] if i < len(cells) else '' for i in keep_idx]
    rows_html.append('<tr>' + ''.join(f'<td>{c}</td>' for c in kept) + '</tr>')

thead = '<tr>' + ''.join(f'<th>{h}</th>' for h in kept_headers) + '</tr>'

# ── BUILD FULL HTML ───────────────────────────────────────────────────────────
intro_html = '<br>'.join(intro)
date_str   = datetime.date.today().isoformat()

html = f"""<!DOCTYPE html>
<html lang="sv"><head><meta charset="UTF-8">
<style>
  @page {{ size: A4 landscape; margin: 10mm; }}
  body   {{ font-family: DejaVu Sans, sans-serif; font-size: 7px; }}
  h1     {{ font-size: 11px; border-bottom: 2px solid #2a6db5; padding-bottom: 3px; }}
  p      {{ margin: 2px 0; font-size: 7px; }}
  table  {{ width: 100%; border-collapse: collapse; margin-top: 6px; }}
  th     {{ background: #1a2a3a; color: white; padding: 2px 4px; text-align: left; font-size: 7px; }}
  td     {{ border: 0.3px solid #ccc; padding: 1px 4px; font-size: 7px; }}
  tr:nth-child(even) td {{ background: #f8f8f8; }}
  .date  {{ font-size: 6px; color: #999; margin-top: 4px; }}
</style>
</head><body>
{intro_html}
<table>
  <thead>{thead}</thead>
  <tbody>{''.join(rows_html)}</tbody>
</table>
<p class="date">Genererat: {date_str}</p>
</body></html>"""

# ── RENDER PDF ────────────────────────────────────────────────────────────────
import os
os.makedirs('output', exist_ok=True)
HTML(string=html).write_pdf(OUTPUT_PDF)
print(f"Done → {OUTPUT_PDF}")
