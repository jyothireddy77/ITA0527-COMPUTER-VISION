import cv2

img = cv2.imread(r"C:\picturees\1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")

if img is None:
    print("Image not loaded.")
else:
    # Flip along Y-axis (horizontal flip)
    flipped = cv2.flip(img, 1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Y-Axis Rotated (Flipped)", flipped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()