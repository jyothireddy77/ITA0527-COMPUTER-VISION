import cv2
import numpy as np

img = cv2.imread(r"C:\picturees\download.jpg")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Example: remove green background
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)   # background mask
foreground = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

cv2.imshow("Original Image", img)
cv2.imshow("Background Removed", foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()