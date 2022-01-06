import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [
            [0, 152, 241, 179, 168, 255],
            [14, 135, 87, 33, 255, 255],
            [23, 0, 0, 132, 255, 255]
            ]


def findcolor(image, colo):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for color in colo:
        lower = np.array(color[0:3])
        print(lower)
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow(str(color[0]), mask)


while True:
    success, img = cap.read()
    findcolor(img, myColors)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
