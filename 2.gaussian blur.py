import cv2

# Read image
image = cv2.imread("C:/picturees/1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")

if image is None:
    print("Image not found")
else:
    # Resize image (width, height)
    resized = cv2.resize(image, (600, 400))   # Change size if needed

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(resized, (5, 5), 0)

    # Show images
    cv2.imshow("Resized Image", resized)
    cv2.imshow("Gaussian Blurred Image", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()