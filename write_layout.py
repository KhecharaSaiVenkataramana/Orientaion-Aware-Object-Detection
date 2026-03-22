import os

template = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }} | OA-YOLO</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <style>
        .nav-auth { display:flex; align-items:center; gap:12px; margin-left:auto; }
        .nav-auth a { color:#aaa; text-decoration:none; font-size:14px; }
        .nav-auth a:hover { color:#00cfff; }
        .nav-user { color:#00cfff; font-size:14px; font-weight:500; }
        .btn-logout {
            background: transparent;
            border: 1px solid #444;
            color: #aaa;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 13px;
            cursor: pointer;
            text-decoration: none;
        }
        .btn-logout:hover { border-color:#00cfff; color:#00cfff; }

        /* ── LOADING OVERLAY ─────────────────────────────────── */
        #loading-overlay {
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(5, 5, 20, 0.92);
            z-index: 9999;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 28px;
        }
        #loading-overlay.active {
            display: flex;
        }

        /* Orbit ring */
        .orbit-ring {
            position: relative;
            width: 160px;
            height: 160px;
        }
        .orbit-path {
            position: absolute;
            inset: 0;
            border-radius: 50%;
            border: 1.5px dashed #00cfff44;
        }
        /* Satellite dot orbiting */
        .satellite-dot {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 160px;
            height: 160px;
            margin: -80px 0 0 -80px;
            animation: orbit 2.2s linear infinite;
            transform-origin: center center;
        }
        .satellite-dot::after {
            content: '';
            position: absolute;
            top: -6px;
            left: 50%;
            transform: translateX(-50%);
            width: 12px;
            height: 12px;
            background: #00cfff;
            border-radius: 50%;
            box-shadow: 0 0 10px #00cfff, 0 0 20px #00cfff88;
        }
        @keyframes orbit {
            from { transform: rotate(0deg); }
            to   { transform: rotate(360deg); }
        }

        /* Earth / planet in center */
        .orbit-planet {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 52px;
            height: 52px;
            border-radius: 50%;
            background: radial-gradient(circle at 35% 35%, #1a6b8a, #0a2a3a);
            box-shadow: 0 0 20px #00cfff33, inset -6px -6px 12px rgba(0,0,0,0.5);
            overflow: hidden;
        }
        .orbit-planet::after {
            content: '';
            position: absolute;
            top: 30%;
            left: 10%;
            width: 45%;
            height: 18%;
            background: #00cfff22;
            border-radius: 50%;
            transform: rotate(-20deg);
        }

        /* Scanning line */
        .scan-line {
            position: absolute;
            inset: 0;
            border-radius: 50%;
            overflow: hidden;
        }
        .scan-line::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            width: 50%;
            height: 100%;
            background: conic-gradient(from 0deg, transparent 70%, #00cfff22 100%);
            animation: scan 2.2s linear infinite;
            transform-origin: left center;
        }
        @keyframes scan {
            from { transform: rotate(0deg); }
            to   { transform: rotate(360deg); }
        }

        /* Signal rings */
        .signal-rings {
            position: absolute;
            inset: 0;
            border-radius: 50%;
        }
        .signal-ring {
            position: absolute;
            border-radius: 50%;
            border: 1px solid #00cfff;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            opacity: 0;
            animation: pulse-ring 2.2s ease-out infinite;
        }
        .signal-ring:nth-child(1) { width: 70px;  height: 70px;  animation-delay: 0s; }
        .signal-ring:nth-child(2) { width: 100px; height: 100px; animation-delay: 0.6s; }
        .signal-ring:nth-child(3) { width: 130px; height: 130px; animation-delay: 1.2s; }
        @keyframes pulse-ring {
            0%   { transform: translate(-50%, -50%) scale(0.3); opacity: 0.8; }
            100% { transform: translate(-50%, -50%) scale(1.1); opacity: 0; }
        }

        /* Text */
        .loading-title {
            color: #00cfff;
            font-size: 18px;
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        .loading-status {
            color: #556;
            font-size: 13px;
            letter-spacing: 1px;
            animation: blink 1.2s ease-in-out infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; }
            50%       { opacity: 0.3; }
        }

        /* Progress dots */
        .loading-dots {
            display: flex;
            gap: 8px;
            align-items: center;
        }
        .loading-dots span {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: #00cfff;
            animation: dot-bounce 1.4s ease-in-out infinite;
        }
        .loading-dots span:nth-child(2) { animation-delay: 0.2s; }
        .loading-dots span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes dot-bounce {
            0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
            40%            { transform: scale(1.2); opacity: 1; }
        }
    </style>
</head>
<body>

<!-- SATELLITE LOADING OVERLAY -->
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
    <div class="loading-title">Scanning Imagery</div>
    <div class="loading-dots">
        <span></span><span></span><span></span>
    </div>
    <div class="loading-status" id="loading-status">Initialising detection model...</div>
</div>

<div class="navbar">
    <div class="logo">
        <a href="/"><img src="{{ url_for('static', filename='ui/logo.png') }}"></a>
    </div>
    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/detection">Detection</a>
        <a href="/datasets">Datasets</a>
        <a href="/learn">Learn</a>
        <a href="/tutorials">Tutorials</a>
        <a href="/about">About</a>
        <a href="/history">History</a>
    </div>
    <div class="nav-auth">
        {% if session.get('username') %}
            <a href="/profile" class="nav-user">&#128113; {{ session['username'] }}</a>
            <a href="/logout" class="btn-logout">Logout</a>
        {% else %}
            <a href="/login">Login</a>
            <a href="/register" style="background:#00cfff; color:#000; padding:4px 14px; border-radius:20px; font-size:13px; text-decoration:none;">Register</a>
        {% endif %}
    </div>
</div>

{% block content %}{% endblock %}

<script>
// ── SATELLITE LOADING ANIMATION ──────────────────────────────
const overlay  = document.getElementById('loading-overlay');
const statusEl = document.getElementById('loading-status');

const messages = [
    "Initialising detection model...",
    "Loading satellite imagery...",
    "Running inference engine...",
    "Processing oriented bounding boxes...",
    "Analysing object density...",
    "Saving results to cloud...",
    "Almost done..."
];

let msgIndex = 0;
let msgTimer = null;

function startLoading() {
    overlay.classList.add('active');
    msgIndex = 0;
    statusEl.textContent = messages[0];
    msgTimer = setInterval(function() {
        msgIndex = (msgIndex + 1) % messages.length;
        statusEl.textContent = messages[msgIndex];
    }, 2000);
}

function stopLoading() {
    overlay.classList.remove('active');
    clearInterval(msgTimer);
}

// Attach to detection form only
document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('.control-panel form');
    if (form) {
        form.addEventListener('submit', function() {
            startLoading();
        });
    }
});

// ── ZOOM ─────────────────────────────────────────────────────
document.querySelectorAll(".zoom-container").forEach(container => {
    const img  = container.querySelector(".zoom-image");
    const lens = container.querySelector(".zoom-lens");
    container.addEventListener("mousemove", e => {
        const rect = container.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        lens.style.display = "block";
        lens.style.left = (x - lens.offsetWidth/2)  + "px";
        lens.style.top  = (y - lens.offsetHeight/2) + "px";
        img.style.transformOrigin = `${(x/rect.width)*100}% ${(y/rect.height)*100}%`;
        img.style.transform = "scale(2.5)";
    });
    container.addEventListener("mouseleave", () => {
        lens.style.display  = "none";
        img.style.transform = "scale(1)";
    });
});
</script>
</body>
</html>
"""

path = os.path.join("C:\\Users\\khech\\OAOD Project\\website", "templates", "layout.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(template)

print("Done! layout.html written.")
print("Has overlay:", "loading-overlay" in template)
print("Has satellite:", "satellite-dot" in template)
print("Has orbit:", "orbit" in template)