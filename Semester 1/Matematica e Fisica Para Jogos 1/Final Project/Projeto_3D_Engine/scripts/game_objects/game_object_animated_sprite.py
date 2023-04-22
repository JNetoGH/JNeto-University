import os
from collections import deque
import pygame as pg
from scripts.game_objects.game_object_static_sprite import GameObjectStaticSprite


class GameObjectAnimatedSprite(GameObjectStaticSprite):
    def __init__(self, game, path="scripts/game_objects/default_sprites/animated/nyan.png/0.png",
                 initial_pos_tile_matrix=(10.5, 5), scale=0.25, height_shift=0.27, animation_time=120):
        super().__init__(game, path, initial_pos_tile_matrix, scale, height_shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images: deque = self.get_images(self.path)
        # stores the passed from the last animation
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)  # passes to next img
            self.current_image = images[0]

    def check_animation_time(self):
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path) -> deque:
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + "/" + file_name).convert_alpha()
                images.append(img)
        return images
