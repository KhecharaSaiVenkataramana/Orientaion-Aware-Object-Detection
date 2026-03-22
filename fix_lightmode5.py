import os, re
BASE = r"C:\Users\khech\OAOD Project\website"

home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

# Find all onmouseover/onmouseout on step cards and print them
print("=== Current hover handlers ===")
matches = re.findall(r'onmouse(?:over|out)="[^"]*"', home)
for i, m in enumerate(matches[:12]):
    print(f"{i}: {m[:120]}")