import os
BASE = r"C:\Users\khech\OAOD Project\website"

css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

if "/* Light mode inline overrides */" not in css:
    css += '''
/* Light mode inline overrides — fixes hardcoded dark colors in templates */
body.light-mode [style*="background:#0d0b22"],
body.light-mode [style*="background: #0d0b22"] { background: #fff !important; }

body.light-mode [style*="background:#07051a"],
body.light-mode [style*="background: #07051a"] { background: #f0f2f8 !important; }

body.light-mode [style*="background:#0a0820"],
body.light-mode [style*="background: #0a0820"] { background: #e8eaf4 !important; }

body.light-mode [style*="background:#03020c"],
body.light-mode [style*="background: #03020c"] { background: #f0f2f8 !important; }

body.light-mode [style*="background:linear-gradient(135deg,#07051a"],
body.light-mode [style*="background: linear-gradient(135deg,#07051a"],
body.light-mode [style*="background:linear-gradient(135deg, #07051a"] {
    background: linear-gradient(135deg,#eef0fb 0%,#f4f5ff 50%,#eef2ff 100%) !important;
}

body.light-mode [style*="background:linear-gradient(135deg,#0d0b22"],
body.light-mode [style*="background: linear-gradient(135deg,#0d0b22"] {
    background: linear-gradient(135deg,#f4f5ff 0%,#eef0fb 100%) !important;
}

/* Text colors */
body.light-mode [style*="color:#8877cc"] { color: #666 !important; }
body.light-mode [style*="color: #8877cc"] { color: #666 !important; }
body.light-mode [style*="color:#fff"] { color: #1a1a2e !important; }
body.light-mode [style*="color: #fff;"] { color: #1a1a2e !important; }
body.light-mode [style*="color:white"] { color: #1a1a2e !important; }
body.light-mode [style*="color:#ccc"] { color: #444 !important; }
body.light-mode [style*="color: #ccc"] { color: #444 !important; }
body.light-mode [style*="color:#aaa"] { color: #555 !important; }

/* Border colors */
body.light-mode [style*="border:1px solid rgba(102,68,255,0.2)"] {
    border-color: rgba(102,68,255,0.2) !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
body.light-mode [style*="border-bottom:1px solid rgba(102,68,255,0.2)"] {
    border-bottom-color: rgba(102,68,255,0.15) !important;
}

/* Team cards specifically */
body.light-mode [style*="border-radius:16px"][style*="padding:30px"],
body.light-mode [style*="border-radius:16px"][style*="padding:28px"],
body.light-mode [style*="border-radius:16px"][style*="padding:32px"] {
    background: #fff !important;
    box-shadow: 0 2px 16px rgba(0,0,0,0.08) !important;
}

/* Avatar circles — keep gradient */
body.light-mode [style*="border-radius:50%"][style*="background:linear-gradient"] {
    color: #fff !important;
}

/* Section labels */
body.light-mode [style*="color:#6644ff"] { color: #5533dd !important; }
body.light-mode [style*="color: #6644ff"] { color: #5533dd !important; }
body.light-mode [style*="color:#00cfff"] { color: #0099cc !important; }
body.light-mode [style*="color: #00cfff"] { color: #0099cc !important; }

/* Monospace labels */
body.light-mode [style*="font-family:'Courier New'"][style*="color:#6644ff"] {
    color: #5533dd !important;
}
body.light-mode [style*="font-family:'Courier New'"][style*="color:#00cfff"] {
    color: #0099cc !important;
}

/* Cards with dark inline backgrounds in about/discuss */
body.light-mode div[style*="background:rgba(13,11,34"] {
    background: rgba(255,255,255,0.95) !important;
    border-color: rgba(102,68,255,0.15) !important;
}
body.light-mode div[style*="background:#0d0b22"] {
    background: #fff !important;
}
body.light-mode div[style*="background:#07051a"] {
    background: #f4f5ff !important;
}

/* Warning/amber boxes */
body.light-mode [style*="background:rgba(186,117,23"] {
    background: rgba(186,117,23,0.08) !important;
}

/* Stats bar */
body.light-mode [style*="background:var(--bg-dark)"] {
    background: #e8eaf4 !important;
}

/* Discuss/About hero gradient */
body.light-mode [style*="background:linear-gradient(135deg,#07051a 0%,#0d0b22"] {
    background: linear-gradient(135deg,#eef0fb 0%,#f4f5ff 50%,#eef2ff 100%) !important;
}

/* Grid lines background pattern */
body.light-mode [style*="rgba(102,68,255,1) 1px,transparent 1px"] {
    opacity: 0.02 !important;
}

/* FAQ buttons in light mode */
body.light-mode .faq-q { color: #1a1a2e !important; }
body.light-mode .suggestion-tile { background: #fff !important; }

/* Code blocks */
body.light-mode code { color: #444 !important; }
body.light-mode [style*="background:#050310"] { background: #f0f0ff !important; }

/* Navbar brand text */
body.light-mode .brand-name,
body.light-mode [style*="color:#00cfff"][style*="letter-spacing:6px"] {
    color: #5533dd !important;
}
body.light-mode [style*="color:#6644ffaa"] { color: #9988cc !important; }

/* Hero gradient text in light mode */
body.light-mode .hero-text h1 {
    background: linear-gradient(135deg,#1a1a2e 0%,#5533dd 60%,#0099cc 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

/* Scroll progress stays coloured */
body.light-mode #scroll-progress {
    background: linear-gradient(90deg, #6644ff, #00cfff) !important;
}

/* Nav active in light */
body.light-mode .nav-links a.active { color: #6644ff !important; }
body.light-mode .nav-links a.active::after { background: linear-gradient(90deg,#6644ff,#00cfff) !important; }

/* Hero stat in light */
body.light-mode .hero-stat { background: rgba(255,255,255,0.92) !important; color: #1a1a2e !important; }
body.light-mode .hero-stat-val { color: #5533dd !important; }
body.light-mode .hero-stat-lbl { color: #888 !important; }

/* Loading overlay stays dark */
body.light-mode #loading-overlay { background: rgba(3,2,12,0.97) !important; }
'''

    with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    print("Light mode overrides added!")
else:
    print("Already exists — updating...")
    import re
    css = re.sub(
        r'/\* Light mode inline overrides.*',
        '',
        css,
        flags=re.DOTALL
    )
    with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    print("Cleared old overrides — re-run this script!")