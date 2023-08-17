import cv2
import numpy as np

image = cv2.imread("blue_car.jpg")
resize_image = cv2.resize(image, (500, 500))
hsv_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)

lower_color = np.array([100, 50, 50])
upper_color = np.array([130, 255, 255])

color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

detected_image = cv2.bitwise_and(resize_image, resize_image, mask=color_mask)

cv2.imshow("Image HSV", hsv_image)
cv2.imshow("Original Image", resize_image)
cv2.imshow("Mask Image", detected_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
