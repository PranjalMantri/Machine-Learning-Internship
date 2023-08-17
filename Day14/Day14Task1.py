import cv2
import numpy as np

image = cv2.imread("blue_car.jpg")
resize_image = cv2.resize(image, (500, 500))
hsv_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)

lower_color = np.array([100, 50, 50])
upper_color = np.array([130, 255, 255])

color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

color = np.array([0, 0, 255])
red_color = np.full_like(resize_image, color)

detected_image = cv2.bitwise_and(red_color, red_color, mask=color_mask)

inverse_color_mask = cv2.bitwise_not(color_mask)
non_masked_partition = cv2.bitwise_and(resize_image, resize_image, mask=inverse_color_mask)
result_image = cv2.add(detected_image, non_masked_partition)

cv2.imshow("Converting to Red", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
