import os
BASE = r"C:\Users\khech\OAOD Project\website"

# ── 1. ADD LIGHT MODE CSS TO style.css ────────────────────────
css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

if "light-mode" not in css:
    css += '''
/* ===== LIGHT MODE ===== */
body.light-mode {
    background: #f0f2f8;
    color: #1a1a2e;
}
body.light-mode .navbar {
    background: rgba(240,242,248,0.92);
    box-shadow: 0 1px 0 rgba(102,68,255,0.15), 0 4px 20px rgba(0,0,0,0.08);
}
body.light-mode .navbar.scrolled {
    background: rgba(235,237,248,0.98);
}
body.light-mode .nav-links a { color: #444; }
body.light-mode .nav-links a:hover { color: #6644ff; }
body.light-mode .nav-links a.active { color: #6644ff; }
body.light-mode .nav-auth a { color: #555; }
body.light-mode .nav-user { color: #6644ff; }

body.light-mode .hero::before {
    background: linear-gradient(to right,
        rgba(240,242,248,0.95) 0%,
        rgba(240,242,248,0.75) 45%,
        rgba(240,242,248,0.1) 100%);
}
body.light-mode .hero-text h1 {
    background: linear-gradient(135deg,#1a1a2e 0%,#6644ff 60%,#00cfff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
body.light-mode .hero-text p { color: #555; }
body.light-mode .hero-stat {
    background: rgba(255,255,255,0.9);
    border-color: rgba(102,68,255,0.3);
}
body.light-mode .hero-stat-val { color: #6644ff; }
body.light-mode .hero-stat-lbl { color: #888; }

body.light-mode .feature-card {
    background: #fff;
    border-color: rgba(102,68,255,0.15);
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
body.light-mode .feature-card h3 { color: #1a1a2e; }
body.light-mode .feature-card p { color: #666; }
body.light-mode .feature-icon-wrap {
    background: rgba(102,68,255,0.08);
    border-color: rgba(102,68,255,0.2);
}

body.light-mode .control-panel {
    background: #e8eaf4;
    border-right-color: rgba(102,68,255,0.15);
}
body.light-mode .control-panel h1 { color: #1a1a2e; }
body.light-mode .section-title { color: #666; }
body.light-mode .file-input,
body.light-mode .dropdown {
    background: #fff;
    border-color: rgba(102,68,255,0.2);
    color: #1a1a2e;
}
body.light-mode .viewer-panel { background: #f0f2f8; }
body.light-mode .viewer-title { color: #1a1a2e; }

body.light-mode .compare-card {
    background: #fff;
    border-color: rgba(102,68,255,0.15);
}
body.light-mode .img-box h3 { color: #6644ff; }
body.light-mode .zoom-image { background: #eee; }

body.light-mode .perf-table { background: #fff; }
body.light-mode .perf-table th {
    background: #e8eaf4;
    color: #6644ff;
}
body.light-mode .perf-table td {
    color: #333;
    border-top-color: rgba(102,68,255,0.1);
}
body.light-mode .perf-table tr:hover td { background: #f5f5ff; }
body.light-mode .summary-box {
    background: #e8eaf4;
    border-color: rgba(102,68,255,0.15);
}
body.light-mode .summary-box p { color: #333; }

body.light-mode .empty-state { background: #f0f2f8; }
body.light-mode .empty-content h2 { color: #1a1a2e; }
body.light-mode .empty-content p { color: #666; }

body.light-mode .results-section h2 { color: #1a1a2e; }
body.light-mode .faq-q {
    background: #e8eaf4;
    border-color: rgba(102,68,255,0.15);
    color: #1a1a2e;
}
body.light-mode .faq-a {
    background: #fff;
    border-color: rgba(102,68,255,0.1);
    color: #555;
}
body.light-mode .card {
    background: #fff;
    border-color: rgba(102,68,255,0.15);
}
body.light-mode .dataset-card {
    background: #fff;
    border-color: rgba(102,68,255,0.15);
}
body.light-mode #scroll-progress {
    background: linear-gradient(90deg, #6644ff, #00cfff);
}
body.light-mode .btn-logout {
    border-color: rgba(102,68,255,0.3);
    color: #666;
}
body.light-mode .loading-title { color: #6644ff; }

/* Toggle switch styles */
.theme-toggle-wrap {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: 8px;
}
.theme-icon {
    font-size: 14px;
    transition: opacity 0.3s, transform 0.3s;
    user-select: none;
}
.toggle-switch {
    position: relative;
    width: 52px;
    height: 28px;
    cursor: pointer;
    flex-shrink: 0;
}
.toggle-switch input {
    opacity: 0;
    width: 0;
    height: 0;
    position: absolute;
}
.toggle-track {
    position: absolute;
    inset: 0;
    border-radius: 28px;
    background: linear-gradient(135deg, #6644ff, #3311aa);
    border: 1px solid rgba(102,68,255,0.5);
    transition: background 0.4s, border-color 0.4s;
    overflow: hidden;
}
.toggle-track::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg,
        rgba(255,255,255,0.06) 0%,
        transparent 60%);
}
/* Stars in dark mode */
.toggle-track::after {
    content: "";
    position: absolute;
    top: 5px; right: 6px;
    width: 3px; height: 3px;
    background: white;
    border-radius: 50%;
    box-shadow: -5px 3px 0 0 white, -9px 0px 0 0 rgba(255,255,255,0.6);
    transition: opacity 0.3s;
    opacity: 0.7;
}
.toggle-knob {
    position: absolute;
    top: 3px;
    left: 3px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: linear-gradient(135deg, #fff 0%, #e0e8ff 100%);
    box-shadow: 0 2px 8px rgba(0,0,0,0.4), 0 0 0 1px rgba(255,255,255,0.1);
    transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1),
                background 0.4s;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
}
/* Checked = light mode */
.toggle-switch input:checked ~ .toggle-track {
    background: linear-gradient(135deg, #87ceeb, #f0c040);
    border-color: rgba(240,192,64,0.5);
}
.toggle-switch input:checked ~ .toggle-track::after {
    opacity: 0;
}
.toggle-switch input:checked ~ .toggle-knob {
    transform: translateX(24px);
    background: linear-gradient(135deg, #fff9e0 0%, #ffe88a 100%);
    box-shadow: 0 2px 8px rgba(240,192,64,0.5), 0 0 12px rgba(255,220,0,0.3);
}
/* Glow ring on hover */
.toggle-switch:hover .toggle-track {
    box-shadow: 0 0 12px rgba(102,68,255,0.4);
}
.toggle-switch input:checked:hover ~ .toggle-track {
    box-shadow: 0 0 12px rgba(240,192,64,0.5);
}
'''
    with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    print("Light mode CSS added!")
else:
    print("Light mode CSS already exists")

# ── 2. ADD TOGGLE TO NAVBAR in layout.html ─────────────────────
layout = open(os.path.join(BASE, "templates", "layout.html"), encoding="utf-8").read()

if "theme-toggle" not in layout:
    old_auth = '''    <div class="nav-auth">
        {% if session.get('username') %}
            <a href="/profile" class="nav-user">&#128113; {{ session['username'] }}</a>
            <a href="/logout" class="btn-logout">Logout</a>
        {% else %}
            <a href="/login">Login</a>
            <a href="/register" style="background:linear-gradient(135deg,#6644ff,#00cfff);color:#fff;padding:6px 16px;border-radius:20px;font-size:13px;text-decoration:none;font-weight:600;transition:0.2s;">Register</a>
        {% endif %}
    </div>'''

    new_auth = '''    <div class="nav-auth">
        {% if session.get('username') %}
            <a href="/profile" class="nav-user">&#128113; {{ session['username'] }}</a>
            <a href="/logout" class="btn-logout">Logout</a>
        {% else %}
            <a href="/login">Login</a>
            <a href="/register" style="background:linear-gradient(135deg,#6644ff,#00cfff);color:#fff;padding:6px 16px;border-radius:20px;font-size:13px;text-decoration:none;font-weight:600;transition:0.2s;">Register</a>
        {% endif %}

        <!-- THEME TOGGLE -->
        <div class="theme-toggle-wrap" title="Toggle light/dark mode">
            <span class="theme-icon" id="icon-moon">&#127769;</span>
            <label class="toggle-switch">
                <input type="checkbox" id="theme-toggle">
                <div class="toggle-track"></div>
                <div class="toggle-knob" id="toggle-knob">&#127769;</div>
            </label>
            <span class="theme-icon" id="icon-sun">&#9728;&#65039;</span>
        </div>
    </div>'''

    layout = layout.replace(old_auth, new_auth)
    print("Toggle added to navbar!")
else:
    print("Toggle already in navbar")

# ── 3. ADD TOGGLE JS before </script> ──────────────────────────
old_js_end = '''// ── BUTTON RIPPLE ────────────────────────────────────────────'''

new_js = '''// ── THEME TOGGLE ─────────────────────────────────────────────
(function() {
    var toggle = document.getElementById('theme-toggle');
    var knob   = document.getElementById('toggle-knob');
    if (!toggle) return;

    // Load saved preference
    var saved = localStorage.getItem('raven-theme');
    if (saved === 'light') {
        document.body.classList.add('light-mode');
        toggle.checked = true;
        if (knob) knob.textContent = '\\u2600\\uFE0F';
    } else {
        if (knob) knob.textContent = '\\u{1F319}';
    }

    toggle.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('light-mode');
            localStorage.setItem('raven-theme', 'light');
            if (knob) knob.textContent = '\\u2600\\uFE0F';
        } else {
            document.body.classList.remove('light-mode');
            localStorage.setItem('raven-theme', 'dark');
            if (knob) knob.textContent = '\\u{1F319}';
        }
    });
})();

// ── BUTTON RIPPLE ─────────────────────────────────────────────'''

if old_js_end in layout:
    layout = layout.replace(old_js_end, new_js)
    print("Toggle JS added!")
else:
    print("JS anchor not found — appending before </script>")
    layout = layout.replace('</script>\n</body>', new_js + '\n</script>\n</body>')

with open(os.path.join(BASE, "templates", "layout.html"), "w", encoding="utf-8") as f:
    f.write(layout)
print("layout.html saved!")
print("\nDone! Restart: python app.py")