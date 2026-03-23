from flask import (Flask, render_template, request,
                   redirect, url_for, session, send_file, jsonify)
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os, cv2, time, uuid, threading
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = _os.environ.get("SECRET_KEY", "oaod_secret_key_change_in_production")

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

STANDARD_MODEL = YOLO("models/yolov8n.pt")
DOTA_MODEL     = YOLO("models/DOTA_Model.pt")
HRSC_MODEL     = YOLO("models/HRSC_Model.pt")
# FAIR1M model — optional, only loaded if file exists
_fair1m_path = os.path.join(os.path.dirname(__file__), "models", "FAIR1M_Model.pt")
FAIR1M_MODEL = YOLO(_fair1m_path) if os.path.exists(_fair1m_path) else None

DOTA_VEHICLE_CLASSES = {9, 10}
FAIR1M_CLASSES = [
    "small-car", "van", "dump-truck", "cargo-truck",
    "other-vehicle", "bus", "excavator", "trailer",
    "truck-tractor", "tractor"
]
FINE_GRAINED_CONF = 0.01

import os as _os
DB_CONFIG = {
    "host":     _os.environ.get("DB_HOST", "bg0mwot4am56wljm4ims-mysql.services.clever-cloud.com"),
    "port":     int(_os.environ.get("DB_PORT", 3306)),
    "user":     _os.environ.get("DB_USER", "uky8zedsjiowpw7m"),
    "password": _os.environ.get("DB_PASSWORD", "wjLZKLUHi5GseDFcv7mL"),
    "database": _os.environ.get("DB_NAME", "bg0mwot4am56wljm4ims"),
    "connect_timeout": 10,
    "cursorclass": pymysql.cursors.DictCursor
}

def get_db():
    import time as _time
    for attempt in range(3):
        try:
            return pymysql.connect(**DB_CONFIG)
        except Exception as e:
            if attempt < 2:
                print(f"[DB] Connection attempt {attempt+1} failed, retrying...")
                _time.sleep(2)
            else:
                raise e

def init_db():
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id            INT AUTO_INCREMENT PRIMARY KEY,
                    username      VARCHAR(80)  NOT NULL UNIQUE,
                    email         VARCHAR(120) NOT NULL UNIQUE,
                    password_hash VARCHAR(256) NOT NULL,
                    joined_at     DATETIME     NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS detections (
                    id            INT AUTO_INCREMENT PRIMARY KEY,
                    user_id       INT          NULL,
                    filename      VARCHAR(255) NOT NULL,
                    model_used    VARCHAR(50)  NOT NULL,
                    objects_found INT          NOT NULL,
                    inference_ms  FLOAT        NOT NULL,
                    fps           FLOAT        NOT NULL,
                    image_size    VARCHAR(30)  NOT NULL,
                    density       FLOAT        NOT NULL,
                    input_path    VARCHAR(512) NOT NULL,
                    output_path   VARCHAR(512) NULL,
                    detected_at   DATETIME     NOT NULL
                )
            """)
            try:
                cur.execute("ALTER TABLE detections ADD COLUMN user_id INT NULL AFTER id")
            except Exception:
                pass
            try:
                cur.execute("ALTER TABLE detections MODIFY output_path VARCHAR(512) NULL")
            except Exception:
                pass
        conn.commit()
        print("Database ready - users + detections tables OK.")
    finally:
        conn.close()

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

def get_current_user():
    if "user_id" not in session:
        return None
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (session["user_id"],))
            return cur.fetchone()
    finally:
        conn.close()

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm", "")
        if not username or not email or not password:
            error = "All fields are required."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != confirm:
            error = "Passwords do not match."
        else:
            conn = get_db()
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT id FROM users WHERE username=%s OR email=%s", (username, email))
                    if cur.fetchone():
                        error = "Username or email already taken."
                    else:
                        pw_hash = generate_password_hash(password)
                        cur.execute("""
                            INSERT INTO users (username, email, password_hash, joined_at)
                            VALUES (%s, %s, %s, %s)
                        """, (username, email, pw_hash, datetime.utcnow()))
                        conn.commit()
                        cur.execute("SELECT id FROM users WHERE username=%s", (username,))
                        user = cur.fetchone()
                        session["user_id"]  = user["id"]
                        session["username"] = username
                        return redirect(url_for("home"))
            finally:
                conn.close()
    return render_template("register.html", title="Register", error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        conn = get_db()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE username=%s", (username,))
                user = cur.fetchone()
            if user and check_password_hash(user["password_hash"], password):
                session["user_id"]  = user["id"]
                session["username"] = user["username"]
                return redirect(url_for("home"))
            else:
                error = "Invalid username or password."
        finally:
            conn.close()
    return render_template("login.html", title="Login", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/profile")
@login_required
def profile():
    user = get_current_user()
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*) AS total,
                       SUM(objects_found) AS total_objects,
                       AVG(inference_ms) AS avg_ms
                FROM detections WHERE user_id = %s
            """, (session["user_id"],))
            stats = cur.fetchone()
    finally:
        conn.close()
    return render_template("profile.html", title="Profile", user=user, stats=stats)

def save_detection(filename, model_used, objects_found, inference_ms,
                   fps, image_size, density, input_path, output_path):
    user_id = session.get("user_id", None)
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO detections
                    (user_id, filename, model_used, objects_found, inference_ms,
                     fps, image_size, density, input_path, output_path, detected_at)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (user_id, filename, model_used, objects_found, inference_ms,
                  fps, image_size, density, input_path, output_path,
                  datetime.utcnow()))
        conn.commit()
    except Exception as e:
        import traceback
        print(f"[DB ERROR] {type(e).__name__}: {e}")
        traceback.print_exc()
    finally:
        conn.close()

def get_user_detections(limit=50):
    user_id = session.get("user_id", None)
    if not user_id:
        return []
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM detections
                WHERE user_id = %s
                ORDER BY detected_at DESC LIMIT %s
            """, (user_id, limit))
            return cur.fetchall()
    except Exception as e:
        print(f"[DB WARNING] Could not fetch history: {e}")
        return []
    finally:
        conn.close()

def cleanup_old_outputs():
    while True:
        time.sleep(3600)
        cutoff = datetime.utcnow() - timedelta(hours=48)
        deleted = 0
        conn = get_db()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, output_path FROM detections
                    WHERE output_path IS NOT NULL AND detected_at < %s
                """, (cutoff,))
                old_rows = cur.fetchall()
            for row in old_rows:
                fpath = row["output_path"]
                if fpath and os.path.exists(fpath):
                    try:
                        os.remove(fpath)
                        deleted += 1
                    except Exception as e:
                        print(f"[CLEANUP] Could not delete {fpath}: {e}")
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE detections SET output_path = NULL
                    WHERE output_path IS NOT NULL AND detected_at < %s
                """, (cutoff,))
            conn.commit()
            print(f"[CLEANUP] Deleted {deleted} expired output images.")
        except Exception as e:
            print(f"[CLEANUP ERROR] {e}")
        finally:
            conn.close()

cleanup_thread = threading.Thread(target=cleanup_old_outputs, daemon=True)
cleanup_thread.start()

@app.route("/download/<path:filename>")
def download_file(filename):
    safe = secure_filename(os.path.basename(filename))
    file_path = os.path.join(OUTPUT_FOLDER, safe)
    if not os.path.exists(file_path):
        return "File not found or expired.", 404
    return send_file(file_path, as_attachment=True, download_name=safe)

@app.route("/detection", methods=["GET", "POST"])
def detection():
    uploaded_images  = []
    result_images    = []
    stats            = []
    output_filenames = []
    total_time       = 0
    total_objects    = 0

    if request.method == "POST":
        files = request.files.getlist("image")
        mode  = request.form.get("mode", "standard")
        conf  = float(request.form.get("conf", 0.25))

        if mode == "dota":
            model, model_name = DOTA_MODEL, "DOTA-OBB"
        elif mode == "hrsc":
            model, model_name = HRSC_MODEL, "HRSC-OBB"
        elif mode == "dota_fg":
            model, model_name = DOTA_MODEL, "DOTA-Fine-grained"
        else:
            model, model_name = STANDARD_MODEL, "Standard YOLOv8"

        for file in files:
            if file and file.filename != "":
                unique_id       = str(uuid.uuid4())[:8]
                filename        = secure_filename(file.filename)
                name, ext       = os.path.splitext(filename)
                input_filename  = f"{name}_{unique_id}{ext}"
                output_filename = f"{name}_{unique_id}_out{ext}"
                input_path      = os.path.join(UPLOAD_FOLDER, input_filename)
                output_path     = os.path.join(OUTPUT_FOLDER, output_filename)

                file.save(input_path)
                uploaded_images.append(f"uploads/{input_filename}")

                image     = Image.open(input_path).convert("RGB")
                img_array = np.array(image)
                h, w, _   = img_array.shape
                pixels    = w * h

                start   = time.time()
                results = model(img_array, conf=conf)
                end     = time.time()
                inference_time = round((end - start) * 1000, 2)

                result = results[0]
                if result.boxes is not None and len(result.boxes) > 0:
                    objects_detected = len(result.boxes)
                elif hasattr(result, "obb") and result.obb is not None:
                    objects_detected = len(result.obb)
                else:
                    objects_detected = 0

                # Fine-grained vehicle classification
                if mode == "dota_fg" and result.obb is not None and len(result.obb) > 0:
                    img_draw = result.plot()
                    H_img, W_img = img_draw.shape[:2]
                    vehicle_count = 0
                    labeled_count = 0

                    for box in result.obb:
                        cls_id = int(box.cls[0].item())
                        if cls_id not in DOTA_VEHICLE_CLASSES:
                            continue
                        vehicle_count += 1

                        xyxyxyxy = box.xyxyxyxy[0].cpu().numpy()
                        x_coords = xyxyxyxy[:, 0]
                        y_coords = xyxyxyxy[:, 1]
                        x1 = max(0, int(x_coords.min()))
                        y1 = max(0, int(y_coords.min()))
                        x2 = min(W_img, int(x_coords.max()))
                        y2 = min(H_img, int(y_coords.max()))
                        crop_w = x2 - x1
                        crop_h = y2 - y1

                        if crop_w < 8 or crop_h < 8:
                            print(f"[FG] Skipped tiny crop {crop_w}x{crop_h}")
                            continue

                        crop = img_array[y1:y2, x1:x2]
                        fg_results = FAIR1M_MODEL(crop, verbose=False, conf=0.01)
                        fg_result  = fg_results[0]

                        if fg_result.obb is not None and len(fg_result.obb) > 0:
                            best_conf = float(fg_result.obb.conf[0].item())
                            best_cls  = int(fg_result.obb.cls[0].item())
                            fine_label = FAIR1M_CLASSES[best_cls]
                            print(f"[FG] crop {crop_w}x{crop_h} -> {fine_label} conf={best_conf:.3f}")
                            if best_conf >= FINE_GRAINED_CONF:
                                labeled_count += 1
                                cv2.putText(
                                    img_draw,
                                    f"{fine_label} {best_conf:.2f}",
                                    (x1, max(0, y1 - 6)),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (0, 255, 128), 1,
                                    cv2.LINE_AA
                                )
                                cv2.rectangle(
                                    img_draw,
                                    (x1, y1), (x2, y2),
                                    (0, 255, 128), 2
                                )
                        else:
                            print(f"[FG] crop {crop_w}x{crop_h} -> no detection")

                    print(f"[FG] Vehicles: {vehicle_count} | Fine-labeled: {labeled_count}")
                    plotted = img_draw
                else:
                    plotted = result.plot()

                cv2.imwrite(output_path, plotted)
                result_images.append(f"outputs/{output_filename}")
                output_filenames.append(output_filename)

                density  = round(objects_detected / (pixels / 1_000_000), 2) if pixels else 0
                fps      = round(1000 / inference_time, 2) if inference_time > 0 else 0
                img_size = f"{w} x {h}"

                stats.append({
                    "name":    filename,
                    "size":    img_size,
                    "objects": objects_detected,
                    "density": density,
                    "time":    inference_time,
                    "fps":     fps,
                    "model":   model_name,
                    "outfile": output_filename
                })

                total_time    += inference_time
                total_objects += objects_detected

                save_detection(
                    filename=filename, model_used=model_name,
                    objects_found=objects_detected, inference_ms=inference_time,
                    fps=fps, image_size=img_size, density=density,
                    input_path=input_path, output_path=output_path
                )

        avg_time    = round(total_time / len(stats), 2) if stats else 0
        avg_objects = round(total_objects / len(stats), 2) if stats else 0
        avg_fps     = round(1000 / avg_time, 2) if avg_time > 0 else 0

        return render_template(
            "detection.html",
            uploaded_images  = uploaded_images,
            result_images    = result_images,
            stats            = stats,
            output_filenames = output_filenames,
            avg_time         = avg_time,
            avg_objects      = avg_objects,
            avg_fps          = avg_fps
        )

    return render_template("detection.html")

@app.route("/download-zip")
def download_zip():
    import zipfile, io
    files_param = request.args.get("files", "")
    filenames = [f.strip() for f in files_param.split(",") if f.strip()]
    if not filenames:
        return "No files specified.", 400

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname in filenames:
            from werkzeug.utils import secure_filename
            safe = secure_filename(fname)
            fpath = os.path.join(OUTPUT_FOLDER, safe)
            if os.path.exists(fpath):
                zf.write(fpath, safe)
    zip_buffer.seek(0)
    return send_file(zip_buffer, as_attachment=True,
                     download_name="detection_results.zip",
                     mimetype="application/zip")

@app.route("/history")
def history():
    records = get_user_detections(limit=50)
    user    = get_current_user()
    return render_template("history.html", records=records, user=user)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/datasets")
def datasets():
    return render_template("datasets.html", title="Datasets")

@app.route("/learn")
def learn():
    return render_template("learn.html", title="Learn")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html", title="Tutorials")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/discuss")
def discuss():
    return render_template("discuss.html", title="Discuss")

@app.route("/send-suggestion", methods=["POST"])
def send_suggestion():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    SMTP_USER     = _os.environ.get("SMTP_USER", "team.ravendetections@gmail.com")
    SMTP_PASSWORD = _os.environ.get("SMTP_PASSWORD", "qpye xwcy ndfh pcbk")
    TEAM_EMAIL    = "team.ravendetections@gmail.com"

    category     = request.form.get("category", "General")
    message      = request.form.get("message", "").strip()
    sender_email = session.get("username", "Anonymous")

    if not message:
        return jsonify({"status": "error", "msg": "Message cannot be empty"}), 400

    if SMTP_USER == "PLACEHOLDER_EMAIL":
        print("[SUGGESTION] From: " + sender_email + " | Cat: " + category + " | Msg: " + message)
        return jsonify({"status": "ok", "msg": "Suggestion received!"})

    try:
        msg = MIMEMultipart("alternative")
        subject = "[RAVEN] " + category + " from " + sender_email
        msg["Subject"] = subject
        msg["From"]    = SMTP_USER
        msg["To"]      = TEAM_EMAIL
        msg["Reply-To"] = sender_email
        body = "<html><body><h2>New RAVEN Suggestion</h2>"
        body += "<p><b>From:</b> " + sender_email + "</p>"
        body += "<p><b>Category:</b> " + category + "</p>"
        body += "<p><b>Message:</b> " + message + "</p>"
        body += "</body></html>"
        msg.attach(MIMEText(body, "html"))
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, TEAM_EMAIL, msg.as_string())
        return jsonify({"status": "ok", "msg": "Suggestion sent!"})
    except Exception as e:
        print("[EMAIL ERROR] " + str(e))
        return jsonify({"status": "error", "msg": "Failed to send. Try again later."})



@app.route("/download-report/csv")
def download_report_csv():
    import csv, io, json
    from urllib.parse import unquote
    stats_param = request.args.get("stats", "[]")
    try:
        stats = json.loads(unquote(stats_param))
    except Exception:
        stats = []
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["#","Filename","Model","Resolution","Objects","Density","Time(ms)","FPS","Output File"])
    for i, row in enumerate(stats, 1):
        writer.writerow([i, row.get("name",""), row.get("model",""), row.get("size",""),
                         row.get("objects",""), row.get("density",""), row.get("time",""),
                         row.get("fps",""), row.get("outfile","")])
    output.seek(0)
    return send_file(io.BytesIO(output.getvalue().encode("utf-8")),
                     as_attachment=True, download_name="raven_report.csv", mimetype="text/csv")


@app.route("/download-report/pdf")
def download_report_pdf():
    import io as _io
    from datetime import datetime as dt
    files_param = request.args.get("files", "")
    filenames   = [f.strip() for f in files_param.split(",") if f.strip()]
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.units import cm
        from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                         Table, TableStyle, Image as RLImage, HRFlowable)
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
    except ImportError:
        return "Run: pip install reportlab", 500

    buf = _io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4,
                            topMargin=2*cm, bottomMargin=2*cm,
                            leftMargin=2*cm, rightMargin=2*cm)

    title_s = ParagraphStyle("T", fontSize=28, fontName="Helvetica-Bold",
                              textColor=colors.HexColor("#00cfff"), alignment=TA_CENTER, spaceAfter=6)
    sub_s   = ParagraphStyle("S", fontSize=11, fontName="Helvetica",
                              textColor=colors.HexColor("#8877cc"), alignment=TA_CENTER, spaceAfter=4)
    sec_s   = ParagraphStyle("H", fontSize=14, fontName="Helvetica-Bold",
                              textColor=colors.HexColor("#6644ff"), spaceBefore=18, spaceAfter=8)
    body_s  = ParagraphStyle("B", fontSize=10, fontName="Helvetica",
                              textColor=colors.HexColor("#cccccc"), spaceAfter=4)

    story = []
    story.append(Spacer(1, 1.5*cm))
    story.append(Paragraph("RAVEN", title_s))
    story.append(Paragraph("Detection Analysis Report", sub_s))
    story.append(Paragraph("Rotated-Annotation Vehicle and Entity Network", sub_s))
    story.append(Spacer(1, 0.4*cm))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#6644ff"), spaceAfter=12))
    story.append(Paragraph("Generated: " + dt.now().strftime("%d %B %Y, %H:%M"), sub_s))
    story.append(Paragraph("Total images: " + str(len(filenames)), sub_s))
    story.append(Spacer(1, 0.8*cm))

    story.append(Paragraph("Detection Results", sec_s))

    conn = get_db()
    outfile_stats = []
    try:
        with conn.cursor() as cur:
            for fname in filenames:
                safe = secure_filename(os.path.basename(fname))
                cur.execute("""SELECT filename,model_used,objects_found,inference_ms,fps,image_size
                               FROM detections WHERE output_path LIKE %s
                               ORDER BY detected_at DESC LIMIT 1""", ("%" + safe + "%",))
                row = cur.fetchone()
                if row:
                    outfile_stats.append(row)
    except Exception:
        pass
    finally:
        conn.close()

    if outfile_stats:
        tdata = [["Filename","Model","Objects","Time(ms)","FPS","Size"]]
        for r in outfile_stats:
            tdata.append([str(r.get("filename",""))[:22], str(r.get("model_used","")),
                          str(r.get("objects_found","")), str(round(r.get("inference_ms",0),1)),
                          str(round(r.get("fps",0),2)), str(r.get("image_size",""))])
        tbl = Table(tdata, repeatRows=1, colWidths=[4.5*cm,3.5*cm,2*cm,2.5*cm,2*cm,3*cm])
        tbl.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#6644ff")),
            ("TEXTCOLOR",(0,0),(-1,0),colors.white),
            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
            ("FONTSIZE",(0,0),(-1,-1),8),
            ("TEXTCOLOR",(0,1),(-1,-1),colors.HexColor("#cccccc")),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.HexColor("#0d0b22"),colors.HexColor("#100e28")]),
            ("GRID",(0,0),(-1,-1),0.3,colors.HexColor("#6644ff44")),
            ("ALIGN",(2,0),(-1,-1),"CENTER"),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ]))
        story.append(tbl)
    else:
        story.append(Paragraph("No database records found for this session.", body_s))

    story.append(Spacer(1, 0.8*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#6644ff44"), spaceAfter=8))
    story.append(Paragraph("Output Images", sec_s))

    img_added = 0
    for fname in filenames:
        safe  = secure_filename(os.path.basename(fname))
        fpath = os.path.join(OUTPUT_FOLDER, safe)
        if os.path.exists(fpath):
            try:
                story.append(Paragraph(safe, body_s))
                # Compress image before embedding
                try:
                    from PIL import Image as PILImage
                    with PILImage.open(fpath) as pil_img:
                        pil_img = pil_img.convert("RGB")
                        # Resize to max 800px wide to reduce PDF size
                        max_w = 800
                        if pil_img.width > max_w:
                            ratio = max_w / pil_img.width
                            new_h = int(pil_img.height * ratio)
                            pil_img = pil_img.resize((max_w, new_h), PILImage.LANCZOS)
                        import tempfile, os as _os
                        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
                        pil_img.save(tmp.name, "JPEG", quality=60, optimize=True)
                        tmp.close()
                        story.append(RLImage(tmp.name, width=16*cm, height=10*cm, kind="proportional"))
                        _os.unlink(tmp.name)
                except Exception:
                    story.append(RLImage(fpath, width=16*cm, height=10*cm, kind="proportional"))
                story.append(Spacer(1, 0.5*cm))
                img_added += 1
            except Exception:
                pass

    if img_added == 0:
        story.append(Paragraph("Output images expired (48h limit) or not found.", body_s))

    story.append(Spacer(1, 1*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#6644ff44"), spaceAfter=8))
    story.append(Paragraph("RAVEN - Detection that never blinks.", sub_s))

    def dark_bg(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor("#07051a"))
        canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
        canvas.restoreState()

    doc.build(story, onFirstPage=dark_bg, onLaterPages=dark_bg)
    buf.seek(0)
    return send_file(buf, as_attachment=True,
                     download_name="raven_report.pdf", mimetype="application/pdf")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
