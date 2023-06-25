import math
import pygame
from engine_JNeto_Productions.components.circle_trigger_component import CircleTriggerComponent
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.game_time_system import GameTime
from physics_game_objects.boat_and_boat_manager import BoatsManager
from regular_game_objects.effects import WaterSplashEffect, ExplosionEffect


class CannonBall(GameObject):

    def __init__(self, cannon_angle, initial_pos: pygame.Vector2, scene, rendering_layer):
        super().__init__("cannon_ball", scene, rendering_layer)

        # SPRITE
        self.sprite = SpriteComponent("res/art/cannon_ball.png", self)
        self.sprite.scale_sprite(0.05)

        # ROTATION ANIMATION
        self.ANIMATION_ROTATION_SPEED = 200
        self.animation_rotation_angle = 0

        # ANGLE
        self.cannon_angle = cannon_angle
        self.cannon_angle_rad = math.radians(self.cannon_angle)

        # MOVE DIRECTION: cos and sin of the angle
        self.direction = pygame.Vector2(math.cos(self.cannon_angle_rad), - math.sin(self.cannon_angle_rad))
        self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction

        # INITIAL POSITION
        self.initial_position = initial_pos
        self.initial_position.y -= 14  # the wheel is the center, so I tried to align with the chamber
        self.initial_position += self.direction*60
        self.transform.move_world_position(initial_pos)

        # COLLIDER
        self.circle_trigger = CircleTriggerComponent(0, 0, 15, self)

        # PHYSICS (Projectile)
        self.initial_thrust = 500
        self.velocity = pygame.Vector2(self.initial_thrust, self.initial_thrust)
        self.mass = 1
        self.radius = 0.1
        self.GRAVITY = 1000
        self.ground_y_pos = 585
        self.air_density = 1.225
        self.DRAG_COEFFICIENT = 0.01

    @property
    def has_reached_the_ground(self):
        # returns true when the ball has reached the ground level
        return self.transform.world_position_read_only.y >= self.ground_y_pos

    # Called once per frame by the game loop
    def game_object_update(self) -> None:
        # Movement
        self.apply_gravity()
        self.apply_air_drag()
        self.move()

        # Rot Animation
        self.animate_rotation()

        # Ground Detector
        if self.check_collision_with_boats():
            self.instantiate_explosion()
            self.destroy()
        elif self.has_reached_the_ground:
            self.instantiate_water_splash()
            self.destroy()

    def apply_gravity(self):
        # formula that was literally took from the slides
        self.velocity.y -= 0.5 * self.GRAVITY * GameTime.DeltaTime
        # stop applying when the CannonBall reaches the ground
        self.velocity.y = 0 if self.has_reached_the_ground else self.velocity.y

    def move(self):
        # updates the cannon ball position
        new_pos = self.transform.world_position_read_only
        new_pos.x += self.velocity.x * self.direction.x * GameTime.DeltaTime
        new_pos.y += self.velocity.y * self.direction.y * GameTime.DeltaTime
        self.transform.move_world_position(new_pos)

    def apply_air_drag(self):
        # applies air drag using the formulas from the math classes
        surface_area = self.radius / 4
        velocity_squared = self.velocity.x ** 2
        drag_force = 0.5 * self.DRAG_COEFFICIENT * self.air_density * velocity_squared * surface_area
        acceleration = - drag_force / self.mass                # Calculate the acceleration based on drag force
        self.velocity.x += acceleration * GameTime.DeltaTime   # Update ball velocity and position

    def animate_rotation(self):
        # Check if the cannonball has reached the ground, and if so, stop the animation
        if self.has_reached_the_ground:
            return
        # Decreases the rotation angle of the animation
        # based on the animation rotation speed and the time passed since the last frame
        self.animation_rotation_angle -= self.ANIMATION_ROTATION_SPEED * GameTime.DeltaTime
        # Set the new rotation angle for the cannonball's transform
        self.transform.set_rotation(self.animation_rotation_angle)

    def check_collision_with_boats(self) -> bool:
        # Iterate through the scene to find any boat that has collided with the cannon ball
        for boat in BoatsManager.BoatsInScene:
            # Use intersection calculations provided by the engine with the current boat
            if self.circle_trigger.is_there_overlap_with_rect(boat.rect_trigger.inner_rect_read_only):
                # Add points to the score manager based on the boat's rank
                self.scene.get_game_object_by_name("score_manager").add_points_according_to_boat_rank(boat.rank)
                # Destroy the collided boat
                boat.destroy()
                return True
        return False

    def instantiate_explosion(self):
        # Creates a new explosion GameObject
        explosion_position = self.transform.world_position_read_only
        explosion_position.y += 10
        ExplosionEffect(explosion_position, self.scene, self.rendering_layer)

    def instantiate_water_splash(self):
        # Creates a new water splash GameObject
        water_splash_position = self.transform.world_position_read_only
        water_splash_position.y -= 10
        WaterSplashEffect(water_splash_position, self.scene, self.rendering_layer)

    def destroy(self):
        # removes the object from the scene letting it free to garbage collection
        self.scene.remove_game_object(self)
