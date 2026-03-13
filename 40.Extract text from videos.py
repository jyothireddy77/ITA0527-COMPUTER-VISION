import cv2
import pytesseract

# Set tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

video = cv2.VideoCapture(r"C:\picturees\WhatsApp Video 2026-03-02 at 3.22.33 PM.mp4")

frame_count = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_count += 1

    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    if text.strip() != "":
        print("Detected Text:", text)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()