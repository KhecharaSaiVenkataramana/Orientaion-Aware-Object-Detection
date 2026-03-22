import os
BASE = r"C:\Users\khech\OAOD Project\website"

home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

old = "\n{% endblock %}"

new = '''
<!-- HOW TO DETECT -->
<div style="padding:80px 120px 0;background:var(--bg-deep);">
    <div style="text-align:center;margin-bottom:56px;">
        <div style="display:inline-block;background:rgba(102,68,255,0.12);
                    border:1px solid rgba(102,68,255,0.35);color:#6644ff;
                    padding:5px 16px;border-radius:30px;font-size:11px;font-weight:700;
                    letter-spacing:3px;margin-bottom:18px;font-family:'Courier New',monospace;">
            HOW IT WORKS
        </div>
        <h2 style="font-size:38px;font-weight:700;margin:0 0 14px;color:#fff;">
            Start detecting in 3 steps
        </h2>
        <p style="color:#8877cc;font-size:16px;max-width:520px;margin:0 auto;line-height:1.7;">
            Upload your aerial imagery, choose a detection model, and get annotated results in seconds.
        </p>
    </div>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px;position:relative;">

        <!-- Connector line -->
        <div style="position:absolute;top:40px;left:calc(16.66% + 20px);right:calc(16.66% + 20px);
                    height:1px;background:linear-gradient(90deg,#6644ff,#00cfff,#6644ff);
                    opacity:0.3;z-index:0;"></div>

        <!-- Step 1 -->
        <div class="reveal reveal-delay-1"
             style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;
                    padding:36px 32px;text-align:center;position:relative;z-index:1;
                    transition:transform 0.3s,border-color 0.3s,box-shadow 0.3s;"
             onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.boxShadow='0 20px 40px rgba(102,68,255,0.2)'"
             onmouseout="this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:28px;font-weight:700;color:#fff;
                        margin:0 auto 24px;
                        box-shadow:0 0 24px rgba(102,68,255,0.5);">1</div>
            <h3 style="font-size:20px;margin:0 0 12px;color:#fff;">Upload Imagery</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Upload a single aerial or satellite image, or select an entire folder
                for batch processing. Supports JPG, PNG and TIFF formats.
            </p>
            <div style="margin-top:20px;padding:10px 16px;background:rgba(102,68,255,0.08);
                        border:1px solid rgba(102,68,255,0.2);border-radius:8px;">
                <span style="color:#6644ff;font-size:12px;font-family:'Courier New',monospace;
                             letter-spacing:1px;">JPG &bull; PNG &bull; TIFF &bull; Folder Upload</span>
            </div>
        </div>

        <!-- Step 2 -->
        <div class="reveal reveal-delay-2"
             style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;
                    padding:36px 32px;text-align:center;position:relative;z-index:1;
                    transition:transform 0.3s,border-color 0.3s,box-shadow 0.3s;"
             onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='#00cfff';this.style.boxShadow='0 20px 40px rgba(0,207,255,0.15)'"
             onmouseout="this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#00cfff,#6644ff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:28px;font-weight:700;color:#fff;
                        margin:0 auto 24px;
                        box-shadow:0 0 24px rgba(0,207,255,0.4);">2</div>
            <h3 style="font-size:20px;margin:0 0 12px;color:#fff;">Choose Model</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Select from 4 detection modes — Standard YOLOv8, DOTA-OBB for aerial objects,
                HRSC-OBB for ships, or DOTA Fine-grained for vehicle sub-classification.
            </p>
            <div style="margin-top:20px;display:flex;flex-direction:column;gap:6px;">
                {% for mode, color in [
                    ("Standard YOLOv8","#8877cc"),
                    ("DOTA-OBB","#00cfff"),
                    ("HRSC-OBB","#6644ff"),
                    ("DOTA Fine-grained","#00cfff")
                ] %}
                <div style="padding:6px 12px;background:rgba(102,68,255,0.06);
                            border:1px solid rgba(102,68,255,0.15);border-radius:6px;
                            color:{{ color }};font-size:12px;font-family:'Courier New',monospace;">
                    {{ mode }}
                </div>
                {% endfor %}
            </div>
        </div>

        <!-- Step 3 -->
        <div class="reveal reveal-delay-3"
             style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;
                    padding:36px 32px;text-align:center;position:relative;z-index:1;
                    transition:transform 0.3s,border-color 0.3s,box-shadow 0.3s;"
             onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.boxShadow='0 20px 40px rgba(102,68,255,0.2)'"
             onmouseout="this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);
                        display:flex;align-items:center;justify-content:center;
                        font-size:28px;font-weight:700;color:#fff;
                        margin:0 auto 24px;
                        box-shadow:0 0 24px rgba(102,68,255,0.5);">3</div>
            <h3 style="font-size:20px;margin:0 0 12px;color:#fff;">Download Results</h3>
            <p style="color:#8877cc;font-size:14px;line-height:1.7;margin:0;">
                Get annotated output images with oriented bounding boxes drawn.
                Download individually, as a ZIP, or export a full PDF report with CSV data.
            </p>
            <div style="margin-top:20px;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;">
                {% for fmt in ["Annotated PNG","PDF Report","CSV Export","ZIP Archive"] %}
                <span style="padding:5px 10px;background:rgba(0,207,255,0.08);
                             border:1px solid rgba(0,207,255,0.2);border-radius:6px;
                             color:#00cfff;font-size:11px;font-family:'Courier New',monospace;">
                    {{ fmt }}
                </span>
                {% endfor %}
            </div>
        </div>

    </div>
</div>

<!-- CTA BOTTOM BANNER -->
<div style="margin:80px 120px;background:linear-gradient(135deg,rgba(102,68,255,0.15) 0%,
            rgba(0,207,255,0.08) 100%);border:1px solid rgba(102,68,255,0.3);
            border-radius:24px;padding:60px 80px;
            display:flex;align-items:center;justify-content:space-between;
            flex-wrap:wrap;gap:32px;position:relative;overflow:hidden;">

    <!-- Background glow -->
    <div style="position:absolute;top:-40px;right:-40px;width:300px;height:300px;
                background:radial-gradient(circle,rgba(102,68,255,0.15) 0%,transparent 70%);
                pointer-events:none;"></div>
    <div style="position:absolute;bottom:-40px;left:200px;width:200px;height:200px;
                background:radial-gradient(circle,rgba(0,207,255,0.1) 0%,transparent 70%);
                pointer-events:none;"></div>

    <div style="position:relative;">
        <div style="display:inline-block;background:rgba(102,68,255,0.15);
                    border:1px solid rgba(102,68,255,0.4);color:#6644ff;
                    padding:4px 14px;border-radius:30px;font-size:10px;font-weight:700;
                    letter-spacing:3px;margin-bottom:16px;font-family:'Courier New',monospace;">
            GET STARTED
        </div>
        <h2 style="font-size:36px;font-weight:700;margin:0 0 12px;
                   background:linear-gradient(135deg,#fff 0%,#00cfff 100%);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                   background-clip:text;">
            Ready to detect?
        </h2>
        <p style="color:#8877cc;font-size:16px;max-width:480px;line-height:1.7;margin:0;">
            Upload your first aerial image and see RAVEN's oriented object detection
            in action. No setup required — detection runs instantly in your browser.
        </p>
    </div>

    <div style="display:flex;flex-direction:column;gap:14px;position:relative;">
        <a href="/detection"
           style="display:inline-block;background:linear-gradient(135deg,#6644ff,#00cfff);
                  color:#fff;padding:16px 40px;border-radius:12px;font-size:16px;
                  font-weight:700;text-decoration:none;letter-spacing:0.5px;
                  text-align:center;transition:0.25s;
                  box-shadow:0 8px 30px rgba(102,68,255,0.4);"
           onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 14px 40px rgba(102,68,255,0.6)'"
           onmouseout="this.style.transform='none';this.style.boxShadow='0 8px 30px rgba(102,68,255,0.4)'">
            Start Detection &rarr;
        </a>
        <a href="/register"
           style="display:inline-block;border:1px solid rgba(102,68,255,0.4);
                  color:#8877cc;padding:12px 40px;border-radius:12px;font-size:14px;
                  text-decoration:none;text-align:center;transition:0.25s;"
           onmouseover="this.style.borderColor='#00cfff';this.style.color='#00cfff'"
           onmouseout="this.style.borderColor='rgba(102,68,255,0.4)';this.style.color='#8877cc'">
            Create Free Account
        </a>
        <div style="text-align:center;color:#555;font-size:12px;">
            No credit card &bull; Free forever
        </div>
    </div>
</div>

{% endblock %}'''

home = home.replace("\n{% endblock %}", new)

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)
print("Done! Added How to Detect + CTA section")
print("Restart: python app.py")