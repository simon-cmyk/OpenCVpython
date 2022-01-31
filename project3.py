# import cv2
#
# cap = cv2.VideoCapture(1)
# cap.set(3, 640)
# cap.set(4, 480)
# cap. set(10, 100)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

import numpy as np
import cv2
from PIL import ImageGrab
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# getting screen's height in pixels
height = root.winfo_screenheight()

# getting screen's width in pixels
width = root.winfo_screenwidth()
print(height, " ", width)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap. set(10, 100)
while True:
    if cv2.waitKey(1) & 0Xff == ord('p'):
        img = ImageGrab.grab(bbox=(0, 0, width, height))  # x, y, w, h
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
