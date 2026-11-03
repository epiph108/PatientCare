"""
Run this from the PatientCare project folder (the one with manage.py):
    python add_logo.py
It adds the favicon and a small logo in the navbar of every template.
Safe to run twice.
"""
import re
from pathlib import Path

TEMPLATES = Path("myapp/templates")
STATIC = Path("myapp/static")

if not TEMPLATES.exists():
    raise SystemExit("Run this from the folder that contains manage.py")
if not (STATIC / "logo-icon.png").exists():
    raise SystemExit("First copy the 4 image files into myapp/static/")

FAVICON = (
    '\n    <link rel="icon" type="image/x-icon" href="{% static \'favicon.ico\' %}">'
    '\n    <link rel="apple-touch-icon" href="{% static \'apple-touch-icon.png\' %}">'
)
OLD_BRAND = '<div class="brand">PatientCare</div>'
NEW_BRAND = (
    '<div class="brand"><img src="{% static \'logo-icon.png\' %}" alt="PatientCare logo" '
    'style="height:34px;width:34px;border-radius:8px;background:#fff;'
    'vertical-align:middle;margin-right:10px;">PatientCare</div>'
)

changed = 0
for f in sorted(TEMPLATES.glob("*.html")):
    text = f.read_text(encoding="utf-8")
    original = text

    if "{% load static %}" not in text:
        text = "{% load static %}\n" + text
    if "favicon.ico" not in text:
        text = re.sub(r"(<head[^>]*>)", lambda m: m.group(1) + FAVICON, text, count=1, flags=re.I)
    text = text.replace(OLD_BRAND, NEW_BRAND)

    if text != original:
        f.write_text(text, encoding="utf-8")
        changed += 1
        print("updated:", f.name)

print(f"Done. {changed} file(s) updated.")
