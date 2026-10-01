import cv2
image = cv2.imread("test.jpg")

height, width, channels = image.shape
# print(type(image))
# print(image.shape)

print(height)
print(width)
print(channels)
print("top-left pixel:", image[0,0])
