import struct
import cv2
import socket
import threading
from cvzone.HandTrackingModule import HandDetector

# Function to handle socket communication
def send_data(sock, data):
    try:
        sock.sendall(struct.pack('i', data))  # Send as a 4-byte integer
        print(f"Sent: {data}")
    except Exception as e:
        print(f"Socket error: {e}")

# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

# SOCK_STREAM means TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "REPLACE IP HERE", 25001

try:
    # Connect to the server
    sock.connect((host, port))

    # Continuously get frames from the webcam
    while True:
        # Capture each frame from the webcam
        success, img = cap.read()

        # Find hands in the current frame
        hands, img = detector.findHands(img, draw=True, flipType=True)

        # Check if any hands are detected
        if hands:
            # Information for the hand detected
            hand1 = hands[0]
            fingers1 = detector.fingersUp(hand1)
            print(f'H1 = {fingers1.count(1)}', end=" ")
            data = fingers1.count(1)

            # Send the data in a separate thread
            threading.Thread(target=send_data, args=(sock, data)).start()

        # Display the image in a window
        cv2.imshow("Image", img)

        # Keep the window open and update it for each frame; wait for 1 millisecond between frames
        cv2.waitKey(1)

finally:
    # Close the socket and release the webcam
    sock.close()
    cap.release()
    cv2.destroyAllWindows()
