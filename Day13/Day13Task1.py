import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Biden.jpg')
resized_img = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(resized_img, (x, y), (x+w, y+h), (255, 255, 0), 2)

cv2.imshow('img', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
