from abc import abstractmethod, ABC
from typing import final


class AbstractComponent(ABC):

    """
    Base abstract class for components attached to game objects.

    It defines the common interface and structure that derived components should follow.

    Attributes:
        game_object: The game object to which this component is attached.
        transform: The Transform component of the game object.
        __component_name: The name of the component class.

    Methods:
        at_add_component: Called when the component is added to a game object.
        get_component_name: Returns the name of the component.
        start_component: Abstract method to be implemented by derived classes for initializing the component.
        update_component: Abstract method to be implemented by derived classes for updating the component's logic.
        render_component: Abstract method to be implemented by derived classes for rendering the component.
        render_gizmos_component: Abstract method to be implemented by derived classes for rendering gizmos related to the component.
    """

    def __init__(self):
        self.game_object = None
        self.transform: 'Transform' = None
        self.__component_name: str = self.__class__.__name__

    @final
    def at_add_component(self) -> None:
        """
        Called when the component is added to a game object.

        Note:
            - This method is called automatically when the component is added to a game object.
            - It sets the transform attribute of the component to the transform component of the game object.
            - This allows easy access to the game object's transform from within the component.
        """
        self.transform = self.game_object.transform

    @final
    def get_component_name(self) -> str:
        """Returns the name of the component.

        Returns:
            str: The name of the component.

        Note:
            - This method returns the name of the component.
            - The name is derived from the class name of the component.
            - It can be used to identify the specific type of component attached to a game object.
        """
        return self.__component_name

    @abstractmethod
    def start_component(self) -> None:
        """
        DO NOT CALL OUT OF THE ENGINE (e.g. in scripts) IT WILL BREAK STUFF IF DONE SO!!!

        Abstract method to be implemented by derived classes for initializing the component.

        Note:
            - This method is called once when the component is initialized.
            - It should be implemented by derived classes to perform any necessary setup or initialization logic.
        """
        pass

    @abstractmethod
    def update_component(self) -> None:
        """
        DO NOT CALL OUT OF THE ENGINE (e.g. in scripts) IT WILL BREAK STUFF IF DONE SO!!!

        Abstract method to be implemented by derived classes for updating the component's logic.

        Note:
            - This method is called every frame to update the component's logic.
            - It should be implemented by derived classes to define the behavior and functionality of the component.
        """
        pass

    @abstractmethod
    def render_component(self) -> None:
        """
        DO NOT CALL OUT OF THE ENGINE (e.g. in scripts) IT WILL BREAK STUFF IF DONE SO!!!

        Abstract method to be implemented by derived classes for rendering the component.

        Note:
            - This method is called every frame to render the component.
            - It should be implemented by derived classes to handle the rendering of the component's visuals.
        """
        pass

    @abstractmethod
    def render_gizmos_component(self) -> None:
        """
        DO NOT CALL OUT OF THE ENGINE (e.g. in scripts) IT WILL BREAK STUFF IF DONE SO!!!

        Abstract method to be implemented by derived classes for rendering gizmos related to the component.

        Note::
            - This method is called every frame to render gizmos related to the component.
            - It should be implemented by derived classes to handle the rendering of visual debugging gizmos,
              such as wireframes, bounding boxes, or other indicators specific to the component's functionality.
              The method does not return any value.
            - Gizmos are visual representations used for debugging and can help visualize the state or behavior of a component.
            - This method is optional to implement, depending on the needs of the derived component class.
            - The rendering of gizmos is typically done using the rendering capabilities provided by the game engine or framework.
        """
        pass
