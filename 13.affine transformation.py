import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df7e0d028.jpg")

# Get image size
rows, cols, ch = img.shape

# Three points in original image
pts1 = np.float32([[50,50], [200,50], [50,200]])

# Corresponding points in transformed image
pts2 = np.float32([[10,100], [200,50], [100,250]])

# Compute Affine matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply transformation
dst = cv2.warpAffine(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()