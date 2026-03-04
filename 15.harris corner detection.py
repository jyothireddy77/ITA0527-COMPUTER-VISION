import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df7e0d028.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

# Apply Harris corner detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate result for marking
dst = cv2.dilate(dst, None)

# Mark corners in red
img[dst > 0.01 * dst.max()] = [0,0,255]

# Display images
cv2.imshow("Harris Corner Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()