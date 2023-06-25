import pygame
from engine_JNeto_Productions.compenentes_dependencies.animation_clip import AnimationClip
from engine_JNeto_Productions.components.animation_controller_component import AnimationControllerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject


class WaterSplashEffect(GameObject):
    def __init__(self, position: pygame.Vector2, scene, rendering_layer):
        super().__init__("water_splash", scene, rendering_layer)

        # positioning
        self.remove_default_rect_image()
        self.transform.move_world_position(pygame.Vector2(position.x, position.y + 10))

        # animation
        self.animation_clip = AnimationClip("water_splash_clip", 10, "res/art/animations/water_splash")
        self.animation_clip.scale_all_frames_of_this_animation(0.35)
        self.animation_controller = AnimationControllerComponent([self.animation_clip], False, self)

        # set the sound
        pygame.mixer.Sound("res/audio/Cannon hitting water 5.wav").play()

    # called once per frame by the game loop
    def game_object_update(self) -> None:
        if self.animation_controller.has_finished:
            self.scene.remove_game_object(self)


# ======================================================================================================================


class ExplosionEffect(GameObject):
    def __init__(self, position: pygame.Vector2, scene, rendering_layer):
        super().__init__("explosion", scene, rendering_layer)

        # positioning
        self.remove_default_rect_image()
        self.transform.move_world_position(position)
        self.transform.move_world_position(pygame.Vector2(position.x, position.y-10))

        # animation
        self.animation_clip = AnimationClip("explosion_clip", 10, "res/art/animations/explosion")
        self.animation_clip.scale_all_frames_of_this_animation(0.25)
        self.animation_controller = AnimationControllerComponent([self.animation_clip], False, self)

        # set the sound
        pygame.mixer.Sound("res/audio/Cannon impact sounds (Hitting ship) 5.wav").play()

    # called once per frame by the game loop
    def game_object_update(self) -> None:
        if self.animation_controller.has_finished:
            self.scene.remove_game_object(self)
