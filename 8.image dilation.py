import cv2
import numpy as np

# Read the image (keep image in same folder as python file)
img = cv2.imread(r"C:\picturees\1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")

# Check if image loaded
if img is None:
    print("Image not loaded. Check file path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create kernel (3x3 matrix)
    kernel = np.ones((3,3), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(gray, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", gray)
    cv2.imshow("Dilated Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()