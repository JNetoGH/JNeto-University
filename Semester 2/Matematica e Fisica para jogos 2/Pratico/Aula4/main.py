import pygame
import sys

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
delta_Time = 0

my_font = pygame.font.Font('freesansbold.ttf', 14)

Gravity = 9.8

VZero: pygame.Vector2 = pygame.Vector2(0, 0)
VForward: pygame.Vector2 = pygame.Vector2(1, 0)
VBackward: pygame.Vector2 = pygame.Vector2(-1, 0)


class GameObject:

    BaseSpeed = 100

    def __init__(self, pos: pygame.Vector2, size):
        self.position: pygame.Vector2 = pos
        self.velocity = pygame.Vector2(0, 0)
        self.speed = GameObject.BaseSpeed
        self.mass = 1
        self.drag = 2
        self.use_gravity = True
        self.radius = size
        self.color = pygame.Color("White")

    @property
    def current_direction(self):
        current_dir = self.velocity.copy()
        if current_dir.magnitude() > 0:
            current_dir = current_dir.normalize()
        return current_dir

    def start(self):
        altVector = pygame.Vector2(1, 0).normalize()
        self.add__force(altVector, 800)

    def update(self):
        if self.use_gravity:
            self.__apply_gravity()

        # moves the obj according o velocity
        self.position = self.position + self.velocity
        print(f"current_dir {self.current_direction}\n")

    def render(self, surface):
        self.__render_info()
        pygame.draw.circle(surface, self.color, self.position, self.radius)

    def add__force(self, force_direction: pygame.Vector2, newtons):
        acceleration = (force_direction * newtons / self.mass)
        self.velocity += acceleration

    def __apply_gravity(self):
        self.add__force(pygame.Vector2(0, 1), Gravity*delta_Time)

    def __render_info(self):
        font_surface = my_font.render(f" speed: {self.speed} | Vx: {self.velocity.x:.2f}, Vy:{self.velocity.y:.2f} )", True, pygame.Color(255, 255, 255))
        font_rect = font_surface.get_rect()
        font_rect.center = (self.position.x, self.position.y - 20)
        display.blit(font_surface, font_rect)


character = GameObject(pygame.Vector2(300, 100), 20)

# Gameloop
is_it_the_first_fame = True
while (True):

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    # FPS
    pygame.display.set_caption(f"FPS {clock.get_fps():.1f} |  Frametime: {delta_Time}")
    delta_Time = clock.tick() / 1000

    # Clears the screen
    display.fill((0, 0, 0))

    # GameObjects updates starts and renders
    if is_it_the_first_fame:
        character.start()
        is_it_the_first_fame = False
    character.update()
    character.render(display)

    # Frame Update
    pygame.display.update()
