import numpy as np
import cv2 as cv

def nothing(x):
    pass

#-- Leitura da imagem
image = cv.imread("emirates.png")
cv.namedWindow("Imagem_final")

# -- barra l1
cv.createTrackbar('L1', "Imagem_final", 200, image.shape[0], nothing)

# -- barra l2
cv.createTrackbar('L2', "Imagem_final", 400, image.shape[0], nothing)

# -- barra d
cv.createTrackbar('d', "Imagem_final", 10, 100, nothing)

# -- Cria array para ponderação
x = np.arange(-image.shape[0]/2, (image.shape[0]/2), dtype=np.float32)

while(1):
    # -- Leitura dos valores das Trackbar's
    l1 = cv.getTrackbarPos('L1', "Imagem_final") - image.shape[0]/2
    l2 = cv.getTrackbarPos('L2', "Imagem_final") - image.shape[0]/2
    d = cv.getTrackbarPos('d', "Imagem_final")

    alfa = (np.tanh((x - l1) / d) - np.tanh((x - l2) / d)) / 2

    # -- Cria imagem alfa e alfa_invertido com os pesos
    alfa_image = np.float32(image.copy())

    for i in range(0, image.shape[0]):
        alfa_image[i, :] = alfa[i]

    inv_alfa_image = 1 - alfa_image

    # -- Borramento da imagem original

    # nivel de borramento
    level = 4
    kernel_1 = np.ones((level, level), dtype=np.uint8)
    kernel_1 = kernel_1 / (level * level)
    image_borrada = cv.filter2D(image, -1, kernel_1)

    # -- Multiplicação das matrizes de pesos pelas imagens
    new_image = cv.multiply(np.float32(image), np.float32(alfa_image))
    new_image = np.uint8(new_image)

    new_borrada = cv.multiply(np.float32(image_borrada), np.float32(inv_alfa_image))
    new_borrada = np.uint8(new_borrada)

    # Criação da imagem final
    image_final = new_image + new_borrada

    cv.imshow("Imagem_final", image_final)

    if cv.waitKey(1) & 0xFF == ord('q'):
        # Ao finalizar a janela, salva a imagem criada
        cv.imwrite('resultado.png', image_final)
        break
