import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Load images to display when the index finger reaches any corner
photos = {
    'top_left': cv2.imread("oten.jpg"),
    'top_right': cv2.imread("oten2.jpg"),
    'bottom_left': cv2.imread("oten3.jpg"),
    'bottom_right': cv2.imread("oten4.jpg"),
}

# Check if images are loaded properly
for corner, photo in photos.items():
    if photo is None:
        print(f"Error: Image not found at path '{corner}.jpg'. Please provide a valid image file.")
        exit()

# Start webcam
cap = cv2.VideoCapture(0)

# Track whether the photo window is already open
photo_window_open = False

# Function to display the false button in the appropriate corner
def display_false_button(frame, corner):
    height, width, _ = frame.shape
    button_color = (0, 0, 255)  # Red color for false button
    button_size = (100, 40)

    if corner == 'top_left':
        cv2.rectangle(frame, (10, 10), (10 + button_size[0], 10 + button_size[1]), button_color, -1)
        cv2.putText(frame, "False", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    elif corner == 'top_right':
        cv2.rectangle(frame, (width - button_size[0] - 10, 10),
                      (width - 10, 10 + button_size[1]), button_color, -1)
        cv2.putText(frame, "False", (width - button_size[0] - 10 + 10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2)
    elif corner == 'bottom_left':
        cv2.rectangle(frame, (10, height - button_size[1] - 10),
                      (10 + button_size[0], height - 10), button_color, -1)
        cv2.putText(frame, "False", (20, height - button_size[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2)
    elif corner == 'bottom_right':
        cv2.rectangle(frame, (width - button_size[0] - 10, height - button_size[1] - 10),
                      (width - 10, height - 10), button_color, -1)
        cv2.putText(frame, "False", (width - button_size[0] - 10 + 10, height - button_size[1] + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Function to draw the detection areas (rectangles for each corner)
def draw_detection_area(frame, corner):
    height, width, _ = frame.shape
    rect_color = (0, 255, 0)  # Green for detection areas
    rect_thickness = 2
    rect_padding = 80  # Increase size of the detection zone (bigger padding)

    # Adjust the detection zone size (larger)
    large_rect_padding = 100  # Larger padding for a bigger detection area

    if corner == 'top_left':
        cv2.rectangle(frame, (10, 10), (10 + large_rect_padding, 10 + large_rect_padding), rect_color, rect_thickness)
    elif corner == 'top_right':
        cv2.rectangle(frame, (width - large_rect_padding - 10, 10),
                      (width - 10, large_rect_padding + 10), rect_color, rect_thickness)
    elif corner == 'bottom_left':
        cv2.rectangle(frame, (10, height - large_rect_padding - 10),
                      (10 + large_rect_padding, height - 10), rect_color, rect_thickness)
    elif corner == 'bottom_right':
        cv2.rectangle(frame, (width - large_rect_padding - 10, height - large_rect_padding - 10),
                      (width - 10, height - 10), rect_color, rect_thickness)

# Start webcam capture
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty frame.")
            continue

        # Get frame dimensions
        height, width, _ = frame.shape

        # Convert to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for hand landmarks
        results = hands.process(rgb_frame)

        # Draw hand landmarks and check for the index finger gesture
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                )

                # Get the position of the index finger tip
                index_tip_x = int(hand_landmarks.landmark[8].x * width)
                index_tip_y = int(hand_landmarks.landmark[8].y * height)

                # Check if index finger is within the detection zones (near the edges)
                corner = None
                if (index_tip_x < 100 and index_tip_y < 100):  # Top-left corner
                    corner = 'top_left'
                elif (index_tip_x > width - 100 and index_tip_y < 100):  # Top-right corner
                    corner = 'top_right'
                elif (index_tip_x < 100 and index_tip_y > height - 100):  # Bottom-left corner
                    corner = 'bottom_left'
                elif (index_tip_x > width - 100 and index_tip_y > height - 100):  # Bottom-right corner
                    corner = 'bottom_right'

                # Draw the detection area for the detected corner
                if corner:
                    draw_detection_area(frame, corner)
                    display_false_button(frame, corner)

                    # Check if index finger is in any corner, show the respective photo if so
                    if corner in photos:
                        print(f"Index finger detected in the {corner} corner!")
                        if not photo_window_open:
                            photo_window_open = True
                            cv2.namedWindow(f"{corner} Photo Display", cv2.WINDOW_NORMAL)
                            resized_photo = cv2.resize(photos[corner], (500, 500))  # Resize the photo for display
                            cv2.imshow(f"{corner} Photo Display", resized_photo)

        # Display the webcam feed
        cv2.imshow('Finger Tracker', frame)

        # Check if 'q' is pressed or photo window is closed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty(f"{corner} Photo Display", cv2.WND_PROP_VISIBLE) < 1:
            photo_window_open = False

cap.release()
cv2.destroyAllWindows()
