from pynput.mouse import Button, Controller
import pyautogui
import module3
import cv2
import time

def assign(frame, count_defects,fingertips,com):
    mouse = Controller()
    if count_defects == 0:
        distance = module3.dist(fingertips[0], com)
        if distance < 150:
            cv2.putText(frame, '0', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        elif distance < 200:
            cv2.putText(frame, 'Double Click', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            mouse.click(Button.left, 2)
            time.sleep(0.5)
        else:
            cv2.putText(frame, "Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
    elif count_defects == 1:
        cv2.putText(frame, "Right", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        pyautogui.moveRel(20, 0)
    elif count_defects == 2:
        cv2.putText(frame, "Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        pyautogui.moveRel(0, 20)
    elif count_defects == 3:
        cv2.putText(frame, "Left", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        pyautogui.moveRel(-20, 0)
    elif count_defects == 4:
        cv2.putText(frame, "Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        pyautogui.moveRel(0, -20)
    else:
        pass

    return frame
