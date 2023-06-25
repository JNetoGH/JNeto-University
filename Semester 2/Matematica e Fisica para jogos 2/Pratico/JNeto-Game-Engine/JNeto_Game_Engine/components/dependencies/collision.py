from JNeto_Game_Engine.components.abstract.abstract_collider import AbstractCollider


class Collision:

    def __init__(self, origin: AbstractCollider, collided: AbstractCollider):

        self.origin: AbstractCollider = origin
        self.collided: AbstractCollider = collided

        self.__has_anything_happened = False
        self.__are_there_triggers_in_this_collision = origin.is_trigger or collided.is_trigger
        self.__dx_collided = False
        self.__dy_collided = False
        self.__dx_intersected_trigger = False
        self.__dy_intersected_trigger = False

    @property
    def are_there_triggers_in_this_collision(self) -> bool:
        return self.__are_there_triggers_in_this_collision

    @property
    def has_anything_happened(self) -> bool:
        return self.__has_anything_happened

    @property
    def dx_collided(self) -> bool:
        return self.__dx_collided

    @property
    def dy_collided(self) -> bool:
        return self.__dy_collided

    @property
    def dx_intersected_trigger(self) -> bool:
        return self.__dx_intersected_trigger

    @property
    def dy_intersected_trigger(self) -> bool:
        return self.__dy_intersected_trigger

    def __eq__(self, other):
        return self.origin == other.origin and self.collided == self.collided

    def collide_or_intersect_trigger_in_dx(self):
        if not self.are_there_triggers_in_this_collision:
            self.__dx_collided = True
        else:
            self.__dx_intersected_trigger = True
        self.__has_anything_happened = True

    def collide_or_intersect_trigger_in_dy(self):
        if not self.are_there_triggers_in_this_collision:
            self.__dy_collided = True
        else:
            self.__dy_intersected_trigger = True
        self.__has_anything_happened = True

