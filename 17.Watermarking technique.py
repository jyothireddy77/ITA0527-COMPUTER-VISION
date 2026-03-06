import cv2
import numpy as np

img = cv2.imread(r"C:\picturees\a2b93c7bdeb07b7dc051b75df97e0d028.jpg")
if img is None:
    raise FileNotFoundError("Could not read input.jpg")

overlay = img.copy()
output = img.copy()

watermark_text = "JR"
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1.5
thickness = 3

(h, w) = img.shape[:2]
(text_w, text_h), baseline = cv2.getTextSize(watermark_text, font, scale, thickness)

# Position bottom-right with padding
x = w - text_w - 20
y = h - 20

# Draw text on overlay (white)
cv2.putText(overlay, watermark_text, (x, y), font, scale, (255, 255, 255), thickness, cv2.LINE_AA)

# Blend overlay with original for transparency
alpha = 0.35  # 0=transparent, 1=solid
cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

cv2.imwrite("watermarked.jpg", output)

cv2.imshow("Original", img)
cv2.imshow("Watermarked", output)
cv2.waitKey(0)
cv2.destroyAllWindows()