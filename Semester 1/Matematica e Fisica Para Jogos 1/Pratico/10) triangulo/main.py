import pygame, sys
import numpy as np
from pygame.locals import *

pygame.init()
pygame.display.set_caption("triangulo")
frame = pygame.display.set_mode((600, 600))
fpsClock = pygame.time.Clock()

ARESTA = 50
HALF_FRAME_WIDTH = frame.get_width() // 2
HALF_FRAME_HEIGHT = frame.get_height() // 2

p0 = [HALF_FRAME_WIDTH, HALF_FRAME_HEIGHT - ARESTA / 2]
p1 = [HALF_FRAME_WIDTH - ARESTA, HALF_FRAME_HEIGHT + ARESTA]
p2 = [HALF_FRAME_WIDTH + ARESTA, HALF_FRAME_HEIGHT + ARESTA]
central_point = pygame.Vector2((p0[0] + p1[0] + p2[0]) / 3, (p0[1] + p1[1] + p2[1]) / 3)


def draw_triangle(p0, p1, p2, cor, width) -> None:
    pygame.draw.line(frame, cor, p0, p1, width)
    pygame.draw.line(frame, cor, p1, p2, width)
    pygame.draw.line(frame, cor, p2, p0, width)


def translate(ponto, dx, dy) -> tuple:
    mTrans = [dx, dy]
    res = np.add(mTrans, ponto)
    return (res[0], res[1])


# move to origin
p0 = translate(p0, -1 * central_point.x, -1 * central_point.y)
p1 = translate(p1, -1 * central_point.x, -1 * central_point.y)
p2 = translate(p2, -1 * central_point.x, -1 * central_point.y)
# updates the central point to origin
central_point = pygame.Vector2((p0[0] + p1[0] + p2[0]) / 3, (p0[1] + p1[1] + p2[1]) / 3)


while True:  # Main loop

    fpsClock.tick()
    pygame.display.set_caption(f"triangle: FPS({fpsClock.get_fps():.1f})")
    frame.fill("blue")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    draw_triangle(p0, p1, p2, pygame.Color(255, 255, 255), 5)
    pygame.draw.circle(frame, pygame.Color(255,0,0), central_point, 7, 7)

    pygame.display.update()
