import numpy as np
import cv2 as cv

image = cv.imread("gabriel.png", 0)

# -- definicao dos kernels
kernel_gauss = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], np.float32)
kernel_gauss = kernel_gauss/16

kernel_laplaciano = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], np.float32)

# -- geracao das imagens
image_gauss = cv.filter2D(image, -1, kernel_gauss)
image_laplaciano = cv.filter2D(image, -1, kernel_laplaciano)
image_gauss_laplace = cv.filter2D(image_gauss, -1, kernel_laplaciano)

image_gauss = np.uint8(image_gauss)
image_laplaciano = np.uint8(image_laplaciano)
image_gauss_laplace = np.uint8(image_gauss_laplace)

# -- exibicao
cv.imshow('gaussiano', image_gauss)
cv.imshow('laplaciano', image_laplaciano)
cv.imshow('gauss_laplaciano', image_gauss_laplace)

cv.imshow('imagem final', image + image_gauss_laplace)
cv.imshow('original', image)
# --
cv.waitKey()

cv.imwrite("gaussiano.png", image_gauss)
cv.imwrite("laplaciano.png", image_laplaciano)
cv.imwrite("laplaciano_gauss.png", image_gauss_laplace)
cv.imwrite("final.png", image + image_gauss_laplace)
