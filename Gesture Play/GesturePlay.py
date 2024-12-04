import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Initialize Mediapipe Hand detection model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Set up camera using OpenCV for default webcam
cap = cv2.VideoCapture(0)

# Variables
width, height = 640, 480  # Frame size
frameR = 100  # Frame region for gesture detection
pTime = 0  # Previous time for FPS calculation
gestureThreshold = 300  # Gesture threshold for action
wScr, hScr = pyautogui.size()  # Get screen size

# Function to check fingers up/down
def fingers_up(landmarks):
    fingers = []
    # Thumb
    if landmarks[4][0] > landmarks[3][0]:
        fingers.append(1)
    else:
        fingers.append(0)
    # 4 Fingers
    for id in range(8, 21, 4):
        if landmarks[id][1] < landmarks[id - 2][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

# Main loop
while True:
    # Read frame from camera
    success, img = cap.read()

    # Convert image to RGB for Mediapipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect hand
    result = hands.process(img_rgb)

    # If hand is detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks and connections
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the landmark positions
            lmList = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([cx, cy])

            if lmList:
                x1, y1 = lmList[8]  # Index finger tip
                x2, y2 = lmList[12]  # Middle finger tip
                fingers = fingers_up(lmList)

                if fingers == [0, 1, 0, 0, 0]:  # Only index finger up
                    cv2.putText(img, "Cursor", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                    # Move cursor
                    x3 = np.interp(x1, (frameR, width - frameR), (0, wScr))
                    y3 = np.interp(y1, (frameR, height - frameR), (0, hScr))
                    pyautogui.moveTo(wScr + 10 - x3, y3)
                    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

                if fingers == [0, 1, 1, 0, 0]:  # Index and middle finger up
                    distance = np.hypot(x2 - x1, y2 - y1)
                    if distance < 35:  # Fingers close together
                        pyautogui.click()

                # Check for gestures based on hand position
                cx, cy = lmList[9]  # Center of palm
                if cy <= gestureThreshold:
                    if fingers == [1, 0, 0, 0, 0]:
                        cv2.putText(img, "Fast Forward", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.press('right')
                    elif fingers == [1, 0, 0, 0, 1]:
                        cv2.putText(img, "Rewind", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.press('left')
                    elif fingers == [1, 1, 1, 1, 1]:
                        cv2.putText(img, "Play / Pause", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.press('space')
                    elif fingers == [0, 1, 1, 1, 0]:
                        cv2.putText(img, "Volume Up", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.hotkey('shift', 'up')
                    elif fingers == [0, 1, 1, 1, 1]:
                        cv2.putText(img, "Volume Down", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.hotkey('shift', 'down')
                    elif fingers == [1, 1, 1, 0, 0]:
                        cv2.putText(img, "Scroll Down", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.scroll(-100)
                    elif fingers == [0, 0, 1, 1, 1]:
                        cv2.putText(img, "Scroll Up", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
                        pyautogui.scroll(100)

    # Frame rate calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Display the image
    cv2.imshow("Image", img)

    # Quit if 'q' is pressed
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
