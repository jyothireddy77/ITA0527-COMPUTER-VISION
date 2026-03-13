import cv2
import numpy as np

def create_colored_boxes(width, height):
    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Box size = 1/10th of image size
    box_w = width // 10
    box_h = height // 10

    # Top-left: Black
    img[0:box_h, 0:box_w] = (0, 0, 0)

    # Top-right: Blue
    img[0:box_h, width-box_w:width] = (255, 0, 0)

    # Bottom-left: Green
    img[height-box_h:height, 0:box_w] = (0, 255, 0)

    # Bottom-right: Red
    img[height-box_h:height, width-box_w:width] = (0, 0, 255)

    return img

w = int(input("Enter image width: "))
h = int(input("Enter image height: "))

output = create_colored_boxes(w, h)

cv2.imshow("Colored Boxes Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()