import cv2
import numpy as np

def draw_rectangle(width, height):
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    start_point = (width // 4, height // 4)
    end_point = (3 * width // 4, 3 * height // 4)

    color = (0, 255, 0)   # Green
    thickness = 3

    cv2.rectangle(img, start_point, end_point, color, thickness)
    return img

w = int(input("Enter image width: "))
h = int(input("Enter image height: "))

output = draw_rectangle(w, h)

cv2.imshow("Rectangle Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()