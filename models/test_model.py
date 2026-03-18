from ultralytics import YOLO

# DOTA model
dota_model = YOLO("dota_model.pt")
dota_model.predict("image.jpg", save=True)

# HRSC model
hrsc_model = YOLO("hrsc_model.pt")
hrsc_model.predict("ship_image.jpg", save=True)