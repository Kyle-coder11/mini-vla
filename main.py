from ultralytics import YOLO
from language import extract_target

model = YOLO("yolo11n.pt")
results = model("test.jpg")
instruction = input("Give the robot an instruction: ")

target = extract_target(instruction)

print()
print("instruction:", instruction)
print("target:", target)
print()

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
            print("Target found!")
            print("Object:", class_name)

            print(
                "Confidence:",
                round(confidence, 2)
            )

            print(
                "Center:",
                (
                    round(center_x.item()),
                    round(center_y.item())
                )
            )

        if not found:
            print("target not found")
