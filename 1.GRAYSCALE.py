import cv2

image = cv2.imread("C:/picturees/1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Image", image)
    cv2.imshow("Gray Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
