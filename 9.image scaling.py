import cv2

img = cv2.imread(r"C:\picturees\2174886-1920x1080-desktop-1080p-marvel-comics-wallpaper-image.jpg")

if img is None:
    print("Image not loaded.")
else:
    height, width = img.shape[:2]

    # Smaller image (50%)
    small = cv2.resize(img, (int(width * 0.5), int(height * 0.5)))

    # Bigger image (120%)
    big = cv2.resize(img, (int(width * 1.2), int(height * 1.2)))

    cv2.imshow("Original", img)
    cv2.imshow("Smaller (5%)", small)
    cv2.imshow("Bigger (40%)", big)

    cv2.waitKey(0)
    cv2.destroyAllWindows()