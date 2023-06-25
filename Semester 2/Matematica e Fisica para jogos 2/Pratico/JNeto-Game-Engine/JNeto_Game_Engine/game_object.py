from typing import TypeVar, Type
from JNeto_Game_Engine.components.abstract.abstract_collider import AbstractCollider
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent
from JNeto_Game_Engine.components.abstract.abstract_script import AbstractScript
from JNeto_Game_Engine.components.dependencies.collision import Collision
from JNeto_Game_Engine.components.transform import Transform
from JNeto_Game_Engine.scene import Scene


class GameObject:

    AbstractComponentSubClass = TypeVar('AbstractComponentSubClass', bound=AbstractComponent)

    def __init__(self, name: str):
        self.__name: str = name
        self.tags: list[str] = list()
        # set by the scene when the game object is added
        self.scene: Scene = None
        # A GameObject is simply a Component list
        # The scripts and colliders are cached for speeding searches up
        self.components: list[AbstractComponent] = list()
        self.colliders: list[AbstractCollider] = list()
        self.scripts: list[AbstractScript] = list()
        # Every GameObject has a single Transform
        self.transform: Transform = Transform()
        self.transform.game_object = self
        self.transform.transform = self.transform
        self.components.append(self.transform)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def overview(self) -> str:
        txt: str = f"GameObject ({self.name})"
        txt += "\nComponents: "
        for component in self.components:
            txt += component.get_component_name() + ", "
        txt += "\nColliders: "
        for collider in self.colliders:
            txt += collider.collider_name + ", "
        txt += "\nScripts: "
        for script in self.scripts:
            txt += script.get_component_name() + ", "
        return txt

    def add_component(self, component: AbstractComponentSubClass) -> Type[AbstractComponentSubClass]:
        # Exceptions checking
        if isinstance(component, Transform):
            raise Exception("A GameObject can't more than one transform")
        elif component in self.components or component in self.scripts:
            raise Exception("You can't add the same instance of component twice")
        # Adding to its list
        if isinstance(component, AbstractScript):
            self.scripts.append(component)
        elif isinstance(component, AbstractCollider):
            self.colliders.append(component)
        else:
            self.components.append(component)
        # Setting component up
        component.game_object = self
        component.at_add_component()
        return component

    def get_component(self, component_type) -> AbstractComponentSubClass:
        if component_type == AbstractScript:
            for script in self.scripts:
                if isinstance(script, component_type):
                    return script
        elif component_type == AbstractCollider:
            for collider in self.colliders:
                if isinstance(collider, component_type):
                    return collider
        else:
            for component in self.components:
                if isinstance(component, component_type):
                    return component

    """
    Physics notifying:
    they are both called by the rigid body 
    """

    def on_collision_enter(self, collisions: list[Collision]) -> None:
        for script in self.scripts:
            script.on_collision_enter(collisions)

    def on_trigger_enter(self, collisions: list[Collision]) -> None:
        for script in self.scripts:
            script.on_trigger_enter(collisions)

    """
    ORDEM DE start e update:
    1 -> start scripts (input components should come first)
    2 -> collider position sync (scripts can manipulate the object's transform, so the sync should come after that)
    3 -> update other components
    """

    def start(self) -> None:
        for script in self.scripts:
            script.start_component()
        for collider in self.colliders:
            collider.start_component()
        for component in self.components:
            component.start_component()

    def update(self) -> None:
        for script in self.scripts:
            script.update_component()
        for collider in self.colliders:
            collider.update_component()
        for component in self.components:
            component.update_component()

    def render(self) -> None:
        for component in self.components:
            component.render_component()

    def render_gizmos(self) -> None:
        for component in self.components:
            component.render_gizmos_component()
        for collider in self.colliders:
            collider.render_gizmos_component()
