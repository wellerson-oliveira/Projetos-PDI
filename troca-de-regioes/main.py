import cv2
import numpy as np

def troca_regioes(image):

    img = image.copy()

    x = int(img.shape[0])
    y = int(img.shape[1])

    #print(x)
    #print(y)

    for i in range(0, int(x/2 - 1)):
        for j in range(0, int(y/2 - 1)):
            img[int(i + x/2), int(j + y/2)] = image[int(i), int(j)]

    for i in range(int(x/2), x):
        for j in range(0, int(y/2 - 1)):
           img[int(i - x/2), int(j + y/2)] = image[int(i), int(j)]

    for i in range(0, int(x/2 - 1)):
        for j in range(int(y/2), y):
            img[int(i + x/2), int(j - y/2)] = image[int(i), int(j)]

    for i in range(int(x/2), x):
        for j in range(int(y/2), y):
           img[int(i - x/2), int(j - y/2)] = image[int(i), int(j)]

    cv2.imshow('Original image', image)
    #cv2.waitKey()
    cv2.imshow('new Image', img)
    cv2.waitKey()

# inicio

image = cv2.imread('gabriel.png', 0)

troca_regioes(image)
