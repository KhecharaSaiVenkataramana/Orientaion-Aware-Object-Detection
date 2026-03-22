import os

BASE = r"C:\Users\khech\OAOD Project\website"

# Fix home.html — update tagline and hero text
home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

old_h1 = '''        <h1>Predator Vision.<br>Machine Precision.<br>Never Blinks.</h1>'''
new_h1 = '''        <h1>Detection that<br>never blinks.</h1>'''

old_badge = '''        <div class="hero-badge">AERIAL OBJECT DETECTION</div>'''
new_badge = '''        <div class="hero-badge">RAVEN &mdash; AERIAL OBJECT DETECTION</div>'''

home = home.replace(old_h1, new_h1)
home = home.replace(old_badge, new_badge)

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)
print("home.html updated")

# Fix layout.html — bigger logo, better navbar branding
layout = open(os.path.join(BASE, "templates", "layout.html"), encoding="utf-8").read()

old_logo = '''        <a href="/">
            <img src="{{ url_for('static', filename='ui/logo.png') }}" style="height:70px;width:70px;border-radius:50%;object-fit:cover;border:2px solid #6644ff55;">
        </a>
        <span class="brand-name">RAVEN</span>'''

new_logo = '''        <a href="/" style="display:flex;align-items:center;gap:14px;text-decoration:none;">
            <img src="{{ url_for('static', filename='ui/logo.png') }}"
                 style="height:78px;width:78px;border-radius:50%;object-fit:cover;
                        border:2px solid #6644ff88;
                        box-shadow:0 0 18px rgba(102,68,255,0.5),0 0 6px rgba(0,207,255,0.3);">
            <div style="display:flex;flex-direction:column;line-height:1.1;">
                <span style="font-family:'Courier New',monospace;font-size:22px;font-weight:700;
                             letter-spacing:6px;color:#00cfff;">RAVEN</span>
                <span style="font-size:10px;color:#6644ffaa;letter-spacing:2.5px;
                             font-family:'Courier New',monospace;">DETECTION THAT NEVER BLINKS</span>
            </div>
        </a>'''

layout = layout.replace(old_logo, new_logo)

# Remove the separate brand-name span since it's now inside the anchor
old_brand = '''        <span class="brand-name">RAVEN</span>'''
if old_brand in layout:
    layout = layout.replace(old_brand, '')

with open(os.path.join(BASE, "templates", "layout.html"), "w", encoding="utf-8") as f:
    f.write(layout)
print("layout.html updated")

# Fix style.css — logo size adjustment
css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

old_logo_css = '''.logo { display:flex; align-items:center; gap:14px; }
.logo img { height:70px; width:70px; border-radius:50%; object-fit:cover; border:2px solid #6644ff55; }'''

new_logo_css = '''.logo { display:flex; align-items:center; gap:14px; }
.logo img { height:78px; width:78px; border-radius:50%; object-fit:cover; border:2px solid #6644ff88; }'''

css = css.replace(old_logo_css, new_logo_css)

with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("style.css updated")

print("\nAll done! Restart server with: python app.py")