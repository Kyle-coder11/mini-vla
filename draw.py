import cv2
image = cv2.imread("test.jpg")

cv2.rectangle(image, (100,100), (400, 400), (0, 255, 0), 5)

cv2.putText(image, "cup", (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


cv2.imwrite("output.jpg", image)
print("saved output.jpa")
