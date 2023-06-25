from pygame import Vector2
from JNeto_Game_Engine.components.abstract.abstract_collider import AbstractCollider
from JNeto_Game_Engine.utilities.JNeto_rect import JNetoRect


class RectCollider(AbstractCollider):

    def __init__(self, collider_name: str, width: float, height: float, is_trigger: bool = False, offset: Vector2 = Vector2(0, 0)):
        super().__init__(collider_name, is_trigger, offset)
        self.shape = JNetoRect(Vector2(0, 0), width, height)
        self.__width: float = width
        self.__height: float = height

    def render_component(self) -> None:
        pass

    def copy(self) -> 'RectCollider':
        return RectCollider(f"Copy-{self.collider_name}", self.__width, self.__height, self._offset)
