import pygame, sys
from pygame.locals import *
import math
import numpy


class Entity:
    def __init__(self, initial_pos: list, shooting_force):
        self.position = initial_pos
        self.is_released = False
        self.shooting_force = shooting_force


pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,600))
dimensions = pygame.display.get_window_size()

my_circle = Entity([0, 0], shooting_force=30)
ang_in_rad = 0
circle_ray = 100
line_length = circle_ray
isGoingToRight: bool = True

# TEXT
textX, textY = 600, 100
vertical_padding = 30
font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render('press A or D to change the direction and R to shoot', True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
textRect.center = (textX // 2, textY // 2)
text2 = font.render(f'press W or S to calibrate the shooting force ({my_circle.shooting_force})', True, (0, 255, 0), (0, 0, 128))
text2Rect = text2.get_rect()
text2Rect.center = (textX // 2, (textY // 2) + vertical_padding)

while True:  # Main loop--

    text2 = font.render(f'press W or S to calibrate shooting force ({my_circle.shooting_force})', True, (0, 255, 0), (0, 0, 128))

    DISPLAYSURF.fill((0, 0, 0)) # clears screen
    DISPLAYSURF.blit(text, textRect) # shows the text
    DISPLAYSURF.blit(text2, text2Rect)  # shows the text

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                isGoingToRight = False
            elif event.key == pygame.K_d:
                isGoingToRight = True
            elif event.key == pygame.K_r:
                my_circle.is_released = True
            elif event.key == pygame.K_w:
                my_circle.shooting_force += 5
            elif event.key == pygame.K_s:
                my_circle.shooting_force -= 5
                if my_circle.shooting_force <= 0:
                    my_circle.shooting_force = 5

    # REVOLVES THE CIRCLE
    if not my_circle.is_released:
        if isGoingToRight:
            ang_in_rad = ang_in_rad - numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º
        else:
            ang_in_rad = ang_in_rad + numpy.pi / 10  # incrementa o angulo em 18º, pois, pi == 180º => pi/10 == 18º
        ang_in_degree = numpy.degrees(ang_in_rad)
        x = (dimensions[0] / 2) + math.sin(ang_in_rad) * circle_ray  # formula: x = centro + sin(ang) * ray
        y = (dimensions[1] / 2) + math.cos(ang_in_rad) * circle_ray  # formula: y = centro + cos(ang) * ray
        my_circle.position = [x, y]

    # SHOOTS THE CIRCLE ACCORDING TO A FORCE
    else:
        line_length += my_circle.shooting_force
        x = (dimensions[0] / 2) + math.sin(ang_in_rad) * line_length  # formula: x = centro + sin(ang) * ray
        y = (dimensions[1] / 2) + math.cos(ang_in_rad) * line_length  # formula: y = centro + cos(ang) * ray
        my_circle.position = [x, y]

    # PRINTS
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255), [dimensions[0] / 2, dimensions[1] / 2], circle_ray, 1)
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), [dimensions[0] / 2, dimensions[1]/2], my_circle.position, 5)
    pygame.draw.circle(DISPLAYSURF, (255, 255, 255),  my_circle.position, 5, 2)

    pygame.time.Clock().tick(15)
    pygame.display.update()