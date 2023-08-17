# Creating drawings in a black canvas

import numpy as np
import cv2

blank_image = 255 * np.ones((400, 600,3), dtype=np.uint8)
cv2.line(blank_image, (100, 100), (200, 200), (0, 255, 255), 5)
cv2.rectangle(blank_image, (100, 100), (200, 200), (0, 0, 255), 10)
cv2.circle(blank_image, (150, 150), 50, (0, 255, 0), 5)
cv2.putText(blank_image, "PRANJAL",(200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 255), 2)

cv2.imshow("Image", blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()