import numpy as np
import cv2 as cv

def nothing(x):
    pass

image = cv.imread("gabriel.png", 0)
cv.namedWindow('imagem borrada')

#Cria barra de nivel de borramento
cv.createTrackbar('level', 'imagem borrada', 0, 20, nothing)

while(1):
    
    # lê dinamicamente o valor atual da barra
    level = cv.getTrackbarPos('level', 'imagem borrada')
    print(level)

    if (level > 0):
        # aplica o filtro, caso o tamanho fornecido pelo usuario seja maior que zero
        kernel_1 = np.ones((level, level), dtype= np.uint8)
        kernel_1 = kernel_1/(level*level)
        image_2 = cv.filter2D(image, -1, kernel_1)
        cv.imshow('imagem borrada', image_2)
    else:
        # exibe imagem original
        cv.imshow('imagem borrada', image)

    cv.imshow('Imagem original', image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

