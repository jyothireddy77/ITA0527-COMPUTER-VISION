import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\picturees\1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")

# Check if image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Adjustable size
width = 600
height = 400

# Resize original image
original = cv2.resize(img, (width, height))

# Rotate 180° along Y-axis (horizontal flip)
rotated = cv2.flip(original, 1)

# Combine images side by side
combined = np.hstack((original, rotated))

# Show result
cv2.imshow("Original (Left) | Rotated Y-axis (Right)", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()