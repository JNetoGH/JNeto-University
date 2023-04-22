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

    def __init__(self, pos: pygame.Vector2, size):
        self.pos: pygame.Vector2 = pos
        self.size = size
        self.color = pygame.Color("White")

    def start(self):
        pass

    def render(self):
        pygame.draw.circle(display, self.color, self.pos, self.size)

    def update(self):
        pass


class Character(GameObject):

    BaseSpeed = 100

    def __init__(self, pos: pygame.Vector2, size):
        super().__init__(pos, size)
        self.velocity = pygame.Vector2(0, 0)
        self.speed = Character.BaseSpeed
        self.mass = 20
        self.drag = 2
        self.use_gravity = True
        self.color = pygame.Color("red")

    @property
    def current_direction(self):
        current_dir = self.velocity.copy()
        if current_dir.magnitude() > 0:
            current_dir = current_dir.normalize()
        return current_dir

    def start(self):
        altVector = pygame.Vector2(1, 0).normalize()
        self.__add__force(altVector, 800)
        # self.__add__force(VBackward, 500)

    def update(self):
        # pseudo physics engine update

        # applies dragging
        """
        self.velocity.x -= self.drag * delta_Time
        self.velocity.y -= self.drag * delta_Time
        if abs(self.velocity.x) < 0:
            self.velocity.x = 0
        if abs(self.velocity.y) < 0:
            self.velocity.y = 0
        """

        # applies gravity
        if (self.use_gravity):
            self.__add__force(pygame.Vector2(0, 1), Gravity)

        # moves the obj according o velocity
        self.pos = self.pos + self.velocity

        # prints the internal of the pseudo physics engine
        # print(f"velocity {self.velocity}")
        print(f"current_dir {self.current_direction}\n")

        # clears velocity
        # self.velocity = pygame.Vector2(0, 0)

    def render(self):
        super(Character, self).render()
        self.__render_info()

    def __add__force(self, force_direction: pygame.Vector2, newtons):
        force = (force_direction * newtons / self.mass) * delta_Time
        self.velocity += force

    def __render_info(self):
        font_surface = my_font.render(f" speed: {self.speed} | Vx: {self.velocity.x:.2f}, Vy:{self.velocity.y:.2f} )", True, pygame.Color(255, 255, 255))
        font_rect = font_surface.get_rect()
        font_rect.center = (self.pos.x, self.pos.y - 20)
        display.blit(font_surface, font_rect)


character = Character(pygame.Vector2(300, 100), 10)

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
    character.render()

    # Frame Update
    pygame.display.update()
