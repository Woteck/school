import numpy as np
import pygame
import sys

pygame.init()
ecran = pygame.display.set_mode((533, 533))
imgsurface = pygame.image.load('Recursive/logo.png')
imnp = pygame.surfarray.array3d(imgsurface)

def rotate(img, x, y, taille):
    taille = taille // 2
    pygame.surfarray.blit_array(ecran, img)
    pygame.display.update()
    temp = np.copy(img[y:y + taille, x:x + taille])

    img[y:y + taille, x:x + taille]                           = img[y + taille:y + 2 * taille, x:x + taille]
    img[y + taille:y + 2 * taille, x:x + taille]              = img[y + taille:y + 2 * taille, x + taille:x + 2 * taille]
    img[y + taille:y + 2 * taille, x + taille:x + 2 * taille] = img[y:y + taille, x + taille:x + 2 * taille]
    img[y:y + taille, x + taille:x + 2 * taille]              = temp

    if taille > 1:
        rotate(img, x, y, taille)
        rotate(img, x + taille, y, taille)
        rotate(img, x + taille, y + taille, taille)
        rotate(img, x, y + taille, taille)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    rotate(imnp, 0, 0, 533)
    pygame.display.update()
