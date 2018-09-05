import cv2
import numpy as np

def negativa_regiao(image, x1, y1, x2, y2):

    img = image.copy()

    for i in range(x1, x2):
        for j in range(y1, y2):
            img[i, j] = 255 - image[i,j]

    cv2.imshow('Original image', image)
    cv2.imshow('New image', img)
    cv2.waitKey()


image = cv2.imread('gabriel.png', 0)
negativa_regiao(image, 50, 50, 200, 200)
