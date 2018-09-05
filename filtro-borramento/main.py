import numpy as np
import cv2 as cv

kernel_1 = np.ones((20, 20), dtype= np.uint8)
kernel_1 = kernel_1/400

cap = cv.VideoCapture(0)
ret, frame = cap.read()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Converting to grayscale
    frame_g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    new_frame = cv.filter2D(frame_g, -1, kernel_1)

    cv.imshow('Imagem original', new_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
