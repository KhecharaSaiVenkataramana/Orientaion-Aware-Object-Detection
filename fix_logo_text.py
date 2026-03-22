layout = open("templates/layout.html", encoding="utf-8").read()

old = '''        <a href="/" style="display:flex;align-items:center;gap:14px;text-decoration:none;">
            <img src="{{ url_for('static', filename='ui/logo.png') }}"
                 style="height:78px;width:78px;border-radius:12px;object-fit:cover;
                        border:2px solid #6644ff88;
                        box-shadow:0 0 18px rgba(102,68,255,0.5),0 0 6px rgba(0,207,255,0.3);">
            <div style="display:flex;flex-direction:column;line-height:1.1;">
                <span style="font-family:'Courier New',monospace;font-size:22px;font-weight:700;
                             letter-spacing:6px;color:#00cfff;">RAVEN</span>
                <span style="font-size:10px;color:#6644ffaa;letter-spacing:2.5px;
                             font-family:'Courier New',monospace;">DETECTION THAT NEVER BLINKS</span>
            </div>
        </a>'''

new = '''        <a href="/" style="display:flex;align-items:center;text-decoration:none;position:relative;height:78px;">
            <!-- RAVEN text behind logo -->
            <span style="font-family:'Courier New',monospace;font-size:36px;font-weight:900;
                         letter-spacing:10px;color:#00cfff;opacity:0.15;
                         position:absolute;left:0;top:50%;transform:translateY(-50%);
                         z-index:0;white-space:nowrap;">RAVEN</span>
            <!-- Logo on top -->
            <img src="{{ url_for('static', filename='ui/logo.png') }}"
                 style="height:74px;width:74px;border-radius:10px;object-fit:cover;
                        position:relative;z-index:1;
                        filter:drop-shadow(0 0 12px rgba(0,207,255,0.5));
                        margin-right:8px;">
            <!-- RAVEN text visible -->
            <div style="display:flex;flex-direction:column;line-height:1.1;position:relative;z-index:1;">
                <span style="font-family:'Courier New',monospace;font-size:22px;font-weight:700;
                             letter-spacing:6px;color:#00cfff;">RAVEN</span>
                <span style="font-size:10px;color:#6644ffaa;letter-spacing:2.5px;
                             font-family:'Courier New',monospace;">DETECTION THAT NEVER BLINKS</span>
            </div>
        </a>'''

if old in layout:
    layout = layout.replace(old, new)
    with open("templates/layout.html", "w", encoding="utf-8") as f:
        f.write(layout)
    print("Done!")
else:
    print("Not found — check layout.html logo block")