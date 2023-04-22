import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
ang = 0
circle_ray = 100


while True:  # Main loop--
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    dimensions = pygame.display.get_window_size()

    ang = ang + numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º
    x = (dimensions[0] / 2) + math.sin(ang) * circle_ray  # formula: x = centro + sin(ang) * ray
    y = (dimensions[1] / 2) + math.cos(ang) * circle_ray  # formula: y = centro + cos(ang) * ray

    pygame.draw.circle(DISPLAYSURF, (0, 0, 255), [x, y], 10)

    pygame.display.update()