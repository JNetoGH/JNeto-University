import pygame, sys
from pygame.locals import *

RESOLUTION: tuple = (400, 400)
WINDOW_NAME: str = "JNeto Window"

pygame.init()
MY_DISPLAY_Surface: pygame.surface = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(WINDOW_NAME)

RED = (255, 0, 0)
BLUE = 	(0,0,255)
YELLOW = (255, 234, 0)

def PrintBackground():
    WHITE = (255, 255, 255)
    MY_DISPLAY_Surface.fill(WHITE)

def DrawStuffOnDisplaySurface():

    padding = 10
    pygame.draw.rect(MY_DISPLAY_Surface,RED, pygame.Rect(padding,padding,RESOLUTION[0]-padding*2, RESOLUTION[1]-padding*2), 5)
    pygame.draw.line(MY_DISPLAY_Surface, BLUE, (RESOLUTION[1], 0), (0, RESOLUTION[0]), 5)
    pygame.draw.line(MY_DISPLAY_Surface, BLUE, (0, 0), (RESOLUTION[1], RESOLUTION[1]), 5)
    pygame.draw.circle(MY_DISPLAY_Surface, YELLOW, (200,200), 50, 3)

def RunGameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# MY CALL-STACK
PrintBackground()
DrawStuffOnDisplaySurface()
RunGameLoop()
