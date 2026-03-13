import cv2

img = cv2.imread(r"C:\picturees\images.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load built-in Haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

count = len(faces)
print("Number of faces detected:", count)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()