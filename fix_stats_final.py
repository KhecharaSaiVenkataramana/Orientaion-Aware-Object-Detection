import re, os
BASE = r"C:\Users\khech\OAOD Project\website"

# Fix CSS — force stats to absolute bottom-right corner
css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

# Remove ALL existing hero-stats rules and replace with one clean rule
css = re.sub(r'\.hero-stats \{[^}]+\}', '', css)
css = re.sub(r'/\* Hero stats fix \*/.*?\.hero-stats \{[^}]+\}', '', css, flags=re.DOTALL)

css += '''
/* Hero stats — fixed bottom right */
.hero-stats {
    position: absolute !important;
    bottom: 40px !important;
    right: 80px !important;
    left: auto !important;
    top: auto !important;
    display: flex !important;
    gap: 14px !important;
    z-index: 10 !important;
    animation: pageFadeIn 0.8s ease 0.6s both;
}
.hero-stat {
    text-align: center;
    background: rgba(10,8,32,0.88);
    border: 1px solid rgba(102,68,255,0.4);
    padding: 14px 24px;
    border-radius: 12px;
    backdrop-filter: blur(16px);
    min-width: 110px;
    transition: transform 0.3s, border-color 0.3s;
}
.hero-stat:hover {
    transform: translateY(-4px);
    border-color: var(--cyan);
}
.hero-stat-val {
    font-size: 26px;
    font-weight: 700;
    font-family: 'Courier New', monospace;
    color: var(--cyan);
    display: block;
}
.hero-stat-lbl {
    font-size: 11px;
    color: var(--text-muted);
    letter-spacing: 1.5px;
    margin-top: 5px;
    display: block;
    text-transform: uppercase;
}
'''

with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("CSS fixed!")

# Fix home.html — ensure all 3 stats are present and inside hero div
home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

# Remove any existing hero-stats block
home = re.sub(r'\s*<div class="hero-stats">.*?</div>\s*(?=</div>|<!--)', '', home, flags=re.DOTALL)

# Find the closing of the hero div and insert stats just before it
# Hero structure: <div class="hero">...<div class="hero-text">...</div></div>
old_hero_close = '''    </div>
</div>

<!-- STATS BAR -->'''

new_hero_close = '''    </div>

    <!-- Stats bottom right -->
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-val">0.983</span>
            <span class="hero-stat-lbl">HRSC mAP50</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-val">0.657</span>
            <span class="hero-stat-lbl">DOTA mAP50</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-val">4</span>
            <span class="hero-stat-lbl">Detection Modes</span>
        </div>
    </div>
</div>

<!-- STATS BAR -->'''

if old_hero_close in home:
    home = home.replace(old_hero_close, new_hero_close)
    print("Stats inserted correctly inside hero!")
else:
    print("Pattern not found — printing hero area:")
    idx = home.find('hero-buttons')
    print(repr(home[idx:idx+400]))

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)
print("home.html saved!")
print("Restart: python app.py")