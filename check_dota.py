from ultralytics import YOLO
model = YOLO("models/DOTA_Model.pt")
print("DOTA class names:")
for i, name in model.names.items():
    print(f"  {i}: {name}")