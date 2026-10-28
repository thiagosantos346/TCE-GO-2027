# -*- coding: utf-8 -*-
with open("build_all_guides.py", "r", encoding="utf-8") as f:
    text = f.read()

target = '    for h, slug, htext, _ in headings_info:\n        if h.name in ("h2", "h3", "h4"):'
replacement = '    for h, slug, htext, _ in headings_info:\n        if h.name in ("h2", "h3", "h4"):\n            if not htext or re.match(r"^[\\s\\-_=]+$", htext):\n                continue'

if target in text:
    text = text.replace(target, replacement, 1)
    with open("build_all_guides.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("SUCCESS: updated headings_info loop in build_all_guides.py!")
else:
    print("Target not found")

