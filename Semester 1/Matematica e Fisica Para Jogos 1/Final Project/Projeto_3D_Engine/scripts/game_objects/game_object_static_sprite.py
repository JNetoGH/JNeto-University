import math
import os
from collections import deque

from scripts.game_objects.game_object import GameObject
from settings import settings
import pygame as pg


# static objs only
class GameObjectStaticSprite(GameObject):
    # scale is the same as size
    # height_shift is the same o position in y, the bigger the value, the lower it will be placed
    # they must be individually set to each sprite
    def __init__(self, game, path="scripts/game_objects/default_sprites/static/static_test_cat.png",
                 initial_pos_tile_matrix: list=(10.5, 3.5), scale=0.7, height_shift=0.27):
        self.game = game
        self.player = game.player
        self.x, self.y = initial_pos_tile_matrix
        self.current_image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.current_image.get_width()
        self.IMAGE_HALF_WIDTH = self.current_image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.current_image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.normal_dis = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.SPRITE_SCALE = scale
        self.SPRITE_HEIGHT_SHIFT = height_shift

    def get_sprite_projection(self):
        proj = settings.SCREEN_DIST / self.normal_dis * self.SPRITE_SCALE
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.current_image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_sift = proj_height * self.SPRITE_HEIGHT_SHIFT
        pos = self.screen_x - self.sprite_half_width, settings.SCREEN_HALF_HEIGHT - proj_height // 2 + height_sift

        # adds the projection to the render list
        self.game.raycasting.objects_to_render.append((self.normal_dis, image, pos))

    def get_sprite(self):
        # distance from player
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx = dx
        self.dy = dy
        # theta = the angle the player is looking at the sprite
        self.theta = math.atan2(dy, dx)
        # delta = the difference between the theta angle and the player's direction angle
        delta = self.theta - self.player.angle

        # makes sure delta is max 2pi (1 trig. circle)
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        # the amount of rays cast at that angle
        delta_rays = delta / settings.DELTA_ANGLE

        self.screen_x = (settings.HALF_NUM_RAYS + delta_rays) * settings.SCALE
        self.dist = math.hypot(dx, dy)
        # fish ball effect removed
        self.normal_dis = self.dist * math.cos(delta)

        # another performance enhance that makes sure to do not render what is out of frame when an img is too close to the player
        if -self.IMAGE_HALF_WIDTH < self.screen_x < (
                settings.SCREEN_WIDTH + self.IMAGE_HALF_WIDTH) and self.normal_dis > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()
