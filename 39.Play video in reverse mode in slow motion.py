import cv2

video_path = r"C:\picturees\WhatsApp Video 2026-03-13 at 1.57.40 PM.mp4"
cap = cv2.VideoCapture(video_path)

frames = []

# Read all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play in reverse slow motion
for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion Video", frame)

    # Delay increased for slow motion
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()