import cv2
import numpy as np

def draw_circle(width, height):
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    center = (width // 2, height // 2)
    radius = min(width, height) // 4
    color = (255, 0, 0)   # Blue
    thickness = 3

    cv2.circle(img, center, radius, color, thickness)
    return img

w = int(input("Enter image width: "))
h = int(input("Enter image height: "))

output = draw_circle(w, h)

cv2.imshow("Circle Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()