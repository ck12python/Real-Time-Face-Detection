import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,0)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("face",frame)
    cv2.imshow("gray",gray)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()