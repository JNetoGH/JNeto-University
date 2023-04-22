import pygame, sys
from pygame.locals import *
import numpy


class Entity:

    def __init__(self, initial_pos, speed):
        self.position = initial_pos
        self.direction = [0, 0]
        self.speed = speed

    def stop(self):
        self.direction = [0, 0]

    def move(self):
        if self.direction != [0,0]:
            normalizedDir = self.direction / numpy.linalg.norm(self.direction)
            velocity = numpy.multiply(self.speed, normalizedDir)
            self.position = numpy.add(self.position, velocity)

    def render(self):
        pygame.draw.circle(DISPLAYSURF, (255, 255, 255), my_circle.position, 5)
        self.render_label()

    def render_label(self):
        off_set = 15
        textX, textY = self.position[0], self.position[1]
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render(f"X{my_circle.position[0]} Y:{my_circle.position[1]}", True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (textX+off_set, textY+off_set)
        DISPLAYSURF.blit(text, textRect)  # shows the text


pygame.init()
DISPLAYSURF = pygame.display.set_mode((600,600))
dimensions = pygame.display.get_window_size()

my_circle = Entity([300, 300], 5)



# TEXT
while True:  # Main loop--

    DISPLAYSURF.fill((255, 255, 255)) # clears screen

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                my_circle.direction = [1, 0]
            if event.key == pygame.K_LEFT:
                my_circle.direction = [-1, 0]
            if event.key == pygame.K_UP:
                my_circle.direction = [0, -1]
            if event.key == pygame.K_DOWN:
                my_circle.direction = [0, 1]
        elif event.type == pygame.KEYUP:
            my_circle.stop()

    my_circle.move()

    # RENDER
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), [300, 600], [300, 0], 2)
    pygame.draw.line(DISPLAYSURF, (255, 0, 0), [0, 300], [600, 300], 2)
    my_circle.render()
    pygame.draw.line(DISPLAYSURF, (0, 255, 0), [300, 300], my_circle.position, 1)

    # RENDER ANGLE
    angleX, angleY = 300, 300
    angle = numpy.arctan2(angleY - my_circle.position[0], angleX - my_circle.position[1])
    angle_text_off_set = 10
    angle_font = pygame.font.Font('freesansbold.ttf', 10)
    angle_in_degree = numpy.round(numpy.degrees(angle))
    angle_text = angle_font.render(f"angle: {angle_in_degree}", True, (0, 255, 0), (0, 0, 128))
    angle_textRect = angle_text.get_rect()
    angle_textRect.center = (angleX + angle_text_off_set, angleY + angle_text_off_set)
    DISPLAYSURF.blit(angle_text, angle_textRect)  # shows the text


    # IMG ARROW
    img = pygame.image.load("arrow.png")
    img_size = (40, 40)
    # scale down
    img = pygame.transform.scale(img, img_size)
    # rotate arrow
    img = pygame.transform.rotate(img, -angle_in_degree)
    DISPLAYSURF.blit(img, my_circle.position)

    pygame.time.Clock().tick(15)
    pygame.display.update()
