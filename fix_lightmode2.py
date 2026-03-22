import os
BASE = r"C:\Users\khech\OAOD Project\website"

css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

css += '''
/* ── Light mode text fixes ── */

/* Large gradient headings in light mode — make them dark and readable */
body.light-mode [style*="-webkit-text-fill-color:transparent"],
body.light-mode [style*="-webkit-text-fill-color: transparent"] {
    -webkit-text-fill-color: transparent !important;
    background: linear-gradient(135deg, #1a1a2e 0%, #5533dd 60%, #0099cc 100%) !important;
    -webkit-background-clip: text !important;
    background-clip: text !important;
}

/* Specifically fix "Talk to the team" and similar large headings */
body.light-mode h1[style*="font-size:52px"],
body.light-mode h1[style*="font-size: 52px"],
body.light-mode h1[style*="font-size:48px"],
body.light-mode h1[style*="font-size: 48px"] {
    -webkit-text-fill-color: transparent !important;
    background: linear-gradient(135deg, #1a1a2e 0%, #5533dd 50%, #0099cc 100%) !important;
    -webkit-background-clip: text !important;
    background-clip: text !important;
    opacity: 1 !important;
}

/* Section h2 headings */
body.light-mode h2[style*="color:#fff"],
body.light-mode h2[style*="color: #fff"] {
    color: #1a1a2e !important;
}

/* Any remaining white text in light mode */
body.light-mode p[style*="color:#8877cc"],
body.light-mode p[style*="color: #8877cc"] {
    color: #555 !important;
}

/* Navbar brand in light */
body.light-mode span[style*="color:#00cfff"][style*="letter-spacing:6px"] {
    color: #4422ee !important;
}
body.light-mode span[style*="color:#6644ffaa"] {
    color: #8866cc !important;
}

/* Register button stays colorful */
body.light-mode a[style*="background:linear-gradient(135deg,#6644ff,#00cfff)"] {
    color: #fff !important;
}

/* Hero h1 specifically */
body.light-mode .hero-text h1 {
    background: linear-gradient(135deg, #0d0d2b 0%, #5533dd 55%, #0088bb 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

/* "Start detecting in 3 steps" heading */
body.light-mode h2[style*="color:#fff"],
body.light-mode h2[style*="color: #fff;"] {
    color: #1a1a2e !important;
}

/* "Ready to detect?" CTA heading */
body.light-mode h2[style*="-webkit-text-fill-color:transparent"],
body.light-mode h2[style*="-webkit-text-fill-color: transparent"] {
    background: linear-gradient(135deg, #1a1a2e 0%, #5533dd 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}

/* CTA banner background in light */
body.light-mode [style*="background:linear-gradient(135deg,rgba(102,68,255,0.15)"] {
    background: linear-gradient(135deg, rgba(102,68,255,0.08) 0%, rgba(0,207,255,0.05) 100%) !important;
    border-color: rgba(102,68,255,0.2) !important;
}

/* Step number circles stay gradient */
body.light-mode [style*="background:linear-gradient(135deg,#6644ff,#00cfff)"][style*="border-radius:50%"] {
    color: #fff !important;
}

/* Feature link color */
body.light-mode .feature-link { color: #5533dd !important; }

/* Stat bar in light */
body.light-mode [style*="color:#00cfff"][style*="font-size:36px"] {
    color: #5533dd !important;
}
body.light-mode [style*="color:#6644ff"][style*="font-size:36px"] {
    color: #0088bb !important;
}
'''

with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("Done! Light mode text fixes applied.")
print("Restart: python app.py")