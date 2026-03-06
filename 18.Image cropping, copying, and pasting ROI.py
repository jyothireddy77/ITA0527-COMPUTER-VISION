import cv2

img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df97e0d028.jpg")
if img is None:
    raise FileNotFoundError("Could not read input.jpg")

h, w = img.shape[:2]

# Define ROI (x, y, width, height)
x, y, rw, rh = 50, 50, 200, 200

# Crop ROI
roi = img[y:y+rh, x:x+rw].copy()

# Paste ROI to a new location (top-right example)
new_x = w - rw - 20
new_y = 20

# Safety check
if new_y + rh > h or new_x + rw > w:
    raise ValueError("Paste location exceeds image bounds")

img[new_y:new_y+rh, new_x:new_x+rw] = roi

cv2.imwrite("roi_pasted.jpg", img)

cv2.imshow("ROI", roi)
cv2.imshow("ROI Pasted", img)
cv2.waitKey(0)
cv2.destroyAllWindows()