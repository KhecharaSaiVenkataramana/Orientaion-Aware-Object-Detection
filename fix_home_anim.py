content = open(r"C:\Users\khech\OAOD Project\website\templates\home.html", encoding="utf-8").read()

# Add hero stats + scroll reveal classes
old = '        <div class="hero-buttons">'
new = '''        <div class="hero-buttons">'''

# Add stats to hero and reveal to features
old2 = '</div>\n\n<section class="features">'
new2 = '''</div>

    <!-- Hero stats -->
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

<section class="features">'''

old3 = '    <div class="feature-card">'
new3 = '    <div class="feature-card reveal">'

if old2 in content:
    content = content.replace(old2, new2)
    print("Hero stats added")
else:
    print("Hero stats block not matched — skipping")

content = content.replace(old3, new3)
print("Scroll reveal added to feature cards")

with open(r"C:\Users\khech\OAOD Project\website\templates\home.html", "w", encoding="utf-8") as f:
    f.write(content)
print("home.html updated!")