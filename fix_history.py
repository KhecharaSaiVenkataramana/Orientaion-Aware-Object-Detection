import os

template = """\
{% extends "layout.html" %}
{% block content %}
<div style="max-width:1100px; margin:40px auto; padding:0 20px;">

    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;">
        <h2 style="color:#00cfff; margin:0;">Detection History</h2>
        {% if session.get('username') %}
        <span style="color:#555; font-size:13px;">Showing detections for <span style="color:#00cfff;">{{ session['username'] }}</span></span>
        {% endif %}
    </div>
    <p style="color:#888; margin:0 0 28px; font-size:14px;">All images processed - saved to cloud database. Showing last 50 results.</p>

    {% if not session.get('username') %}
    <div style="background:#00cfff11; border:1px solid #00cfff44; border-radius:12px; padding:32px; text-align:center; margin-bottom:32px;">
        <p style="color:#aaa; margin:0 0 16px; font-size:15px;">Sign in to see your personal detection history.</p>
        <div style="display:flex; gap:12px; justify-content:center;">
            <a href="/login" style="background:#00cfff; color:#000; padding:10px 28px; border-radius:8px; text-decoration:none; font-size:14px; font-weight:600;">Login</a>
            <a href="/register" style="background:transparent; color:#00cfff; border:1px solid #00cfff; padding:10px 28px; border-radius:8px; text-decoration:none; font-size:14px;">Register</a>
        </div>
    </div>
    {% endif %}

    {% if records %}
    <table style="width:100%; border-collapse:collapse; font-size:14px;">
        <thead>
            <tr style="background:#0f3460; color:#00cfff; text-align:left;">
                <th style="padding:12px 14px;">#</th>
                <th style="padding:12px 14px;">Output</th>
                <th style="padding:12px 14px;">Filename</th>
                <th style="padding:12px 14px;">Model</th>
                <th style="padding:12px 14px;">Objects</th>
                <th style="padding:12px 14px;">Time (ms)</th>
                <th style="padding:12px 14px;">FPS</th>
                <th style="padding:12px 14px;">Size</th>
                <th style="padding:12px 14px;">Detected at</th>
                <th style="padding:12px 14px;">Download</th>
            </tr>
        </thead>
        <tbody>
            {% for r in records %}
            {% set raw = r.output_path if r.output_path else '' %}
            {% set fname = raw.replace('\\\\', '/').split('/')[-1] %}
            <tr style="border-bottom:1px solid #1e1e3a; color:#eee;"
                onmouseover="this.style.background='#ffffff08'"
                onmouseout="this.style.background='transparent'">
                <td style="padding:11px 14px;">{{ r.id }}</td>
                <td style="padding:11px 14px;">
                    {% if raw %}
                    <img src="{{ url_for('static', filename='outputs/' + fname) }}"
                         alt="result" onclick="openModal(this.src)"
                         onerror="this.style.display='none'"
                         style="width:60px; height:42px; object-fit:cover; border-radius:4px; border:1px solid #333; cursor:pointer;">
                    {% else %}
                    <span style="background:#333; color:#666; padding:3px 8px; border-radius:4px; font-size:11px;">Expired</span>
                    {% endif %}
                </td>
                <td style="padding:11px 14px;">{{ r.filename }}</td>
                <td style="padding:11px 14px;">
                    {% if 'DOTA' in r.model_used %}
                        <span style="background:#4527a022; color:#9575cd; padding:3px 10px; border-radius:20px; font-size:12px;">{{ r.model_used }}</span>
                    {% elif 'HRSC' in r.model_used %}
                        <span style="background:#00695c22; color:#4db6ac; padding:3px 10px; border-radius:20px; font-size:12px;">{{ r.model_used }}</span>
                    {% else %}
                        <span style="background:#1565c022; color:#64b5f6; padding:3px 10px; border-radius:20px; font-size:12px;">{{ r.model_used }}</span>
                    {% endif %}
                </td>
                <td style="padding:11px 14px;">
                    <span style="background:#00ff8822; color:#00ff88; padding:3px 10px; border-radius:20px;">{{ r.objects_found }}</span>
                </td>
                <td style="padding:11px 14px;">{{ r.inference_ms }}</td>
                <td style="padding:11px 14px;">{{ r.fps }}</td>
                <td style="padding:11px 14px;">{{ r.image_size }}</td>
                <td style="padding:11px 14px; white-space:nowrap;">{{ r.detected_at.strftime('%d %b %Y, %H:%M') if r.detected_at else '' }}</td>
                <td style="padding:11px 14px;">
                    {% if raw %}
                    <a href="/download/{{ fname }}"
                       style="background:#00cfff22; color:#00cfff; padding:4px 12px; border-radius:6px; font-size:12px; text-decoration:none; border:1px solid #00cfff44; white-space:nowrap;">
                        Download
                    </a>
                    {% else %}
                    <span style="color:#444; font-size:12px;">-</span>
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    {% else %}
    <div style="text-align:center; padding:60px 20px; color:#555; font-size:15px;">
        {% if session.get('username') %}
            No detections yet. <a href="/detection" style="color:#00cfff;">Run your first detection!</a>
        {% else %}
            <a href="/login" style="color:#00cfff;">Login</a> to see your history.
        {% endif %}
    </div>
    {% endif %}
</div>

<div id="imgModal" onclick="closeModal()"
     style="display:none; position:fixed; top:0; left:0; width:100%; height:100%;
            background:rgba(0,0,0,0.88); z-index:9999; align-items:center; justify-content:center;">
    <span onclick="closeModal()"
          style="position:fixed; top:20px; right:30px; color:#fff; font-size:36px; cursor:pointer;">&times;</span>
    <img id="modalImg" src="" alt="enlarged"
         style="max-width:90%; max-height:90%; border-radius:8px;">
</div>

<script>
function openModal(src) {
    document.getElementById('modalImg').src = src;
    document.getElementById('imgModal').style.display = 'flex';
}
function closeModal() {
    document.getElementById('imgModal').style.display = 'none';
}
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
});
</script>
{% endblock %}"""

path = os.path.join("templates", "history.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(template)

c = open(path, encoding="utf-8").read()
print("Written:", len(c), "chars")
print("Extends layout:", "extends" in c)
print("Has login prompt:", "Sign in to see" in c)
print("First 60:", repr(c[:60]))