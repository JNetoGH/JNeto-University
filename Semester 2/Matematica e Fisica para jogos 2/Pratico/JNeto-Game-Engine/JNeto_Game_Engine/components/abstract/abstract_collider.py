from abc import abstractmethod, ABC
from typing import final
from pygame import Vector2
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent
from JNeto_Game_Engine.game_data import GameData
from JNeto_Game_Engine.utilities.abstract.JNeto_abstract_shape import JNetoAbstractShape
from JNeto_Game_Engine.utilities.color_list import PASTEL_GREEN, PASTEL_YELLOW


class AbstractCollider(AbstractComponent, ABC):

    def __init__(self, collider_name: str, is_trigger: bool = False, offset: Vector2 = Vector2(0, 0)):
        super().__init__()
        self.is_trigger: bool = is_trigger
        self.has_friction = True
        self.collider_name: str = collider_name
        self._offset: Vector2 = offset
        self.shape: JNetoAbstractShape = None

    @final
    def __align_collider_with_transform(self) -> None:
        self.shape.move(Vector2(self.transform.position.x + self._offset.x, self.transform.position.y + self._offset.y))

    @final
    def start_component(self) -> None:
        self.__align_collider_with_transform()

    @final
    def update_component(self) -> None:
        self.__align_collider_with_transform()

    @abstractmethod
    def render_component(self) -> None:
        pass

    @final
    def render_gizmos_component(self) -> None:
        gismos_width = 2
        color = PASTEL_GREEN if not self.is_trigger else PASTEL_YELLOW
        self.shape.draw(GameData.GAME_SURFACE, color, gismos_width)
