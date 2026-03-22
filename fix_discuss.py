import os

BASE = r"C:\Users\khech\OAOD Project\website"

# ── 1. ADD /discuss ROUTE TO APP.PY ────────────────────────────
app_path = os.path.join(BASE, "app.py")
content = open(app_path, encoding="utf-8").read()

old = '@app.route("/about")\ndef about():\n    return render_template("about.html", title="About")'
new = '''@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/discuss")
def discuss():
    return render_template("discuss.html", title="Discuss")'''

if '/discuss' not in content:
    content = content.replace(old, new)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("discuss route added to app.py")
else:
    print("discuss route already exists")

# ── 2. UPDATE LAYOUT.HTML — add Discuss to navbar ──────────────
layout_path = os.path.join(BASE, "templates", "layout.html")
layout = open(layout_path, encoding="utf-8").read()

old_nav = '''        <a href="/about">About</a>
        <a href="/history">History</a>'''
new_nav = '''        <a href="/about">About</a>
        <a href="/history">History</a>
        <a href="/discuss">Discuss</a>'''

if '/discuss' not in layout:
    layout = layout.replace(old_nav, new_nav)
    with open(layout_path, "w", encoding="utf-8") as f:
        f.write(layout)
    print("Discuss added to navbar")
else:
    print("Discuss already in navbar")

# ── 3. UPDATE ABOUT.HTML ────────────────────────────────────────
about = '''\
{% extends "layout.html" %}
{% block content %}

<!-- HERO -->
<div style="background:linear-gradient(135deg,#07051a 0%,#0d0b22 50%,#0a0820 100%);
            padding:80px 120px 60px;border-bottom:1px solid rgba(102,68,255,0.2);
            position:relative;overflow:hidden;">
    <div style="position:absolute;inset:0;opacity:0.04;
                background-image:linear-gradient(rgba(102,68,255,1) 1px,transparent 1px),
                linear-gradient(90deg,rgba(102,68,255,1) 1px,transparent 1px);
                background-size:40px 40px;"></div>
    <div style="position:relative;">
        <div style="display:inline-block;background:rgba(102,68,255,0.12);
                    border:1px solid rgba(102,68,255,0.35);color:#6644ff;
                    padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                    letter-spacing:3px;margin-bottom:22px;font-family:'Courier New',monospace;">
            ABOUT RAVEN
        </div>
        <h1 style="font-size:52px;font-weight:700;margin:0 0 16px;
                   background:linear-gradient(135deg,#fff 0%,#00cfff 60%,#6644ff 100%);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
            Detection that never blinks.
        </h1>
        <p style="font-size:18px;color:#8877cc;max-width:680px;line-height:1.7;margin:0;">
            RAVEN is an AI-powered aerial object detection platform built to see what others miss —
            rotated vehicles, ships, and structures in satellite and drone imagery,
            detected with machine precision and zero margin for error.
        </p>
    </div>
</div>

<!-- WHAT IS RAVEN -->
<div style="padding:70px 120px 0;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;padding:40px;">
            <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">WHAT IS RAVEN</div>
            <h2 style="font-size:26px;margin:0 0 16px;color:#fff;">Rotated-Annotation Vehicle &amp; Entity Network</h2>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;">
                RAVEN is a web platform that runs state-of-the-art Oriented Bounding Box (OBB)
                detection on aerial imagery. Unlike standard detectors that use horizontal boxes,
                RAVEN predicts the exact rotation angle of every object — giving tighter, more
                accurate detections in dense and complex aerial scenes.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:20px;padding:40px;">
            <div style="color:#00cfff;font-size:11px;font-weight:700;letter-spacing:3px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">THE MISSION</div>
            <h2 style="font-size:26px;margin:0 0 16px;color:#fff;">Built for aerial intelligence</h2>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;">
                From traffic monitoring and ship tracking to defense surveillance and disaster
                response — RAVEN was designed to handle real-world aerial detection challenges
                that standard tools fail at. Every feature exists to make detection faster,
                more accurate, and more accessible.
            </p>
        </div>
    </div>
</div>

<!-- OBB VS HBB VISUAL -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">CORE TECHNOLOGY</div>
    <h2 style="font-size:32px;margin:0 0 14px;color:#fff;">OBB vs HBB — why rotation matters</h2>
    <p style="color:#8877cc;font-size:15px;line-height:1.7;max-width:720px;margin:0 0 36px;">
        Traditional object detectors use Horizontal Bounding Boxes (HBB) — rectangles that are
        always axis-aligned. When objects in aerial imagery appear at arbitrary angles, HBB boxes
        must be oversized to contain the object, capturing a lot of irrelevant background.
        Oriented Bounding Boxes (OBB) solve this by adding a rotation angle θ, allowing the box
        to wrap tightly around the object at any orientation.
    </p>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:30px;">

        <!-- HBB card -->
        <div style="background:#0d0b22;border:1px solid rgba(255,80,80,0.3);border-radius:20px;padding:36px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(255,80,80,0.15);color:#ff5050;padding:4px 12px;
                             border-radius:20px;font-size:11px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">HBB</span>
                <span style="color:#ff5050;font-size:14px;font-weight:600;">Horizontal Bounding Box</span>
            </div>
            <!-- SVG illustration of HBB -->
            <svg viewBox="0 0 280 160" style="width:100%;margin-bottom:20px;background:#050310;border-radius:12px;padding:10px;">
                <!-- Aerial background grid -->
                <line x1="0" y1="40" x2="280" y2="40" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="0" y1="80" x2="280" y2="80" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="0" y1="120" x2="280" y2="120" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="70" y1="0" x2="70" y2="160" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="140" y1="0" x2="140" y2="160" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="210" y1="0" x2="210" y2="160" stroke="#1a1a3a" stroke-width="0.5"/>
                <!-- Rotated vehicle shape (truck at angle) -->
                <g transform="translate(140,80) rotate(-35)">
                    <rect x="-38" y="-14" width="76" height="28" rx="4" fill="#2244aa" stroke="#4466cc" stroke-width="1"/>
                    <rect x="-38" y="-14" width="28" height="28" rx="3" fill="#1a3388"/>
                    <circle cx="-22" cy="16" r="6" fill="#333"/>
                    <circle cx="22" cy="16" r="6" fill="#333"/>
                    <circle cx="-22" cy="-16" r="6" fill="#333"/>
                    <circle cx="22" cy="-16" r="6" fill="#333"/>
                </g>
                <!-- HBB — large wasteful box -->
                <rect x="88" y="34" width="104" height="92" rx="3"
                      fill="rgba(255,80,80,0.08)" stroke="#ff5050" stroke-width="2" stroke-dasharray="5 3"/>
                <!-- Wasted area indicators -->
                <text x="98" y="52" fill="#ff505055" font-size="9" font-family="monospace">wasted</text>
                <text x="162" y="115" fill="#ff505055" font-size="9" font-family="monospace">wasted</text>
                <!-- Label -->
                <rect x="88" y="20" width="104" height="16" rx="3" fill="#ff5050"/>
                <text x="140" y="31" text-anchor="middle" fill="white" font-size="10" font-family="monospace" font-weight="bold">HBB — 68% background</text>
            </svg>
            <ul style="color:#8877cc;font-size:13px;line-height:1.8;padding-left:18px;margin:0;">
                <li>Box is always axis-aligned (0° or 90°)</li>
                <li>Captures large background areas around rotated objects</li>
                <li>Reduces confidence score accuracy</li>
                <li>Poor localization for vehicles, ships at angles</li>
                <li>IoU calculations are less precise</li>
            </ul>
        </div>

        <!-- OBB card -->
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.3);border-radius:20px;padding:36px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(0,207,255,0.15);color:#00cfff;padding:4px 12px;
                             border-radius:20px;font-size:11px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">OBB</span>
                <span style="color:#00cfff;font-size:14px;font-weight:600;">Oriented Bounding Box</span>
            </div>
            <!-- SVG illustration of OBB -->
            <svg viewBox="0 0 280 160" style="width:100%;margin-bottom:20px;background:#050310;border-radius:12px;padding:10px;">
                <!-- Grid -->
                <line x1="0" y1="40" x2="280" y2="40" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="0" y1="80" x2="280" y2="80" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="0" y1="120" x2="280" y2="120" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="70" y1="0" x2="70" y2="160" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="140" y1="0" x2="140" y2="160" stroke="#1a1a3a" stroke-width="0.5"/>
                <line x1="210" y1="0" x2="210" y2="160" stroke="#1a1a3a" stroke-width="0.5"/>
                <!-- Same rotated vehicle -->
                <g transform="translate(140,80) rotate(-35)">
                    <rect x="-38" y="-14" width="76" height="28" rx="4" fill="#2244aa" stroke="#4466cc" stroke-width="1"/>
                    <rect x="-38" y="-14" width="28" height="28" rx="3" fill="#1a3388"/>
                    <circle cx="-22" cy="16" r="6" fill="#333"/>
                    <circle cx="22" cy="16" r="6" fill="#333"/>
                    <circle cx="-22" cy="-16" r="6" fill="#333"/>
                    <circle cx="22" cy="-16" r="6" fill="#333"/>
                </g>
                <!-- OBB — tight rotated box -->
                <g transform="translate(140,80) rotate(-35)">
                    <rect x="-44" y="-20" width="88" height="40" rx="3"
                          fill="rgba(0,207,255,0.08)" stroke="#00cfff" stroke-width="2"/>
                    <!-- Corner ticks -->
                    <path d="M-44,-20 L-44,-10 M-44,-20 L-34,-20" fill="none" stroke="#00cfff" stroke-width="1.5"/>
                    <path d="M44,-20 L44,-10 M44,-20 L34,-20" fill="none" stroke="#00cfff" stroke-width="1.5"/>
                    <path d="M-44,20 L-44,10 M-44,20 L-34,20" fill="none" stroke="#00cfff" stroke-width="1.5"/>
                    <path d="M44,20 L44,10 M44,20 L34,20" fill="none" stroke="#00cfff" stroke-width="1.5"/>
                </g>
                <!-- Angle indicator -->
                <path d="M140,80 L165,80" stroke="#6644ff" stroke-width="1" stroke-dasharray="3 2"/>
                <path d="M140,80 L158,68" stroke="#6644ff" stroke-width="1.5" marker-end="url(#arr)"/>
                <text x="162" y="76" fill="#6644ff" font-size="9" font-family="monospace">θ=-35°</text>
                <!-- Label -->
                <rect x="88" y="20" width="104" height="16" rx="3" fill="#00cfff"/>
                <text x="140" y="31" text-anchor="middle" fill="#000" font-size="10" font-family="monospace" font-weight="bold">OBB — 8% background</text>
            </svg>
            <ul style="color:#8877cc;font-size:13px;line-height:1.8;padding-left:18px;margin:0;">
                <li>Box rotates to match object orientation angle θ</li>
                <li>Minimal background captured — tight fit</li>
                <li>Higher confidence and localization accuracy</li>
                <li>Essential for vehicles, ships, aircraft at angles</li>
                <li>Rotated IoU gives precise overlap measurement</li>
            </ul>
        </div>

    </div>

    <!-- Summary stat bar -->
    <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;
                padding:28px 36px;display:flex;justify-content:space-around;align-items:center;">
        <div style="text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#ff5050;font-family:'Courier New',monospace;">~68%</div>
            <div style="color:#8877cc;font-size:13px;margin-top:4px;">HBB background waste</div>
        </div>
        <div style="width:1px;height:60px;background:rgba(102,68,255,0.3);"></div>
        <div style="text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">~8%</div>
            <div style="color:#8877cc;font-size:13px;margin-top:4px;">OBB background waste</div>
        </div>
        <div style="width:1px;height:60px;background:rgba(102,68,255,0.3);"></div>
        <div style="text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">8x</div>
            <div style="color:#8877cc;font-size:13px;margin-top:4px;">tighter localization</div>
        </div>
        <div style="width:1px;height:60px;background:rgba(102,68,255,0.3);"></div>
        <div style="text-align:center;">
            <div style="font-size:36px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">+θ</div>
            <div style="color:#8877cc;font-size:13px;margin-top:4px;">rotation angle predicted</div>
        </div>
    </div>
</div>

<!-- PLATFORM CAPABILITIES -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">PLATFORM CAPABILITIES</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">What RAVEN can do</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#127947;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Multi-Model Detection</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Four detection modes — Standard YOLOv8, DOTA-OBB, HRSC-OBB, and
                DOTA Fine-grained — each optimised for different aerial scenarios
                and object types.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128230;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Batch Processing</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Upload a single image or an entire folder of hundreds of images.
                RAVEN processes all of them sequentially and delivers
                individual downloadable results for each.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128202;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Performance Analytics</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Every detection logs inference time, FPS, object count and density.
                Track model performance across different images and compare
                results from the history dashboard.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128274;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">User Accounts</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Register for a free account to keep your detection history private.
                Results are linked to your account and auto-expire after 48 hours
                for clean storage management.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128190;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Cloud History</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                All detections are stored in a Clever Cloud MySQL database.
                Browse, revisit and download past detection results
                at any time from the history page.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#127919;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Fine-Grained Classification</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                DOTA Fine-grained mode sub-classifies detected vehicles into
                10 specific types — cars, vans, trucks, buses, trailers,
                excavators, tractors and more using a FAIR1M-trained model.
            </p>
        </div>
    </div>
</div>

<!-- MODEL PERFORMANCE -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">MODEL PERFORMANCE</div>
    <h2 style="font-size:32px;margin:0 0 16px;color:#fff;">Detection accuracy</h2>
    <p style="color:#8877cc;font-size:15px;line-height:1.7;max-width:720px;margin:0 0 36px;">
        mAP50 (Mean Average Precision at IoU threshold 0.5) measures how well the model
        identifies and localises objects. A score of 1.0 is perfect. The scores below
        reflect performance on held-out validation sets not seen during training.
    </p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;margin-bottom:8px;">0.657</div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">DOTA mAP50</div>
            <div style="color:#8877cc;font-size:13px;line-height:1.6;">
                YOLOv8 OBB trained on DOTA v1.0<br>
                15 aerial object categories<br>
                Planes, ships, vehicles, harbours
            </div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.25);border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;margin-bottom:8px;">0.983</div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">HRSC mAP50</div>
            <div style="color:#8877cc;font-size:13px;line-height:1.6;">
                Fine-tuned on HRSC2016<br>
                Ship detection specialist<br>
                Near-perfect accuracy
            </div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;margin-bottom:8px;">0.165</div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">FAIR1M mAP50</div>
            <div style="color:#8877cc;font-size:13px;line-height:1.6;">
                Fine-grained vehicle classifier<br>
                10 vehicle sub-categories<br>
                Limited by 1,732 training images
            </div>
        </div>
    </div>
</div>

<!-- APPLICATION USE CASES -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">APPLICATIONS</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Real-world use cases</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:32px;display:flex;gap:20px;">
            <div style="font-size:36px;flex-shrink:0;">&#128652;</div>
            <div>
                <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Traffic &amp; Urban Monitoring</h3>
                <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                    Count and classify vehicles in parking lots, intersections and highways
                    from drone imagery. RAVEN identifies whether a space holds a car, truck
                    or bus — useful for smart city planning, congestion analysis and
                    automated parking management systems.
                </p>
            </div>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:32px;display:flex;gap:20px;">
            <div style="font-size:36px;flex-shrink:0;">&#128674;</div>
            <div>
                <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Port &amp; Maritime Surveillance</h3>
                <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                    RAVEN's HRSC model achieves 0.983 mAP50 on ship detection —
                    making it suitable for monitoring vessel movements in ports,
                    detecting unauthorised ships in restricted waters and supporting
                    coast guard and maritime logistics operations.
                </p>
            </div>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:32px;display:flex;gap:20px;">
            <div style="font-size:36px;flex-shrink:0;">&#128250;</div>
            <div>
                <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Defense &amp; Intelligence</h3>
                <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                    Detect aircraft, helicopters, military vehicles and storage tanks
                    in satellite imagery. Oriented detection is critical in defense
                    applications where objects are rarely aligned to the image axis —
                    RAVEN gives precise localisation at any angle.
                </p>
            </div>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:32px;display:flex;gap:20px;">
            <div style="font-size:36px;flex-shrink:0;">&#127754;</div>
            <div>
                <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Disaster Assessment</h3>
                <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                    After floods, earthquakes or wildfires, aerial imagery is captured
                    to assess damage. RAVEN can rapidly detect and count affected
                    vehicles, collapsed structures and relief assets to assist
                    emergency response teams with situational awareness.
                </p>
            </div>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:32px;display:flex;gap:20px;">
            <div style="font-size:36px;flex-shrink:0;">&#127963;</div>
            <div>
                <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Urban &amp; Infrastructure Planning</h3>
                <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                    City planners use aerial imagery to analyse land use, road density
                    and building layouts. RAVEN automates object counting and density
                    calculations that previously required manual annotation —
                    accelerating planning workflows significantly.
                </p>
            </div>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:32px;display:flex;gap:20px;">
            <div style="font-size:36px;flex-shrink:0;">&#128200;</div>
            <div>
                <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Research &amp; Academic Use</h3>
                <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                    RAVEN serves as a research platform for exploring oriented object
                    detection on aerial datasets. The batch processing and export
                    features make it easy to run large-scale experiments and generate
                    annotated output datasets for further study.
                </p>
            </div>
        </div>

    </div>
</div>

<!-- TECH STACK -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">TECHNOLOGY STACK</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Built with</h2>
    <div style="display:flex;flex-wrap:wrap;gap:14px;">
        {% for tech in [
            ("YOLOv8 OBB","#6644ff"),("Flask","#00cfff"),("PyTorch","#6644ff"),
            ("OpenCV","#00cfff"),("MySQL","#6644ff"),("Python","#00cfff"),
            ("DOTA Dataset","#6644ff"),("HRSC2016","#00cfff"),("FAIR1M","#6644ff"),
            ("NumPy","#00cfff"),("Werkzeug","#6644ff"),("HTML / CSS / JS","#00cfff")
        ] %}
        <span style="background:rgba({{ '102,68,255' if tech[1]=='#6644ff' else '0,207,255' }},0.1);
                     border:1px solid {{ tech[1] }}44;color:{{ tech[1] }};
                     padding:8px 18px;border-radius:30px;font-size:13px;font-weight:600;">
            {{ tech[0] }}
        </span>
        {% endfor %}
    </div>
</div>

<!-- TEAM -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">THE TEAM</div>
    <h2 style="font-size:32px;margin:0 0 10px;color:#fff;">Built by</h2>
    <p style="color:#8877cc;font-size:15px;margin:0 0 36px;line-height:1.7;">
        A team of 4th-year Data Science and ML Engineering students who built RAVEN
        as an academic research project in aerial object detection.
    </p>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#6644ff,#00cfff);
                        display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">A</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Anudeep Gonuguntla</h3>
            <div style="color:#00cfff;font-size:10px;letter-spacing:1.5px;font-family:'Courier New',monospace;margin-bottom:10px;">FRONTEND &amp; DEPLOYMENT</div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">Website architecture, UI/UX design, frontend development and cloud deployment.</p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#005577,#00cfff);
                        display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">K</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Khechara Sai Venkata Ramana Boppudi</h3>
            <div style="color:#00cfff;font-size:10px;letter-spacing:1.5px;font-family:'Courier New',monospace;margin-bottom:10px;">DEEP LEARNING &amp; MODEL TRAINING</div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">YOLOv8 OBB training on DOTA &amp; HRSC, FAIR1M fine-grained pipeline and backend integration.</p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#3311aa,#6644ff);
                        display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">D</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Dhanoosh Reddy Devalapalle</h3>
            <div style="color:#6644ff;font-size:10px;letter-spacing:1.5px;font-family:'Courier New',monospace;margin-bottom:10px;">TESTING &amp; DATABASE</div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">System testing, quality assurance and cloud MySQL database design and management.</p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.15);border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#440055,#aa44ff);
                        display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">N</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Nitya Sri Santoshini Nandanavanam</h3>
            <div style="color:#aa44ff;font-size:10px;letter-spacing:1.5px;font-family:'Courier New',monospace;margin-bottom:10px;">CONTRIBUTOR</div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">Project contributor and team member supporting the research and development of RAVEN.</p>
        </div>
    </div>
</div>

<!-- FAQ -->
<div style="padding:60px 120px 80px;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">FAQ</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Frequently asked questions</h2>
    <div style="max-width:860px;">
        {% set faqs = [
            ("What is RAVEN?",
             "RAVEN stands for Rotated-Annotation Vehicle &amp; Entity Network. It is an AI-powered web platform that detects objects in aerial and satellite imagery using Oriented Bounding Box (OBB) detection — predicting not just where an object is, but also its exact rotation angle for tighter, more accurate results."),
            ("How does OBB detection work?",
             "Standard detection uses horizontal bounding boxes always aligned to the image axes. When aerial objects appear rotated, these boxes waste space capturing background. OBB adds a rotation angle θ to every prediction, wrapping tightly around the object at any orientation — dramatically improving accuracy."),
            ("Which models are used?",
             "RAVEN uses four models — Standard YOLOv8n for general detection, a YOLOv8-OBB model trained on DOTA for 15 aerial categories, a YOLOv8-OBB model fine-tuned on HRSC2016 for ship detection, and a FAIR1M-trained model for fine-grained vehicle sub-classification."),
            ("What datasets were used for training?",
             "Three datasets: DOTA v1.0 with 15 aerial object categories, HRSC2016 for ship detection with oriented annotations, and FAIR1M with 37 fine-grained sub-categories used to train the vehicle classifier."),
            ("How accurate is the detection?",
             "DOTA model: 0.657 mAP50 across 15 categories. HRSC ship model: 0.983 mAP50 — near-perfect. FAIR1M fine-grained classifier: 0.165 mAP50 across 10 vehicle types, limited by the 1,732 image training set."),
            ("What image formats are supported?",
             "JPG, JPEG, PNG and TIFF formats are supported — covering standard photography, satellite imagery and drone capture. You can upload individual images or an entire folder for batch processing."),
            ("Is my data stored?",
             "Detection metadata (object count, inference time, model used, image size) is stored in cloud MySQL. Actual image files are stored temporarily. If logged in, your history is private and only visible to you."),
            ("How long are results saved?",
             "Output images are automatically deleted after 48 hours. Detection statistics remain in your history permanently so you can track usage over time even after the images expire."),
            ("Can I use RAVEN without an account?",
             "Yes — detection runs without an account. However results won't be saved to history. Creating a free account takes under 30 seconds and gives you private history with download access for 48 hours per detection."),
            ("What is DOTA Fine-grained mode?",
             "A two-stage pipeline — first the DOTA model detects all objects and labels vehicles broadly. Then for each vehicle, RAVEN crops the region and passes it through a FAIR1M-trained model to sub-classify it as a small car, van, cargo truck, dump truck, bus, trailer, excavator, tractor or truck-tractor.")
        ] %}
        {% for q, a in faqs %}
        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                {{ q }} <span style="float:right;transition:transform 0.3s;">+</span>
            </button>
            <div class="faq-a">{{ a }}</div>
        </div>
        {% endfor %}
    </div>
</div>

<script>
function toggleFaq(btn) {
    var answer = btn.nextElementSibling;
    var icon = btn.querySelector('span');
    var isOpen = answer.classList.contains('show');
    document.querySelectorAll('.faq-a').forEach(function(a){ a.classList.remove('show'); });
    document.querySelectorAll('.faq-q span').forEach(function(s){ s.textContent='+'; s.style.transform='rotate(0deg)'; });
    if (!isOpen) { answer.classList.add('show'); icon.textContent='+'; icon.style.transform='rotate(45deg)'; }
}
</script>
{% endblock %}
'''

with open(os.path.join(BASE, "templates", "about.html"), "w", encoding="utf-8") as f:
    f.write(about)
print("about.html written")

# ── 4. CREATE DISCUSS.HTML ──────────────────────────────────────
discuss = '''\
{% extends "layout.html" %}
{% block content %}

<!-- HERO -->
<div style="background:linear-gradient(135deg,#07051a 0%,#0d0b22 50%,#0a0820 100%);
            padding:80px 120px 60px;border-bottom:1px solid rgba(102,68,255,0.2);
            position:relative;overflow:hidden;">
    <div style="position:absolute;inset:0;opacity:0.04;
                background-image:linear-gradient(rgba(102,68,255,1) 1px,transparent 1px),
                linear-gradient(90deg,rgba(102,68,255,1) 1px,transparent 1px);
                background-size:40px 40px;"></div>
    <div style="position:relative;">
        <div style="display:inline-block;background:rgba(102,68,255,0.12);
                    border:1px solid rgba(102,68,255,0.35);color:#6644ff;
                    padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                    letter-spacing:3px;margin-bottom:22px;font-family:'Courier New',monospace;">
            DISCUSS
        </div>
        <h1 style="font-size:52px;font-weight:700;margin:0 0 16px;
                   background:linear-gradient(135deg,#fff 0%,#00cfff 60%,#6644ff 100%);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
            Talk to the team.
        </h1>
        <p style="font-size:18px;color:#8877cc;max-width:620px;line-height:1.7;margin:0;">
            Have questions, suggestions or feedback about RAVEN? Reach out to us directly
            or connect on our platforms. We are always open to ideas and collaboration.
        </p>
    </div>
</div>

<!-- CONTACT CARDS -->
<div style="padding:70px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">GET IN TOUCH</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Contact the team</h2>

    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">

        <!-- Anudeep -->
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:28px;">
            <div style="width:52px;height:52px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:20px;font-weight:700;margin-bottom:14px;color:#fff;">A</div>
            <h3 style="font-size:15px;margin:0 0 4px;color:#fff;">Anudeep Gonuguntla</h3>
            <div style="color:#00cfff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">FRONTEND &amp; DEPLOYMENT</div>
            <div style="display:flex;flex-direction:column;gap:10px;">
                <a href="mailto:placeholder@email.com"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#00cfff'" onmouseout="this.style.color='#8877cc'">
                    <span style="font-size:16px;">&#128140;</span> Email
                </a>
                <a href="https://linkedin.com/in/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#00cfff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128101;</span> LinkedIn
                </a>
                <a href="https://github.com/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#00cfff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128196;</span> GitHub
                </a>
            </div>
        </div>

        <!-- Khechara -->
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:16px;padding:28px;">
            <div style="width:52px;height:52px;border-radius:50%;
                        background:linear-gradient(135deg,#005577,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:20px;font-weight:700;margin-bottom:14px;color:#fff;">K</div>
            <h3 style="font-size:15px;margin:0 0 4px;color:#fff;">Khechara Sai Venkata Ramana</h3>
            <div style="color:#00cfff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">DEEP LEARNING &amp; TRAINING</div>
            <div style="display:flex;flex-direction:column;gap:10px;">
                <a href="mailto:placeholder@email.com"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#00cfff'" onmouseout="this.style.color='#8877cc'">
                    <span style="font-size:16px;">&#128140;</span> Email
                </a>
                <a href="https://linkedin.com/in/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#00cfff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128101;</span> LinkedIn
                </a>
                <a href="https://github.com/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#00cfff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128196;</span> GitHub
                </a>
            </div>
        </div>

        <!-- Dhanoosh -->
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:28px;">
            <div style="width:52px;height:52px;border-radius:50%;
                        background:linear-gradient(135deg,#3311aa,#6644ff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:20px;font-weight:700;margin-bottom:14px;color:#fff;">D</div>
            <h3 style="font-size:15px;margin:0 0 4px;color:#fff;">Dhanoosh Reddy Devalapalle</h3>
            <div style="color:#6644ff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">TESTING &amp; DATABASE</div>
            <div style="display:flex;flex-direction:column;gap:10px;">
                <a href="mailto:placeholder@email.com"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#6644ff'" onmouseout="this.style.color='#8877cc'">
                    <span style="font-size:16px;">&#128140;</span> Email
                </a>
                <a href="https://linkedin.com/in/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#6644ff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128101;</span> LinkedIn
                </a>
                <a href="https://github.com/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#6644ff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128196;</span> GitHub
                </a>
            </div>
        </div>

        <!-- Nitya -->
        <div style="background:#0d0b22;border:1px solid rgba(170,68,255,0.2);border-radius:16px;padding:28px;">
            <div style="width:52px;height:52px;border-radius:50%;
                        background:linear-gradient(135deg,#440055,#aa44ff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:20px;font-weight:700;margin-bottom:14px;color:#fff;">N</div>
            <h3 style="font-size:15px;margin:0 0 4px;color:#fff;">Nitya Sri Santoshini Nandanavanam</h3>
            <div style="color:#aa44ff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">CONTRIBUTOR</div>
            <div style="display:flex;flex-direction:column;gap:10px;">
                <a href="mailto:placeholder@email.com"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#aa44ff'" onmouseout="this.style.color='#8877cc'">
                    <span style="font-size:16px;">&#128140;</span> Email
                </a>
                <a href="https://linkedin.com/in/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#aa44ff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128101;</span> LinkedIn
                </a>
                <a href="https://github.com/placeholder"
                   style="display:flex;align-items:center;gap:8px;color:#8877cc;font-size:13px;text-decoration:none;transition:0.2s;"
                   onmouseover="this.style.color='#aa44ff'" onmouseout="this.style.color='#8877cc'" target="_blank">
                    <span style="font-size:16px;">&#128196;</span> GitHub
                </a>
            </div>
        </div>

    </div>
</div>

<!-- FUTURE UPDATES -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">ROADMAP</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Future updates &amp; suggestions</h2>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;">

        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(0,207,255,0.15);color:#00cfff;padding:4px 12px;
                             border-radius:20px;font-size:10px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">PLANNED</span>
                <h3 style="font-size:17px;margin:0;color:#fff;">Real-time video detection</h3>
            </div>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Extend RAVEN to process live drone video feeds frame-by-frame,
                outputting OBB detections in real time with adjustable confidence
                thresholds and model switching on the fly.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(102,68,255,0.15);color:#6644ff;padding:4px 12px;
                             border-radius:20px;font-size:10px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">PLANNED</span>
                <h3 style="font-size:17px;margin:0;color:#fff;">Full FAIR1M dataset training</h3>
            </div>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                The current FAIR1M model was trained on 1,732 images. Training on the full
                15,000 image dataset (requires official registration) would push mAP50
                from 0.165 to an estimated 0.35-0.50+ for fine-grained vehicle classification.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(0,207,255,0.15);color:#00cfff;padding:4px 12px;
                             border-radius:20px;font-size:10px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">PLANNED</span>
                <h3 style="font-size:17px;margin:0;color:#fff;">Heatmap &amp; density visualisation</h3>
            </div>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Add an overlay mode that generates object density heatmaps on top of
                aerial imagery — making it easy to identify congestion hotspots,
                high-traffic areas and clustering patterns at a glance.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(102,68,255,0.15);color:#6644ff;padding:4px 12px;
                             border-radius:20px;font-size:10px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">PLANNED</span>
                <h3 style="font-size:17px;margin:0;color:#fff;">Analytics dashboard</h3>
            </div>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                A dedicated dashboard page showing your detection history as charts —
                objects detected over time, model usage breakdown, average inference
                speed trends and per-class detection frequency.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(0,255,100,0.1);color:#00ff88;padding:4px 12px;
                             border-radius:20px;font-size:10px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">SUGGESTION</span>
                <h3 style="font-size:17px;margin:0;color:#fff;">API access</h3>
            </div>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Expose RAVEN as a REST API so developers can integrate aerial object
                detection into their own applications — sending images programmatically
                and receiving structured JSON detection results.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
                <span style="background:rgba(0,255,100,0.1);color:#00ff88;padding:4px 12px;
                             border-radius:20px;font-size:10px;font-weight:700;letter-spacing:2px;
                             font-family:'Courier New',monospace;">SUGGESTION</span>
                <h3 style="font-size:17px;margin:0;color:#fff;">Custom model upload</h3>
            </div>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Allow users to upload their own YOLOv8 OBB .pt model files and run
                detection with their custom weights — turning RAVEN into a
                general-purpose aerial detection platform beyond the built-in models.
            </p>
        </div>

    </div>
</div>

<!-- FEEDBACK SECTION -->
<div style="padding:60px 120px 80px;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">FEEDBACK</div>
    <h2 style="font-size:32px;margin:0 0 16px;color:#fff;">Share your thoughts</h2>
    <p style="color:#8877cc;font-size:15px;line-height:1.7;max-width:620px;margin:0 0 36px;">
        Found a bug? Have a feature request? Want to collaborate on extending RAVEN?
        We would love to hear from you. Reach out to any team member directly
        using the contact links above.
    </p>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:700px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:14px;padding:24px;text-align:center;">
            <div style="font-size:28px;margin-bottom:10px;">&#128027;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:6px;">Report a bug</div>
            <div style="color:#8877cc;font-size:12px;line-height:1.5;">Found something broken? Tell us exactly what happened.</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:14px;padding:24px;text-align:center;">
            <div style="font-size:28px;margin-bottom:10px;">&#128161;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:6px;">Suggest a feature</div>
            <div style="color:#8877cc;font-size:12px;line-height:1.5;">Have an idea that would make RAVEN better?</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:14px;padding:24px;text-align:center;">
            <div style="font-size:28px;margin-bottom:10px;">&#129309;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:6px;">Collaborate</div>
            <div style="color:#8877cc;font-size:12px;line-height:1.5;">Interested in extending this research further?</div>
        </div>
    </div>
</div>

{% endblock %}
'''

with open(os.path.join(BASE, "templates", "discuss.html"), "w", encoding="utf-8") as f:
    f.write(discuss)
print("discuss.html written")
print("\nAll done! Run: python app.py")