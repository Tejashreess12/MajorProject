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
    cv2.imshow("Hand", frame)
    cv2.setWindowProperty("Hand", cv2.WND_PROP_TOPMOST, 1)
    k = cv2.waitKey(5)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
