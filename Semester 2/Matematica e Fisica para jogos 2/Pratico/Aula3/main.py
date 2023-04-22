import pygame
import sys

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
delta_Time = 0
my_font = pygame.font.Font('freesansbold.ttf', 14)

VZero: pygame.Vector2 = pygame.Vector2(0, 0)
VForward: pygame.Vector2 = pygame.Vector2(1, 0)
VBackward: pygame.Vector2 = pygame.Vector2(-1, 0)

class GameObject:

    def __init__(self, pos: pygame.Vector2, size):
        self.pos: pygame.Vector2 = pos
        self.size = size
        self.color = pygame.Color("White")

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
        self.current_dir = VForward
        self.acceleration = 20
        self.color = pygame.Color("red")

    def update(self):
        if self.current_dir == VForward and self.pos.x >= display.get_width():
            self.current_dir = VBackward
        elif self.current_dir == VBackward and self.pos.x <= 0:
            self.current_dir = VForward
        self.__move_to_dir(self.current_dir)

    def render(self):
        super(Character, self).render()
        self.__render_info()

    def __move_to_dir(self, dir: pygame.Vector2):
        self.speed += self.acceleration * delta_Time
        self.velocity = self.speed * dir * delta_Time
        self.pos = self.pos + self.velocity

    def __render_info(self):
        font_surface = my_font.render(f" speed: {self.speed} | Vx: {self.velocity.x:.2f}, Vy:{self.velocity.y:.2f} )", True, pygame.Color(255, 255, 255))
        font_rect = font_surface.get_rect()
        font_rect.center = (self.pos.x, self.pos.y - 20)
        display.blit(font_surface, font_rect)


character = Character(pygame.Vector2(300, 400), 10)

# Gameloop
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

    # GameObjects updates and renders
    character.update()
    character.render()

    # Frame Update
    pygame.display.update()
