# -*- coding: utf-8 -*-
with open("build_all_guides.py", "r", encoding="utf-8") as f:
    text = f.read()

# Replace:
#         if nxt and nxt.name in ("ul", "ol"):
#             nxt.name = "ul"
#             classes = nxt.get("class", [])
#             if "sumario-list" not in classes:
#                 classes.append("sumario-list")
#             nxt["class"] = classes
#             sumario_ul = nxt

old = '''        if nxt and nxt.name in ("ul", "ol"):
            nxt.name = "ul"
            classes = nxt.get("class", [])
            if "sumario-list" not in classes:
                classes.append("sumario-list")
            nxt["class"] = classes
            sumario_ul = nxt'''

new = '''        if nxt and nxt.name in ("ul", "ol"):
            classes = nxt.get("class", [])
            if "sumario-list" not in classes:
                classes.append("sumario-list")
            nxt["class"] = classes
            sumario_ul = nxt'''

if old in text:
    text = text.replace(old, new, 1)
    with open("build_all_guides.py", "w", encoding="utf-8") as f:
        f.write(text)
    print("SUCCESS: Preserved ol tag in build_all_guides.py!")
else:
    print("Old snippet not found!")

