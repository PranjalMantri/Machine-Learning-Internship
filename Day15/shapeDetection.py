import cv2

image = cv2.imread("shape.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 100)

c, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in c:
    ep = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, ep, True)

    num_v = len(approx)

    if num_v == 3:
        shape_name = "Triangle"
    elif num_v == 4:
        shape_name = "Rectangle"
    elif num_v == 5:
        shape_name = "Pentagon"
    elif num_v == 6:
        shape_name = "Hexagon"
    else:
        shape_name = "Circle"

    print(shape_name)

    cv2.drawContours(image, [contour], -1, (0, 0, 0), 2)
    x, y = contour[0][0]
    cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()