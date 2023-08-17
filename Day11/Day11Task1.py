# Processing images using opencv and storing it in a folder

import cv2
import os

image_directory = "C:\Pranjal\Practicals\ML Internship\Day11\Images\Images"
images = os.listdir(image_directory)

os.mkdir(image_directory + "/" + "resized_images")
os.mkdir(image_directory + "/" + "blur_images")
os.mkdir(image_directory + "/" + "edges")
os.mkdir(image_directory + "/" + "gray_images")

for i in range(len(images)):
    path = image_directory + "/" + images[i]

    img = cv2.imread(path)

    print(images[i])
    resized_image = cv2.resize(img, (500, 500))

    blur_image = cv2.GaussianBlur(resized_image, (5, 5), 0)
    edges = cv2.Canny(img, threshold1=100, threshold2=100)
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    os.chdir(image_directory + "/" + "resized_images")
    filename = "Resized_image" + str(i + 1) + ".jpeg"
    cv2.imwrite(filename, resized_image)

    os.chdir(image_directory + "/" + "blur_images")
    filename = "Blur_image" + str(i + 1) + ".jpeg"
    cv2.imwrite(filename, blur_image)

    os.chdir(image_directory + "/" + "edges")
    filename = "Edges" + str(i + 1) + ".jpeg"
    cv2.imwrite(filename, edges)

    os.chdir(image_directory + "/" + "gray_images")
    filename = "Gray_image" + str(i + 1) + ".jpeg"
    cv2.imwrite(filename, gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
