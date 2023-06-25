from abc import abstractmethod
from typing import final, TypeVar
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent
from JNeto_Game_Engine.components.abstract.abstract_script import AbstractScript
from JNeto_Game_Engine.components.dependencies.collision import Collision
from JNeto_Game_Engine.game_object import GameObject
from JNeto_Game_Engine.scene import Scene


class Behaviour(AbstractScript):

    AbstractComponentSubClass = TypeVar('AbstractComponentSubClass', bound=AbstractComponent)

    def __init__(self):
        super().__init__()
        self.game_object: GameObject = self.game_object
        self.scene: Scene = None

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

    @final
    def get_component(self, component_type: AbstractComponentSubClass) -> AbstractComponentSubClass:
        return self.game_object.get_component(component_type)

    @final
    def start_component(self) -> None:
        self.scene = self.game_object.scene
        self.start()

    @final
    def update_component(self) -> None:
        self.update()

    @final
    def render_component(self) -> None:
        pass

    @final
    def render_gizmos_component(self) -> None:
        pass
