from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os
import cv2
import time
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load model once
model = YOLO("models/yolov8n.pt")


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html", title="Home")


# ---------------- DETECTION ----------------
@app.route("/detection", methods=["GET", "POST"])
def detection():

    uploaded_images = []
    result_images = []
    stats = []

    total_time = 0
    total_objects = 0

    if request.method == "POST":

        files = request.files.getlist("image")
        mode = request.form.get("mode", "standard")
        conf = float(request.form.get("conf", 0.25))

        for file in files:

            if file and file.filename != "":

                # Unique naming
                unique_id = str(uuid.uuid4())[:8]
                filename = secure_filename(file.filename)
                name, ext = os.path.splitext(filename)

                input_filename = f"{name}_{unique_id}{ext}"
                output_filename = f"{name}_{unique_id}_out{ext}"

                input_path = os.path.join(UPLOAD_FOLDER, input_filename)
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)

                # Save input image
                file.save(input_path)
                uploaded_images.append(f"uploads/{input_filename}")

                # Read image
                image = Image.open(input_path).convert("RGB")
                img_array = np.array(image)

                h, w, _ = img_array.shape
                pixels = w * h

                # Inference
                start = time.time()
                results = model(img_array, conf=conf)
                end = time.time()

                inference_time = round((end - start) * 1000, 2)

                result = results[0]
                objects_detected = len(result.boxes)

                # Save detected image
                plotted = result.plot()
                cv2.imwrite(output_path, plotted)
                result_images.append(f"outputs/{output_filename}")

                # Extra performance metrics
                density = round(objects_detected / (pixels / 1_000_000), 2) if pixels else 0
                fps = round(1000 / inference_time, 2) if inference_time > 0 else 0

                stats.append({
                    "name": filename,
                    "size": f"{w} x {h}",
                    "objects": objects_detected,
                    "density": density,
                    "time": inference_time,
                    "fps": fps,
                    "model": "Standard YOLOv8" if mode == "standard" else "Orientation-Aware"
                })

                total_time += inference_time
                total_objects += objects_detected

    # Average summary
    avg_time = round(total_time / len(stats), 2) if stats else 0
    avg_objects = round(total_objects / len(stats), 2) if stats else 0
    avg_fps = round(1000 / avg_time, 2) if avg_time > 0 else 0

    return render_template(
        "detection.html",
        uploaded_images=uploaded_images,
        result_images=result_images,
        stats=stats,
        avg_time=avg_time,
        avg_objects=avg_objects,
        avg_fps=avg_fps
    )


# ---------------- OTHER PAGES ----------------
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


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
