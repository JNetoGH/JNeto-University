import pygame
from engine_JNeto_Productions.components.rect_trigger_component import RectTriggerComponent
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from game_objects_main_scene.boat_and_boat_manager import BoatsManager
from game_objects_main_scene.player_stats import HeartsManager


# ======================================================================================================================


class Platform(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("platform", scene, rendering_layer)
        self.sprite = SpriteComponent("res/art/platform.png", self)
        self.sprite.scale_sprite(2)
        self.transform.move_world_position(pygame.Vector2(self.image_rect.width/2-3, 350))


# ======================================================================================================================


class Background(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("background", scene, rendering_layer)
        self.sprite = SpriteComponent("res/art/sky_background.jpg", self)
        self.sprite.scale_sprite(0.5)
        self.transform.set_rotation(180)
        self.transform.move_world_position(pygame.Vector2(1000, 200))

        # platform
        self.fortress_platform = Platform(self.scene, self.rendering_layer)
        self.cannon_platform = Platform(self.scene, self.rendering_layer)
        self.fortress_platform.transform.move_world_position(pygame.Vector2(140, 425))

# ======================================================================================================================


class Fortress(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("platform", scene, rendering_layer)
        self.sprite = SpriteComponent("res/art/fortress.png", self)
        self.sprite.scale_sprite(0.025)
        self.transform.move_world_position(pygame.Vector2(140, 280))
        self.rect_trigger = RectTriggerComponent(0, 0, 100, 200, self)

    def game_object_update(self) -> None:
        self.__check_boat_collision()

    def __check_boat_collision(self):
        for boat in BoatsManager.BoatsInScene:
            if self.rect_trigger.is_there_overlap_with_rect(boat.rect_trigger.inner_rect_read_only):
                boat.destroy()
                HeartsManager.HealthPoints -= 1
                HeartsManager.update_hearts()
