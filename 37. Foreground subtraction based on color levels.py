import cv2
import numpy as np

img = cv2.imread(r"C:\picturees\download.jpg")

# Convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Example: detect red foreground and remove it
lower1 = np.array([0, 120, 70])
upper1 = np.array([10, 255, 255])

lower2 = np.array([170, 120, 70])
upper2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = mask1 + mask2

# Remove foreground
background_only = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

cv2.imshow("Original Image", img)
cv2.imshow("Foreground Removed", background_only)
cv2.waitKey(0)
cv2.destroyAllWindows()