import re, os
BASE = r"C:\Users\khech\OAOD Project\website"

css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

# Fix hero stats position — bottom right, doesn't overlap text
old = re.search(r'\.hero-stats \{[^}]+\}', css)
if old:
    print("Found:", old.group()[:80])
    css = css.replace(old.group(), '''.hero-stats {
    position: absolute;
    bottom: 32px;
    right: 80px;
    display: flex;
    gap: 14px;
    z-index: 2;
    animation: pageFadeIn 0.8s ease 0.6s both;
}''')
    print("Hero stats position fixed")
else:
    print("Not found — appending override")
    css += '''
.hero-stats {
    position: absolute;
    bottom: 32px;
    right: 80px;
    display: flex;
    gap: 14px;
    z-index: 2;
}
'''

# Make hero tall enough so stats don't overlap text
css = re.sub(r'\.hero \{\s*height: \d+px;', '.hero {\n    height: 720px;', css)

# Stat card style
old_stat = re.search(r'\.hero-stat \{[^}]+\}', css)
if old_stat:
    css = css.replace(old_stat.group(), '''.hero-stat {
    text-align: center;
    background: rgba(10,8,32,0.85);
    border: 1px solid rgba(102,68,255,0.35);
    padding: 14px 22px;
    border-radius: 12px;
    backdrop-filter: blur(16px);
    transition: transform 0.3s, border-color 0.3s;
    min-width: 110px;
}''')
    print("Stat card style updated")

with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("CSS saved!")

# Also make sure hero-stats is INSIDE the .hero div in home.html
home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

# Remove stats if they're outside hero
if 'hero-stats' in home:
    # Check if stats are inside <div class="hero"> 
    hero_match = re.search(r'<div class="hero">(.*?)</div>\s*\n\s*<!--\s*STATS', home, re.DOTALL)
    if hero_match:
        print("Stats already inside hero — OK")
    else:
        print("Stats position in HTML:")
        idx = home.find('hero-stats')
        print(repr(home[max(0,idx-200):idx+50]))
else:
    print("No hero-stats in home.html — checking why")
    
print("\nDone! Run: python app.py")