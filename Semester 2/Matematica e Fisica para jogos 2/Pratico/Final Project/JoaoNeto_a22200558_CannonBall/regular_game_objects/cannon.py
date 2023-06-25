import pygame
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.components.text_render_component import TextRenderComponent
from engine_JNeto_Productions.components.timer_component import TimerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.game_time_system import GameTime
from engine_JNeto_Productions.systems.input_manager_system import InputManager
from physics_game_objects.cannon_ball import CannonBall


class Cannon(GameObject):

    def __init__(self, scene, rendering_layer):
        super().__init__("cannon", scene, rendering_layer)

        #  sprite
        self.sprite = SpriteComponent("res/art/cannon.png", self)
        self.sprite.scale_sprite(0.25)

        # position
        self.transform.move_world_position(pygame.Vector2(40, 455))

        # rotation
        self.ANGULAR_SPEED = 80
        self.MAX_ANGLE = 80
        self.MIN_ANGLE = 25
        self.angle = 45

        # shooting timer and sound
        self.instantiation_cooldown_in_sec = 1.2
        self.cannon_ball_instantiation_timer = TimerComponent(self.instantiation_cooldown_in_sec * 1000, self)
        self.cannon_sound_effect = pygame.mixer.Sound("res/audio/Cannon shots 2.wav")

        # text description
        self.cool_down_text_render = TextRenderComponent(f"cooldown: 0ms", 25, pygame.Color(0, 100, 0), 85, -130, self)
        self.angle_text_render = TextRenderComponent(f"angle: {self.angle:.1f}º", 20, pygame.Color("black"), 80, -100, self)

    # called when the scene is set by the game loop
    def game_object_start(self) -> None:
        # destroy previous cannon balls
        for gm_obj in self.scene.game_object_list:
            if isinstance(gm_obj, CannonBall):
                gm_obj.transform.move_world_position(pygame.Vector2(10000000, 10000000))
                gm_obj.destroy()

    # Called once per frame by the game loop
    def game_object_update(self) -> None:

        # rotation
        self.rotate_cannon()

        # cooldown text
        cooldown = self.cannon_ball_instantiation_timer.duration_in_ms_read_only - self.cannon_ball_instantiation_timer.elapsed_time_read_only
        if cooldown < 0:
            cooldown = 0
            self.cool_down_text_render.set_color(pygame.Color(0, 100, 0))
        else:
            self.cool_down_text_render.set_color(pygame.Color(190, 0, 0))
        self.cool_down_text_render.set_text(f"cooldown: {cooldown:.0f}ms")

        # shooting
        if (InputManager.is_key_pressed(pygame.K_SPACE)) and not self.cannon_ball_instantiation_timer.is_timer_active_read_only:
            self.shoot()

    def rotate_cannon(self):

        # generates the new angle using the set angular speed and InputManager
        increment = self.ANGULAR_SPEED * GameTime.DeltaTime
        self.angle += increment if InputManager.Vertical_Axis == -1 else 0
        self.angle -= increment if InputManager.Vertical_Axis == 1 else 0

        # keeps the angle in allowed range
        self.angle = self.MAX_ANGLE if self.angle > self.MAX_ANGLE else self.angle
        self.angle = self.MIN_ANGLE if self.angle < self.MIN_ANGLE else self.angle

        # rotates
        self.transform.set_rotation(self.angle)

        # updates text
        self.angle_text_render.set_text(f"angle: {self.angle:.1f}º")

    def shoot(self):
        self.cannon_ball_instantiation_timer.activate()
        CannonBall(self.angle, self.transform.world_position_read_only, self.scene,
                   self.scene.camera.get_rendering_layer_by_name("layer_1"))
        self.cannon_sound_effect.play()
