from ultralytics import YOLO
model = YOLO("yolo11n.pt")

results = model("test.jpg")
for result in results:

    boxes = result.boxes

    for box in boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = model.names[class_id]
        coordinates = box.xyxy[0]

        x1, y1, x2, y2 = box.xyxy[0]

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        print("Object:", class_name)
        print("Confidence:", confidence)
        print(
            "Center:",
            center_x.item(),
            center_y.item()
        )

        print("----------------")

result.save(filename="detect.jpg")
print("detection complete!")
