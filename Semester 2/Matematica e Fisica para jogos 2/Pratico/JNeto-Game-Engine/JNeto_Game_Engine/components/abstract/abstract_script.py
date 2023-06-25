from abc import ABC, abstractmethod
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent
from JNeto_Game_Engine.components.dependencies.collision import Collision


class AbstractScript(AbstractComponent, ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def on_collision_enter(self, collisions: list[Collision]) -> None:
        pass

    @abstractmethod
    def on_trigger_enter(self, collisions_with: list[Collision]) -> None:
        pass

    @abstractmethod
    def start_component(self) -> None:
        pass

    @abstractmethod
    def update_component(self) -> None:
        pass

    @abstractmethod
    def render_component(self) -> None:
        pass

    @abstractmethod
    def render_gizmos_component(self) -> None:
        pass
