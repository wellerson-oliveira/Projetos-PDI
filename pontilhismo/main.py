import numpy as np
import cv2 as cv
import random

# -- Leitura da imagem
image = cv.imread("imagem-rapha.png")

nrow = image.shape[0]
ncol = image.shape[1]

# -- parametros do programa
step = 5
raio_maior = 3
raio_menor = 2
center_des = 4
canny_low = 50
canny_high = 3 * canny_low

# -- Cria copia da imagem e deixa todos os pixels brancos
new_image = np.copy(image)
new_image[:,:,:] = 255

# -- Para cada step pixels, copia o pixel da imagem original
for i in range(0, nrow - 1, step):
    for j in range(0, ncol - 1, step):
        new_image[i, j, 0] = image[i, j, 0]
        new_image[i, j, 1] = image[i, j, 1]
        new_image[i, j, 2] = image[i, j, 2]

# -- Cria copia da imagem original e deixa em tom de cinza 230
pont_image = np.copy(new_image)
pont_image[:,:,:] = 230

# -- Para cada pixel encontrado em "new_image" que seja uma copia da imagem original desenha um circulo
#    com a cor daquele pixel. O centro do circulo é sorteado na variavel center
for i in range(0, nrow - 1):
    for j in range(0, ncol - 1):
        if (new_image[i, j, 0] != 255 and new_image[i, j, 1] != 255 and new_image[i, j, 2] != 255):
            # - sorteia deslocamento do centro
            center = random.randint(0, center_des)

            # - recupera cor da imagem original para desenhar circulos
            color = np.array((image[i, j, 0], image[i, j, 1], image[i, j, 2]))
            c = tuple(map(int, color))

            cv.circle(pont_image, (j + center, i + center), raio_maior, c , -1, cv.LINE_AA)

# -- Usa o algoritmo de Canny para detectar as bordas da imagem
border_image = np.copy(image)
border_image[:, :, 0] = cv.Canny(pont_image, canny_low, canny_high)
border_image[:, :, 1] = border_image[:, :, 0]
border_image[:, :, 2] = border_image[:, :, 0]

image_final = np.copy(pont_image)

# -- Preenche as bordas com circulos menores
for i in range(0, nrow - 1):
    for j in range(0, ncol - 1):
        if (border_image[i, j, 0] > 100):
            # - recupera cor da imagem original para desenhar circulos
            color = np.array((image[i, j, 0], image[i, j, 1], image[i, j, 2]))
            c = tuple(map(int, color))

            cv.circle(image_final, (j, i), raio_menor, c , -1, cv.LINE_AA)

# -- Exibe resultados

cv.imshow("Original", image)
cv.imshow("Pontilhismo_bruto", pont_image)
cv.imshow("Pontilhismo_slice", image_final)
cv.waitKey()
