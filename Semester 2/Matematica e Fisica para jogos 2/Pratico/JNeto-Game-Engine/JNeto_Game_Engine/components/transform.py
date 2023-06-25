from pygame import Vector2
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent


class Transform(AbstractComponent):

    def __init__(self):
        super().__init__()
        self.position: Vector2 = Vector2(0, 0)

    def start_component(self) -> None:
        pass

    def update_component(self) -> None:
        pass

    def render_component(self) -> None:
        pass

    def render_gizmos_component(self) -> None:
        pass
