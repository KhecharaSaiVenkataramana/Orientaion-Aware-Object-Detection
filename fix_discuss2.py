import os

BASE = r"C:\Users\khech\OAOD Project\website"

discuss = open(os.path.join(BASE, "templates", "discuss.html"), encoding="utf-8").read()

old = '''<!-- FEEDBACK SECTION -->
<div style="padding:60px 120px 80px;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">FEEDBACK</div>
    <h2 style="font-size:32px;margin:0 0 16px;color:#fff;">Share your thoughts</h2>
    <p style="color:#8877cc;font-size:15px;line-height:1.7;max-width:620px;margin:0 0 36px;">
        Found a bug? Have a feature request? Want to collaborate on extending RAVEN?
        We would love to hear from you. Reach out to any team member directly
        using the contact links above.
    </p>

    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:700px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:14px;padding:24px;text-align:center;">
            <div style="font-size:28px;margin-bottom:10px;">&#128027;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:6px;">Report a bug</div>
            <div style="color:#8877cc;font-size:12px;line-height:1.5;">Found something broken? Tell us exactly what happened.</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(0,207,255,0.2);border-radius:14px;padding:24px;text-align:center;">
            <div style="font-size:28px;margin-bottom:10px;">&#128161;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:6px;">Suggest a feature</div>
            <div style="color:#8877cc;font-size:12px;line-height:1.5;">Have an idea that would make RAVEN better?</div>
        </div>
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:14px;padding:24px;text-align:center;">
            <div style="font-size:28px;margin-bottom:10px;">&#129309;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;margin-bottom:6px;">Collaborate</div>
            <div style="color:#8877cc;font-size:12px;line-height:1.5;">Interested in extending this research further?</div>
        </div>
    </div>
</div>'''

new = '''<!-- SUGGESTION BOX -->
<div style="padding:60px 120px 80px;">
    <div style="color:#6644ff;font-size:11px;font-weight:700;letter-spacing:3px;
                font-family:'Courier New',monospace;margin-bottom:8px;">SEND A SUGGESTION</div>
    <h2 style="font-size:32px;margin:0 0 16px;color:#fff;">Share your thoughts</h2>
    <p style="color:#8877cc;font-size:15px;line-height:1.7;max-width:620px;margin:0 0 36px;">
        Found a bug? Have a feature idea? Want to collaborate?
        Send us a message directly — we read every submission.
        {% if session.get("username") %}
        Your message will be sent from your account email.
        {% else %}
        <a href="/login" style="color:#00cfff;">Log in</a> to send with your email so we can reply to you.
        {% endif %}
    </p>

    <!-- Category tiles -->
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:700px;margin-bottom:36px;">
        <div class="suggestion-tile" onclick="selectCategory(this,'Bug Report')"
             style="background:#0d0b22;border:2px solid rgba(102,68,255,0.2);border-radius:14px;
                    padding:24px;text-align:center;cursor:pointer;transition:0.25s;">
            <div style="font-size:28px;margin-bottom:10px;">&#128027;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;">Report a bug</div>
            <div style="color:#8877cc;font-size:12px;margin-top:6px;">Something broken?</div>
        </div>
        <div class="suggestion-tile" onclick="selectCategory(this,'Feature Request')"
             style="background:#0d0b22;border:2px solid rgba(102,68,255,0.2);border-radius:14px;
                    padding:24px;text-align:center;cursor:pointer;transition:0.25s;">
            <div style="font-size:28px;margin-bottom:10px;">&#128161;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;">Feature request</div>
            <div style="color:#8877cc;font-size:12px;margin-top:6px;">Idea to make RAVEN better?</div>
        </div>
        <div class="suggestion-tile" onclick="selectCategory(this,'Collaboration')"
             style="background:#0d0b22;border:2px solid rgba(102,68,255,0.2);border-radius:14px;
                    padding:24px;text-align:center;cursor:pointer;transition:0.25s;">
            <div style="font-size:28px;margin-bottom:10px;">&#129309;</div>
            <div style="color:#fff;font-size:14px;font-weight:600;">Collaborate</div>
            <div style="color:#8877cc;font-size:12px;margin-top:6px;">Extend this research?</div>
        </div>
    </div>

    <!-- Message box (hidden until category selected) -->
    <div id="suggestion-form" style="display:none;max-width:700px;">
        <div style="background:#0d0b22;border:1px solid rgba(102,68,255,0.3);
                    border-radius:16px;padding:32px;">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:20px;">
                <span style="background:rgba(102,68,255,0.15);color:#6644ff;padding:4px 14px;
                             border-radius:20px;font-size:12px;font-weight:700;
                             font-family:'Courier New',monospace;" id="category-badge">
                    Bug Report
                </span>
                <span style="color:#8877cc;font-size:13px;">Selected category</span>
            </div>

            <textarea id="suggestion-text"
                placeholder="Describe your suggestion, bug or idea in detail..."
                style="width:100%;min-height:140px;background:#07051a;
                       border:1px solid rgba(102,68,255,0.3);border-radius:10px;
                       color:#fff;padding:16px;font-size:14px;font-family:inherit;
                       resize:vertical;outline:none;box-sizing:border-box;line-height:1.6;"
                onfocus="this.style.borderColor='#6644ff'"
                onblur="this.style.borderColor='rgba(102,68,255,0.3)'"></textarea>

            <div style="display:flex;align-items:center;justify-content:space-between;margin-top:16px;">
                <div id="form-status" style="font-size:13px;color:#8877cc;"></div>
                <button onclick="submitSuggestion()"
                    style="background:linear-gradient(135deg,#6644ff,#00cfff);
                           color:#fff;border:none;padding:12px 32px;border-radius:10px;
                           font-size:14px;font-weight:700;cursor:pointer;
                           letter-spacing:0.5px;transition:0.25s;"
                    onmouseover="this.style.transform='translateY(-2px)'"
                    onmouseout="this.style.transform='none'">
                    Send Suggestion &#8594;
                </button>
            </div>
        </div>
    </div>

    <!-- Success message -->
    <div id="success-msg" style="display:none;max-width:700px;">
        <div style="background:rgba(0,255,136,0.08);border:1px solid rgba(0,255,136,0.3);
                    border-radius:16px;padding:32px;text-align:center;">
            <div style="font-size:48px;margin-bottom:16px;">&#10003;</div>
            <h3 style="color:#00ff88;font-size:20px;margin:0 0 10px;">Suggestion sent!</h3>
            <p style="color:#8877cc;font-size:14px;margin:0 0 20px;">
                We have received your message and will get back to you soon.
            </p>
            <button onclick="resetForm()"
                style="background:transparent;border:1px solid rgba(102,68,255,0.4);
                       color:#6644ff;padding:10px 24px;border-radius:8px;
                       font-size:13px;cursor:pointer;">
                Send another
            </button>
        </div>
    </div>
</div>

<script>
var selectedCategory = "";

function selectCategory(tile, category) {
    document.querySelectorAll('.suggestion-tile').forEach(function(t) {
        t.style.borderColor = 'rgba(102,68,255,0.2)';
        t.style.background = '#0d0b22';
    });
    tile.style.borderColor = '#6644ff';
    tile.style.background = 'rgba(102,68,255,0.08)';
    selectedCategory = category;
    document.getElementById('category-badge').textContent = category;
    document.getElementById('suggestion-form').style.display = 'block';
    document.getElementById('suggestion-form').scrollIntoView({behavior:'smooth',block:'nearest'});
}

function submitSuggestion() {
    var msg = document.getElementById('suggestion-text').value.trim();
    var status = document.getElementById('form-status');

    if (!msg) {
        status.textContent = 'Please write a message first.';
        status.style.color = '#ff5050';
        return;
    }

    status.textContent = 'Sending...';
    status.style.color = '#8877cc';

    var formData = new FormData();
    formData.append('category', selectedCategory);
    formData.append('message', msg);

    fetch('/send-suggestion', {method:'POST', body:formData})
        .then(function(r){ return r.json(); })
        .then(function(data) {
            if (data.status === 'ok') {
                document.getElementById('suggestion-form').style.display = 'none';
                document.getElementById('success-msg').style.display = 'block';
            } else {
                status.textContent = data.msg;
                status.style.color = '#ff5050';
            }
        })
        .catch(function() {
            status.textContent = 'Network error. Please try again.';
            status.style.color = '#ff5050';
        });
}

function resetForm() {
    document.getElementById('success-msg').style.display = 'none';
    document.getElementById('suggestion-form').style.display = 'none';
    document.getElementById('suggestion-text').value = '';
    document.getElementById('form-status').textContent = '';
    selectedCategory = '';
    document.querySelectorAll('.suggestion-tile').forEach(function(t) {
        t.style.borderColor = 'rgba(102,68,255,0.2)';
        t.style.background = '#0d0b22';
    });
}
</script>'''

if old in discuss:
    discuss = discuss.replace(old, new)
    with open(os.path.join(BASE, "templates", "discuss.html"), "w", encoding="utf-8") as f:
        f.write(discuss)
    print("discuss.html updated with suggestion box!")
else:
    print("Block not found - discuss.html may need full rewrite")