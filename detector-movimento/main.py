import numpy as np
import tkinter
from matplotlib import pyplot as plt
import cv2 as cv

cap = cv.VideoCapture(0)

ret, frame = cap.read()

frame2 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
ret, frame2 = cv.threshold(frame2, 100, 255,cv.THRESH_BINARY)
hist_bg = cv.calcHist([frame2], [0], None, [256], [0,256])

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    new_hist = cv.calcHist([gray], [0], None, [256], [0,256])

    dif = hist_bg - new_hist
    err = np.abs(dif)
    err_mean = np.mean(err)
    print(err_mean)

    if err_mean > 60:
        frame_trigger = frame.copy()
        frame_trigger[:, :, 0] = 0
        frame_trigger[:, :, 1] = 0
        cv.imshow('frame', frame_trigger)

    else:
        cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    hist_bg = new_hist

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
