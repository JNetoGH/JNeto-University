from settings import settings
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = settings.PLAYER_INITIAL_POS
        self.angle = settings.PLAYER_ANGLE

        # shooting
        self.shot = False

    # shooting
    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot:
                self.shot = True

    def move(self):
        # increments in x-axis and y-axis
        dx, dy = 0, 0

        # makes the increment having in count the player's angle
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        speed = settings.PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # basically moves the player if there is no wall collision using the deltas x and y
        self.check_wall_collisions_and_move_player(dx, dy)

    def check_wall_collisions_and_move_player(self, dx, dy):
        # player size
        scale = settings.PLAYER_SIZE_SCALE / self.game.delta_time
        # applying increments/decrements to the coordinates if there is no wall adding the increment
        if self.no_walls_at(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.no_walls_at(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def no_walls_at(self, x, y):
        return (x, y) not in self.game.map.world_map_not_null_obj_coordinates

    # for 3D representation
    def mouse_rotation(self):
        mx, my = pg.mouse.get_pos()
        # available area for mouse inputs
        if mx < settings.MOUSE_BORDER_LEFT or mx > settings.MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([settings.SCREEN_HALF_WIDTH, settings.SCREEN_HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-settings.MOUSE_MAX_RELATIVE_MOV, min(settings.MOUSE_MAX_RELATIVE_MOV, self.rel))
        self.angle += self.rel * settings.MOUSE_SENSITIVITY * self.game.delta_time

    # for 2D representation, the keys will be used
    def keys_rotation(self):
        keys = pg.key.get_pressed()
        # increments/decrements the rot angle using  keys, basically rotates player
        if self.game.view_mode == settings.ViewMode.VIEW_2D:
            if keys[pg.K_q]:
                self.angle -= settings.PLAYER_ROT_SPEED * self.game.delta_time
            if keys[pg.K_e]:
                self.angle += settings.PLAYER_ROT_SPEED * self.game.delta_time

    def draw(self):
        # the line that represents where the player is looking at, represents the angle line
        pg.draw.line(self.game.screen, "blue", (self.x * 100, self.y * 100),
                     (self.x * 100 + settings.SCREEN_WIDTH * math.cos(self.angle),
                      self.y * 100 + settings.SCREEN_WIDTH * math.sin(self.angle)),
                     2)
        # represents the player as a ball
        pg.draw.circle(self.game.screen, "green", (self.x * 100, self.y * 100), radius=15)

    def update(self):
        self.move()
        if self.game.view_mode == settings.ViewMode.VIEW_3D:
            self.mouse_rotation()
        elif self.game.view_mode == settings.ViewMode.VIEW_2D:
            self.keys_rotation()

        # makes sure the angle remains in 2pi (1 trig. circle)
        self.angle %= math.tau

    @property
    def pos(self):
        return self.x, self.y

    # which tile of the map
    @property
    def tile_map_pos(self):
        return int(self.x), int(self.y)