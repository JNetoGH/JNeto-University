from JNeto_Game_Engine.components.abstract.abstract_collider import AbstractCollider
from JNeto_Game_Engine.utilities.JNeto_circle import JNetoCircle
from pygame import Vector2


class CircleCollider(AbstractCollider):

    def __init__(self, collider_name: str, radius: float, is_trigger: bool = False, offset: Vector2 = Vector2(0, 0)):
        super().__init__(collider_name, is_trigger, offset)
        self.__radius: float = radius
        self.shape = JNetoCircle(Vector2(0, 0), self.__radius)

    def render_component(self) -> None:
        pass

    def copy(self) -> 'CircleCollider':
        return CircleCollider(f"Copy-{self.collider_name}", self.__radius, self._offset)
