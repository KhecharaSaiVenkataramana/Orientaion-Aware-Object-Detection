import os

BASE = r"C:\Users\khech\OAOD Project\website"

about = '''\
{% extends "layout.html" %}
{% block content %}

<!-- HERO BANNER -->
<div style="background:linear-gradient(135deg,#07051a 0%,#0d0b22 50%,#0a0820 100%);
            padding:80px 120px 60px;
            border-bottom:1px solid rgba(102,68,255,0.2);
            position:relative;overflow:hidden;">
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
                        font-family:'Courier New',monospace;margin-bottom:16px;">WHAT IS RAVEN</div>
            <h2 style="font-size:26px;margin:0 0 16px;color:#fff;">
                Rotated-Annotation Vehicle &amp; Entity Network
            </h2>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;">
                RAVEN is a web platform that runs state-of-the-art Oriented Bounding Box (OBB)
                detection on aerial imagery. Unlike standard detectors that use horizontal boxes,
                RAVEN predicts the exact rotation angle of every object — giving tighter, more
                accurate detections in dense and complex aerial scenes.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);
                    border-radius:20px;padding:40px;">
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
                Standard YOLOv8, DOTA-OBB, HRSC-OBB, and DOTA Fine-grained —
                four detection modes for different aerial scenarios.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128230;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Batch Processing</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Upload a single image or an entire folder of hundreds of images.
                RAVEN processes them all and delivers downloadable results.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128202;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Performance Analytics</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Every detection logs inference time, FPS, object count and density —
                giving full visibility into model performance.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128274;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">User Accounts</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Register and log in to keep your detection history private.
                Results auto-expire after 48 hours for clean cloud storage.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#128190;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Cloud History</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                All detections stored in cloud MySQL. Browse, filter
                and download past results any time.
            </p>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:30px;transition:0.3s;"
             onmouseover="this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)'"
             onmouseout="this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none'">
            <div style="font-size:28px;margin-bottom:14px;">&#127919;</div>
            <h3 style="font-size:17px;margin:0 0 10px;color:#00cfff;">Fine-Grained Classification</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                DOTA Fine-grained mode sub-classifies vehicles into cars, vans,
                trucks, buses and trailers using a FAIR1M-trained secondary model.
            </p>
        </div>
    </div>
</div>

<!-- MODEL PERFORMANCE -->
<div style="padding:60px 120px 0;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">MODEL PERFORMANCE</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Detection accuracy</h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;margin-bottom:8px;">0.657</div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">DOTA mAP50</div>
            <div style="color:#8877cc;font-size:13px;">YOLOv8 OBB trained on DOTA v1.0<br>15 aerial object categories</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.25);border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;margin-bottom:8px;">0.983</div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">HRSC mAP50</div>
            <div style="color:#8877cc;font-size:13px;">Fine-tuned on HRSC2016 ship dataset<br>Near-perfect ship detection</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.18);border-radius:16px;padding:36px;text-align:center;">
            <div style="font-size:48px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;margin-bottom:8px;">0.165</div>
            <div style="color:#fff;font-size:16px;font-weight:600;margin-bottom:8px;">FAIR1M mAP50</div>
            <div style="color:#8877cc;font-size:13px;">Fine-grained vehicle classifier<br>10 vehicle sub-categories</div>
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

        <!-- Member 1 -->
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);
                    border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">A</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Anudeep Gonuguntla</h3>
            <div style="color:#00cfff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:10px;">
                FRONTEND &amp; DEPLOYMENT
            </div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">
                Website architecture, UI/UX design, frontend development
                and cloud deployment of the platform.
            </p>
        </div>

        <!-- Member 2 -->
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);
                    border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;
                        background:linear-gradient(135deg,#005577,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">K</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Khechara Sai Venkata Ramana Boppudi</h3>
            <div style="color:#00cfff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:10px;">
                DEEP LEARNING &amp; MODEL TRAINING
            </div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">
                YOLOv8 OBB training on DOTA &amp; HRSC, FAIR1M fine-grained
                vehicle classification pipeline and backend integration.
            </p>
        </div>

        <!-- Member 3 -->
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);
                    border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;
                        background:linear-gradient(135deg,#3311aa,#6644ff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">D</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Dhanoosh Reddy Devalapalle</h3>
            <div style="color:#6644ff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:10px;">
                TESTING &amp; DATABASE
            </div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">
                System testing, quality assurance and cloud MySQL
                database design and management.
            </p>
        </div>

        <!-- Member 4 -->
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.15);
                    border-radius:16px;padding:30px;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;
                        background:linear-gradient(135deg,#440055,#aa44ff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:24px;font-weight:700;margin:0 auto 16px;color:#fff;">N</div>
            <h3 style="font-size:15px;margin:0 0 6px;color:#fff;">Nitya Sri Santoshini Nandanavanam</h3>
            <div style="color:#aa44ff;font-size:10px;letter-spacing:1.5px;
                        font-family:'Courier New',monospace;margin-bottom:10px;">
                CONTRIBUTOR
            </div>
            <p style="color:#8877cc;font-size:12px;line-height:1.6;margin:0;">
                Project contributor and team member supporting the
                research and development of the RAVEN platform.
            </p>
        </div>

    </div>
</div>

<!-- FAQ -->
<div style="padding:60px 120px 80px;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">FAQ</div>
    <h2 style="font-size:32px;margin:0 0 36px;color:#fff;">Frequently asked questions</h2>

    <div style="max-width:860px;">

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                What is RAVEN? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                RAVEN stands for Rotated-Annotation Vehicle &amp; Entity Network. It is an
                AI-powered web platform that detects objects in aerial and satellite imagery
                using Oriented Bounding Box (OBB) detection — predicting not just where an
                object is, but also its exact rotation angle for tighter, more accurate results.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                How does OBB detection work? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                Standard object detection uses horizontal bounding boxes (HBB) which waste space
                when objects are rotated. Oriented Bounding Box detection adds a rotation angle (θ)
                to every prediction, allowing the box to tightly wrap the object at any angle.
                This dramatically improves accuracy in aerial imagery where vehicles, ships and
                buildings appear at arbitrary orientations.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                Which models are used? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                RAVEN uses three main models — Standard YOLOv8n for general detection,
                a custom YOLOv8-OBB model fine-tuned on the DOTA dataset for aerial object
                detection across 15 categories, and a second YOLOv8-OBB model fine-tuned
                on HRSC2016 specifically for ship detection. A fourth FAIR1M-trained model
                handles fine-grained vehicle sub-classification.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                What datasets were used for training? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                Three datasets were used. DOTA (Dataset for Object deTection in Aerial images)
                contains 15 object categories in aerial imagery. HRSC2016 is a ship detection
                dataset with oriented annotations. FAIR1M is a fine-grained aerial object
                recognition dataset with 37 sub-categories used for the vehicle classifier.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                How accurate is the detection? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                The DOTA model achieves 0.657 mAP50 across 15 aerial object categories.
                The HRSC ship detection model achieves 0.983 mAP50 — near-perfect accuracy
                for ship detection. The FAIR1M fine-grained vehicle classifier achieves
                0.165 mAP50 across 10 vehicle sub-categories, limited by the training
                dataset size of 1,732 images.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                What image formats are supported? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                RAVEN supports JPG, JPEG, PNG and TIFF formats — covering standard
                photography, satellite imagery, and drone capture formats. You can
                upload individual images or an entire folder at once for batch processing.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                Is my data stored? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                Detection metadata such as object count, inference time, model used and
                image size is stored in a cloud MySQL database. The actual image files
                are stored temporarily on the server. If you are logged in, your history
                is linked to your account and only visible to you.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                How long are results saved? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                Output images are automatically deleted after 48 hours to keep the server clean.
                However the detection statistics — object count, inference time, model and
                image size — remain in your history permanently so you can track your
                usage over time even after the images expire.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                Can I use RAVEN without an account? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                Yes — detection runs without an account. However your results will not
                be saved to history and you will not be able to revisit past detections.
                Creating a free account takes under 30 seconds and gives you a personal
                history with download access for 48 hours after each detection.
            </div>
        </div>

        <div class="faq-item">
            <button class="faq-q" onclick="toggleFaq(this)">
                What is DOTA Fine-grained mode? <span style="float:right;transition:0.3s;">+</span>
            </button>
            <div class="faq-a">
                DOTA Fine-grained is a two-stage detection mode. First the standard DOTA model
                detects all objects and assigns broad labels like large-vehicle or small-vehicle.
                Then for each vehicle detection, RAVEN crops that region and passes it through
                a second model trained on FAIR1M to sub-classify it as a small car, van,
                cargo truck, dump truck, bus, trailer, excavator, tractor or truck-tractor.
            </div>
        </div>

    </div>
</div>

<script>
function toggleFaq(btn) {
    var answer = btn.nextElementSibling;
    var icon = btn.querySelector('span');
    var isOpen = answer.classList.contains('show');
    document.querySelectorAll('.faq-a').forEach(function(a) {
        a.classList.remove('show');
    });
    document.querySelectorAll('.faq-q span').forEach(function(s) {
        s.textContent = '+';
        s.style.transform = 'rotate(0deg)';
    });
    if (!isOpen) {
        answer.classList.add('show');
        icon.textContent = '+';
        icon.style.transform = 'rotate(45deg)';
    }
}
</script>

{% endblock %}
'''

with open(os.path.join(BASE, "templates", "about.html"), "w", encoding="utf-8") as f:
    f.write(about)
print("about.html written with team + FAQ!")