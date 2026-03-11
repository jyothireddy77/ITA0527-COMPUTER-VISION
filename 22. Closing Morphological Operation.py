import cv2
import numpy as np

img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df97e0d028.jpg", 0)
kernel = np.ones((5, 5), np.uint8)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", binary)
cv2.imshow("Closing", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()