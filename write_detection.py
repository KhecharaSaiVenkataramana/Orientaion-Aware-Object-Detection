import os

BASE = r"C:\Users\khech\OAOD Project\website"

template = """\
{% extends "layout.html" %}
{% block content %}

<div class="detect-layout">

    <!-- LEFT PANEL -->
    <div class="control-panel">

        <h1>Detection Workspace</h1>

        <form method="POST" enctype="multipart/form-data" id="detect-form" onsubmit="return checkBeforeSubmit()">

            <label class="section-title">Upload Aerial Images</label>

            <div style="display:flex;gap:8px;margin-bottom:12px;">
                <button type="button" id="tab-files" onclick="switchTab('files')"
                    style="flex:1;padding:8px;border-radius:8px;border:1px solid #00cfff;
                           background:#00cfff;color:#000;font-size:13px;cursor:pointer;font-weight:600;">
                    Images
                </button>
                <button type="button" id="tab-folder" onclick="switchTab('folder')"
                    style="flex:1;padding:8px;border-radius:8px;border:1px solid #444;
                           background:transparent;color:#aaa;font-size:13px;cursor:pointer;">
                    Folder
                </button>
            </div>

            <div id="input-files">
                <input type="file" name="image" id="file-input" multiple accept="image/*,.tif,.tiff"
                       required class="file-input">
                <div style="color:#555;font-size:12px;margin-top:4px;">
                    Select one or more images (JPG, PNG, TIFF)
                </div>
            </div>

            <div id="input-folder" style="display:none;">
                <input type="file" name="image" id="folder-input" multiple accept="image/*,.tif,.tiff"
                       webkitdirectory mozdirectory class="file-input">
                <div style="color:#555;font-size:12px;margin-top:4px;">
                    Select a folder - all images inside will be processed
                </div>
                <div id="folder-count" style="color:#00cfff;font-size:13px;margin-top:6px;"></div>
                <div id="folder-warning" style="display:none;margin-top:12px;
                     background:rgba(186,117,23,0.12);border:1px solid rgba(186,117,23,0.5);
                     border-radius:10px;padding:14px 16px;">
                    <div style="color:#ef9f27;font-size:13px;font-weight:600;margin-bottom:6px;">
                        Large batch detected
                    </div>
                    <div id="warning-text" style="color:#ba7517;font-size:12px;line-height:1.6;margin-bottom:10px;"></div>
                    <div style="display:flex;gap:8px;">
                        <button type="button" onclick="proceedAnyway()"
                            style="flex:1;padding:7px;border-radius:7px;border:1px solid #ef9f27;
                                   background:rgba(186,117,23,0.2);color:#ef9f27;font-size:12px;
                                   font-weight:600;cursor:pointer;">
                            Proceed anyway
                        </button>
                        <button type="button" onclick="cancelBatch()"
                            style="flex:1;padding:7px;border-radius:7px;border:1px solid #444;
                                   background:transparent;color:#aaa;font-size:12px;cursor:pointer;">
                            Cancel
                        </button>
                    </div>
                </div>
            </div>

            <label class="section-title" style="margin-top:20px;">Confidence Threshold</label>
            <input type="range" name="conf" min="0.1" max="1" step="0.05" value="0.25"
                   oninput="confValue.innerText=parseFloat(this.value).toFixed(2)" class="slider">
            <div class="slider-value">Confidence: <b id="confValue">0.25</b></div>
            <div class="slider-help">
                Lower value &rarr; more detections | Higher value &rarr; stricter filtering
            </div>

            <label class="section-title">Detection Mode</label>
            <select name="mode" id="mode-select" class="dropdown">
                <option value="standard">Standard YOLOv8</option>
                <option value="dota">DOTA-OBB</option>
                <option value="hrsc">HRSC-OBB</option>
                <option value="dota_fg">DOTA Fine-grained</option>
            </select>

            <button type="submit" class="run-btn" id="run-btn">Run Detection</button>

        </form>
    </div>

    <!-- RIGHT PANEL -->
    <div class="viewer-panel">

        {% if not uploaded_images %}
        <div class="empty-state">
            <div class="empty-content">
                <img src="{{ url_for('static', filename='ui/upload.svg') }}" class="empty-illustration">
                <h2>UPLOAD IMAGE</h2>
                <p>Upload aerial or satellite imagery to begin detection.</p>
                <div class="formats">JPG &middot; PNG &middot; TIFF &middot; Drone &amp; Satellite imagery supported</div>
            </div>
        </div>

        {% else %}

        <h1 class="viewer-title">Detection Results</h1>

        {% if stats %}
        <div style="display:flex;gap:10px;justify-content:flex-end;margin-bottom:16px;flex-wrap:wrap;">
            <a href="/download-report/csv?files={{ output_filenames|join(',') }}&stats={{ stats|tojson|urlencode }}"
               style="background:rgba(102,68,255,0.15);color:#6644ff;border:1px solid rgba(102,68,255,0.4);
                      padding:8px 18px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;">
                Export CSV
            </a>
            <a href="/download-report/pdf?files={{ output_filenames|join(',') }}"
               style="background:rgba(0,207,255,0.12);color:#00cfff;border:1px solid rgba(0,207,255,0.4);
                      padding:8px 18px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;">
                Download PDF Report
            </a>
            {% if output_filenames|length > 1 %}
            <a href="/download-zip?files={{ output_filenames|join(',') }}"
               style="background:#00cfff;color:#000;padding:8px 18px;border-radius:8px;
                      text-decoration:none;font-size:13px;font-weight:600;">
                Download All ({{ output_filenames|length }})
            </a>
            {% endif %}
        </div>
        {% endif %}

        <div class="grid-view">
            {% for i in range(uploaded_images|length) %}
            <div class="compare-card">
                <div class="img-box">
                    <h3>Input</h3>
                    <div class="zoom-container">
                        <img class="zoom-image" src="{{ url_for('static', filename=uploaded_images[i]) }}">
                        <div class="zoom-lens"></div>
                    </div>
                </div>
                <div class="img-box">
                    <h3>Output</h3>
                    <div class="zoom-container">
                        <img class="zoom-image" src="{{ url_for('static', filename=result_images[i]) }}">
                        <div class="zoom-lens"></div>
                    </div>
                    {% if output_filenames and i < output_filenames|length %}
                    <div style="text-align:center;margin-top:10px;">
                        <a href="/download/{{ output_filenames[i] }}"
                           style="display:inline-block;background:#00cfff22;color:#00cfff;
                                  border:1px solid #00cfff44;padding:6px 20px;border-radius:8px;
                                  text-decoration:none;font-size:13px;font-weight:500;">
                            Download Result
                        </a>
                    </div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>

        {% if stats %}
        <div class="results-section">
            <h2>Detection Performance Summary</h2>
            <table class="perf-table">
                <thead>
                    <tr>
                        <th>Image</th><th>Resolution</th><th>Objects</th>
                        <th>Density</th><th>Time (ms)</th><th>FPS</th>
                        <th>Model</th><th>Download</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in stats %}
                    <tr>
                        <td>{{ row.name }}</td><td>{{ row.size }}</td>
                        <td>{{ row.objects }}</td><td>{{ row.density }}</td>
                        <td>{{ row.time }}</td><td>{{ row.fps }}</td>
                        <td>{{ row.model }}</td>
                        <td>
                            {% if row.outfile %}
                            <a href="/download/{{ row.outfile }}" style="color:#00cfff;font-size:12px;text-decoration:none;">Download</a>
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
            <div class="summary-box">
                <p><b>Average Time:</b> {{ avg_time }} ms</p>
                <p><b>Average Objects:</b> {{ avg_objects }}</p>
                <p><b>Estimated FPS:</b> {{ avg_fps }}</p>
            </div>
            <div style="display:flex;gap:10px;margin-top:20px;flex-wrap:wrap;">
                <a href="/download-report/csv?files={{ output_filenames|join(',') }}&stats={{ stats|tojson|urlencode }}"
                   style="background:rgba(102,68,255,0.15);color:#6644ff;border:1px solid rgba(102,68,255,0.4);
                          padding:10px 24px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;">
                    Export CSV
                </a>
                <a href="/download-report/pdf?files={{ output_filenames|join(',') }}"
                   style="background:rgba(0,207,255,0.12);color:#00cfff;border:1px solid rgba(0,207,255,0.4);
                          padding:10px 24px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;">
                    Download PDF Report
                </a>
            </div>
        </div>
        {% endif %}

        {% endif %}
    </div>
</div>

<script>
var warningAcknowledged = false;

function switchTab(tab) {
    var filesDiv    = document.getElementById('input-files');
    var folderDiv   = document.getElementById('input-folder');
    var tabFiles    = document.getElementById('tab-files');
    var tabFolder   = document.getElementById('tab-folder');
    var fileInput   = document.getElementById('file-input');
    var folderInput = document.getElementById('folder-input');
    if (tab === 'files') {
        filesDiv.style.display  = 'block';
        folderDiv.style.display = 'none';
        tabFiles.style.background   = '#00cfff';
        tabFiles.style.color        = '#000';
        tabFiles.style.borderColor  = '#00cfff';
        tabFolder.style.background  = 'transparent';
        tabFolder.style.color       = '#aaa';
        tabFolder.style.borderColor = '#444';
        fileInput.required   = true;
        folderInput.required = false;
    } else {
        filesDiv.style.display  = 'none';
        folderDiv.style.display = 'block';
        tabFolder.style.background  = '#00cfff';
        tabFolder.style.color       = '#000';
        tabFolder.style.borderColor = '#00cfff';
        tabFiles.style.background   = 'transparent';
        tabFiles.style.color        = '#aaa';
        tabFiles.style.borderColor  = '#444';
        fileInput.required   = false;
        folderInput.required = true;
    }
}

function getEstimatedTime(count) {
    var mode = document.getElementById('mode-select') ? document.getElementById('mode-select').value : 'dota';
    var secs = {'standard':2,'dota':3,'hrsc':3,'dota_fg':5}[mode] || 3;
    var total = count * secs;
    if (total < 60) return total + ' seconds';
    return Math.ceil(total/60) + ' minute' + (Math.ceil(total/60) > 1 ? 's' : '');
}

document.addEventListener('DOMContentLoaded', function() {
    var fi = document.getElementById('folder-input');
    if (fi) {
        fi.addEventListener('change', function() {
            var count = this.files.length;
            warningAcknowledged = false;
            var counter = document.getElementById('folder-count');
            var warning = document.getElementById('folder-warning');
            var warnTxt = document.getElementById('warning-text');
            if (counter) counter.textContent = count + ' image' + (count !== 1 ? 's' : '') + ' selected';
            if (count > 12 && warning && warnTxt) {
                warnTxt.textContent = count + ' images selected. Estimated processing time: ' + getEstimatedTime(count) + '. Large batches may take a while.';
                warning.style.display = 'block';
            } else if (warning) {
                warning.style.display = 'none';
            }
        });
    }
});

function proceedAnyway() {
    warningAcknowledged = true;
    document.getElementById('folder-warning').style.display = 'none';
}

function cancelBatch() {
    document.getElementById('folder-input').value = '';
    document.getElementById('folder-count').textContent = '';
    document.getElementById('folder-warning').style.display = 'none';
    warningAcknowledged = false;
}

function checkBeforeSubmit() {
    var fi      = document.getElementById('folder-input');
    var warning = document.getElementById('folder-warning');
    var isFolder = document.getElementById('input-folder').style.display !== 'none';
    if (isFolder && fi && fi.files.length > 12 && !warningAcknowledged) {
        warning.style.display = 'block';
        warning.scrollIntoView({behavior:'smooth',block:'nearest'});
        return false;
    }
    return true;
}
</script>

{% endblock %}
"""

with open(os.path.join(BASE, "templates", "detection.html"), "w", encoding="utf-8") as f:
    f.write(template)
print("detection.html written!")
print("Has folder warning:", "folder-warning" in template)
print("Has CSV button:", "Export CSV" in template)
print("Has PDF button:", "PDF Report" in template)