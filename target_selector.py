from ultralytics import YOLO
model = YOLO("yolo11n.pt")
results = model("test.jpg")



target = input("What object should the robot find?").lower()
found = False

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        if class_name == target:
            found = True
            confidence = float(box.conf[0])
            x1, y1, x2, y2 = box.xyxy[0]
            center_x = (x1+x2)/2
            center_y = (y1+y2)/2
            print("target found!")
            print("object:", class_name)
            print("confidence", round(confidence,2))
            print("Center:",
                (
                    round(center_x.item()),
                    round(center_y.item())
                ))
            
        if found == False:
            print("target no found!")