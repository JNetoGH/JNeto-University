import math
from pygame import Vector2
from pygame.color import Color
from JNeto_Game_Engine.components.abstract.abstract_collider import AbstractCollider
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent
from JNeto_Game_Engine.components.circle_collider import CircleCollider
from JNeto_Game_Engine.components.dependencies.collision import Collision
from JNeto_Game_Engine.components.rect_collider import RectCollider
from JNeto_Game_Engine.game_data import GameData
from JNeto_Game_Engine.utilities.abstract.JNeto_abstract_shape import JNetoAbstractShape
from JNeto_Game_Engine.utilities.color_list import PASTEL_RED, PASTEL_INDIGO


class Rigidbody(AbstractComponent):

    """
    A class that represents the Rigidbody component.\n

    Class Attributes:
        - __VELOCITY_DECIMAL_PLACES (int): Caps velocity at X decimal places to avoid errors with long floats (min. 2).
        - __EXTRAPOLATION_AMOUNT (float): Applied to transform when the object collides with both axis projections.

    Instance Attributes:
        - __collided_with_this_frame (list[AbstractCollider]): List of colliders collided with this frame.
        - __Vx_collided_this_frame (bool): Boolean value indicating if the object has collided with X axis this frame.
        - __Vy_collided_this_frame (bool): Boolean value indicating if the object has collided with Y axis this frame.
        - use_gravity (bool): Boolean value indicating if the object uses gravity.
        - use_drag (bool): Boolean value indicating if the object uses drag_coefficient.
        - bounces (bool): Boolean value indicating if the object bounces.
        - drag_coefficient (Vector2): A vector that represents the drag_coefficient force.
        - velocity (Vector2): A vector that represents the velocity of the object.
        - mass (float): The mass of the object.
        - gravity_scale (float): The gravity scale of the object.
        - bounciness (float): Multiplier of the force applied back after a collision, ranges from 0 (0%) to 1 (100%).
        - __bouncing_force (Vector2): The bouncing force applied to the velocity, set every frame.
    """

    __VELOCITY_DECIMAL_PLACES = 3
    __EXTRAPOLATION_AMOUNT = 0.25

    def __init__(self):
        super().__init__()

        # Collisions
        self.__collisions_this_frame: list[Collision] = []
        self.__trigger_collisions_this_frame: list[Collision] = []
        self.__Vx_collided_this_frame: bool = True
        self.__Vy_collided_this_frame: bool = True

        # Rigidbody Settings
        self.mass: float = 1
        self.use_gravity: bool = True
        self.use_drag: bool = True
        self.bounces: bool = False

        # Coefficient Settings
        self.gravity_coefficient: float = 1
        self.bounciness_coefficient: float = 0.5
        self.drag_coefficient: Vector2 = Vector2(30, 0)

        # Vectorial Internals
        self.velocity: Vector2 = Vector2(0, 0)
        self.__bouncing_force: Vector2 = Vector2(0, 0)

    # ================================================================================================================
    #  PROPERTIES
    # ================================================================================================================

    @property
    def current_direction(self) -> Vector2:
        return self.velocity.copy() if self.velocity.magnitude() == 0 else self.velocity.normalize().magnitude()

    @property
    def speed(self) -> float:
        return self.velocity.magnitude()

    @property
    def instantaneous_speed(self) -> float:
        return self.instantaneous_velocity.magnitude()

    @property
    def instantaneous_velocity(self) -> Vector2:
        return Rigidbody.__cap_vector(self.velocity.copy() * GameData.Delta_Time, Rigidbody.__VELOCITY_DECIMAL_PLACES)

    @property
    def instantaneous_gravity(self) -> Vector2:
        return (0.5 * GameData.Gravity * GameData.Delta_Time) * self.gravity_coefficient

    # ================================================================================================================
    #  STATIC METHODS
    # ================================================================================================================

    @staticmethod
    def __cap_vector(vector: Vector2, decimal_places: int) -> Vector2:
        """Simply sounds a certain number of places in order to keep the calculation more accurate."""
        return Vector2(round(vector.x, decimal_places), round(vector.y, decimal_places))

    # ================================================================================================================
    #  PUBLIC METHODS
    # ================================================================================================================

    def add_force(self, force_direction: Vector2, force_units) -> None:
        """Applies a force to the velocity: (F = m * a) => (a = F / m)"""
        acceleration = (force_direction * force_units / self.mass)
        self.velocity += acceleration

    def update_component(self) -> None:

        # Caps velocity decimal places
        self.velocity = Rigidbody.__cap_vector(self.velocity, Rigidbody.__VELOCITY_DECIMAL_PLACES)

        # Applies gravity
        if self.use_gravity:
            self.__apply_gravity_on_velocity()

        # Caps velocity decimal places
        self.velocity = Rigidbody.__cap_vector(self.velocity, Rigidbody.__VELOCITY_DECIMAL_PLACES)

        # Checks for collisions, then, moves the rigidbody with the instantaneous velocity.
        self.__move_projections_and_get_collisions(self.instantaneous_velocity)
        self.__move_rigid_body(self.instantaneous_velocity)
        self.__apply_extrapolation()
        self.__apply_bouncing()
        self.__apply_drag_on_velocity()  # DRAG: only Applied when the object is not stationary
        self.__notify_scripts()

    # ================================================================================================================
    #  PRIVATE METHODS (FORCES & Motion)
    # ================================================================================================================

    def __move_rigid_body(self, delta_increment):
        """Moves the object's position to the increment checking for collisions in X and Y this frame."""
        if not self.__Vx_collided_this_frame:
            self.transform.position.x += delta_increment.x
        if not self.__Vy_collided_this_frame:
            self.transform.position.y += delta_increment.y

    def __apply_gravity_on_velocity(self) -> None:
        """
        Applies gravitational acceleration to the velocity of the object.
        This simulates the effect of gravity on the object's motion.
        """
        self.velocity += self.instantaneous_gravity

    def __apply_extrapolation(self):
        """
        - Applied only when it's trapped inside another game object's collider and directly to the transform.
        - Extrapolates towards the opposite direction of the velocity a bit every frame, til it's no more overlapping.
        - The call order must be set carefully because it can interfere
          with the collider. It should not be called before moving the object with the rigid body, as the transform
          position needs to be synchronized with the collider during component updates.
        - The extrapolation amount is determined by the Rigidbody class attribute __EXTRAPOLATION_AMOUNT.
        """
        if self.__Vx_collided_this_frame and self.__Vy_collided_this_frame:
            extrapolation: Vector2 = Vector2()
            extrapolation.x = - math.copysign(1, self.velocity.x) * Rigidbody.__EXTRAPOLATION_AMOUNT
            extrapolation.y = - math.copysign(1, self.velocity.y) * Rigidbody.__EXTRAPOLATION_AMOUNT
            self.transform.position.x += extrapolation.x
            self.transform.position.y += extrapolation.y
            print(f"{self.game_object.name} extrapolation: {extrapolation}")

    def __apply_drag_on_velocity(self) -> None:
        """
        - Only Applied when the object is not stationary.
        - The drag_coefficient force decrement is calculated independently for each axis (X and Y)
        - Drag force is applied towards the opposite direction of the movement of each axis, until it changes the object
          direction, then, stops the object (sets the velocity on that axis to 0) in order to prevent the object from
          keep moving towards the opposite direction.\n
        """
        # drag_coefficient decrement DX
        if self.velocity.x != 0:
            pre_drag_dx_direction = math.copysign(1, self.velocity.x)
            drag_dx_decrement = - self.velocity.normalize().x * self.drag_coefficient.x * GameData.Delta_Time
            self.velocity.x += drag_dx_decrement
            pos_drag_dx_direction = math.copysign(1, self.velocity.x)
            direction_changed: bool = pos_drag_dx_direction != pre_drag_dx_direction
            if direction_changed:
                self.velocity.x = 0
        # drag_coefficient decrement DY
        if self.velocity.y != 0:
            pre_drag_dy_direction = math.copysign(1, self.velocity.y)
            drag_dy_decrement = - self.velocity.normalize().y * self.drag_coefficient.y * GameData.Delta_Time
            self.velocity.y += drag_dy_decrement
            pos_drag_dy_direction = math.copysign(1, self.velocity.y)
            direction_changed: bool = pos_drag_dy_direction != pre_drag_dy_direction
            if direction_changed:
                self.velocity.y = 0

    def __apply_bouncing(self):
        """
        Applies bouncing behavior to the object if enabled, using a bouncing force based on the object's velocity
        and the bounciness coefficient.

        Note:
            - The minimum bouncing threshold is set to 3 by default (can be adjusted).
            - The bouncing force is calculated based on the object's velocity and the bounciness coefficient.
            - Prints the bouncing force if the object bounces due to a collision.
        """
        if self.bounces:
            # - It's the limit force of how much an obj can bounce back, required in order to do not bouncing forever
            # Without it just the instantaneous gravity can make the obj bounce back, so I check if the bouncing force
            # is bigger than the bouncing generate by the instantaneous gravity.
            min_bouncing = 3  # it's good around 2 to 4
            self.__bouncing_force = - self.velocity * self.bounciness_coefficient
            self.__bouncing_force.x = self.__bouncing_force.x if abs(
                self.__bouncing_force.x) > min_bouncing and self.__Vx_collided_this_frame else 0
            self.__bouncing_force.y = self.__bouncing_force.y if abs(
                self.__bouncing_force.y) > min_bouncing and self.__Vy_collided_this_frame else 0
        # clears velocity when it collides, e.g. object is grounded, if velocity.y is not cleaned
        # it will get gravity acceleration forever, or bounces if the obj is marked to bounce
        if self.__Vx_collided_this_frame:
            self.velocity.x = self.__bouncing_force.x
        if self.__Vy_collided_this_frame:
            self.velocity.y = self.__bouncing_force.y
        # Prints the bouncing force
        bounced = (self.__Vx_collided_this_frame or self.__Vy_collided_this_frame) and self.bounces and self.__bouncing_force.magnitude() != 0
        if bounced:
            print(f"{self.game_object.name} bounced: {self.__bouncing_force}\n")

    # ================================================================================================================
    #  PRIVATE METHODS (COLLISIONS)
    # ================================================================================================================

    def __move_projections_and_get_collisions(self, delta_increment: Vector2) -> None:

        """
        Moves the object's projections and detects/stores collisions.

        The method clears collision and trigger intersection lists from the previous frame and resets control variables
        for X and Y collisions.

        The method updates the object's projections in the X and Y directions based on the given `delta_increment`,
        making collision detection with other colliders in the scene by checking the intersections between projections.

        Then updates the control variables for X and Y collisions and adds the collided or triggered colliders to the
        respective collision lists.

        Note:
            - The collision and trigger intersection lists are cleared at the beginning of the method.
            - The control variables (`__Vx_collided_this_frame` and `__Vy_collided_this_frame`) are also cleared.
            - Projections are calculated for each own collider in the X and Y directions.
            - Collision detection is performed based on the type of other colliders (RectCollider or CircleCollider).
            - The collided or triggered colliders are added to the respective collision lists if anything happened.
            - Triggers do not constrain movement like regular colliders.
        """

        # Clears the collisions and trigger intersections that happened last frame, and also the control fields
        self.__collisions_this_frame = []
        self.__trigger_collisions_this_frame = []
        self.__Vx_collided_this_frame = False
        self.__Vy_collided_this_frame = False

        # Setting lists of AbstractCollider for collision checking
        others_colliders = self.__get_other_game_object_colliders()
        own_colliders: list[AbstractCollider] = self.game_object.colliders

        # Checking for collisions with every other collider in scene
        for own_collider in own_colliders:

            # Setting Projections
            proj_dx: JNetoAbstractShape = own_collider.shape.get_projection(delta_increment.x, 0)
            proj_dy: JNetoAbstractShape = own_collider.shape.get_projection(0, delta_increment.y)

            # Gizmos of the projection
            if GameData.Show_Scene_Gizmos:
                proj_dy.draw_doted(GameData.GAME_SURFACE, PASTEL_RED, 2)
                proj_dx.draw_doted(GameData.GAME_SURFACE, PASTEL_INDIGO, 2)

            # Checking collision or trigger with every other collider
            for other_collider in others_colliders:

                # Stores a hypothetical collision, there will be further check if happened or not
                possible_collision: Collision = Collision(own_collider, other_collider)

                # proj_dx collision checking for each kind of collider
                if isinstance(other_collider, RectCollider):
                    if proj_dx.intersects_with_JNetoRect(other_collider.shape):
                        possible_collision.collide_or_intersect_trigger_in_dx()
                    if proj_dy.intersects_with_JNetoRect(other_collider.shape):
                        possible_collision.collide_or_intersect_trigger_in_dy()

                # proj_dy collision checking for each kind of collider
                if isinstance(other_collider, CircleCollider):
                    if proj_dx.intersects_with_JNetoCircle(other_collider.shape):
                        possible_collision.collide_or_intersect_trigger_in_dx()
                    if proj_dy.intersects_with_JNetoCircle(other_collider.shape):
                        possible_collision.collide_or_intersect_trigger_in_dy()

                # Checks if it has collided this frame with any collider (cleaned at method calling)
                # Adds the collided collider to the collided with list, used to notify the script
                # Triggers don't need control variables, cuz they don't constrain the movement like regular colliders
                self.__Vx_collided_this_frame = True if possible_collision.dx_collided else self.__Vx_collided_this_frame
                self.__Vy_collided_this_frame = True if possible_collision.dy_collided else self.__Vy_collided_this_frame
                if possible_collision.has_anything_happened and possible_collision not in self.__collisions_this_frame:
                    if possible_collision.origin.is_trigger:
                        self.__trigger_collisions_this_frame.append(possible_collision)
                    else:
                        self.__collisions_this_frame.append(possible_collision)

    def __get_other_game_object_colliders(self) -> list[AbstractCollider]:
        """
        - Returns a list of colliders from other game objects in the scene.
        - This method retrieves the colliders from other game objects in the scene and returns them as a list.
        - It excludes colliders from the current game object to prevent self-collisions.

        Returns:
            list[AbstractCollider]: A list of AbstractCollider objects.
        """
        others_colliders: list[AbstractCollider] = []
        for other_game_object in self.game_object.scene.game_objects_scene_list:
            # can't collide against itself
            if other_game_object == self.game_object:
                continue
            for collider in other_game_object.colliders:
                others_colliders.append(collider)
        return others_colliders

    def __notify_scripts(self):
        """
        - This method notifies the scripts attached to the game object that implement the `on_collision_enter` or `on_trigger_enter` methods.
        - It checks for trigger collisions and regular collisions separately.
        - If trigger collisions occurred during the frame, it calls the `on_trigger_enter` method on the game object with the trigger collisions list.
        - If regular collisions occurred during the frame, it calls the`on_collision_enter` method on the game object with the collisions list.
        """
        # simply notify every script of this game object that implements a on collision or on trigger
        if self.__trigger_collisions_this_frame != []:
            self.game_object.on_trigger_enter(self.__trigger_collisions_this_frame)
        if self.__collisions_this_frame != []:
            self.game_object.on_collision_enter(self.__collisions_this_frame)

    # ================================================================================================================
    #  METHODS FROM AbstractComponent SUPER CLASS
    # ================================================================================================================

    def render_gizmos_component(self, ) -> None:
        data = [
            (f"{self.get_component_name()}", (0, -159)),
            (f"Drag? {self.use_drag} | Gravity? {self.use_gravity} | Bounces? {self.bounces}", (0, -139)),
            (f"Drag (x: {self.drag_coefficient.x} y: {self.drag_coefficient.y}) |"
             f" G.Coef.: {self.gravity_coefficient} | Bounciness: {self.bounciness_coefficient * 100}%", (0, -119)),
            (f"Pos (x: {self.transform.position.x:.2f} y: {self.transform.position.y:.2f}) |"
             f" DXcol: {self.__Vx_collided_this_frame} | DYcol: {self.__Vy_collided_this_frame}", (0, -99)),
            (f"Inst.Velocity (speed: {self.instantaneous_speed:.1f}u/f |"
             f" x: {self.instantaneous_velocity.x:.{Rigidbody.__VELOCITY_DECIMAL_PLACES}f}u/f |"
             f" y: {self.instantaneous_velocity.y:.{Rigidbody.__VELOCITY_DECIMAL_PLACES}f}u/f)", (0, -79)),
            (f"Velocity (speed: {self.speed:.1f}u/s | "
             f"x: {self.velocity.x:.{Rigidbody.__VELOCITY_DECIMAL_PLACES}f}u/s | "
             f"y: {self.velocity.y:.{Rigidbody.__VELOCITY_DECIMAL_PLACES}f}u/s)", (0, -59))
        ]
        for label, position in data:
            surface = GameData.DEFAULT_FONT.render(label, True, Color("white"))
            rect = surface.get_rect()
            rect.center = (self.transform.position.x + position[0], self.transform.position.y + position[1])
            GameData.GAME_SURFACE.blit(surface, rect)

    def start_component(self) -> None:
        pass

    def render_component(self) -> None:
        pass
