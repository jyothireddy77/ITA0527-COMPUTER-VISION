import cv2

cap = cv2.VideoCapture(r"c:\picturees\WhatsApp Video 2026-03-02 at 3.22.33 PM.mp4")   # Use "video.mp4" for saved video

speed = 30   # Default normal speed

if not cap.isOpened():
    print("Error opening video")
else:
    print("Press N-Normal | S-Slow | F-Fast | Q-Quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video", frame)

        key = cv2.waitKey(speed) & 0xFF

        if key == ord('s'):      # Slow motion
            speed = 100
        elif key == ord('f'):    # Fast motion
            speed = 5
        elif key == ord('n'):    # Normal speed
            speed = 30
        elif key == ord('q'):    # Quit
            break

cap.release()
cv2.destroyAllWindows()