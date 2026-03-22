import os

BASE = r"C:\Users\khech\OAOD Project\website"

# ── 1. FIX NAVBAR — make it fixed so it stays on scroll ────────
css_path = os.path.join(BASE, "static", "style.css")
css = open(css_path, encoding="utf-8").read()

old_nav = '''.navbar {
    position: absolute;
    top: 0; left: 0; right: 0;'''

new_nav = '''.navbar {
    position: fixed;
    top: 0; left: 0; right: 0;'''

if old_nav in css:
    css = css.replace(old_nav, new_nav)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Navbar fixed: position changed to fixed")
else:
    print("Navbar already fixed or not found")

# ── 2. REWRITE ABOUT.HTML ───────────────────────────────────────
about = '''\
{% extends "layout.html" %}
{% block content %}

<!-- HERO BANNER -->
<div style="background:linear-gradient(135deg,#07051a 0%,#0d0b22 50%,#0a0820 100%);
            padding:80px 120px 60px;
            border-bottom:1px solid rgba(102,68,255,0.2);
            position:relative;overflow:hidden;">

    <!-- Background grid lines -->
    <div style="position:absolute;inset:0;opacity:0.04;
                background-image:linear-gradient(rgba(102,68,255,1) 1px,transparent 1px),
                linear-gradient(90deg,rgba(102,68,255,1) 1px,transparent 1px);
                background-size:40px 40px;"></div>

    <div style="position:relative;">
        <div style="display:inline-block;background:rgba(102,68,255,0.12);
                    border:1px solid rgba(102,68,255,0.35);color:#6644ff;
                    padding:5px 16px;border-radius:30px;font-size:11px;
                    font-weight:700;letter-spacing:3px;margin-bottom:22px;
                    font-family:'Courier New',monospace;">
            ABOUT RAVEN
        </div>
        <h1 style="font-size:52px;font-weight:700;margin:0 0 16px;
                   background:linear-gradient(135deg,#fff 0%,#00cfff 60%,#6644ff 100%);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                   background-clip:text;">
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

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);
                    border-radius:20px;padding:40px;">
            <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">
                WHAT IS RAVEN
            </div>
            <h2 style="font-size:26px;margin:0 0 16px;color:#fff;">
                Rotated-Annotation Vehicle &amp; Entity Network
            </h2>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;">
                RAVEN is a web platform that runs state-of-the-art
                Oriented Bounding Box (OBB) detection on aerial imagery.
                Unlike standard detectors that use horizontal boxes,
                RAVEN predicts the exact rotation angle of every object —
                giving tighter, more accurate detections in dense and
                complex aerial scenes.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);
                    border-radius:20px;padding:40px;">
            <div style="color:#00cfff;font-size:11px;font-weight:700;letter-spacing:3px;
                        font-family:'Courier New',monospace;margin-bottom:16px;">
                THE MISSION
            </div>
            <h2 style="font-size:26px;margin:0 0 16px;color:#fff;">
                Built for aerial intelligence
            </h2>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;">
                From traffic monitoring and ship tracking to defense surveillance
                and disaster response — RAVEN was designed to handle real-world
                aerial detection challenges that standard tools fail at.
                Every feature exists to make detection faster, more accurate,
                and more accessible.
            </p>
        </div>

    </div>
</div>

<!-- PLATFORM CAPABILITIES -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">
        PLATFORM CAPABILITIES
    </div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">What RAVEN can do</h2>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#127947;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Multi-Model Detection</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Standard YOLOv8, DOTA-OBB, HRSC-OBB, and DOTA Fine-grained —
                four detection modes for different aerial scenarios.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128230;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Batch Processing</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Upload a single image or an entire folder of hundreds of images.
                RAVEN processes them all and delivers downloadable results.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128202;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Performance Analytics</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Every detection logs inference time, FPS, object count,
                and density — giving you full visibility into model performance.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128274;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">User Accounts</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Register and log in to keep your detection history private.
                Results auto-expire after 48 hours for clean cloud storage.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128190;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Cloud History</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                All detections are stored in a cloud MySQL database.
                Browse, filter, and download past results any time.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#127919;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Fine-Grained Classification</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                DOTA Fine-grained mode sub-classifies vehicles into
                cars, vans, trucks, buses, trailers and more using a
                FAIR1M-trained secondary model.
            </p>
        </div>

    </div>
</div>

<!-- MODEL PERFORMANCE -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">
        MODEL PERFORMANCE
    </div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Detection accuracy</h2>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#00cfff;
                        font-family:'Courier New',monospace;margin-bottom:8px;">
                0.657
            </div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">DOTA mAP50</div>
            <div style="color:#8877cc;font-size:13px;">YOLOv8 OBB trained on DOTA v1.0<br>15 aerial object categories</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.25);
                    border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#00cfff;
                        font-family:'Courier New',monospace;margin-bottom:8px;">
                0.983
            </div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">HRSC mAP50</div>
            <div style="color:#8877cc;font-size:13px;">Fine-tuned on HRSC2016 ship dataset<br>Near-perfect ship detection</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#6644ff;
                        font-family:'Courier New',monospace;margin-bottom:8px;">
                0.165
            </div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">FAIR1M mAP50</div>
            <div style="color:#8877cc;font-size:13px;">Fine-grained vehicle classifier<br>10 vehicle sub-categories</div>
        </div>
    </div>
</div>

<!-- TECH STACK -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">
        TECHNOLOGY STACK
    </div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Built with</h2>

    <div style="display:flex;flex-wrap:wrap;gap:14px;">
        {% for tech in [
            ("YOLOv8 OBB","#6644ff"),("Flask","#00cfff"),("PyTorch","#6644ff"),
            ("OpenCV","#00cfff"),("MySQL","#6644ff"),("Python","#00cfff"),
            ("DOTA Dataset","#6644ff"),("HRSC2016","#00cfff"),("FAIR1M","#6644ff"),
            ("NumPy","#00cfff"),("Werkzeug","#6644ff"),("HTML/CSS/JS","#00cfff")
        ] %}
        <span style="background:rgba({{ '102,68,255' if tech[1]=='#6644ff' else '0,207,255' }},0.1);
                     border:1px solid {{ tech[1] }}44;color:{{ tech[1] }};
                     padding:8px 18px;border-radius:30px;font-size:13px;
                     font-weight:600;letter-spacing:0.5px;">
            {{ tech[0] }}
        </span>
        {% endfor %}
    </div>
</div>

<!-- TEAM -->
<div style="padding:60px 120px 80px;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">
        THE TEAM
    </div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Built by</h2>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:36px;text-align:center;">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:28px;font-weight:700;margin:0 auto 18px;color:#fff;">
                A
            </div>
            <h3 style="font-size:18px;margin:0 0 6px;color:#fff;">Anudeep Gonuguntla</h3>
            <div style="color:#6644ff;font-size:12px;letter-spacing:1px;
                        font-family:'Courier New',monospace;margin-bottom:12px;">
                LEAD DEVELOPER
            </div>
            <p style="color:#8877cc;font-size:13px;line-height:1.6;margin:0;">
                Original website architecture, Flask backend, UI/UX design
                and full-stack integration.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);
                    border-radius:16px;padding:36px;text-align:center;">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#3311aa,#6644ff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:28px;font-weight:700;margin:0 auto 18px;color:#fff;">
                T
            </div>
            <h3 style="font-size:18px;margin:0 0 6px;color:#fff;">Team</h3>
            <div style="color:#6644ff;font-size:12px;letter-spacing:1px;
                        font-family:'Courier New',monospace;margin-bottom:12px;">
                MODEL TRAINING &amp; RESEARCH
            </div>
            <p style="color:#8877cc;font-size:13px;line-height:1.6;margin:0;">
                YOLOv8 OBB training on DOTA and HRSC datasets,
                FAIR1M fine-grained vehicle classification pipeline,
                cloud database integration.
            </p>
        </div>

        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);
                    border-radius:16px;padding:36px;text-align:center;">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#005577,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:28px;margin:0 auto 18px;">
                &#127979;
            </div>
            <h3 style="font-size:18px;margin:0 0 6px;color:#fff;">Academic Project</h3>
            <div style="color:#00cfff;font-size:12px;letter-spacing:1px;
                        font-family:'Courier New',monospace;margin-bottom:12px;">
                RESEARCH &amp; DEVELOPMENT
            </div>
            <p style="color:#8877cc;font-size:13px;line-height:1.6;margin:0;">
                Built as part of an academic research project in aerial
                object detection with orientation-aware deep learning models.
            </p>
        </div>

    </div>
</div>

{% endblock %}
'''

with open(os.path.join(BASE, "templates", "about.html"), "w", encoding="utf-8") as f:
    f.write(about)
print("about.html written")
print("All done! Restart: python app.py")