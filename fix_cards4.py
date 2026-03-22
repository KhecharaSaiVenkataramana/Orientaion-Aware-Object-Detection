css = open("static/style.css", encoding="utf-8").read()

card_css = """
.step-card {
    background: #0d0b22;
}
body.light-mode .step-card {
    background: #ffffff !important;
    color: #111;
}
body.light-mode .step-card p,
body.light-mode .step-card h3 {
    color: #333 !important;
}
"""

if '.step-card' not in css:
    css = css + card_css
    with open("static/style.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Done!")
else:
    print("Already exists")