from scripts.game_objects.game_object_animated_sprite import *
from settings import settings


class GameObjectAnimatedFixedOnScreen(GameObjectAnimatedSprite):
    def __init__(self, game, path="scripts/game_objects/default_sprites/fixed_animated/weapon/0.png", scale=0.4, animation_time=90, pos= (-1,-1)):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque([pg.transform.smoothscale(img,
                      (self.current_image.get_width() * scale, self.current_image.get_height() * scale)) for img in self.images])

        self.gm_obj_pos = pos
        if self.gm_obj_pos == (-1, -1):
            self.gm_obj_pos = (settings.SCREEN_HALF_WIDTH - self.images[0].get_width() // 2,
                               settings.SCREEN_HEIGHT - self.images[0].get_height())

    def draw(self):
        self.game.screen.blit(self.images[0], self.gm_obj_pos)

    def update(self):
        pass