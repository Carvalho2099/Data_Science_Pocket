import cv2
import numpy as np

imagePath = r'imagem/Fruit-Vegetable-Processing.jpg'

# lendo imagem
image = cv2.imread(imagePath)
# criando imagem do mesmo tamanho para ser o 'brilho'
bright = np.zeros_like(image)
# adicionando brilho de q00 em cada pixel
bright[:, :] = [100, 100, 100]
# some 100 em cada pixel da imagem
brilho = cv2.add(image, bright)
# caso a soma ultrapasse 255 (máximo), limite-o a 255 (branco)
brilho[brilho > 255] = 255

# resultado
cv2.imshow('imagem original', image)
cv2.waitKey()
cv2.imshow('imagem com brilho', brilho)
#espere um comando
cv2.waitKey()
