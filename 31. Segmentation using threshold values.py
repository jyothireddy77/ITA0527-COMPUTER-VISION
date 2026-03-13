import cv2

# Load image
img = cv2.imread(r"C:\picturees\download.jpg", 0)   # grayscale image

# Given threshold value
threshold_value = 127

# Apply segmentation
_, segmented = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

# Show output
cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()