from ultralytics import YOLO
from language import extract_target
from policy import choose_action
import cv2


image = cv2.imread("test.jpg")
height, width, channels = image.shape


model = YOLO("yolo11n.pt")
results = model("test.jpg")


# NEW: collect all objects detected by YOLO
detected_objects = []

for result in results:
    for box in result.boxes:

        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        detected_objects.append(class_name)


# Show the detected objects
print("Detected objects:")

for obj in detected_objects:
    print("-", obj)


print()


# User instruction
instruction = input("Give the robot an instruction: ")


# LLM chooses the target using BOTH:
# instruction + detected objects
target = extract_target(
    instruction,
    detected_objects
)


print()
print("Instruction:", instruction)
print("Target:", target)
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


            # Convert PyTorch tensors to normal integers
            x1 = int(x1.item())
            y1 = int(y1.item())
            x2 = int(x2.item())
            y2 = int(y2.item())


            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2


            # Draw bounding box
            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                4
            )


            # Draw center point
            cv2.circle(
                image,
                (
                    round(center_x),
                    round(center_y)
                ),
                8,
                (0, 0, 255),
                -1
            )


            print("Target found!")
            print("Object:", class_name)

            print(
                "Confidence:",
                round(confidence, 2)
            )

            print(
                "Center:",
                (
                    round(center_x),
                    round(center_y)
                )
            )


            # Choose robot action
            action = choose_action(
                center_x,
                width
            )

            print(
                "Robot action:",
                action
            )


            # Draw action text
            cv2.putText(
                image,
                action,
                (100, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                (0, 255, 0),
                8
            )


if not found:
    print("Target not found.")


cv2.imwrite(
    "result.jpg",
    image
)

print("Saved result.jpg")