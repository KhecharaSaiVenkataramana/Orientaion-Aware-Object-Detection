import re

css = open("static/style.css", encoding="utf-8").read()

light_mode_vars = """
body.light-mode {
    --bg-card: #ffffff;
    --bg-dark: #f0f0f8;
    --bg-deep: #e8e8f0;
    --bg-panel: #f5f5ff;
}
"""

if 'body.light-mode' not in css:
    css = css + light_mode_vars
    print("Light mode vars added!")
else:
    css = re.sub(
        r'body\.light-mode\s*\{[^}]*\}',
        light_mode_vars.strip(),
        css
    )
    print("Light mode vars updated!")

with open("static/style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Done!")