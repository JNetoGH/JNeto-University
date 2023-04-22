import pygame, sys
from pygame.locals import *
import math
import numpy


pygame.init()
DISPLAY_SURF = pygame.display.set_mode((400, 400))

# TEXT
textX, textY = 400, 100
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('press A and D or left and right arrow', True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
textRect.center = (textX // 2, textY // 2)

CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)


class JNetoLine:
    def __init__(self, initial_pos: list, amplitude, fase, frequency):
        self.initial_pos: list = initial_pos
        self.current_pos: list = [initial_pos[0], initial_pos[1]]
        self.angle = 0
        self.frequency = frequency
        self.fase = fase
        self.amplitude = amplitude

    def reset_pos_to_initial(self):
        self.current_pos[0] = self.initial_pos[0]
        self.current_pos[1] = self.initial_pos[1]


line1: JNetoLine = JNetoLine([10, 200], 30, numpy.pi, 1)
line2: JNetoLine = JNetoLine([10, 300], 20, numpy.pi, 2)

while True:

    # shows the text
    DISPLAY_SURF.blit(text, textRect)

    # INCREMENTS X_axis and angle
    line1.current_pos[0] += 1
    line1.angle += 0.1
    line2.current_pos[0] += 1
    line2.angle += 0.1

    # if event.key == pygame.K_RIGHT or event.key == pygame.K_a
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_RIGHT or event.key == K_a or event.key == K_LEFT or event.key == K_d:
                # CLEARS THE SCREEN
                DISPLAY_SURF.fill((0, 0, 0))
                # RESETS THE CURRENT CIRCLE BACK TO THE LINE INITIAL POSITION
                line1.reset_pos_to_initial()
                line2.reset_pos_to_initial()
                if event.key == K_RIGHT or event.key == K_a:  # SETS A NEW FASE TO THE LINES A NEW FASE
                    line1.fase += 0.01
                    line2.fase += 0.01
                elif event.key == K_LEFT or event.key == K_d:  # SETS A NEW FASE TO THE LINES A NEW FASE
                    line1.fase -= 0.01
                    line2.fase -= 0.01
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    # DRAWING MY LINES
    pygame.draw.circle(DISPLAY_SURF, CYAN, [line1.current_pos[0], line1.current_pos[1] + line1.amplitude * math.cos(line1.angle * line1.frequency + line1.fase)], 1)
    pygame.draw.circle(DISPLAY_SURF, YELLOW,  [line2.current_pos[0], line2.current_pos[1] + line2.amplitude * math.cos(line2.angle * line2.frequency + line2.fase)], 1)
    pygame.display.update()
