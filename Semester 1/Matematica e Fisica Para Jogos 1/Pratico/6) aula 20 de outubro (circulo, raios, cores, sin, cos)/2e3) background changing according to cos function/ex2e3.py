import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
ang = 0


while True:  # Main loop--
    pygame.time.Clock().tick(15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ang = ang + numpy.pi / 10
    valRed = (math.cos(ang) + 1) / 2 * 255
    DISPLAYSURF.fill((valRed, 0, 0))

    dimensions = pygame.display.get_window_size()
    pygame.draw.circle(DISPLAYSURF, (255,255,255), [dimensions[0] / 2, dimensions[1] / 2], 40)

    pygame.display.update()
