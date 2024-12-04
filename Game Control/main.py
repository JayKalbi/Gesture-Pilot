import cv2
import mediapipe as mp
import time
import numpy as np
from controlkeys import right_pressed, left_pressed, up_pressed, down_pressed
from controlkeys import KeyOn, KeyOff

left_key_pressed = left_pressed
right_key_pressed = right_pressed
up_key_pressed = up_pressed
down_key_pressed = down_pressed

time.sleep(2.0)
current_key_pressed = set()

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        key_count = 0
        key_pressed = 0
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []
        text = ''
        if results.multi_hand_landmarks:
            for idx, classification in enumerate(results.multi_handedness):
                if classification.classification[0].index == idx:
                    label = classification.classification[0].label
                    text = '{}'.format(label)
                else:
                    label = classification.classification[0].label
                    text = '{}'.format(label)
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        fingers = []

        if len(lmList) != 0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            total = fingers.count(1)
            if total == 4 and text == "Right":
                cv2.rectangle(image, (400, 300), (600, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(image, "LEFT", (400, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 255), 5)

                KeyOn(left_key_pressed)
                key_pressed = left_key_pressed
                keyPressed = True
                current_key_pressed.add(left_key_pressed)
                key_count += 1

            elif total == 5 and text == "Left":
                cv2.rectangle(image, (400, 300), (600, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(image, "RIGHT", (400, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 255, 0), 5)

                KeyOn(right_key_pressed)
                key_pressed = right_key_pressed
                keyPressed = True
                current_key_pressed.add(right_key_pressed)
                key_count += 1

            elif total == 1:
                cv2.rectangle(image, (400, 300), (600, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(image, "UP", (400, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 255, 0), 5)

                KeyOn(up_key_pressed)
                key_pressed = up_key_pressed
                keyPressed = True
                current_key_pressed.add(up_key_pressed)
                key_count += 1

            elif total == 0:
                cv2.rectangle(image, (400, 300), (600, 425), (255, 255, 255), cv2.FILLED)
                cv2.putText(image, "DOWN", (400, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 255, 0), 5)

                KeyOn(down_key_pressed)
                key_pressed = down_key_pressed
                keyPressed = True
                current_key_pressed.add(down_key_pressed)
                key_count += 1

        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                KeyOff(key)
            current_key_pressed = set()

        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key_pressed != key:
                    KeyOff(key)
            current_key_pressed = set()
            current_key_pressed.add(key_pressed)

        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
