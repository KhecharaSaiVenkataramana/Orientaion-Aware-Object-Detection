import os
BASE = r"C:\Users\khech\OAOD Project\website"

home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

# Replace generic emoji icons with styled SVG icons + better cards
old_features = '''<section class="features">
    <div class="feature-card reveal">
        <div class="feature-icon">&#9654;</div>
        <h3>Object Detection</h3>
        <p>Run oriented bounding box detection on aerial and satellite imagery.</p>
        <a href="/detection" class="feature-link">Open Tool &rarr;</a>
    </div>
    <div class="feature-card reveal">
        <div class="feature-icon">&#128190;</div>
        <h3>Datasets</h3>
        <p>Explore DOTA, HRSC, and FAIR1M training datasets used in RAVEN.</p>
        <a href="/datasets" class="feature-link">Explore &rarr;</a>
    </div>
    <div class="feature-card reveal">
        <div class="feature-icon">&#128202;</div>
        <h3>Detection History</h3>
        <p>View your past detections, download results, and track performance.</p>
        <a href="/history" class="feature-link">View History &rarr;</a>
    </div>
    <div class="feature-card reveal">
        <div class="feature-icon">&#9881;</div>
        <h3>About RAVEN</h3>
        <p>Learn about the architecture, models, and research behind this system.</p>
        <a href="/about" class="feature-link">View &rarr;</a>
    </div>
</section>'''

new_features = '''<section class="features">

    <div class="feature-card reveal reveal-delay-1">
        <div class="feature-icon-wrap">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
                <rect x="4" y="4" width="12" height="12" rx="2"
                      stroke="#00cfff" stroke-width="1.5" fill="none" transform="rotate(-15 10 10)"/>
                <rect x="20" y="6" width="10" height="10" rx="1.5"
                      stroke="#6644ff" stroke-width="1.5" fill="none" transform="rotate(10 25 11)"/>
                <rect x="8" y="20" width="14" height="10" rx="2"
                      stroke="#00cfff" stroke-width="1.5" fill="none" transform="rotate(-8 15 25)"/>
                <circle cx="28" cy="26" r="5" stroke="#6644ff" stroke-width="1.5" fill="none"/>
                <line x1="25" y1="31" x2="32" y2="31" stroke="#6644ff" stroke-width="1" opacity="0.4"/>
                <line x1="28" y1="28" x2="28" y2="35" stroke="#6644ff" stroke-width="1" opacity="0.4"/>
            </svg>
        </div>
        <h3>Object Detection</h3>
        <p>Run oriented bounding box detection on aerial and satellite imagery with 4 model modes.</p>
        <a href="/detection" class="feature-link">Open Tool &rarr;</a>
    </div>

    <div class="feature-card reveal reveal-delay-2">
        <div class="feature-icon-wrap">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
                <rect x="3" y="8" width="30" height="22" rx="3" stroke="#6644ff" stroke-width="1.5" fill="none"/>
                <rect x="3" y="8" width="30" height="7" rx="3" fill="rgba(102,68,255,0.15)"/>
                <line x1="3" y1="15" x2="33" y2="15" stroke="#6644ff" stroke-width="1" opacity="0.5"/>
                <line x1="10" y1="15" x2="10" y2="30" stroke="#6644ff" stroke-width="1" opacity="0.3"/>
                <line x1="18" y1="15" x2="18" y2="30" stroke="#6644ff" stroke-width="1" opacity="0.3"/>
                <line x1="26" y1="15" x2="26" y2="30" stroke="#6644ff" stroke-width="1" opacity="0.3"/>
                <rect x="6" y="10" width="8" height="3" rx="1" fill="#6644ff" opacity="0.6"/>
                <rect x="12" y="18" width="4" height="8" rx="1" fill="#00cfff" opacity="0.7"/>
                <rect x="20" y="21" width="4" height="5" rx="1" fill="#6644ff" opacity="0.7"/>
                <rect x="28" y="19" width="3" height="7" rx="1" fill="#00cfff" opacity="0.7"/>
                <circle cx="29" cy="7" r="3" fill="#00cfff" opacity="0.8"/>
            </svg>
        </div>
        <h3>Datasets</h3>
        <p>Explore DOTA, HRSC, and FAIR1M datasets — the backbone of RAVEN's training pipeline.</p>
        <a href="/datasets" class="feature-link">Explore &rarr;</a>
    </div>

    <div class="feature-card reveal reveal-delay-3">
        <div class="feature-icon-wrap">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
                <circle cx="18" cy="18" r="14" stroke="#6644ff" stroke-width="1.5" fill="none" stroke-dasharray="4 3"/>
                <circle cx="18" cy="18" r="8" stroke="#00cfff" stroke-width="1.5" fill="none"/>
                <circle cx="18" cy="18" r="3" fill="#00cfff"/>
                <line x1="18" y1="4" x2="18" y2="10" stroke="#6644ff" stroke-width="1.5"/>
                <line x1="18" y1="26" x2="18" y2="32" stroke="#6644ff" stroke-width="1.5"/>
                <line x1="4" y1="18" x2="10" y2="18" stroke="#6644ff" stroke-width="1.5"/>
                <line x1="26" y1="18" x2="32" y2="18" stroke="#6644ff" stroke-width="1.5"/>
                <rect x="24" y="24" width="9" height="9" rx="2" fill="#03020c" stroke="#00cfff" stroke-width="1.2"/>
                <polyline points="26,28.5 27.5,30 30,27" stroke="#00cfff" stroke-width="1.2" fill="none" stroke-linecap="round"/>
            </svg>
        </div>
        <h3>Detection History</h3>
        <p>Browse past detections, compare model performance, and download annotated results.</p>
        <a href="/history" class="feature-link">View History &rarr;</a>
    </div>

    <div class="feature-card reveal reveal-delay-4">
        <div class="feature-icon-wrap">
            <svg width="36" height="36" viewBox="0 0 36 36" fill="none">
                <path d="M18 3 L21 12 L30 12 L23 18 L26 27 L18 21 L10 27 L13 18 L6 12 L15 12 Z"
                      stroke="#6644ff" stroke-width="1.5" fill="rgba(102,68,255,0.12)" stroke-linejoin="round"/>
                <circle cx="18" cy="15" r="3" fill="#00cfff" opacity="0.9"/>
                <line x1="18" y1="27" x2="18" y2="33" stroke="#6644ff" stroke-width="1.5"/>
                <line x1="14" y1="31" x2="22" y2="31" stroke="#6644ff" stroke-width="1.5"/>
            </svg>
        </div>
        <h3>About RAVEN</h3>
        <p>The architecture, training pipeline, team, and research behind RAVEN's detection system.</p>
        <a href="/about" class="feature-link">View &rarr;</a>
    </div>

</section>'''

if old_features in home:
    home = home.replace(old_features, new_features)
    print("Feature cards updated with SVG icons!")
else:
    # Try without reveal classes
    print("Exact match failed — trying partial replacement")
    import re
    home = re.sub(
        r'<section class="features">.*?</section>',
        new_features,
        home,
        flags=re.DOTALL
    )
    print("Replaced via regex")

# Fix hero stats — move them BELOW hero, not inside it
if 'hero-stats' in home:
    # Remove from inside hero and add as separate section
    home = re.sub(
        r'\s*<div class="hero-stats">.*?</div>\s*',
        '\n',
        home,
        flags=re.DOTALL
    )
    print("Removed old hero-stats from hero")

# Add stats as a proper bar between hero and features
home = home.replace(
    '\n<section class="features">',
    '''
<!-- STATS BAR -->
<div style="background:var(--bg-dark);border-top:1px solid rgba(102,68,255,0.15);
            border-bottom:1px solid rgba(102,68,255,0.15);padding:28px 120px;">
    <div style="display:flex;gap:0;justify-content:space-around;align-items:center;">
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#00cfff;
                        font-family:\'Courier New\',monospace;">0.983</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;
                        text-transform:uppercase;margin-top:4px;">HRSC mAP50</div>
        </div>
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#00cfff;
                        font-family:\'Courier New\',monospace;">0.657</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;
                        text-transform:uppercase;margin-top:4px;">DOTA mAP50</div>
        </div>
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#6644ff;
                        font-family:\'Courier New\',monospace;">4</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;
                        text-transform:uppercase;margin-top:4px;">Detection Modes</div>
        </div>
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#00cfff;
                        font-family:\'Courier New\',monospace;">15</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;
                        text-transform:uppercase;margin-top:4px;">DOTA Classes</div>
        </div>
        <div style="text-align:center;padding:0 40px;">
            <div style="font-size:36px;font-weight:700;color:#6644ff;
                        font-family:\'Courier New\',monospace;">48h</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;
                        text-transform:uppercase;margin-top:4px;">Auto Cleanup</div>
        </div>
    </div>
</div>

<section class="features">'''
)

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)
print("home.html saved!")

# Add feature-icon-wrap CSS to style.css
css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()
if "feature-icon-wrap" not in css:
    css += '''
/* Feature icon wrap */
.feature-icon-wrap {
    width: 64px; height: 64px;
    border-radius: 16px;
    background: rgba(102,68,255,0.1);
    border: 1px solid rgba(102,68,255,0.25);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 20px;
    transition: background 0.3s, border-color 0.3s, transform 0.3s;
}
.feature-card:hover .feature-icon-wrap {
    background: rgba(102,68,255,0.2);
    border-color: var(--purple);
    transform: scale(1.1) rotate(-3deg);
}
'''
    with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    print("CSS updated with feature-icon-wrap!")
else:
    print("CSS already has feature-icon-wrap")