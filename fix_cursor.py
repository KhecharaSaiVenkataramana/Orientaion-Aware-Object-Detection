import re

# Fix 1 — cursor dot: remove transition so it follows mouse instantly
layout = open("templates/layout.html", encoding="utf-8").read()
old = '''.cursor-dot {
    position: fixed;
    width: 6px; height: 6px;
    background: var(--cyan);
    border-radius: 50%;
    pointer-events: none;
    z-index: 99999;
    transform: translate(-50%,-50%);
    transition: opacity 0.3s;
    opacity: 0;
    box-shadow: 0 0 8px var(--cyan);
}'''
new = '''.cursor-dot {
    position: fixed;
    width: 8px; height: 8px;
    background: var(--cyan);
    border-radius: 50%;
    pointer-events: none;
    z-index: 99999;
    transform: translate(-50%,-50%);
    opacity: 0;
    box-shadow: 0 0 10px var(--cyan), 0 0 20px rgba(0,207,255,0.4);
    transition: opacity 0.2s;
}'''
if old in layout:
    layout = layout.replace(old, new)
    print("Cursor CSS fixed")
else:
    print("Cursor CSS not found in layout — checking style.css")

# Also fix the JS to use left/top directly without transform
old_js = '''    document.addEventListener('mousemove', function(e) {
        mx = e.clientX; my = e.clientY;
        dot.style.opacity = '1';
        dot.style.left = mx + 'px';
        dot.style.top  = my + 'px';
    });'''
new_js = '''    document.addEventListener('mousemove', function(e) {
        dot.style.opacity = '1';
        dot.style.left = e.clientX + 'px';
        dot.style.top  = e.clientY + 'px';
    });'''
if old_js in layout:
    layout = layout.replace(old_js, new_js)
    print("Cursor JS fixed")
else:
    print("Cursor JS already clean")

with open("templates/layout.html", "w", encoding="utf-8") as f:
    f.write(layout)

# Fix 2 — hero stats: rewrite home.html stats block directly
home = open("templates/home.html", encoding="utf-8").read()

# Add stats right before closing </div> of hero section
# Find the hero-buttons div and add stats after it
if 'hero-stats' not in home:
    old_hero_end = '''        <div class="hero-buttons">
            <a href="/detection" class="btn-primary">Run Detection</a>
            <a href="/datasets" class="btn-secondary">Explore Datasets</a>
        </div>
    </div>
</div>'''
    new_hero_end = '''        <div class="hero-buttons">
            <a href="/detection" class="btn-primary">Run Detection</a>
            <a href="/datasets" class="btn-secondary">Explore Datasets</a>
        </div>
    </div>

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
</div>'''

    if old_hero_end in home:
        home = home.replace(old_hero_end, new_hero_end)
        print("Hero stats added!")
    else:
        print("Hero end block not matched — printing last 20 lines of home.html:")
        lines = home.split('\n')
        for i, line in enumerate(lines[-20:], len(lines)-20):
            print(f"{i+1}: {repr(line)}")
else:
    print("Hero stats already present")

# Add reveal class to feature cards
home = home.replace(
    '    <div class="feature-card">',
    '    <div class="feature-card reveal">'
)

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home)
print("home.html saved!")