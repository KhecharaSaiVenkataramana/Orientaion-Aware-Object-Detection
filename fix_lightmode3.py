import os
BASE = r"C:\Users\khech\OAOD Project\website"

css = open(os.path.join(BASE, "static", "style.css"), encoding="utf-8").read()

css += '''
/* ── Light mode step cards + hover fixes ── */

/* Step cards background section */
body.light-mode [style*="padding:80px 120px 0;background:var(--bg-deep)"],
body.light-mode [style*="padding:80px 120px 0; background:var(--bg-deep)"] {
    background: #f0f2f8 !important;
}

/* "How it works" heading */
body.light-mode [style*="font-size:38px"][style*="color:#fff"] {
    color: #1a1a2e !important;
}
body.light-mode [style*="font-size:38px"][style*="color: #fff"] {
    color: #1a1a2e !important;
}

/* Step cards — white in light mode, no dark hover */
body.light-mode [style*="background:#0d0b22"][style*="border-radius:20px"],
body.light-mode [style*="background: #0d0b22"][style*="border-radius:20px"] {
    background: #fff !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
}

/* Prevent onmouseover from going dark in light mode */
body.light-mode div[onmouseover*="translateY"] {
    transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s !important;
}
body.light-mode div[onmouseover*="0d0b25"] {
    background: #fff !important;
}

/* Step card inner chips/tags */
body.light-mode [style*="background:rgba(102,68,255,0.08)"][style*="border-radius:8px"],
body.light-mode [style*="background:rgba(102,68,255,0.06)"][style*="border-radius:6px"] {
    background: rgba(102,68,255,0.06) !important;
    color: #5533dd !important;
}
body.light-mode [style*="background:rgba(0,207,255,0.08)"][style*="border-radius:6px"] {
    background: rgba(0,207,255,0.06) !important;
    color: #0088bb !important;
}

/* CTA bottom banner */
body.light-mode [style*="margin:80px 120px"][style*="background:linear-gradient"] {
    background: linear-gradient(135deg,rgba(102,68,255,0.07) 0%,rgba(0,207,255,0.04) 100%) !important;
    border-color: rgba(102,68,255,0.2) !important;
}

/* CTA text */
body.light-mode [style*="color:#8877cc"][style*="font-size:16px"] {
    color: #555 !important;
}

/* "No credit card" small text */
body.light-mode [style*="color:#555"][style*="font-size:12px"] {
    color: #888 !important;
}

/* HOW IT WORKS badge */
body.light-mode [style*="background:rgba(102,68,255,0.12)"][style*="border-radius:30px"] {
    background: rgba(102,68,255,0.08) !important;
}

/* Connector line between steps */
body.light-mode [style*="background:linear-gradient(90deg,#6644ff,#00cfff,#6644ff)"] {
    opacity: 0.2 !important;
}

/* Fix feature card dark hover in light mode */
body.light-mode .feature-card:hover {
    background: #fff !important;
    transform: translateY(-10px);
    border-color: #6644ff !important;
    box-shadow: 0 20px 40px rgba(102,68,255,0.12) !important;
}

/* Fix compare-card hover in light */
body.light-mode .compare-card:hover {
    background: #fff !important;
    border-color: rgba(102,68,255,0.3) !important;
}

/* Fix perf table row hover */
body.light-mode .perf-table tr:hover td {
    background: #f5f5ff !important;
}

/* Fix dataset card hover */
body.light-mode .dataset-card:hover {
    background: #fff !important;
}

/* Fix card hover */
body.light-mode .card:hover {
    background: #fff !important;
}

/* Section with dark bg that contains step cards */
body.light-mode section,
body.light-mode .features {
    background: #f0f2f8 !important;
}

/* Fix the "How it works" dark section wrapper */
body.light-mode div[style*="background:var(--bg-deep)"] {
    background: #f0f2f8 !important;
}
body.light-mode div[style*="background: var(--bg-deep)"] {
    background: #f0f2f8 !important;
}
'''

with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("Done! Restart: python app.py")