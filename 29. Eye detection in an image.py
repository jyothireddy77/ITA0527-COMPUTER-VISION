import cv2

# Load eye cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Read image
img = cv2.imread(r"C:\picturees\WhatsApp Image 2026-03-11 at 3.27.25 PM.jpeg")

if img is None:
    print("Error: Image not found.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect eyes
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

# Draw rectangles
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

print("Number of eyes detected:", len(eyes))

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()