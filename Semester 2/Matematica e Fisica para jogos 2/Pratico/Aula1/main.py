import pygame
import sys

pygame.init()
display = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
delta_Time = 0
my_font = pygame.font.Font('freesansbold.ttf', 14)

class GameObject:

    def __init__(self, pos: pygame.Vector2, size):
        self.pos: pygame.Vector2 = pos
        self.size = size
        self.color = pygame.Color("White")

    def render(self):
        pygame.draw.circle(display, self.color, self.pos, self.size)

    def update(self):
        pass


class Follower(GameObject):

    def __init__(self, pos: pygame.Vector2, size, target):
        super().__init__(pos, size)
        self.target = target
        self.velocity = 0
        self.speed = 100
        self.color = pygame.Color("red")

    def update(self):
        self.update_speed_via_arrows()
        dir = (self.target.pos - self.pos).normalize()
        self.velocity = self.speed * dir * delta_Time
        self.pos = self.pos + self.velocity
        self.print_status()

    def render(self):
        super(Follower, self).render()
        self.render_info()

    def update_speed_via_arrows(self):
        keys = pygame.key.get_pressed()
        changing_speed_rate = 100
        if keys[pygame.K_DOWN]:
            follower.speed -= changing_speed_rate * delta_Time
            if follower.speed < 0:
                follower.speed = 0
        elif keys[pygame.K_UP]:
            follower.speed += changing_speed_rate * delta_Time

    def render_info(self):
        font_surface = my_font.render(f" speed: {self.speed} | Vx: {self.velocity[0]:.2f}, Vy:{self.velocity[1]:.2f} )", True, pygame.Color(255, 255, 255))
        font_rect = font_surface.get_rect()
        font_rect.center = (self.pos.x, self.pos.y - 20)
        display.blit(font_surface, font_rect)
        pass

    def print_status(self):
        print(f"Follower Velocity: {self.velocity}")
        print(f"Follower Speed: {self.speed}\n")


target = GameObject(pygame.Vector2(640 // 2, 480 // 2), 5)
follower = Follower(pygame.Vector2(300, 400), 10, target)

# Gameloop
while (True):

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target.pos.x = pygame.mouse.get_pos()[0]
            target.pos.y = pygame.mouse.get_pos()[1]

    # FPS
    pygame.display.set_caption(f"FPS {clock.get_fps():.1f}")
    delta_Time = clock.tick() / 1000

    # Clears the screen
    display.fill((0, 0, 0))

    # GameObjects updates and renders
    target.update()
    follower.update()
    target.render()
    follower.render()

    # Frame Update
    pygame.display.update()
