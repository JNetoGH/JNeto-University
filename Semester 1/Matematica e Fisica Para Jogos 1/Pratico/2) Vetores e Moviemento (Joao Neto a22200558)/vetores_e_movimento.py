import pygame, sys, numpy

pygame.init()
screen = pygame.display.set_mode((400,300))

fpsClock = pygame.time.Clock()
FPS = 15

WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)

vector2Pos = [10,10]
vector2Dir = [0,0]

while True:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT:
                vector2Dir = [1, 0]
            if event.key == pygame.K_LEFT:
                vector2Dir = [-1, 0]
            if event.key == pygame.K_UP:
                vector2Dir = [0, -1]
            if event.key == pygame.K_DOWN:
                vector2Dir = [0, 1]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE_COLOR)
    vector2Pos = numpy.add(vector2Pos, vector2Dir)
    pygame.draw.circle(screen, BLACK_COLOR, vector2Pos, 4)
    pygame.display.update()
    fpsClock.tick(FPS)

