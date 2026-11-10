import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Load the image from which to read the QR code
image = cv2.imread('qrcode.png')

# Decode the QR code
decoded_objects = decode(image)

# Loop over all decoded objects
for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode('utf-8'))

    # Get the points of the QR code polygon
    points = obj.polygon

    # Convert the points into a format suitable for polylines
    if len(points) > 4:  # If the QR code is not a simple rectangle
        hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
        hull = np.int32(hull)
        cv2.polylines(image, [hull], isClosed=True, color=(0, 255, 0), thickness=2)
    else:
        # Directly draw the rectangle if the QR code is a simple polygon
        points = np.array(points, dtype=np.int32)
        cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

# Display the image with the rectangle
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
