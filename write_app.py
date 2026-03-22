import os

code = '''from flask import (Flask, render_template, request,
                   redirect, url_for, session, send_file)
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
app.secret_key = "oaod_secret_key_change_in_production"

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

STANDARD_MODEL = YOLO("models/yolov8n.pt")
DOTA_MODEL     = YOLO("models/DOTA_Model.pt")
HRSC_MODEL     = YOLO("models/HRSC_Model.pt")
FAIR1M_MODEL   = YOLO(r"C:\\Users\\khech\\OAOD Project\\runs\\obb\\FAIR1M_Vehicle_Model_v2\\weights\\best.pt")

DOTA_VEHICLE_CLASSES = {9, 10}
FAIR1M_CLASSES = [
    "small-car", "van", "dump-truck", "cargo-truck",
    "other-vehicle", "bus", "excavator", "trailer",
    "truck-tractor", "tractor"
]
FINE_GRAINED_CONF = 0.3

DB_CONFIG = {
    "host":     "bg0mwot4am56wljm4ims-mysql.services.clever-cloud.com",
    "port":     3306,
    "user":     "uky8zedsjiowpw7m",
    "password": "wjLZKLUHi5GseDFcv7mL",
    "database": "bg0mwot4am56wljm4ims",
    "connect_timeout": 10,
    "cursorclass": pymysql.cursors.DictCursor
}

def get_db():
    return pymysql.connect(**DB_CONFIG)

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

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
'''

path = os.path.join("C:\\Users\\khech\\OAOD Project\\website", "app.py")
with open(path, "w", encoding="utf-8") as f:
    f.write(code)

c = open(path, encoding="utf-8").read()
print("Written:", len(c), "chars")
print("HAS AUTH:", "login_required" in c)
print("HAS FAIR1M:", "FAIR1M_MODEL" in c)
print("HAS dota_fg:", "dota_fg" in c)
print("HAS CLEANUP:", "cleanup_old_outputs" in c)
print("HAS DOWNLOAD:", "download_file" in c)