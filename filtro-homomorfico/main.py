import numpy as np
import cv2 as cv

# -- Leitura da imagem
image = cv.imread("re6.jpg", 0)
nrow = image.shape[0]
ncol = image.shape[1]

# -- calcula o tamanho da DFT
dft_row = cv.getOptimalDFTSize(nrow)
dft_col = cv.getOptimalDFTSize(ncol)

# -- padding
nimg = np.zeros((nrow,ncol), dtype=np.uint8)
nimg[:dft_row,:dft_col] = image

# -- calcula o ln da imagem para separar as componentes de iluminancia e reflectancia
ln_image = np.log(np.float32(nimg))

# -- calcula a transformada de fourier da nova imagem
dft_ln_image = cv.dft(np.float32(ln_image), flags = cv.DFT_COMPLEX_OUTPUT)
dft_ln_image = np.fft.fftshift(dft_ln_image)
mag_image = 20*np.log(cv.magnitude(dft_ln_image[:, :, 0], dft_ln_image[:, :, 1]))

# -- prepara o filtro homomorfico
# parametros
gammaH = 3
gammaL = 0.5
c = 0.8
D0 = 5

filter = np.copy(ln_image)

# -- filtro
for i in range(0, dft_row - 1):
    for j in range(0, dft_col - 1):
        D = (i - dft_row / 2) * (i - dft_row / 2) + (j - dft_col / 2) * (j - dft_col / 2)
        filter[i, j] = (gammaH - gammaL)*(1 - np.exp(-c*(D/D0)) ) + gammaL

# -- Aplicando o filtro
filter_img = np.copy(dft_ln_image)

filter_img[:, :, 0] = cv.multiply(filter, dft_ln_image[:, :, 0])
filter_img[:, :, 1] = cv.multiply(filter, dft_ln_image[:, :, 1])

# -- Voltando para o dominio do espaco
filter_img_shift = np.fft.ifftshift(filter_img)
img_space = cv.idft(filter_img_shift)
img_space = cv.magnitude(img_space[:, :, 0], img_space[:, :, 1])
img_space = cv.normalize(img_space, None, 0, 255, cv.NORM_MINMAX)

new_image = np.uint8(img_space)

# -- torcendo para dar certo
cv.imshow("Original", nimg)
cv.imshow("Filtrada", new_image)
cv.waitKey()

#cv.imwrite("re6_realce.jpg", new_image)
