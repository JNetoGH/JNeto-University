import pygame

from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen


class MenuBackground(GameObject):
    def __init__(self, scene, rendering_layer):
        super().__init__("menu_back_ground", scene, rendering_layer)
        self.remove_default_rect_image()
        self.transform.move_world_position(pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight))
        self.single_sprite = SpriteComponent("res/art/menu/menu.png", self)
        self.single_sprite.scale_sprite(1.25)
