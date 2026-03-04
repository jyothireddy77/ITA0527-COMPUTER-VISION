import cv2

# Read image
img = cv2.imread(r"C:\picturees\1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")

if img is None:
    print("Error: Image not found")
    exit()

# Resize factor (adjust if needed)
scale = 0.5   # 50% of original size

width = int(img.shape[1] * scale)
height = int(img.shape[0] * scale)

# Resize original image
resized = cv2.resize(img, (width, height))

# Rotate 270° clockwise
rotated = cv2.rotate(resized, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Show images
cv2.imshow("Original Image", resized)
cv2.imshow("Rotated 270° Clockwise", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()