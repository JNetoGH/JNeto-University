import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((400, 400));

red = 0
blue = 0
green = 0
incremento_de_cor = 10

while True:
    pygame.time.Clock().tick(15)

    if red < 255 - incremento_de_cor:
        red += incremento_de_cor
    elif blue < 255 - incremento_de_cor:
        blue += incremento_de_cor
    elif green < 255 - incremento_de_cor:
        green += incremento_de_cor
    elif red >= 255 - incremento_de_cor and blue >= 255 - incremento_de_cor and green >= 255 - incremento_de_cor:
        # reseta as cores
        red = 0
        blue = 0
        green = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                # reseta as cores se pressionar 0
                red = 0
                blue = 0
                green = 0

    print(f"cor atual (r:{red}, b:{blue}, g:{green})")
    DISPLAY_SURF.fill((red,green, blue))
    pygame.display.update()