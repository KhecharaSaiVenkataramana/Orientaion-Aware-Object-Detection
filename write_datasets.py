import os
BASE = r"C:\Users\khech\OAOD Project\website"

page = '''{% extends "layout.html" %}
{% block content %}

<!-- HERO HEADER -->
<div style="background:linear-gradient(135deg,#07051a 0%,#0d0b22 50%,#0a0820 100%);
            padding:70px 120px 50px;border-bottom:1px solid rgba(102,68,255,0.2);
            position:relative;overflow:hidden;">
    <div style="position:absolute;inset:0;opacity:0.04;
                background-image:linear-gradient(rgba(102,68,255,1) 1px,transparent 1px),
                linear-gradient(90deg,rgba(102,68,255,1) 1px,transparent 1px);
                background-size:40px 40px;"></div>
    <div style="position:relative;">
        <div style="display:inline-block;background:rgba(102,68,255,0.12);
                    border:1px solid rgba(102,68,255,0.35);color:#6644ff;
                    padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                    letter-spacing:3px;margin-bottom:18px;font-family:'Courier New',monospace;">
            TRAINING DATA
        </div>
        <h1 style="font-size:48px;font-weight:700;margin:0 0 14px;
                   background:linear-gradient(135deg,#fff 0%,#00cfff 60%,#6644ff 100%);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
            Aerial Detection Datasets
        </h1>
        <p style="font-size:17px;color:#8877cc;max-width:680px;line-height:1.7;margin:0 0 36px;">
            RAVEN is trained on three industry-standard aerial object detection datasets,
            each providing oriented bounding box annotations essential for rotation-aware detection.
        </p>
        <!-- Quick stats -->
        <div style="display:flex;gap:32px;flex-wrap:wrap;">
            <div style="background:rgba(13,11,34,0.7);border:1px solid rgba(102,68,255,0.3);
                        padding:16px 28px;border-radius:12px;text-align:center;">
                <div style="font-size:28px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">3</div>
                <div style="font-size:11px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Datasets</div>
            </div>
            <div style="background:rgba(13,11,34,0.7);border:1px solid rgba(102,68,255,0.3);
                        padding:16px 28px;border-radius:12px;text-align:center;">
                <div style="font-size:28px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">5,599</div>
                <div style="font-size:11px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Total Images</div>
            </div>
            <div style="background:rgba(13,11,34,0.7);border:1px solid rgba(102,68,255,0.3);
                        padding:16px 28px;border-radius:12px;text-align:center;">
                <div style="font-size:28px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">26</div>
                <div style="font-size:11px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Object Classes</div>
            </div>
            <div style="background:rgba(13,11,34,0.7);border:1px solid rgba(102,68,255,0.3);
                        padding:16px 28px;border-radius:12px;text-align:center;">
                <div style="font-size:28px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">OBB</div>
                <div style="font-size:11px;color:#8877cc;letter-spacing:2px;text-transform:uppercase;margin-top:4px;">Annotation Type</div>
            </div>
        </div>
    </div>
</div>

<!-- WHY OBB -->
<div style="padding:60px 120px 0;">
    <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;padding:40px;
                display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;">
        <div>
            <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                        font-family:'Courier New',monospace;margin-bottom:12px;">WHY ORIENTED BOUNDING BOXES?</div>
            <h2 style="font-size:26px;margin:0 0 16px;color:#fff;">Standard boxes fail on aerial imagery</h2>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 16px;">
                In satellite and drone imagery, objects appear at arbitrary angles. A plane on a runway,
                a ship in a harbour, or a vehicle on a curved road — none of these align neatly to
                the horizontal axis.
            </p>
            <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0;">
                Horizontal Bounding Boxes (HBB) must be oversized to contain rotated objects,
                capturing large areas of irrelevant background. Oriented Bounding Boxes (OBB)
                add a rotation angle θ, wrapping tightly around each object and dramatically
                improving detection accuracy and IoU scores.
            </p>
        </div>
        <div style="display:flex;flex-direction:column;gap:16px;">
            <div style="background:rgba(255,80,80,0.08);border:1px solid rgba(255,80,80,0.3);
                        border-radius:12px;padding:20px 24px;display:flex;align-items:center;gap:16px;">
                <div style="font-size:28px;">&#10060;</div>
                <div>
                    <div style="color:#ff5050;font-weight:600;font-size:14px;margin-bottom:4px;">HBB — Horizontal Bounding Box</div>
                    <div style="color:#8877cc;font-size:13px;line-height:1.6;">Axis-aligned rectangle. Wastes ~60-70% of box area on background. Poor IoU on rotated objects.</div>
                </div>
            </div>
            <div style="background:rgba(0,207,255,0.08);border:1px solid rgba(0,207,255,0.3);
                        border-radius:12px;padding:20px 24px;display:flex;align-items:center;gap:16px;">
                <div style="font-size:28px;">&#10004;</div>
                <div>
                    <div style="color:#00cfff;font-weight:600;font-size:14px;margin-bottom:4px;">OBB — Oriented Bounding Box</div>
                    <div style="color:#8877cc;font-size:13px;line-height:1.6;">Rotated rectangle with angle θ. Tight fit around object at any orientation. Precise IoU measurement.</div>
                </div>
            </div>
            <div style="background:rgba(102,68,255,0.08);border:1px solid rgba(102,68,255,0.3);
                        border-radius:12px;padding:16px 24px;text-align:center;">
                <span style="color:#6644ff;font-size:22px;font-weight:700;font-family:'Courier New',monospace;">8x</span>
                <span style="color:#8877cc;font-size:13px;margin-left:10px;">tighter localization with OBB vs HBB</span>
            </div>
        </div>
    </div>
</div>

<!-- ================= DOTA ================= -->
<div style="padding:60px 120px 0;">
    <div style="display:inline-block;background:rgba(0,207,255,0.1);border:1px solid rgba(0,207,255,0.3);
                color:#00cfff;padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                letter-spacing:3px;margin-bottom:24px;font-family:'Courier New',monospace;">
        DATASET 01
    </div>
    <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;overflow:hidden;">

        <!-- Header -->
        <div style="padding:36px 40px;border-bottom:1px solid rgba(102,68,255,0.15);
                    display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:20px;">
            <div>
                <h2 style="font-size:32px;margin:0 0 8px;color:#fff;">DOTA v1.0</h2>
                <p style="color:#8877cc;font-size:15px;margin:0;">Dataset for Object deTection in Aerial Images</p>
            </div>
            <div style="display:flex;gap:12px;">
                <a href="https://captain-whu.github.io/DOTA/" target="_blank"
                   style="background:linear-gradient(135deg,#6644ff,#00cfff);color:#fff;
                          padding:10px 22px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;">
                    Download Dataset
                </a>
                <a href="https://arxiv.org/abs/1711.10398" target="_blank"
                   style="border:1px solid rgba(102,68,255,0.4);color:#6644ff;
                          padding:10px 22px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;">
                    Read Paper
                </a>
            </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0;">

            <!-- Left: info -->
            <div style="padding:36px 40px;border-right:1px solid rgba(102,68,255,0.15);">
                <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 24px;">
                    DOTA is the largest and most widely used benchmark for aerial object detection.
                    Collected from Google Earth, GF-2 and JL-1 satellites, images range from
                    800×800 to 20000×20000 pixels covering diverse scenes including cities,
                    airports, harbours, and highway intersections.
                </p>
                <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 24px;">
                    Every object is annotated with an oriented bounding box (x1,y1,x2,y2,x3,y3,x4,y4)
                    — four corner points at arbitrary angles — making it the gold standard for
                    rotation-aware detection research.
                </p>

                <!-- Key stats -->
                <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-bottom:24px;">
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);
                                border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">2,806</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Total Images</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);
                                border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">188,282</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Total Instances</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);
                                border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">15</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Object Classes</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);
                                border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">0.657</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">RAVEN mAP50</div>
                    </div>
                </div>

                <div style="background:#07051a;border:1px solid rgba(102,68,255,0.15);
                            border-radius:10px;padding:16px 20px;">
                    <div style="color:#00cfff;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:10px;">ANNOTATION FORMAT</div>
                    <code style="color:#8877cc;font-size:12px;line-height:1.8;">
                        x1 y1 x2 y2 x3 y3 x4 y4 category difficult<br>
                        <span style="color:#6644ff;">116.0 305.0 298.0 304.0 298.0 340.0 116.0 341.0 plane 0</span>
                    </code>
                </div>
            </div>

            <!-- Right: classes -->
            <div style="padding:36px 40px;">
                <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                            font-family:'Courier New',monospace;margin-bottom:16px;">15 OBJECT CLASSES</div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                    {% for cls in [
                        ("Plane","#00cfff"),("Ship","#6644ff"),
                        ("Storage Tank","#00cfff"),("Baseball Diamond","#6644ff"),
                        ("Tennis Court","#00cfff"),("Basketball Court","#6644ff"),
                        ("Ground Track Field","#00cfff"),("Harbor","#6644ff"),
                        ("Bridge","#00cfff"),("Large Vehicle","#6644ff"),
                        ("Small Vehicle","#00cfff"),("Helicopter","#6644ff"),
                        ("Roundabout","#00cfff"),("Soccer Ball Field","#6644ff"),
                        ("Swimming Pool","#00cfff")
                    ] %}
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.15);
                                border-radius:8px;padding:8px 14px;display:flex;align-items:center;gap:8px;">
                        <div style="width:6px;height:6px;border-radius:50%;background:{{ cls[1] }};flex-shrink:0;"></div>
                        <span style="color:#ccc;font-size:13px;">{{ cls[0] }}</span>
                    </div>
                    {% endfor %}
                </div>

                <div style="margin-top:20px;background:#07051a;border:1px solid rgba(102,68,255,0.15);
                            border-radius:10px;padding:16px 20px;">
                    <div style="color:#00cfff;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:10px;">RAVEN TRAINING SPLIT</div>
                    <div style="display:flex;gap:16px;">
                        <div style="text-align:center;">
                            <div style="color:#00cfff;font-size:18px;font-weight:700;">1,411</div>
                            <div style="color:#8877cc;font-size:11px;">Train</div>
                        </div>
                        <div style="width:1px;background:rgba(102,68,255,0.2);"></div>
                        <div style="text-align:center;">
                            <div style="color:#6644ff;font-size:18px;font-weight:700;">458</div>
                            <div style="color:#8877cc;font-size:11px;">Validation</div>
                        </div>
                        <div style="width:1px;background:rgba(102,68,255,0.2);"></div>
                        <div style="text-align:center;">
                            <div style="color:#00cfff;font-size:18px;font-weight:700;">937</div>
                            <div style="color:#8877cc;font-size:11px;">Test</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        {% if True %}
        <div style="padding:24px 40px;background:#07051a;border-top:1px solid rgba(102,68,255,0.15);">
            <img src="{{ url_for('static', filename='ui/DOTA.png') }}"
                 style="width:100%;max-height:260px;object-fit:cover;border-radius:12px;
                        border:1px solid rgba(102,68,255,0.2);">
        </div>
        {% endif %}
    </div>
</div>

<!-- ================= HRSC ================= -->
<div style="padding:60px 120px 0;">
    <div style="display:inline-block;background:rgba(102,68,255,0.1);border:1px solid rgba(102,68,255,0.3);
                color:#6644ff;padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                letter-spacing:3px;margin-bottom:24px;font-family:'Courier New',monospace;">
        DATASET 02
    </div>
    <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;overflow:hidden;">

        <div style="padding:36px 40px;border-bottom:1px solid rgba(102,68,255,0.15);
                    display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:20px;">
            <div>
                <h2 style="font-size:32px;margin:0 0 8px;color:#fff;">HRSC2016</h2>
                <p style="color:#8877cc;font-size:15px;margin:0;">High-Resolution Ship Collections 2016</p>
            </div>
            <div style="display:flex;gap:12px;">
                <a href="https://www.kaggle.com/datasets/guofeng/hrsc2016" target="_blank"
                   style="background:linear-gradient(135deg,#6644ff,#00cfff);color:#fff;
                          padding:10px 22px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;">
                    Download Dataset
                </a>
                <a href="https://arxiv.org/abs/1702.06216" target="_blank"
                   style="border:1px solid rgba(102,68,255,0.4);color:#6644ff;
                          padding:10px 22px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;">
                    Read Paper
                </a>
            </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0;">
            <div style="padding:36px 40px;border-right:1px solid rgba(102,68,255,0.15);">
                <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 24px;">
                    HRSC2016 is the premier benchmark for oriented ship detection from
                    high-resolution optical satellite imagery. Images are collected from
                    Google Earth covering six famous harbours — including Brest in France,
                    Boston in the USA, and San Diego Naval Base.
                </p>
                <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 24px;">
                    Each ship instance is annotated with an oriented bounding box and a fine-grained
                    ship category from a 26-class taxonomy — covering aircraft carriers, destroyers,
                    submarines, container ships, fishing boats and more.
                    RAVEN fine-tuned its DOTA model on HRSC, recovering 99.7% of mAP gap.
                </p>

                <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-bottom:24px;">
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">1,061</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Total Images</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">2,976</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Ship Instances</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">26</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Ship Sub-classes</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">0.983</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">RAVEN mAP50</div>
                    </div>
                </div>

                <!-- Training result highlight -->
                <div style="background:rgba(0,207,255,0.08);border:1px solid rgba(0,207,255,0.3);
                            border-radius:12px;padding:20px 24px;">
                    <div style="color:#00cfff;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:10px;">FINE-TUNING RESULT</div>
                    <div style="display:flex;align-items:center;gap:16px;">
                        <div style="text-align:center;">
                            <div style="color:#ff5050;font-size:20px;font-weight:700;">0.009</div>
                            <div style="color:#8877cc;font-size:11px;">Before fine-tune</div>
                        </div>
                        <div style="color:#6644ff;font-size:20px;">&#8594;</div>
                        <div style="text-align:center;">
                            <div style="color:#00cfff;font-size:20px;font-weight:700;">0.983</div>
                            <div style="color:#8877cc;font-size:11px;">After fine-tune</div>
                        </div>
                        <div style="text-align:center;margin-left:8px;">
                            <div style="color:#00ff88;font-size:20px;font-weight:700;">+99.7%</div>
                            <div style="color:#8877cc;font-size:11px;">mAP gap recovered</div>
                        </div>
                    </div>
                </div>
            </div>

            <div style="padding:36px 40px;">
                <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                            font-family:'Courier New',monospace;margin-bottom:16px;">SHIP CATEGORIES (SAMPLE)</div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:20px;">
                    {% for ship in [
                        "Aircraft Carrier","Destroyer","Submarine",
                        "Container Ship","Bulk Carrier","Tanker",
                        "Fishing Boat","Patrol Boat","Tugboat",
                        "Warship","Hovercraft","Yacht",
                        "Ferry","Cargo Ship","Cruiser","Landing Ship"
                    ] %}
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.15);
                                border-radius:8px;padding:8px 14px;display:flex;align-items:center;gap:8px;">
                        <div style="width:6px;height:6px;border-radius:50%;background:#00cfff;flex-shrink:0;"></div>
                        <span style="color:#ccc;font-size:12px;">{{ ship }}</span>
                    </div>
                    {% endfor %}
                </div>

                <div style="background:#07051a;border:1px solid rgba(102,68,255,0.15);
                            border-radius:10px;padding:16px 20px;">
                    <div style="color:#00cfff;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:10px;">RAVEN TRAINING SPLIT</div>
                    <div style="display:flex;gap:16px;">
                        <div style="text-align:center;">
                            <div style="color:#00cfff;font-size:18px;font-weight:700;">750</div>
                            <div style="color:#8877cc;font-size:11px;">Train</div>
                        </div>
                        <div style="width:1px;background:rgba(102,68,255,0.2);"></div>
                        <div style="text-align:center;">
                            <div style="color:#6644ff;font-size:18px;font-weight:700;">124</div>
                            <div style="color:#8877cc;font-size:11px;">Validation</div>
                        </div>
                        <div style="width:1px;background:rgba(102,68,255,0.2);"></div>
                        <div style="text-align:center;">
                            <div style="color:#00cfff;font-size:18px;font-weight:700;">187</div>
                            <div style="color:#8877cc;font-size:11px;">Test</div>
                        </div>
                    </div>
                </div>

                <div style="margin-top:16px;background:#07051a;border:1px solid rgba(102,68,255,0.15);
                            border-radius:10px;padding:16px 20px;">
                    <div style="color:#00cfff;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:8px;">IMAGE RESOLUTION</div>
                    <div style="color:#8877cc;font-size:13px;line-height:1.6;">
                        300 &times; 300 to 1500 &times; 900 pixels<br>
                        Ground resolution: 0.4m &mdash; 2.0m per pixel<br>
                        Source: Google Earth optical imagery
                    </div>
                </div>
            </div>
        </div>

        <div style="padding:24px 40px;background:#07051a;border-top:1px solid rgba(102,68,255,0.15);">
            <img src="{{ url_for('static', filename='ui/HRSC.png') }}"
                 style="width:100%;max-height:260px;object-fit:cover;border-radius:12px;
                        border:1px solid rgba(102,68,255,0.2);">
        </div>
    </div>
</div>

<!-- ================= FAIR1M ================= -->
<div style="padding:60px 120px 80px;">
    <div style="display:inline-block;background:rgba(102,68,255,0.1);border:1px solid rgba(102,68,255,0.3);
                color:#6644ff;padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                letter-spacing:3px;margin-bottom:24px;font-family:'Courier New',monospace;">
        DATASET 03
    </div>
    <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;overflow:hidden;">

        <div style="padding:36px 40px;border-bottom:1px solid rgba(102,68,255,0.15);
                    display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:20px;">
            <div>
                <h2 style="font-size:32px;margin:0 0 8px;color:#fff;">FAIR1M</h2>
                <p style="color:#8877cc;font-size:15px;margin:0;">Fine-grained Aircraft and Vehicle Recognition Dataset</p>
            </div>
            <div style="display:flex;gap:12px;">
                <a href="https://www.gaofen-challenge.com" target="_blank"
                   style="background:linear-gradient(135deg,#6644ff,#00cfff);color:#fff;
                          padding:10px 22px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;">
                    Request Access
                </a>
                <a href="https://arxiv.org/abs/2103.05569" target="_blank"
                   style="border:1px solid rgba(102,68,255,0.4);color:#6644ff;
                          padding:10px 22px;border-radius:8px;font-size:13px;font-weight:600;text-decoration:none;">
                    Read Paper
                </a>
            </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0;">
            <div style="padding:36px 40px;border-right:1px solid rgba(102,68,255,0.15);">
                <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 24px;">
                    FAIR1M is a fine-grained aerial recognition dataset specifically designed
                    for vehicle and aircraft sub-classification. Unlike DOTA which uses broad
                    categories like "large-vehicle", FAIR1M provides 37 sub-categories —
                    distinguishing between small cars, vans, cargo trucks, dump trucks,
                    buses, trailers, excavators, tractors and more.
                </p>
                <p style="color:#8877cc;line-height:1.8;font-size:15px;margin:0 0 24px;">
                    RAVEN uses FAIR1M as a secondary classifier in the DOTA Fine-grained
                    detection mode — when DOTA detects a vehicle region, that crop is passed
                    to the FAIR1M model for precise sub-classification.
                    The full dataset (15,000 images) requires registration at gaofen-challenge.com.
                    RAVEN was trained on the publicly available 1,732-image subset.
                </p>

                <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-bottom:24px;">
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">1,732</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Available Images</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">72,453</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Vehicle Annotations</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#00cfff;font-family:'Courier New',monospace;">10</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">Vehicle Sub-classes</div>
                    </div>
                    <div style="background:#07051a;border:1px solid rgba(102,68,255,0.2);border-radius:10px;padding:14px 18px;">
                        <div style="font-size:22px;font-weight:700;color:#6644ff;font-family:'Courier New',monospace;">0.165</div>
                        <div style="font-size:12px;color:#8877cc;margin-top:3px;">RAVEN mAP50</div>
                    </div>
                </div>

                <!-- Training progression -->
                <div style="background:#07051a;border:1px solid rgba(102,68,255,0.15);
                            border-radius:10px;padding:16px 20px;">
                    <div style="color:#00cfff;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:12px;">TRAINING PROGRESSION</div>
                    {% for v, map, desc in [
                        ("v1","0.022","20 epochs, imgsz=480, batch=4"),
                        ("v2","0.042","62 epochs, cos_lr, cls=1.0"),
                        ("v3","0.108","Fresh yolov8s-obb, 34 epochs"),
                        ("v4","0.165","Fine-tuned from v3, 164 epochs")
                    ] %}
                    <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
                        <span style="background:rgba(102,68,255,0.2);color:#6644ff;padding:2px 8px;
                                     border-radius:4px;font-size:11px;font-family:'Courier New',monospace;
                                     min-width:24px;text-align:center;">{{ v }}</span>
                        <div style="flex:1;background:rgba(102,68,255,0.1);border-radius:4px;height:6px;overflow:hidden;">
                            <div style="background:linear-gradient(90deg,#6644ff,#00cfff);height:100%;
                                        width:{{ (map|float / 0.165 * 100)|int }}%;border-radius:4px;"></div>
                        </div>
                        <span style="color:#00cfff;font-size:13px;font-weight:700;
                                     font-family:'Courier New',monospace;min-width:40px;">{{ map }}</span>
                        <span style="color:#8877cc;font-size:11px;">{{ desc }}</span>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <div style="padding:36px 40px;">
                <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                            font-family:'Courier New',monospace;margin-bottom:16px;">10 VEHICLE SUB-CLASSES</div>
                {% set classes = [
                    ("Small Car","32,887","#00cfff"),
                    ("Van","29,973","#6644ff"),
                    ("Dump Truck","4,618","#00cfff"),
                    ("Cargo Truck","2,671","#6644ff"),
                    ("Other Vehicle","1,259","#00cfff"),
                    ("Bus","309","#6644ff"),
                    ("Excavator","240","#00cfff"),
                    ("Trailer","216","#6644ff"),
                    ("Truck Tractor","213","#00cfff"),
                    ("Tractor","67","#6644ff")
                ] %}
                {% for name, count, color in classes %}
                <div style="margin-bottom:10px;">
                    <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                        <span style="color:#ccc;font-size:13px;">{{ name }}</span>
                        <span style="color:{{ color }};font-size:12px;font-family:'Courier New',monospace;">{{ count }}</span>
                    </div>
                    <div style="background:rgba(102,68,255,0.1);border-radius:4px;height:5px;overflow:hidden;">
                        <div style="background:{{ color }};height:100%;opacity:0.8;
                                    width:{{ ([count|replace(",","")|int / 32887 * 100, 100]|min)|int }}%;
                                    border-radius:4px;"></div>
                    </div>
                </div>
                {% endfor %}

                <div style="margin-top:20px;background:rgba(186,117,23,0.1);
                            border:1px solid rgba(186,117,23,0.35);border-radius:10px;padding:16px 20px;">
                    <div style="color:#ef9f27;font-size:12px;font-weight:700;letter-spacing:2px;
                                font-family:'Courier New',monospace;margin-bottom:8px;">DATASET LIMITATION</div>
                    <p style="color:#8877cc;font-size:13px;line-height:1.6;margin:0;">
                        The publicly available subset contains only 1,732 of the full 15,000 images.
                        The full dataset requires official registration at gaofen-challenge.com.
                        Training on the full dataset would push mAP50 from 0.165 to an estimated 0.35-0.50+.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock %}
'''

with open(os.path.join(BASE, "templates", "datasets.html"), "w", encoding="utf-8") as f:
    f.write(page)
print("datasets.html written!")
print("Lines:", len(page.split('\n')))