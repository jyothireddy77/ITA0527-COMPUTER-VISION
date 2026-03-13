import cv2

# Load face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load smile cascade
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# Read image
img = cv2.imread(r"C:\picturees\download.jpg")

if img is None:
    print("Error: Image not found.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces first
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Detect smile inside each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    face_gray = gray[y:y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        face_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 25)
    )

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(face_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)

print("Smile detection completed")

cv2.imshow("Smile Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()