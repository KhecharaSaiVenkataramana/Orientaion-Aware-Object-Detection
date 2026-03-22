import os
BASE = r"C:\Users\khech\OAOD Project\website"

# ── STYLE.CSS ─────────────────────────────────────────────────
css = '''/* ===== RAVEN GLOBAL ===== */
:root {
    --cyan:        #00cfff;
    --purple:      #6644ff;
    --purple-dark: #3311aa;
    --bg-deep:     #03020c;
    --bg-dark:     #07051a;
    --bg-card:     #0d0b22;
    --bg-panel:    #0a0820;
    --border:      rgba(102,68,255,0.2);
    --border-hover:#6644ff;
    --text-muted:  #8877cc;
}

/* ── PAGE FADE-IN ── */
@keyframes pageFadeIn {
    from { opacity:0; transform:translateY(12px); }
    to   { opacity:1; transform:translateY(0); }
}
body {
    margin: 0;
    font-family: "Segoe UI", Arial, sans-serif;
    background: var(--bg-deep);
    color: white;
    padding-top: 78px;
    animation: pageFadeIn 0.5s ease both;
}
a { text-decoration: none; }

/* ── SCROLL REVEAL ── */
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}
.reveal.visible {
    opacity: 1;
    transform: translateY(0);
}
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
.reveal-delay-4 { transition-delay: 0.4s; }

/* ===== NAVBAR ===== */
.navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 90px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 70px;
    background: rgba(3,2,12,0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    z-index: 1000;
    box-shadow: 0 1px 0 rgba(102,68,255,0.2), 0 4px 30px rgba(0,0,0,0.5);
    transition: background 0.3s, box-shadow 0.3s;
}
.navbar.scrolled {
    background: rgba(3,2,12,0.97);
    box-shadow: 0 1px 0 rgba(102,68,255,0.35), 0 8px 40px rgba(0,0,0,0.8);
}

.logo { display:flex; align-items:center; gap:14px; }
.logo img {
    height:78px; width:78px;
    border-radius:50%; object-fit:cover;
    border:2px solid #6644ff88;
    box-shadow: 0 0 18px rgba(102,68,255,0.5), 0 0 6px rgba(0,207,255,0.3);
    transition: transform 0.3s, box-shadow 0.3s;
}
.logo img:hover {
    transform: scale(1.08) rotate(3deg);
    box-shadow: 0 0 28px rgba(102,68,255,0.8), 0 0 12px rgba(0,207,255,0.5);
}

.brand-name {
    font-family: 'Courier New', monospace;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 6px;
    color: var(--cyan);
}

.nav-links { display:flex; gap:32px; }
.nav-links a {
    color: #aaa;
    font-size: 15px;
    font-weight: 500;
    letter-spacing: 1px;
    transition: color 0.2s;
    position: relative;
    padding-bottom: 4px;
}
.nav-links a::after {
    content: '';
    position: absolute;
    bottom: -4px; left: 0;
    width: 0; height: 2px;
    background: linear-gradient(90deg, var(--purple), var(--cyan));
    transition: width 0.3s cubic-bezier(0.4,0,0.2,1);
    border-radius: 2px;
}
.nav-links a:hover { color: var(--cyan); }
.nav-links a:hover::after { width: 100%; }
.nav-links a.active { color: var(--cyan); }
.nav-links a.active::after { width: 100%; }

/* ===== HERO ===== */
.hero {
    height: 680px;
    background: url('/static/ui/aerial.jpg') center/cover no-repeat;
    display: flex;
    align-items: center;
    padding: 0 120px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: linear-gradient(to right,
        rgba(3,2,12,0.95) 0%,
        rgba(3,2,12,0.75) 45%,
        rgba(3,2,12,0.2) 100%);
}
/* Animated scan line across hero */
.hero::after {
    content: "";
    position: absolute;
    top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg,
        transparent 0%,
        rgba(102,68,255,0.04) 50%,
        transparent 100%);
    animation: heroScan 6s ease-in-out infinite;
}
@keyframes heroScan {
    0%   { left: -60%; }
    100% { left: 120%; }
}

.hero-text {
    position: relative;
    max-width: 640px;
    animation: pageFadeIn 0.8s ease 0.2s both;
}

.hero-badge {
    display: inline-block;
    background: rgba(102,68,255,0.15);
    border: 1px solid rgba(102,68,255,0.4);
    color: var(--purple);
    padding: 5px 16px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 22px;
    font-family: 'Courier New', monospace;
    animation: badgePulse 3s ease-in-out infinite;
}
@keyframes badgePulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(102,68,255,0.3); }
    50%      { box-shadow: 0 0 0 6px rgba(102,68,255,0); }
}

.hero-text h1 {
    font-size: 54px;
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 22px;
    background: linear-gradient(135deg, #ffffff 0%, var(--cyan) 60%, var(--purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    background-size: 200% 200%;
    animation: gradientShift 6s ease infinite;
}
@keyframes gradientShift {
    0%,100% { background-position: 0% 50%; }
    50%      { background-position: 100% 50%; }
}

.hero-text p {
    font-size: 17px;
    color: #9988cc;
    line-height: 1.7;
    margin-bottom: 10px;
}

.hero-buttons { margin-top: 32px; display:flex; gap:14px; }

/* ── HERO STATS ── */
.hero-stats {
    position: absolute;
    bottom: 40px;
    right: 120px;
    display: flex;
    gap: 32px;
    animation: pageFadeIn 0.8s ease 0.6s both;
}
.hero-stat {
    text-align: center;
    background: rgba(13,11,34,0.7);
    border: 1px solid rgba(102,68,255,0.3);
    padding: 16px 24px;
    border-radius: 12px;
    backdrop-filter: blur(8px);
    transition: transform 0.3s, border-color 0.3s;
}
.hero-stat:hover {
    transform: translateY(-4px);
    border-color: var(--cyan);
}
.hero-stat-val {
    font-size: 28px;
    font-weight: 700;
    font-family: 'Courier New', monospace;
    color: var(--cyan);
    display: block;
}
.hero-stat-lbl {
    font-size: 11px;
    color: var(--text-muted);
    letter-spacing: 1px;
    margin-top: 4px;
    display: block;
}

/* ===== BUTTONS ===== */
.btn-primary {
    background: linear-gradient(135deg, var(--purple), var(--cyan));
    background-size: 200% 200%;
    padding: 13px 28px;
    border-radius: 8px;
    color: white;
    font-weight: 600;
    font-size: 15px;
    transition: 0.25s;
    border: none;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}
.btn-primary::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    transition: left 0.5s;
}
.btn-primary:hover::before { left: 100%; }
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(102,68,255,0.5);
    background-position: right center;
}
.btn-primary:active { transform: translateY(0) scale(0.97); }

.btn-secondary {
    border: 1px solid rgba(102,68,255,0.5);
    padding: 13px 28px;
    border-radius: 8px;
    color: #aaa;
    font-size: 15px;
    transition: 0.25s;
    position: relative;
    overflow: hidden;
}
.btn-secondary:hover {
    border-color: var(--cyan);
    color: var(--cyan);
    background: rgba(0,207,255,0.05);
}

/* ===== FEATURES ===== */
.features {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 24px;
    padding: 70px 100px;
}

.feature-card {
    background: var(--bg-card);
    padding: 32px 26px;
    border-radius: 16px;
    border: 1px solid var(--border);
    transition: transform 0.35s cubic-bezier(0.4,0,0.2,1),
                border-color 0.35s, box-shadow 0.35s;
    position: relative;
    overflow: hidden;
}
.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--purple), var(--cyan));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.35s ease;
}
.feature-card:hover {
    transform: translateY(-10px);
    border-color: var(--purple);
    box-shadow: 0 20px 40px rgba(102,68,255,0.2), 0 0 0 1px rgba(102,68,255,0.1);
}
.feature-card:hover::before { transform: scaleX(1); }

.feature-icon {
    font-size: 28px;
    margin-bottom: 16px;
    display: block;
    transition: transform 0.3s;
}
.feature-card:hover .feature-icon { transform: scale(1.2) rotate(-5deg); }

.feature-card h3 { font-size: 18px; margin-bottom: 10px; color: white; }
.feature-card p  { color: var(--text-muted); font-size: 14px; line-height: 1.6; margin-bottom: 18px; }
.feature-link    { color: var(--cyan); font-size: 13px; font-weight: 600; letter-spacing: 0.5px; transition: letter-spacing 0.2s; }
.feature-card:hover .feature-link { letter-spacing: 1.5px; }

/* ===== PAGE HEADER ===== */
.page-header {
    background: var(--bg-dark);
    padding: 60px 120px;
    border-bottom: 1px solid var(--border);
}
.page-header h1 { font-size: 38px; margin-bottom: 10px; }
.page-header p  { color: var(--text-muted); }

/* ===== CARDS ===== */
.card {
    background: var(--bg-card);
    padding: 28px;
    border-radius: 14px;
    margin: 40px 120px;
    border: 1px solid var(--border);
    transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    border-color: var(--purple);
    box-shadow: 0 12px 35px rgba(102,68,255,0.15);
}

/* ===== DETECTION WORKSPACE ===== */
.detect-layout {
    display: grid;
    grid-template-columns: 550px 1fr;
    min-height: calc(100vh - 90px);
}

.control-panel {
    background: var(--bg-dark);
    padding: 60px 45px;
    border-right: 1px solid var(--border);
}
.control-panel h1 { font-size: 36px; margin-bottom: 28px; color: #fff; }

.section-title {
    display: block;
    margin-top: 25px;
    margin-bottom: 8px;
    font-size: 14px;
    color: var(--text-muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    font-weight: 600;
}

.file-input, .dropdown {
    width: 100%;
    padding: 12px 14px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    color: white;
    font-size: 15px;
    transition: border-color 0.2s, box-shadow 0.2s;
    box-sizing: border-box;
}
.file-input:focus, .dropdown:focus {
    outline: none;
    border-color: var(--purple);
    box-shadow: 0 0 0 3px rgba(102,68,255,0.15);
}
.dropdown:hover { border-color: rgba(102,68,255,0.5); }

.slider { width:100%; margin-top:10px; accent-color: var(--purple); }
.slider-value { margin-top:6px; color:var(--cyan); font-size:15px; }
.slider-help { font-size:13px; color:var(--text-muted); margin-top:5px; }

.run-btn {
    margin-top: 30px;
    width: 100%;
    padding: 15px;
    background: linear-gradient(135deg, var(--purple), var(--cyan));
    background-size: 200% 200%;
    border: none;
    border-radius: 12px;
    color: white;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 1px;
    transition: 0.25s;
    position: relative;
    overflow: hidden;
}
.run-btn::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent);
    transition: left 0.5s;
}
.run-btn:hover::before { left: 100%; }
.run-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 35px rgba(102,68,255,0.5);
}
.run-btn:active { transform: translateY(0) scale(0.98); }

.viewer-panel {
    background: var(--bg-deep);
    padding: 40px 50px;
    overflow-y: auto;
}
.viewer-title { font-size: 36px; margin-bottom: 30px; }

.empty-state { height:70vh; display:flex; align-items:center; justify-content:center; }
.empty-content { text-align:center; max-width:520px; }
.empty-illustration { width:400px; opacity:0.7; margin-bottom:18px; transition: opacity 0.3s, transform 0.3s; }
.empty-illustration:hover { opacity:0.9; transform: scale(1.03); }
.empty-content h2 { font-size:26px; margin-bottom:8px; }
.empty-content p  { color:var(--text-muted); font-size:18px; margin-bottom:18px; }
.formats { font-size:13px; color:#555; }

/* IMAGE GRID */
.grid-view { display:flex; flex-direction:column; gap:40px; }
.compare-card {
    background: var(--bg-card);
    padding: 25px;
    border-radius: 16px;
    border: 1px solid var(--border);
    display: flex;
    gap: 30px;
    transition: border-color 0.3s, box-shadow 0.3s;
    animation: pageFadeIn 0.5s ease both;
}
.compare-card:hover {
    border-color: rgba(102,68,255,0.4);
    box-shadow: 0 8px 30px rgba(102,68,255,0.1);
}
.img-box { width:50%; display:flex; flex-direction:column; }
.img-box h3 { font-size:16px; margin-bottom:10px; color:var(--cyan); letter-spacing:1px; }
.img-box img {
    width:100%; height:420px;
    object-fit:contain;
    background:#000;
    border-radius:12px;
    border: 1px solid var(--border);
    padding:12px;
}

/* PERFORMANCE TABLE */
.results-section { margin-top:35px; }
.results-section h2 { font-size:24px; margin-bottom:18px; }
.perf-table {
    width:100%; border-collapse:collapse;
    background:var(--bg-card);
    border-radius:14px; overflow:hidden;
}
.perf-table th {
    background:var(--bg-panel);
    padding:16px; font-size:13px;
    text-align:left; color:var(--cyan);
    letter-spacing:1px;
}
.perf-table td {
    padding:14px 16px; font-size:14px;
    border-top:1px solid var(--border);
    transition: background 0.2s;
}
.perf-table td:nth-child(n+2) { text-align:center; font-weight:500; }
.perf-table tr:hover td { background:#0d0b28; }

.summary-box {
    margin-top: 20px;
    display: flex;
    justify-content: space-around;
    background: var(--bg-panel);
    padding: 22px;
    border-radius: 14px;
    border: 1px solid var(--border);
}
.summary-box p { font-size:16px; }
.summary-box b { color:var(--cyan); font-size:18px; }

/* ZOOM */
.zoom-container { position:relative; overflow:hidden; border-radius:12px; }
.zoom-image {
    width:100%; height:420px;
    object-fit:contain;
    background:#000;
    transition: transform 0.08s ease-out;
    cursor:crosshair;
}
.zoom-lens {
    position:absolute;
    width:140px; height:140px;
    border:2px solid var(--purple);
    background:rgba(102,68,255,0.08);
    display:none;
    pointer-events:none;
    border-radius:4px;
    box-shadow: 0 0 15px rgba(102,68,255,0.3);
}

/* DATASET PAGE */
.dataset-card {
    display:flex; gap:40px;
    background:var(--bg-card);
    margin:50px 120px;
    padding:35px;
    border-radius:18px;
    border:1px solid var(--border);
    transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
}
.dataset-card:hover {
    transform:translateY(-6px);
    border-color:var(--purple);
    box-shadow:0 20px 40px rgba(102,68,255,0.15);
}
.dataset-img img { width:420px; height:260px; object-fit:cover; border-radius:14px; }
.dataset-info h2 { font-size:26px; margin-bottom:12px; }
.dataset-info p  { color:var(--text-muted); margin-bottom:18px; line-height:1.6; }
.dataset-specs { display:grid; grid-template-columns:repeat(2,1fr); gap:12px; margin-bottom:20px; color:#ccc; }
.dataset-buttons a { margin-right:12px; }

/* HISTORY TABLE */
.perf-table th { color:var(--cyan); }

/* SECTION BADGE */
.section-badge {
    display:inline-block;
    background:rgba(102,68,255,0.12);
    color:var(--purple);
    padding:5px 14px;
    border-radius:30px;
    font-size:11px;
    font-weight:800;
    margin-bottom:18px;
    letter-spacing:2px;
    border:1px solid rgba(102,68,255,0.3);
}

/* FAQ */
.faq-q {
    width:100%; text-align:left;
    padding:18px 22px;
    background:var(--bg-panel);
    border:1px solid var(--border);
    color:white; font-weight:600;
    cursor:pointer; border-radius:10px;
    margin-top:12px; transition:0.25s;
    font-size:15px;
}
.faq-q:hover { border-color:var(--purple); background:var(--bg-card); box-shadow: 0 4px 15px rgba(102,68,255,0.15); }
.faq-a {
    display:none;
    padding:20px 24px;
    background:var(--bg-card);
    border-radius:0 0 10px 10px;
    color:var(--text-muted);
    border:1px solid var(--border);
    border-top:none;
    line-height:1.7;
}
.faq-a.show { display:block; animation: pageFadeIn 0.3s ease both; }

/* STEP */
.step { background:var(--bg-panel); padding:8px 12px; border-radius:8px; font-size:15px; color:#ccc; }
.step span { background:var(--purple); color:white; padding:2px 7px; border-radius:50%; margin-right:6px; font-weight:600; }

/* INFO BOX */
.info-box { background:var(--bg-dark); padding:25px; border-radius:15px; border-left:4px solid var(--purple); }
.spec-list { list-style:none; padding:0; margin-top:20px; }
.spec-list li { padding:12px 0; border-bottom:1px solid var(--border); transition: padding-left 0.2s; }
.spec-list li:hover { padding-left: 8px; }
.spec-list li b { color:var(--cyan); margin-right:10px; }

/* TUTORIAL */
.tutorial-container { margin:60px 120px; }
.tutorial-step { display:flex; gap:30px; margin-bottom:60px; }
.step-number {
    min-width:60px; height:60px; border-radius:50%;
    background:linear-gradient(135deg,var(--purple),var(--cyan));
    color:white; font-size:24px;
    display:flex; align-items:center; justify-content:center;
    font-weight:bold;
    box-shadow: 0 0 20px rgba(102,68,255,0.4);
}
.step-content { background:var(--bg-card); padding:30px; border-radius:14px; flex:1; border:1px solid var(--border); }
.tip { margin-top:15px; padding:12px; background:#052e16; border-left:4px solid #22c55e; }
.warning { margin-top:15px; padding:12px; background:#2e1a05; border-left:4px solid #f59e0b; }
.tutorial-note { margin:20px 120px; padding:14px; background:var(--bg-dark); border-left:4px solid var(--purple); color:#ccc; }

/* ── GLOW PULSE on key elements ── */
@keyframes glowPulse {
    0%,100% { box-shadow: 0 0 10px rgba(102,68,255,0.3); }
    50%      { box-shadow: 0 0 25px rgba(102,68,255,0.6), 0 0 8px rgba(0,207,255,0.3); }
}

/* ── CURSOR TRAIL (handled in JS) ── */
.cursor-dot {
    position: fixed;
    width: 6px; height: 6px;
    background: var(--cyan);
    border-radius: 50%;
    pointer-events: none;
    z-index: 99999;
    transform: translate(-50%,-50%);
    transition: opacity 0.3s;
    opacity: 0;
    box-shadow: 0 0 8px var(--cyan);
}

/* ── SCROLL PROGRESS BAR ── */
#scroll-progress {
    position: fixed;
    top: 90px; left: 0;
    height: 2px;
    width: 0%;
    background: linear-gradient(90deg, var(--purple), var(--cyan));
    z-index: 999;
    transition: width 0.1s linear;
}
'''

# ── LAYOUT.HTML ───────────────────────────────────────────────
layout = '''\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }} | RAVEN</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <style>
        .nav-auth { display:flex; align-items:center; gap:12px; margin-left:auto; }
        .nav-auth a { color:#aaa; text-decoration:none; font-size:14px; transition:color 0.2s; }
        .nav-auth a:hover { color:#00cfff; }
        .nav-user { color:#00cfff; font-size:14px; font-weight:500; }
        .btn-logout {
            background: transparent;
            border: 1px solid #6644ff55;
            color: #aaa; padding: 4px 12px;
            border-radius: 20px; font-size: 13px;
            cursor: pointer; text-decoration: none;
            transition: 0.2s;
        }
        .btn-logout:hover { border-color:#00cfff; color:#00cfff; background:rgba(0,207,255,0.05); }

        /* ── LOADING OVERLAY ── */
        #loading-overlay {
            display: none; position: fixed; inset: 0;
            background: rgba(3,2,12,0.97); z-index: 9999;
            align-items: center; justify-content: center;
            flex-direction: column; gap: 28px;
        }
        #loading-overlay.active { display: flex; }
        .orbit-ring { position:relative; width:160px; height:160px; }
        .orbit-path { position:absolute; inset:0; border-radius:50%; border:1.5px dashed #6644ff44; }
        .satellite-dot {
            position:absolute; top:50%; left:50%;
            width:160px; height:160px; margin:-80px 0 0 -80px;
            animation:orbit 2.2s linear infinite; transform-origin:center;
        }
        .satellite-dot::after {
            content:''; position:absolute; top:-6px; left:50%;
            transform:translateX(-50%); width:12px; height:12px;
            background:#00cfff; border-radius:50%;
            box-shadow:0 0 10px #00cfff,0 0 20px #6644ff88;
        }
        @keyframes orbit{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
        .orbit-planet {
            position:absolute; top:50%; left:50%;
            transform:translate(-50%,-50%); width:52px; height:52px;
            border-radius:50%; background:radial-gradient(circle at 35% 35%,#3311aa,#0a0520);
            overflow:hidden;
        }
        .orbit-planet::after {
            content:''; position:absolute; top:30%; left:10%;
            width:45%; height:18%; background:#00cfff22;
            border-radius:50%; transform:rotate(-20deg);
        }
        .scan-line { position:absolute; inset:0; border-radius:50%; overflow:hidden; }
        .scan-line::before {
            content:''; position:absolute; top:0; left:50%;
            width:50%; height:100%;
            background:conic-gradient(from 0deg,transparent 70%,#6644ff22 100%);
            animation:scan 2.2s linear infinite; transform-origin:left center;
        }
        @keyframes scan{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
        .signal-rings { position:absolute; inset:0; border-radius:50%; }
        .signal-ring {
            position:absolute; border-radius:50%; border:1px solid #6644ff;
            top:50%; left:50%; transform:translate(-50%,-50%) scale(0);
            opacity:0; animation:pulse-ring 2.2s ease-out infinite;
        }
        .signal-ring:nth-child(1){width:70px;height:70px;animation-delay:0s}
        .signal-ring:nth-child(2){width:100px;height:100px;animation-delay:0.6s}
        .signal-ring:nth-child(3){width:130px;height:130px;animation-delay:1.2s}
        @keyframes pulse-ring{0%{transform:translate(-50%,-50%) scale(0.3);opacity:0.8}100%{transform:translate(-50%,-50%) scale(1.1);opacity:0}}
        .loading-title { color:#00cfff; font-size:18px; font-weight:600; letter-spacing:4px; text-transform:uppercase; font-family:'Courier New',monospace; }
        .loading-status { color:#6644ff99; font-size:13px; letter-spacing:1px; animation:blink 1.2s ease-in-out infinite; font-family:'Courier New',monospace; }
        @keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}
        .loading-dots { display:flex; gap:8px; align-items:center; }
        .loading-dots span { width:6px; height:6px; border-radius:50%; background:#6644ff; animation:dot-bounce 1.4s ease-in-out infinite; }
        .loading-dots span:nth-child(2){animation-delay:0.2s}
        .loading-dots span:nth-child(3){animation-delay:0.4s}
        @keyframes dot-bounce{0%,80%,100%{transform:scale(0.6);opacity:0.4}40%{transform:scale(1.2);opacity:1}}
    </style>
</head>
<body>

<!-- SCROLL PROGRESS BAR -->
<div id="scroll-progress"></div>

<!-- CURSOR DOT -->
<div class="cursor-dot" id="cursor-dot"></div>

<!-- LOADING OVERLAY -->
<div id="loading-overlay">
    <div class="orbit-ring">
        <div class="orbit-path"></div>
        <div class="scan-line"></div>
        <div class="signal-rings">
            <div class="signal-ring"></div>
            <div class="signal-ring"></div>
            <div class="signal-ring"></div>
        </div>
        <div class="orbit-planet"></div>
        <div class="satellite-dot"></div>
    </div>
    <div class="loading-title">RAVEN Scanning</div>
    <div class="loading-dots"><span></span><span></span><span></span></div>
    <div class="loading-status" id="loading-status">Initialising detection model...</div>
</div>

<div class="navbar" id="main-navbar">
    <div class="logo">
        <a href="/" style="display:flex;align-items:center;gap:14px;text-decoration:none;">
            <img src="{{ url_for('static', filename='ui/logo.png') }}"
                 style="height:78px;width:78px;border-radius:50%;object-fit:cover;
                        border:2px solid #6644ff88;
                        box-shadow:0 0 18px rgba(102,68,255,0.5),0 0 6px rgba(0,207,255,0.3);">
            <div style="display:flex;flex-direction:column;line-height:1.1;">
                <span style="font-family:'Courier New',monospace;font-size:22px;font-weight:700;
                             letter-spacing:6px;color:#00cfff;">RAVEN</span>
                <span style="font-size:10px;color:#6644ffaa;letter-spacing:2.5px;
                             font-family:'Courier New',monospace;">DETECTION THAT NEVER BLINKS</span>
            </div>
        </a>
    </div>
    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/detection">Detection</a>
        <a href="/datasets">Datasets</a>
        <a href="/about">About</a>
        <a href="/history">History</a>
        <a href="/discuss">Discuss</a>
    </div>
    <div class="nav-auth">
        {% if session.get('username') %}
            <a href="/profile" class="nav-user">&#128113; {{ session['username'] }}</a>
            <a href="/logout" class="btn-logout">Logout</a>
        {% else %}
            <a href="/login">Login</a>
            <a href="/register" style="background:linear-gradient(135deg,#6644ff,#00cfff);color:#fff;padding:6px 16px;border-radius:20px;font-size:13px;text-decoration:none;font-weight:600;transition:0.2s;">Register</a>
        {% endif %}
    </div>
</div>

{% block content %}{% endblock %}

<script>
// ── ACTIVE NAV LINK ──────────────────────────────────────────
(function() {
    var path = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(function(a) {
        var href = a.getAttribute('href');
        if (href === path || (href !== '/' && path.startsWith(href))) {
            a.classList.add('active');
        }
    });
})();

// ── NAVBAR SCROLL EFFECT ─────────────────────────────────────
window.addEventListener('scroll', function() {
    var nb = document.getElementById('main-navbar');
    if (window.scrollY > 40) nb.classList.add('scrolled');
    else nb.classList.remove('scrolled');

    // Scroll progress bar
    var sp = document.getElementById('scroll-progress');
    if (sp) {
        var pct = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
        sp.style.width = Math.min(pct, 100) + '%';
    }
});

// ── CURSOR DOT ───────────────────────────────────────────────
(function() {
    var dot = document.getElementById('cursor-dot');
    if (!dot) return;
    var mx = 0, my = 0;
    document.addEventListener('mousemove', function(e) {
        mx = e.clientX; my = e.clientY;
        dot.style.opacity = '1';
        dot.style.left = mx + 'px';
        dot.style.top  = my + 'px';
    });
    document.addEventListener('mouseleave', function() { dot.style.opacity = '0'; });
})();

// ── SCROLL REVEAL ────────────────────────────────────────────
(function() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    var obs = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
            if (e.isIntersecting) {
                e.target.classList.add('visible');
                obs.unobserve(e.target);
            }
        });
    }, { threshold: 0.12 });
    els.forEach(function(el) { obs.observe(el); });
})();

// ── LOADING OVERLAY ──────────────────────────────────────────
var overlay  = document.getElementById('loading-overlay');
var statusEl = document.getElementById('loading-status');
var messages = [
    "Initialising detection model...",
    "Loading aerial imagery...",
    "Running inference engine...",
    "Processing oriented bounding boxes...",
    "Analysing object density...",
    "Saving results to cloud...",
    "Almost done..."
];
var msgIndex = 0, msgTimer = null;
function startLoading() {
    overlay.classList.add('active');
    msgIndex = 0;
    statusEl.textContent = messages[0];
    msgTimer = setInterval(function() {
        msgIndex = (msgIndex + 1) % messages.length;
        statusEl.textContent = messages[msgIndex];
    }, 2000);
}
document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('.control-panel form');
    if (form) { form.addEventListener('submit', function() { startLoading(); }); }
});

// ── ZOOM ─────────────────────────────────────────────────────
document.querySelectorAll(".zoom-container").forEach(function(container) {
    var img  = container.querySelector(".zoom-image");
    var lens = container.querySelector(".zoom-lens");
    container.addEventListener("mousemove", function(e) {
        var rect = container.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        lens.style.display = "block";
        lens.style.left = (x - lens.offsetWidth/2)  + "px";
        lens.style.top  = (y - lens.offsetHeight/2) + "px";
        img.style.transformOrigin = (x/rect.width*100) + "% " + (y/rect.height*100) + "%";
        img.style.transform = "scale(2.5)";
    });
    container.addEventListener("mouseleave", function() {
        lens.style.display  = "none";
        img.style.transform = "scale(1)";
    });
});

// ── BUTTON RIPPLE ────────────────────────────────────────────
document.addEventListener('click', function(e) {
    var btn = e.target.closest('.btn-primary, .run-btn');
    if (!btn) return;
    var circle = document.createElement('span');
    var d = Math.max(btn.clientWidth, btn.clientHeight);
    var rect = btn.getBoundingClientRect();
    circle.style.cssText = 'position:absolute;border-radius:50%;background:rgba(255,255,255,0.25);' +
        'width:' + d + 'px;height:' + d + 'px;' +
        'left:' + (e.clientX - rect.left - d/2) + 'px;' +
        'top:'  + (e.clientY - rect.top  - d/2) + 'px;' +
        'transform:scale(0);animation:ripple 0.6s linear;pointer-events:none;';
    if (!document.getElementById('ripple-style')) {
        var st = document.createElement('style');
        st.id = 'ripple-style';
        st.textContent = '@keyframes ripple{to{transform:scale(4);opacity:0}}';
        document.head.appendChild(st);
    }
    btn.style.position = 'relative';
    btn.style.overflow = 'hidden';
    btn.appendChild(circle);
    setTimeout(function() { circle.remove(); }, 700);
});
</script>
</body>
</html>
'''

with open(os.path.join(BASE, "static", "style.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("style.css written!")

with open(os.path.join(BASE, "templates", "layout.html"), "w", encoding="utf-8") as f:
    f.write(layout)
print("layout.html written!")
print("\nAnimations added:")
print("  - Page fade-in on load")
print("  - Scroll reveal (.reveal class)")
print("  - Active nav link highlight")
print("  - Navbar darkens on scroll")
print("  - Scroll progress bar at top")
print("  - Cyan cursor dot")
print("  - Hero animated scan line + gradient shift")
print("  - Hero stats panel")
print("  - Shimmer effect on buttons")
print("  - Button ripple on click")
print("  - Feature cards: top border slide + icon bounce")
print("  - Feature link letter-spacing on hover")
print("  - FAQ answers fade in")
print("  - Logo spin+glow on hover")