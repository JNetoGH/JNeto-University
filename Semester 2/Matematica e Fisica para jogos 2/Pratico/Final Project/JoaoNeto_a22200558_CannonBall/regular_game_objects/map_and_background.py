import pygame
from engine_JNeto_Productions.components.rect_trigger_component import RectTriggerComponent
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.components.text_render_component import TextRenderComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from physics_game_objects.boat_and_boat_manager import BoatsManager
from regular_game_objects.player_stats import HeartsManager


# ======================================================================================================================


class Platform(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("platform", scene, rendering_layer)
        # setting the sprite
        self.sprite = SpriteComponent("res/art/platform.png", self)
        self.sprite.scale_sprite(2)
        # setting the position
        self.transform.move_world_position(pygame.Vector2(self.image_rect.width/2-3, 550))


# ======================================================================================================================


class Background(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("background", scene, rendering_layer)
        # setting the background sprite
        self.sprite = SpriteComponent("res/art/sky_background.jpg", self)
        self.sprite.scale_sprite(0.5)
        # setting the background position
        self.transform.set_rotation(180)
        self.transform.move_world_position(pygame.Vector2(1000, 200))
        # setting the cannon platform
        self.fortress_platform = Platform(self.scene, self.rendering_layer)
        self.cannon_platform = Platform(self.scene, self.rendering_layer)
        self.fortress_platform.transform.move_world_position(pygame.Vector2(140, 625))


# ======================================================================================================================


class Fortress(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("platform", scene, rendering_layer)
        # setting the sprite
        self.sprite = SpriteComponent("res/art/fortress.png", self)
        self.sprite.scale_sprite(0.025)
        # setting the position
        self.transform.move_world_position(pygame.Vector2(140, 480))
        # setting the trigger collider
        self.rect_trigger = RectTriggerComponent(0, 0, 100, 200, self)

    # Called once per frame by the Game Loop
    def game_object_update(self) -> None:
        self.__check_boat_collision()

    def __check_boat_collision(self):
        for boat in BoatsManager.BoatsInScene:
            if self.rect_trigger.is_there_overlap_with_rect(boat.rect_trigger.inner_rect_read_only):
                boat.destroy()
                HeartsManager.HealthPoints -= 1
                HeartsManager.update_hearts()


# ======================================================================================================================


class Sea(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("sea", scene, rendering_layer)
        # setting the Text Render Component
        TextRenderComponent("developed by J.Neto", 12, pygame.Color(0, 0, 0), 600, -180, self)
        # setting the sprite
        self.image = pygame.Surface((9000, 500))
        self.image.fill(pygame.color.Color(0, 143, 179))
        # setting the position
        self.transform.move_world_position(pygame.Vector2(0, 850))
