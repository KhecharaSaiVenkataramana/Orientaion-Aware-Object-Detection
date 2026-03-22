import os

content = """\
{% extends "layout.html" %}
{% block content %}

<!-- HERO -->
<div class="hero">
    <div class="hero-text">
        <div class="hero-badge">RAVEN — AERIAL OBJECT DETECTION</div>
        <h1>Detection that<br>never blinks.</h1>
        <p>RAVEN — Rotated-Annotation Vehicle & Entity Network.<br>
        Detect oriented objects in aerial imagery with unmatched accuracy<br>
        using YOLOv8 OBB models trained on DOTA and HRSC datasets.</p>
        <div class="hero-buttons">
            <a href="/detection" class="btn-primary">Run Detection</a>
            <a href="/datasets" class="btn-secondary">Explore Datasets</a>
        </div>
    </div>

    <!-- Stats inside hero bottom right -->
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
<div style="background:#07051a; border-top:1px solid rgba(102,68,255,0.2);
            border-bottom:1px solid rgba(102,68,255,0.2);
            padding:28px 120px; display:flex; gap:60px; align-items:center;">
    <div style="flex:1; text-align:center;">
        <div style="font-size:32px; font-weight:700; color:#00cfff; font-family:'Courier New',monospace;">72,453</div>
        <div style="font-size:12px; color:#8877cc; letter-spacing:1px; margin-top:4px;">Vehicle Annotations</div>
    </div>
    <div style="width:1px; height:50px; background:rgba(102,68,255,0.3);"></div>
    <div style="flex:1; text-align:center;">
        <div style="font-size:32px; font-weight:700; color:#6644ff; font-family:'Courier New',monospace;">15</div>
        <div style="font-size:12px; color:#8877cc; letter-spacing:1px; margin-top:4px;">DOTA Classes</div>
    </div>
    <div style="width:1px; height:50px; background:rgba(102,68,255,0.3);"></div>
    <div style="flex:1; text-align:center;">
        <div style="font-size:32px; font-weight:700; color:#00cfff; font-family:'Courier New',monospace;">1,732</div>
        <div style="font-size:12px; color:#8877cc; letter-spacing:1px; margin-top:4px;">FAIR1M Images</div>
    </div>
    <div style="width:1px; height:50px; background:rgba(102,68,255,0.3);"></div>
    <div style="flex:1; text-align:center;">
        <div style="font-size:32px; font-weight:700; color:#6644ff; font-family:'Courier New',monospace;">OBB</div>
        <div style="font-size:12px; color:#8877cc; letter-spacing:1px; margin-top:4px;">Oriented Bounding Box</div>
    </div>
</div>

<!-- FEATURE CARDS -->
<section style="padding:80px 100px; background:var(--bg-deep);">
    <div style="text-align:center; margin-bottom:56px;">
        <div style="display:inline-block; background:rgba(102,68,255,0.1); border:1px solid rgba(102,68,255,0.3);
                    color:#6644ff; padding:5px 18px; border-radius:30px; font-size:11px;
                    font-weight:800; letter-spacing:3px; margin-bottom:18px; font-family:'Courier New',monospace;">
            CAPABILITIES
        </div>
        <h2 style="font-size:38px; margin:0 0 14px; background:linear-gradient(135deg,#fff,#00cfff);
                   -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
            What RAVEN can do
        </h2>
        <p style="color:#8877cc; font-size:16px; max-width:500px; margin:0 auto;">
            From single images to full folder batches — detect, classify, and export with precision.
        </p>
    </div>

    <div style="display:grid; grid-template-columns:repeat(4,1fr); gap:24px;">

        <div class="feature-card reveal" style="text-align:center;">
            <div style="font-size:40px; margin-bottom:18px; display:block;">🎯</div>
            <h3>Object Detection</h3>
            <p>Run oriented bounding box detection on aerial and satellite imagery with 4 specialized models.</p>
            <a href="/detection" class="feature-link">Open Tool →</a>
        </div>

        <div class="feature-card reveal reveal-delay-1" style="text-align:center;">
            <div style="font-size:40px; margin-bottom:18px; display:block;">🛰️</div>
            <h3>Datasets</h3>
            <p>Explore DOTA, HRSC, and FAIR1M training datasets used to build RAVEN's detection models.</p>
            <a href="/datasets" class="feature-link">Explore →</a>
        </div>

        <div class="feature-card reveal reveal-delay-2" style="text-align:center;">
            <div style="font-size:40px; margin-bottom:18px; display:block;">📊</div>
            <h3>Detection History</h3>
            <p>View your past detections, download annotated results, and track performance over time.</p>
            <a href="/history" class="feature-link">View History →</a>
        </div>

        <div class="feature-card reveal reveal-delay-3" style="text-align:center;">
            <div style="font-size:40px; margin-bottom:18px; display:block;">⚙️</div>
            <h3>About RAVEN</h3>
            <p>Learn about the architecture, models, and research behind this detection system.</p>
            <a href="/about" class="feature-link">View →</a>
        </div>

    </div>
</section>

<!-- HOW IT WORKS -->
<section style="padding:80px 120px; background:#07051a; border-top:1px solid rgba(102,68,255,0.15);">
    <div style="text-align:center; margin-bottom:56px;">
        <div style="display:inline-block; background:rgba(0,207,255,0.08); border:1px solid rgba(0,207,255,0.25);
                    color:#00cfff; padding:5px 18px; border-radius:30px; font-size:11px;
                    font-weight:800; letter-spacing:3px; margin-bottom:18px; font-family:'Courier New',monospace;">
            HOW IT WORKS
        </div>
        <h2 style="font-size:38px; margin:0; background:linear-gradient(135deg,#fff,#6644ff);
                   -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
            Three steps to detection
        </h2>
    </div>

    <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:32px; max-width:900px; margin:0 auto;">
        <div class="reveal" style="text-align:center; padding:32px 24px;
             background:var(--bg-card); border-radius:16px; border:1px solid rgba(102,68,255,0.2);">
            <div style="width:56px; height:56px; background:linear-gradient(135deg,#6644ff,#00cfff);
                        border-radius:50%; display:flex; align-items:center; justify-content:center;
                        font-size:22px; font-weight:700; margin:0 auto 20px; color:white;">1</div>
            <h3 style="margin:0 0 10px; font-size:18px;">Upload Image</h3>
            <p style="color:#8877cc; font-size:14px; line-height:1.6; margin:0;">
                Upload a single aerial image or an entire folder of images for batch processing.
            </p>
        </div>
        <div class="reveal reveal-delay-1" style="text-align:center; padding:32px 24px;
             background:var(--bg-card); border-radius:16px; border:1px solid rgba(102,68,255,0.2);">
            <div style="width:56px; height:56px; background:linear-gradient(135deg,#6644ff,#00cfff);
                        border-radius:50%; display:flex; align-items:center; justify-content:center;
                        font-size:22px; font-weight:700; margin:0 auto 20px; color:white;">2</div>
            <h3 style="margin:0 0 10px; font-size:18px;">Choose Model</h3>
            <p style="color:#8877cc; font-size:14px; line-height:1.6; margin:0;">
                Select from Standard YOLOv8, DOTA-OBB, HRSC-OBB, or DOTA Fine-grained models.
            </p>
        </div>
        <div class="reveal reveal-delay-2" style="text-align:center; padding:32px 24px;
             background:var(--bg-card); border-radius:16px; border:1px solid rgba(102,68,255,0.2);">
            <div style="width:56px; height:56px; background:linear-gradient(135deg,#6644ff,#00cfff);
                        border-radius:50%; display:flex; align-items:center; justify-content:center;
                        font-size:22px; font-weight:700; margin:0 auto 20px; color:white;">3</div>
            <h3 style="margin:0 0 10px; font-size:18px;">Get Results</h3>
            <p style="color:#8877cc; font-size:14px; line-height:1.6; margin:0;">
                Download annotated images, export CSV data, or generate a full PDF report.
            </p>
        </div>
    </div>
</section>

<!-- CTA -->
<section style="padding:80px 120px; text-align:center; background:var(--bg-deep);
                border-top:1px solid rgba(102,68,255,0.15);">
    <h2 style="font-size:42px; margin:0 0 16px;
               background:linear-gradient(135deg,#fff 0%,#00cfff 50%,#6644ff 100%);
               -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
        Ready to detect?
    </h2>
    <p style="color:#8877cc; font-size:17px; margin:0 0 36px;">
        Upload your first aerial image and see RAVEN in action.
    </p>
    <a href="/detection" class="btn-primary" style="font-size:17px; padding:16px 40px;">
        Start Detection →
    </a>
</section>

{% endblock %}
"""

with open(r"C:\Users\khech\OAOD Project\website\templates\home.html", "w", encoding="utf-8") as f:
    f.write(content)
print("home.html written!")