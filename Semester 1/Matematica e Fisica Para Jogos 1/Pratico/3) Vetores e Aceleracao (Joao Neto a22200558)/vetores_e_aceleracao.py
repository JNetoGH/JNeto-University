import pygame, sys, numpy

pygame.init()
screen = pygame.display.set_mode((400,300))

fpsClock = pygame.time.Clock()
FPS = 15

WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

baseSpeed = 8
vector2Pos = [10,10]
vector2Dir = [1,0]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    vector2Normalized = vector2Dir/numpy.linalg.norm(vector2Dir)
    vector2Velocity = numpy.multiply(baseSpeed, vector2Normalized)
    vector2Pos = numpy.add(vector2Pos, vector2Velocity)

    screen.fill(WHITE_COLOR)
    pygame.draw.circle(screen, BLACK_COLOR, vector2Pos, 4)
    pygame.display.update()
    fpsClock.tick(FPS)