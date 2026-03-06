import cv2
import numpy as np

img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df97e0d028.jpg")
if img is None:
    raise FileNotFoundError("Could not read input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary (often used for morphology)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((5, 5), np.uint8)     # structuring element
erosion = cv2.erode(binary, kernel, iterations=1)

cv2.imwrite("binary.jpg", binary)
cv2.imwrite("erosion.jpg", erosion)

cv2.imshow("Binary", binary)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()