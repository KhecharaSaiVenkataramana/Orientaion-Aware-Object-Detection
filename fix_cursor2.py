layout = open("templates/layout.html", encoding="utf-8").read()
css = open("static/style.css", encoding="utf-8").read()

# Remove cursor dot HTML
layout = layout.replace('<div class="cursor-dot" id="cursor-dot"></div>', '')

# Remove cursor dot JS
start = layout.find("// ── CURSOR DOT")
end = layout.find("// ──", start + 5)
if start != -1 and end != -1:
    layout = layout[:start] + layout[end:]
    print("Cursor JS removed")

# Remove cursor dot CSS
start2 = css.find(".cursor-dot {")
end2 = css.find("}", start2) + 1
if start2 != -1:
    css = css[:start2] + css[end2:]
    print("Cursor CSS removed")

with open("templates/layout.html", "w", encoding="utf-8") as f:
    f.write(layout)
with open("static/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Done - cursor dot removed!")