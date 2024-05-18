from ultralytics import YOLO 

model = YOLO('yolov8n.pt')

results = model.track(source="./resources/test.mp4", show=True)