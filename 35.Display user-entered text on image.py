import cv2

img = cv2.imread(r"C:\picturees\download.jpg")

text = input("elegant: ")

font = cv2.FONT_HERSHEY_SIMPLEX
position = (50, 50)
font_scale = 1
color = (0, 0, 255)   # Red
thickness = 2

cv2.putText(img, text, position, font, font_scale, color, thickness)

cv2.imshow("Text on Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()