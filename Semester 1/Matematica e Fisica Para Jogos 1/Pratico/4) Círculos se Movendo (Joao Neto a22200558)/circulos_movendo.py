import pygame, sys, numpy

pygame.init()
screen = pygame.display.set_mode((400, 300))
fpsClock = pygame.time.Clock()
FPS: int = 15
WHITE_COLOR: tuple = (255, 255, 255)
BLACK_COLOR: tuple = (0, 0, 0)


class JNetoEntity:

    vector2MovDir: list = [1, 0]  # moving forward by default
    vector2Pos: list = [0, 0]

    def __init__(self, base_speed: int, initial_position: list, ):
        self.vector2Pos = initial_position
        self.baseSpeed = base_speed

    def move_entity_forward(self):
        vector2_normalized = self.vector2MovDir / numpy.linalg.norm(self.vector2MovDir)
        vector2_velocity = numpy.multiply(self.baseSpeed, vector2_normalized)
        self.vector2Pos = numpy.add(self.vector2Pos, vector2_velocity)


circle1: JNetoEntity = JNetoEntity(1, [10, 50])
circle2: JNetoEntity = JNetoEntity(5, [10, 100])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # calling my move method
    circle1.move_entity_forward()
    circle2.move_entity_forward()
    # render
    screen.fill(WHITE_COLOR)
    pygame.draw.circle(screen, BLACK_COLOR, circle1.vector2Pos, 10)
    pygame.draw.circle(screen, BLACK_COLOR, circle2.vector2Pos, 10)
    pygame.display.update()
    fpsClock.tick(FPS)
