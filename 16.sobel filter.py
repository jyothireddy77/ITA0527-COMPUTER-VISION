import cv2
import numpy as np

# Read input
img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df97e0d028.jpg")
if img is None:
    raise FileNotFoundError("Could not read input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Reduce noise (optional but helps)
gray_blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Sobel gradients
sx = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)

# Convert to uint8 images
abs_sx = cv2.convertScaleAbs(sx)
abs_sy = cv2.convertScaleAbs(sy)

# Combine gradients
sobel_combined = cv2.addWeighted(abs_sx, 0.5, abs_sy, 0.5, 0)

cv2.imwrite("sobel_x.jpg", abs_sx)
cv2.imwrite("sobel_y.jpg", abs_sy)
cv2.imwrite("sobel_combined.jpg", sobel_combined)

cv2.imshow("Original", img)
cv2.imshow("Sobel X", abs_sx)
cv2.imshow("Sobel Y", abs_sy)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()