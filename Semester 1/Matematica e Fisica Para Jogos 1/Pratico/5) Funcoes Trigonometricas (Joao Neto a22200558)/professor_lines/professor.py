import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))

WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

x1 = 10
y1 = 50
angle = 0
y2 = y1 + 50  # 50 y1 + 50 == initialposYAnterior + 50
y3 = y1 + 100  # igual acima mas 100
y4 = y1 + 150  # igual acima mas 100

while True:  # Main loop--

    my_lines_fases = numpy.pi # Deslocamento da origem do gráfico

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x1 = x1 + 1
    angle = angle + 0.1
    pygame.draw.circle(DISPLAYSURF, WHITE, [x1, y1 + math.cos(angle)], 1)

    amplitude = 10
    pygame.draw.circle(DISPLAYSURF, (255, 0, 0), [x1, y2 + amplitude * math.cos(angle)], 1)

    fase = numpy.pi  # Deslocamento da origem do gráfico
    pygame.draw.circle(DISPLAYSURF, (255, 126, 126), [x1, y3 + amplitude * math.cos(angle + fase)], 1)

    frequencia = 0.5
    pygame.draw.circle(DISPLAYSURF, (0, 0, 255), [x1, y4 + amplitude * math.cos(angle * frequencia)], 1)

    pygame.display.update()
