import numpy as np
import cv2 as cv
import random

# -- Leitura da imagem
image = cv.imread("ragnaldo.jpeg")

nrow = image.shape[0]
ncol = image.shape[1]

# -- parametros para o kmeans
ncluster = 6
niter = 1000

# -- Cria matriz para receber a imagem quantizada
new_image = np.copy(image)

# -- Alterando do formato (row x col x 3) para (n x 3) onde n = row*col
sample = np.reshape(image, (nrow*ncol, 3))

# -- define criterio de parada do algoritmo
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, niter, 0.001)

# -- executa o kmeans e salvando as imagens
for k in range(1, 11):
    ret, label, center = cv.kmeans(np.float32(sample), ncluster, None, criteria, 1, cv.KMEANS_RANDOM_CENTERS)

    label_matrix = np.reshape(label, (nrow, ncol))


    for i in range(0, nrow-1):
        for j in range(0, ncol):
            centro_pixel = label_matrix[i, j]
            new_image[i, j, :] = center[centro_pixel]

    new_image = np.uint8(new_image)
    cv.imwrite("./images/image_" + str(k) + ".jpg", new_image)

#cv.imshow("Imagem original", image)
#cv.imshow("Imagem quantizada", new_image)
#cv.waitKey()
