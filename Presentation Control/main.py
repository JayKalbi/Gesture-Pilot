
import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Variables
width, height = 1280, 720
folderpath = "Presentation"

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Get the list of presentation images
pathImages = sorted(os.listdir(folderpath), key=len)

# Variables
imgNumber = 0
hs, ws = int(120 * 1), int(213 * 1)
gestureThreshold = 300
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationNumber = 0
annotationStart = False

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Import Images
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderpath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 8)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']
        
        
      
      
        # Constraint values for easier drawing
        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height - 150], [0, height]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold:  # if hand is at the height of the face
            annotationStart = False

            # Gesture 1 - Left (All fingers up with left hand)
            if fingers == [1, 1, 1, 1, 1] and hand['type'] == 'Left':
                annotationStart = False
            
                buttonPressed = True
                annotations = [[]]
                annotationNumber = 0
                if imgNumber < len(pathImages) - 1:
                    imgNumber += 1
                else:
                    imgNumber = 0  # Cycle to the first image

            # Gesture 2 - Right (All fingers up with Right hand)
            if fingers == [1, 1, 1, 1, 1] and hand['type'] == 'Right':
                annotationStart = False
                print("Left")
                buttonPressed = True
                annotations = [[]]
                annotationNumber = 0
                if imgNumber > 0:
                    imgNumber -= 1
                else:
                    imgNumber = len(pathImages) - 1  # Cycle to the last image

        # Gesture 3 - Show Pointer (Index finger only)
        if fingers == [0, 1, 0, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotationStart = False

        # Gesture 4 - Draw Pointer (Index and middle fingers up)
        if fingers == [0, 1, 1, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        # Gesture 5 - Erase (Middle three fingers up)
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPressed = True
    
    else:
        annotationStart = False

    # Button Pressed Iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 200), 8)

    # Adding webcam image on the slide
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
