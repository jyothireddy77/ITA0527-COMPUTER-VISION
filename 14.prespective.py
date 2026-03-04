import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\picturees\2174886-1920x1080-desktop-1080p-marvel-comics-wallpaper-image.jpg")

rows, cols, ch = img.shape

# Four points in original image
pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])

# Corresponding points in output image
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])

# Perspective transform matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
dst = cv2.warpPerspective(img, M, (300,300))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformation", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()