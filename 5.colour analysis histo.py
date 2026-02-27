import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if image loaded properly
    if image is None:
        print("Image not found")
        return

    # Define color channels
    color_channels = ('b', 'g', 'r')

    plt.figure(figsize=(10, 5))

    # Loop through each channel
    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")
        plt.xlim([0, 256])  # Pixel intensity range

    # Graph labels
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


# Call the function
analyze_histogram("C:/picturees/1776119-2048x1365-desktop-hd-kawasaki-z900-background-image.jpg")