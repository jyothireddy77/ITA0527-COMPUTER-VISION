import cv2

# Input and output video paths
input_video = r"C:\picturees\WhatsApp Video 2026-03-02 at 3.52.37 PM.mp4"
output_video = "reversed_output.mp4"

# Open input video
cap = cv2.VideoCapture(input_video)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Read all frames
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Reverse frames
frames.reverse()

# Create output writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Write reversed frames
for frame in frames:
    out.write(frame)

out.release()

print("Reversed video saved as", output_video)