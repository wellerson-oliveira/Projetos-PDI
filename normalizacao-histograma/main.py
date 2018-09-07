import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

image = cv.imread("rapha.png")
image = cv.resize(src = image, dst = None, dsize = (0, 0), fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)

cv.imshow("Imagem", image)
cv.waitKey()

plt.subplot(131)
plt.hist(image[:, :, 0].ravel(),256,[0,256], color = 'b');
plt.subplot(132)
plt.hist(image[:, :, 1].ravel(),256,[0,256], color = 'g');
plt.subplot(133)
plt.hist(image[:, :, 2].ravel(),256,[0,256], color = 'r');

plt.show()


# normalizing
new_image = image.copy()

new_image = cv.normalize(image, new_image, 0, 255, cv.NORM_MINMAX)
cv.imshow("Imagem 2", new_image)
cv.waitKey()

plt.subplot(131)
plt.hist(new_image[:, :, 0].ravel(),256,[0,256], color = 'b');
plt.subplot(132)
plt.hist(new_image[:, :, 1].ravel(),256,[0,256], color = 'g');
plt.subplot(133)
plt.hist(new_image[:, :, 2].ravel(),256,[0,256], color = 'r');

plt.show()
