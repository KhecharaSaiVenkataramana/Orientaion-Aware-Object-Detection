"""
OAOD Project — Flask App with Cloud MySQL Database
Original website by: Anudeep Gonuguntla
Database integration: added by your team

What's new vs the original app.py:
  - Connects to Clever Cloud MySQL on startup
  - Creates a 'detections' table automatically
  - Saves every detection result to the cloud database
  - New route: /history  — view all past detections
"""

from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
import cv2
import time
from werkzeug.utils import secure_filename
import uuid

# ── NEW: Database imports ──────────────────────────────────────────────────────
import pymysql
from datetime import datetime

app = Flask(__name__)

# ── FOLDERS ───────────────────────────────────────────────────────────────────
UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ── LOAD MODELS ───────────────────────────────────────────────────────────────
STANDARD_MODEL = YOLO("models/yolov8n.pt")
DOTA_MODEL     = YOLO("models/DOTA_Model.pt")
HRSC_MODEL     = YOLO("models/HRSC_Model.pt")


# ── DATABASE CONFIG (Clever Cloud MySQL) ──────────────────────────────────────
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
    """Open a fresh connection to MySQL. Always close after use."""
    return pymysql.connect(**DB_CONFIG)


def init_db():
    """
    Create the detections table if it doesn't exist yet.
    Called once when the server starts.
    """
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS detections (
                    id              INT AUTO_INCREMENT PRIMARY KEY,
                    filename        VARCHAR(255)    NOT NULL,
                    model_used      VARCHAR(50)     NOT NULL,
                    objects_found   INT             NOT NULL,
                    inference_ms    FLOAT           NOT NULL,
                    fps             FLOAT           NOT NULL,
                    image_size      VARCHAR(30)     NOT NULL,
                    density         FLOAT           NOT NULL,
                    input_path      VARCHAR(512)    NOT NULL,
                    output_path     VARCHAR(512)    NOT NULL,
                    detected_at     DATETIME        NOT NULL
                )
            """)
        conn.commit()
        print("Database ready — detections table OK.")
    finally:
        conn.close()


def save_detection(filename, model_used, objects_found, inference_ms,
                   fps, image_size, density, input_path, output_path):
    """
    Save one detection result to the cloud database.
    Called after every successful inference.
    """
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO detections
                    (filename, model_used, objects_found, inference_ms,
                     fps, image_size, density, input_path, output_path, detected_at)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                filename, model_used, objects_found, inference_ms,
                fps, image_size, density, input_path, output_path,
                datetime.utcnow()
            ))
        conn.commit()
    except Exception as e:
        import traceback
        print(f"[DB ERROR] {type(e).__name__}: {e}")
        traceback.print_exc()
    finally:
        conn.close()


def get_all_detections(limit=50):
    """Fetch the most recent detections from the database."""
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM detections
                ORDER BY detected_at DESC
                LIMIT %s
            """, (limit,))
            return cur.fetchall()
    except Exception as e:
        print(f"[DB WARNING] Could not fetch history: {e}")
        return []
    finally:
        conn.close()


# ── INITIALISE DATABASE ON STARTUP ────────────────────────────────────────────
init_db()


# ── ROUTES ────────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/detection", methods=["GET", "POST"])
def detection():
    uploaded_images = []
    result_images   = []
    stats           = []
    total_time      = 0
    total_objects   = 0

    if request.method == "POST":
        files = request.files.getlist("image")
        mode  = request.form.get("mode", "standard")
        conf  = float(request.form.get("conf", 0.25))

        # Model selection
        if mode == "dota":
            model      = DOTA_MODEL
            model_name = "DOTA-OBB"
        elif mode == "hrsc":
            model      = HRSC_MODEL
            model_name = "HRSC-OBB"
        else:
            model      = STANDARD_MODEL
            model_name = "Standard YOLOv8"

        for file in files:
            if file and file.filename != "":

                # Unique filenames
                unique_id        = str(uuid.uuid4())[:8]
                filename         = secure_filename(file.filename)
                name, ext        = os.path.splitext(filename)
                input_filename   = f"{name}_{unique_id}{ext}"
                output_filename  = f"{name}_{unique_id}_out{ext}"
                input_path       = os.path.join(UPLOAD_FOLDER, input_filename)
                output_path      = os.path.join(OUTPUT_FOLDER, output_filename)

                # Save uploaded image
                file.save(input_path)
                uploaded_images.append(f"uploads/{input_filename}")

                # Read image
                image     = Image.open(input_path).convert("RGB")
                img_array = np.array(image)
                h, w, _   = img_array.shape
                pixels    = w * h

                # Run inference
                start   = time.time()
                results = model(img_array, conf=conf)
                end     = time.time()
                inference_time = round((end - start) * 1000, 2)

                result = results[0]

                # Count detections (works for both standard YOLO and OBB)
                if result.boxes is not None and len(result.boxes) > 0:
                    objects_detected = len(result.boxes)
                elif hasattr(result, "obb") and result.obb is not None:
                    objects_detected = len(result.obb)
                else:
                    objects_detected = 0

                # Save annotated output image
                plotted = result.plot()
                cv2.imwrite(output_path, plotted)
                result_images.append(f"outputs/{output_filename}")

                # Performance metrics
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
                    "model":   model_name
                })

                total_time    += inference_time
                total_objects += objects_detected

                # ── NEW: Save to cloud MySQL ───────────────────────────────
                save_detection(
                    filename      = filename,
                    model_used    = model_name,
                    objects_found = objects_detected,
                    inference_ms  = inference_time,
                    fps           = fps,
                    image_size    = img_size,
                    density       = density,
                    input_path    = input_path,
                    output_path   = output_path,
                )

        # Average metrics
        avg_time    = round(total_time / len(stats), 2) if stats else 0
        avg_objects = round(total_objects / len(stats), 2) if stats else 0
        avg_fps     = round(1000 / avg_time, 2) if avg_time > 0 else 0

        return render_template(
            "detection.html",
            uploaded_images = uploaded_images,
            result_images   = result_images,
            stats           = stats,
            avg_time        = avg_time,
            avg_objects     = avg_objects,
            avg_fps         = avg_fps
        )

    return render_template("detection.html")


# ── NEW: History route — view all past detections ─────────────────────────────
@app.route("/history")
def history():
    """
    Shows a table of all past detections from the cloud database.
    Add a link to this page from your navbar: href="/history"
    """
    records = get_all_detections(limit=50)
    return render_template("history.html", records=records)


# ── EXISTING ROUTES (unchanged) ───────────────────────────────────────────────
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


# ── RUN SERVER ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
