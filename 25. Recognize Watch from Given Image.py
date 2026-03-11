import cv2

# Read main image and watch template
img = cv2.imread(r"C:\picturees\TOP_TEN_WATCHES_61542.jpg")
template = cv2.imread(r"C:\picturees\TOP_TEN_WATCHES_61542n.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

w, h = gray_template.shape[::-1]

# Template matching
result = cv2.matchTemplate(gray_img, gray_template, cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

cv2.imshow("Detected Watch", img)
cv2.waitKey(0)
cv2.destroyAllWindows()