import numpy as np
import cv2 as cv

image = cv.imread("rapha.png")
image = cv.resize(src = image, dst = None, dsize = (0, 0), fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)

#hist_image = cv.calcHist([image], [0], None, [256], [0,256])

cv.imshow("Imagem", image)
cv.waitKey()

# normalizing
new_image = image.copy()

new_image = cv.normalize(image, new_image, 0, 255, cv.NORM_MINMAX)
cv.imshow("Imagem 2", new_image)
cv.waitKey()
