import os
BASE = r"C:\Users\khech\OAOD Project\website"

home = '''{% extends "layout.html" %}
{% block content %}

<div class="hero">
    <div class="hero-text">
        <div class="hero-badge">RAVEN &mdash; AERIAL OBJECT DETECTION</div>
        <h1>Detection that<br>never blinks.</h1>
        <p>
            RAVEN &mdash; Rotated-Annotation Vehicle &amp; Entity Network.<br>
            Detect oriented objects in aerial imagery with unmatched accuracy<br>
            using YOLOv8 OBB models trained on DOTA and HRSC datasets.
        </p>
        <div class="hero-buttons">
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
</div>

<!-- STATS BAR -->
<div style="background:var(--bg-dark);border-top:1px solid rgba(102,68,255,0.15);
            border-bottom:1px solid rgba(102,68,255,0.15);padding:28px 120px;">
    <div style="display:flex;justify-content:space-around;align-items:center;">
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">72,453</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Vehicle Annotations</div>
        </div>
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">15</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">DOTA Classes</div>
        </div>
        <div style="text-align:center;padding:0 40px;border-right:1px solid rgba(102,68,255,0.2);">
            <div style="font-size:36px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">1,732</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">FAIR1M Images</div>
        </div>
        <div style="text-align:center;padding:0 40px;">
            <div style="font-size:36px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">OBB</div>
            <div style="font-size:12px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Oriented Bounding Box</div>
        </div>
    </div>
</div>

<section class="features">

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
                <rect x="12" y="18" width="4" height="8" rx="1" fill="#00cfff" opacity="0.7"/>
                <rect x="20" y="21" width="4" height="5" rx="1" fill="#6644ff" opacity="0.7"/>
                <rect x="28" y="19" width="3" height="7" rx="1" fill="#00cfff" opacity="0.7"/>
            </svg>
        </div>
        <h3>Datasets</h3>
        <p>Explore DOTA, HRSC, and FAIR1M datasets &mdash; the backbone of RAVEN's training pipeline.</p>
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
            </svg>
        </div>
        <h3>About RAVEN</h3>
        <p>The architecture, training pipeline, team, and research behind RAVEN's detection system.</p>
        <a href="/about" class="feature-link">View &rarr;</a>
    </div>

</section>

{% endblock %}
'''

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)
print("home.html cleanly rewritten!")
print("hero-stats count:", home.count("hero-stats"))
print("Restart: python app.py")