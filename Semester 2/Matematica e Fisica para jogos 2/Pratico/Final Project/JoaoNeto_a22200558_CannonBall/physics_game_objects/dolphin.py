import enum

import pygame
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.game_time_system import GameTime


class DolphinStatus(enum.Enum):
    ASCENDING = 0
    DESCENDING = 1


class Dolphin(GameObject):

    Gravity = 9.8
    WaterLevel = 620  # Initial position of the water level
    DescendingLimit = 690
    WaterDensity = 4.5  # Density of water (higher value for denser water)

    def __init__(self, initial_pos: pygame.Vector2, scene, rendering_layer):
        super().__init__("cannon_ball", scene, rendering_layer)

        # SPRITE
        self.sprite = SpriteComponent("res/art/dolphin.png", self)
        self.sprite.scale_sprite(0.3)

        # INITIAL POSITION
        self.initial_position = initial_pos
        self.transform.move_world_position(self.initial_position)

        # STATE CONTROL
        self.dolphin_status = DolphinStatus.ASCENDING

        # USED FOR THE PHYSICS OF THE MOVEMENT
        self.pos_y = self.transform.world_position_read_only.y
        self.dolphin_mass = 1.5  # Smaller mass
        self.dolphin_height = 10

    # Called when the scene is set by the game loop
    def game_object_start(self) -> None:
        self.transform.move_world_position(self.initial_position)
        self.dolphin_status = DolphinStatus.ASCENDING

    # Called once per frame by the game loop
    def game_object_update(self) -> None:

        # updates the dolphin status
        if self.dolphin_status == DolphinStatus.ASCENDING and self.pos_y < Dolphin.WaterLevel:
            self.dolphin_status = DolphinStatus.DESCENDING
        elif self.dolphin_status == DolphinStatus.DESCENDING and self.pos_y > Dolphin.DescendingLimit:
            self.dolphin_status = DolphinStatus.ASCENDING

        if self.dolphin_status == DolphinStatus.ASCENDING:  # Rectangle is in the buoyancy phase
            # uses physics to make the dolphin float up
            self.float()
        elif self.dolphin_status == DolphinStatus.DESCENDING:
            # simple movement towards the bottom, nothing really fancy
            self.pos_y += 30 * GameTime.DeltaTime

        # moves the dolphin
        self.transform.move_world_position(pygame.Vector2(self.transform.world_position_read_only.x, self.pos_y))

    def float(self):
        # Calculate the submerged depth
        submerged_depth = ((self.pos_y + self.dolphin_height) - Dolphin.WaterLevel)
        # total_volume=0. # m^3 (dimensions: 1m x 0.4m x 0.1m)
        submerged_volume = 0.4 * submerged_depth / self.dolphin_height
        # Calculate the buoyant force
        buoyant_force = Dolphin.WaterDensity * Dolphin.Gravity * submerged_volume
        # Calculate the net force
        net_force = self.dolphin_mass * Dolphin.Gravity - buoyant_force
        # Apply the net force to the rectangle's position
        acceleration = net_force / self.dolphin_mass
        self.pos_y += acceleration * GameTime.DeltaTime