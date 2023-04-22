import math
import pygame
from engine_JNeto_Productions.compenentes_dependencies.animation_clip import AnimationClip
from engine_JNeto_Productions.components.animation_controller_component import AnimationControllerComponent
from engine_JNeto_Productions.components.circle_trigger_component import CircleTriggerComponent
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.components.text_render_component import TextRenderComponent
from engine_JNeto_Productions.components.timer_component import TimerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.game_time_system import GameTime
from engine_JNeto_Productions.systems.input_manager_system import InputManager
from game_objects_main_scene.boat_and_boat_manager import BoatsManager


# ======================================================================================================================

class WaterSplash(GameObject):
    def __init__(self, position:pygame.Vector2,scene, rendering_layer):
        super().__init__("water_splash", scene, rendering_layer)
        self.remove_default_rect_image()
        self.transform.move_world_position(position)

        # animation
        self.animation_clip = AnimationClip("water_splash_clip", 10, "res/art/animations/water_splash")
        self.animation_clip.scale_all_frames_of_this_animation(0.35)
        self.animation_controller = AnimationControllerComponent([self.animation_clip], False, self)

        # sound
        pygame.mixer.Sound("res/audio/Cannon hitting water 5.wav").play()

    def game_object_update(self) -> None:
        if self.animation_controller.has_finished:
            self.scene.remove_game_object(self)


# ======================================================================================================================

class Explosion(GameObject):
    def __init__(self, position:pygame.Vector2,scene, rendering_layer):
        super().__init__("explosion", scene, rendering_layer)
        self.remove_default_rect_image()
        self.transform.move_world_position(position)

        # animation
        self.animation_clip = AnimationClip("explosion_clip", 10, "res/art/animations/explosion")
        self.animation_clip.scale_all_frames_of_this_animation(0.25)
        self.animation_controller = AnimationControllerComponent([self.animation_clip], False, self)

        pygame.mixer.Sound("res/audio/Cannon impact sounds (Hitting ship) 5.wav").play()

    def game_object_update(self) -> None:
        if self.animation_controller.has_finished:
            self.scene.remove_game_object(self)

# ======================================================================================================================

class CannonBall(GameObject):
    def __init__(self, cannon_angle, initial_pos: pygame.Vector2, scene, rendering_layer):
        super().__init__("cannon_ball", scene, rendering_layer)
        self.sprite = SpriteComponent("res/art/cannon_ball.png", self)
        self.sprite.scale_sprite(0.05)

        # ROTATION ANIMATION
        self.ANIMATION_ROTATION_SPEED = 200
        self.animation_rotation_angle = 0

        # ANGLE
        self.cannon_angle = cannon_angle
        self.cannon_angle_rad = math.radians(self.cannon_angle)

        # DIR
        self.direction = pygame.Vector2(math.cos(self.cannon_angle_rad), - math.sin(self.cannon_angle_rad))
        self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction

        # INITIAL POSITION
        self.initial_position = initial_pos
        self.initial_position.y -= 14  # the wheel is the center, so i try to align with the chamber
        self.initial_position += self.direction*60
        self.transform.move_world_position(initial_pos)

        # SPEED
        self.THRUST = 480

        # PHYSICS
        self.velocity = pygame.Vector2(self.THRUST, self.THRUST)
        self.GROUND_Y_POS = 380
        self.GRAVITY = 480
        self.AIR_DRAG = 48

        # COLLIDER
        self.circle_trigger = CircleTriggerComponent(0, 0, 15, self)

    @property
    def has_reached_the_ground(self):
        return self.transform.world_position_read_only.y >= self.GROUND_Y_POS

    def game_object_update(self) -> None:
        self.apply_gravity()
        self.apply_air_drag()
        self.move()
        self.animate_rotation()

        if self.check_collision_with_boats():
            self.instantiate_explosion()
            self.destroy()
        elif self.has_reached_the_ground:
            self.instantiate_water_splash()
            self.destroy()

    def move(self):
        new_pos = self.transform.world_position_read_only
        new_pos.x += self.velocity.x * self.direction.x * GameTime.DeltaTime
        new_pos.y += self.velocity.y * self.direction.y * GameTime.DeltaTime
        self.transform.move_world_position(new_pos)

    def apply_gravity(self):
        self.velocity.y -= 0.5 * self.GRAVITY * GameTime.DeltaTime * 2
        # stop applying when the CannonBall reaches the ground
        self.velocity.y = 0 if self.has_reached_the_ground else self.velocity.y

    def apply_air_drag(self):
        self.velocity.x -= self.AIR_DRAG * GameTime.DeltaTime
        # stop applying when the CannonBall reaches the ground or has been already stop by the air drag
        self.velocity.x = 0 if self.velocity.x < 0 or self.has_reached_the_ground else self.velocity.x

    def animate_rotation(self):
        if self.has_reached_the_ground:
            return
        self.animation_rotation_angle -= self.ANIMATION_ROTATION_SPEED * GameTime.DeltaTime
        self.transform.set_rotation(self.animation_rotation_angle)

    def check_collision_with_boats(self) -> bool:
        for boat in BoatsManager.BoatsInScene:
            if self.circle_trigger.is_there_overlap_with_rect(boat.rect_trigger.inner_rect_read_only):
                self.scene.get_game_object_by_name("score_manager").add_points_according_to_boat_rank(boat.rank)
                boat.destroy()
                return True
        return False

    def instantiate_explosion(self):
        explosion_position = self.transform.world_position_read_only
        explosion_position.y += 10
        Explosion(explosion_position, self.scene, self.rendering_layer)

    def instantiate_water_splash(self):
        water_splash_position = self.transform.world_position_read_only
        water_splash_position.y -= 10
        WaterSplash(water_splash_position, self.scene, self.rendering_layer)

    def destroy(self):
        self.scene.remove_game_object(self)

# ======================================================================================================================

class Cannon(GameObject):

    def __init__(self, scene, rendering_layer):
        super().__init__("cannon", scene, rendering_layer)

        #  sprite
        self.sprite = SpriteComponent("res/art/cannon.png", self)
        self.sprite.scale_sprite(0.25)

        # position
        self.transform.move_world_position(pygame.Vector2(40, 255))

        # rotation
        self.ANGULAR_SPEED = 80
        self.MAX_ANGLE = 75
        self.MIN_ANGLE = 22
        self.angle = 45

        # shooting timer and sound
        self.instantiation_cooldown_in_sec = 1.2
        self.cannon_ball_instantiation_timer = TimerComponent(self.instantiation_cooldown_in_sec * 1000, self)
        self.cannon_sound_effect = pygame.mixer.Sound("res/audio/Cannon shots 2.wav")

        # text description
        self.cool_down_text_render = TextRenderComponent(f"cooldown: 0ms", 14, pygame.Color(0, 100, 0), 30, -120, self)
        self.angle_text_render = TextRenderComponent(f"{self.angle:.1f}º", 14, pygame.Color("black"), 80, -100, self)

    def game_object_scene_set_start(self) -> None:
        # destroy previous cannon balls
        for gm_obj in self.scene.game_object_list:
            if isinstance(gm_obj, CannonBall):
                gm_obj.transform.move_world_position(pygame.Vector2(10000000, 10000000))
                gm_obj.destroy()

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
        if (InputManager.is_key_pressed(pygame.K_SPACE) or pygame.mouse.get_pressed()[0]) and not self.cannon_ball_instantiation_timer.is_timer_active_read_only:
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
        self.angle_text_render.set_text(f"{self.angle:.1f}º: +(↑ or W) -(↓ or S)")

    def shoot(self):
        self.cannon_ball_instantiation_timer.activate()
        CannonBall(self.angle, self.transform.world_position_read_only, self.scene,
                   self.scene.camera.get_rendering_layer_by_name("layer_1"))
        self.cannon_sound_effect.play()
