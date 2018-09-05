import numpy as np
import tkinter
from matplotlib import pyplot as plt
import cv2 as cv

cap = cv.VideoCapture(0)
ret, frame = cap.read()
frame_f = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

x, y = frame_f.shape[:2]
n = 10
cont = 0

frames = np.zeros([x, y, n], dtype = np.uint8)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Converting to grayscale
    frame_g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    frames[:, :, cont % n] = frame_g
    frame_f = np.mean(frames, axis = 2)
    frame_f = np.uint8(frame_f)

    cv.imshow('Imagem original', frame_g)
    cv.imshow('Imagem modificada', frame_f)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    cont += 1
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
