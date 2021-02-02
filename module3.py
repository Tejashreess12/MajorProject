import cv2
import math


def detect_hand(frame, binary):
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    palm_area = 0
    flag = None
    cnt = None
    for (i, c) in enumerate(contours):
        area = cv2.contourArea(c)
        if area > palm_area:
            palm_area = area
            flag = i

    if flag is not None and palm_area > 10000:
        cnt = contours[flag]
        contours = cnt
        cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 2)
        if len(cnt) == 0:
            return frame
        else:
            points = []
            hull = cv2.convexHull(cnt, returnPoints=False)
            defects = cv2.convexityDefects(cnt, hull)
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                end = tuple(cnt[e][0])
                points.append(end)
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    if points[i] and points[j] and dist(points[i], points[j]) < 50:
                        points[j] = None
            filtered = []
            for point in points:
                if point is not None:
                    filtered.append(point)

            fingertips = [pt for idx, pt in zip(range(5), filtered)]
            for fingertip in fingertips:
                cv2.circle(frame, fingertip, 5, (0, 0, 255), -1)

            if len(contours) == 0:
                pass
            else:
                M = cv2.moments(contours)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                com = (cX, cY)
                cv2.circle(frame, com, 10, (255, 0, 0), -1)
            return frame
    else:
        return frame

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (b[1] - a[1]) ** 2)

