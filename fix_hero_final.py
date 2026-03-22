import os, re
BASE = r"C:\Users\khech\OAOD Project\website"

home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

# Count how many hero-stats divs exist
count = home.count('<div class="hero-stats">')
print(f"Found {count} hero-stats divs")

# Remove ALL hero-stats divs
home = re.sub(r'\s*<div class="hero-stats">.*?</div>\s*', '\n', home, flags=re.DOTALL)
print(f"After removal: {home.count('hero-stats')} remaining")

# Now add exactly ONE — right before closing </div> of hero
# The hero div ends just before <!-- STATS BAR --> comment
old = '    </div>\n\n    <!--'
new = '''    </div>

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

    <!--'''

if old in home:
    home = home.replace(old, new, 1)  # replace only FIRST occurrence
    print("One stats block added!")
else:
    print("Pattern not found — showing hero close:")
    idx = home.find('hero-buttons')
    print(repr(home[idx:idx+300]))

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)

final_count = home.count('<div class="hero-stats">')
print(f"Final count of hero-stats: {final_count} (should be 1)")
print("Done! Restart: python app.py")