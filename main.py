import module1
import module2
import module3
import module4
import module5
import pyautogui
import cv2
from pynput.mouse import Button, Controller
mouse = Controller()

cap = cv2.VideoCapture(0)
hist = module1.capture_histogram(0)
pyautogui.FAILSAFE = False
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (250, 100), (600, 450), (0, 255, 0), 0)
    if not ret:
        break

    detected_hand, masked, raw = module2.locate_object(frame, hist)
    frame, fingertips, com = module3.detect_hand(frame, detected_hand)
    count_defects = module4.recognise(detected_hand)
    module5.assign(frame,count_defects,fingertips,com)
    '''
    if count_defects == 0:
        distance = module3.dist(fingertips[0], com)
        if distance < 150:
            cv2.putText(frame, '0', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            #mouse.click(Button.left, 2)
        elif distance < 200:
            cv2.putText(frame, 'Best of luck', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            #mouse.click(Button.left, 1)
    elif count_defects == 1:
        cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        #pyautogui.moveRel(25, 0)
    elif count_defects == 2:
        cv2.putText(frame, "THREE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        #pyautogui.moveRel(0, 25)
    elif count_defects == 3:
        cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        #pyautogui.moveRel(-25, 0)
    elif count_defects == 4:
        cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        #pyautogui.moveRel(0, -25)
    else:
        pass
'''
    cv2.imshow("Hand", frame)
    k = cv2.waitKey(5)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
