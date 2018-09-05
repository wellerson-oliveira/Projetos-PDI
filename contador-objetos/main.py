import cv2
import numpy as np
import time

def verifica(fila_x, fila_y, x, y):

    for i in range(0, len(fila_x) - 1):
        if fila_x[i] == x and fila_y[i] == y:
            return True
    return False

def floodfill(seed_x, seed_y, rotulo, value):

    fila_x = [seed_x]
    fila_y = [seed_y]

    while len(fila_x) > 0:
        if seed_x < img.shape[0] - 1:
            if img[seed_x + 1, seed_y] == value:
                r = verifica(fila_x, fila_y, seed_x+1, seed_y)
                if r == False:
                    fila_x.append(seed_x + 1)
                    fila_y.append(seed_y)

        if seed_y < img.shape[0] - 1:
            if img[seed_x, seed_y + 1] == value:
                r = verifica(fila_x, fila_y, seed_x, seed_y+1)
                if r == False:
                    fila_x.append(seed_x)
                    fila_y.append(seed_y + 1)

        if seed_x > 0:
            if img[seed_x - 1, seed_y] == value:
                r = verifica(fila_x, fila_y, seed_x-1, seed_y)
                if r == False:
                    fila_x.append(seed_x - 1)
                    fila_y.append(seed_y)

        if seed_y > 0:
            if img[seed_x, seed_y - 1] == value:
                r = verifica(fila_x, fila_y, seed_x, seed_y-1)
                if r == False:
                    fila_x.append(seed_x)
                    fila_y.append(seed_y - 1)

        img[seed_x, seed_y] = rotulo
        fila_x.pop(0)
        fila_y.pop(0)

        if len(fila_x) > 0:
            seed_x = fila_x[0]
            seed_y = fila_y[0]

def define_region():

    floodfill(0, 0, 2, 0)

    cont_buraco = 0

    for i in range(0, x):
        for j in range(0, y):
            if img[i, j] == 0 and img[i, j-1] != 2:
                floodfill(i, j - 1, 2, img[i, j - 1])
                floodfill(i, j, 2, img[i, j])
                cont_buraco += 1

    cv2.imshow("imagem", img)
    cv2.waitKey()

    return cont_buraco

# Load Image
img = cv2.imread('bolhas.png', 0)

# Set limits of image
x = img.shape[0] - 1
y = img.shape[1] - 1

# Set number of regions
num_region = 0

# -- Remove regions in the border

# Regions on the rows
for i in range(0, x):
    floodfill(i, 0, 0, 255)
    floodfill(i, y, 0, 255)

# Regions on the columns
for j in range(0, y):
    floodfill(0, j, 0, 255)
    floodfill(x, j, 0, 255)

for i in range(0, x):
    for j in range(0, y):
        if img[i, j] == 255:
            num_region += 1
            floodfill(i, j, num_region * 10, 255)

num_region_hole = define_region()

print("Numero de regiões: \n", num_region)
print("Numero de regiões com buraco: \n", num_region_hole)
