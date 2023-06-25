import enum
import random
import pygame
from engine_JNeto_Productions.components.rect_trigger_component import RectTriggerComponent
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.components.timer_component import TimerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.game_time_system import GameTime

# ======================================================================================================================


class Rank(enum.Enum):
    NONE = -1
    HUGE = 0
    LARGE = 1
    MEDIUM = 2
    SMALL = 3
    TINY = 4


class AnimationStatus(enum.Enum):
    NONE = -1
    UP = 0
    DOWN = 1

# ======================================================================================================================


class Boat(GameObject):

    # images
    Paths = ["res/art/boats/Huge.png", "res/art/boats/large.png", "res/art/boats/medium.png",
             "res/art/boats/small.png", "res/art/boats/tiny.png"]

    WindForce = 120

    def __init__(self, rank, initial_pos: pygame.Vector2, scene, rendering_layer):
        super().__init__("boat", scene, rendering_layer)

        # set-up
        self.transform.move_world_position(initial_pos)
        self.rank = Rank(rank) # random.randint(0, len(Boat.Paths)-1)
        self.sprite = SpriteComponent(Boat.Paths[self.rank.value], self)
        scale = 0.1

        # Pysics
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.mass = 1

        # trigger
        self.rect_trigger: RectTriggerComponent = RectTriggerComponent(0, 0, 0, height=100, game_object_owner=self)

        # y-axis related
        self.Y_SINKING_MAX = 10
        self.floating_speed = 12
        self.floating_animation_status = AnimationStatus.DOWN

        # Setting boat according to it's rank
        if self.rank == Rank.HUGE:
            scale = 0.1
            self.transform.translate_world_position(pygame.Vector2(0, 5))
            self.rect_trigger.offset_from_game_object_y = 100
            self.mass = 2.5
        elif self.rank == Rank.LARGE:
            scale = 0.055
            self.transform.translate_world_position(pygame.Vector2(0, 38))
            self.rect_trigger.offset_from_game_object_y = 70
            self.mass = 2
        elif self.rank == Rank.MEDIUM:
            scale = 0.05
            self.transform.translate_world_position(pygame.Vector2(0, 54))
            self.rect_trigger.offset_from_game_object_y = 60
            self.mass = 1.5
        elif self.rank == Rank.SMALL:
            scale = 0.045
            self.transform.translate_world_position(pygame.Vector2(0, 60))
            self.rect_trigger.offset_from_game_object_y = 55
            self.mass = 1.25
        elif self.rank == Rank.TINY:
            scale = 0.05
            self.transform.translate_world_position(pygame.Vector2(0, 78))
            self.rect_trigger.offset_from_game_object_y = 45
            self.Y_SINKING_MAX = 6
            self.mass = 1

        # Settings (after rank)
        self.sprite.scale_sprite(scale)
        self.INIT_Y = self.transform.world_position_read_only.y

        # trigger
        self.rect_trigger.width = self.image.get_width()
        if self.rank == Rank.SMALL:
            width = self.rect_trigger.width
            self.rect_trigger.width = width - 15

    # Called once per frame by the game loop
    def game_object_update(self) -> None:
        self.animate_floating()
        self.move_boat_with_wind_force()

    def move_boat_with_wind_force(self):
        # resets velocity to get the new force form the wind
        self.velocity = pygame.Vector2(0, 0)
        wind_direction = pygame.Vector2(-1, 0)
        self.apply_force(wind_direction, Boat.WindForce * GameTime.DeltaTime)
        new_pos = self.transform.world_position_read_only + self.velocity
        self.transform.move_world_position(new_pos)

    def apply_force(self, force_direction: pygame.Vector2, force_units) -> None:
        # Applies a force to the velocity: (F = m * a) => a = (F / m) * direction
        acceleration = (force_units / self.mass) * force_direction
        self.velocity += acceleration

    def animate_floating(self):
        # Makes the boat go up and down
        if self.floating_animation_status == AnimationStatus.UP:
            self.transform.translate_world_position(pygame.Vector2(0, - self.floating_speed * GameTime.DeltaTime))
        elif self.floating_animation_status == AnimationStatus.DOWN:
            self.transform.translate_world_position(pygame.Vector2(0, self.floating_speed * GameTime.DeltaTime))
        if self.transform.world_position_read_only.y <= self.INIT_Y:
            self.floating_animation_status = AnimationStatus.DOWN
            self.transform.move_world_position(pygame.Vector2(self.transform.world_position_read_only.x, self.INIT_Y))
        elif self.transform.world_position_read_only.y - self.INIT_Y >= self.Y_SINKING_MAX:
            self.floating_animation_status = AnimationStatus.UP

    def destroy(self):
        BoatsManager.BoatsInScene.remove(self)
        self.scene.remove_game_object(self)

# ======================================================================================================================


class BoatsManager(GameObject):

    BoatsInScene: list[Boat] = []

    def __init__(self, scene, rendering_layer):
        super().__init__("Boats Manager", scene, rendering_layer)
        self.transform.move_world_position(pygame.Vector2(1500, 500))
        self.remove_default_rect_image()
        self.__inst_frequency_in_sec = 4
        self.instantiation_timer = TimerComponent(self.__inst_frequency_in_sec * 1000, self, self.__instantiate_boat)
        self.__can_instantiate = True

    # Called when the scene is set by the game loop
    def game_object_start(self) -> None:
        # destroy previous boats
        for gm_obj in self.scene.game_object_list:
            if isinstance(gm_obj, Boat):
                gm_obj.transform.move_world_position(pygame.Vector2(10000000, 10000000))
                gm_obj.destroy()
        # enables the instantiation of new boats
        self.__can_instantiate = True
        self.__instantiate_boat()

    # Called once per frame by the game loop
    def game_object_update(self) -> None:
        # instantiation
        if not self.__can_instantiate:
            return
        if not self.instantiation_timer.is_timer_active_read_only:
            # self.instantiation_timer.set_duration_in_ms(difficulty_in_sec * 1000) # disable difficulty
            self.instantiation_timer.activate()

    def __instantiate_boat(self):
        new_boat = Boat(random.randint(0, 4), self.transform.world_position_read_only, self.scene, self.scene.camera.get_rendering_layer_by_name("layer_2"))
        BoatsManager.BoatsInScene.append(new_boat)
