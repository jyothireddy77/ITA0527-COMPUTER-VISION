import cv2

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Read image
img = cv2.imread(r"C:\picturees\WhatsApp Image 2026-03-11 at 3.27.25 PM.jpeg")

if img is None:
    print("Error: Image not found.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

print("Number of faces detected:", len(faces))

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()