from abc import abstractmethod


class Component:

    def __init__(self, game_object_owner):
        self.game_object_owner = game_object_owner
        self.game_object_owner.components_list.append(self)

    @property
    def game_object_owner_read_only(self):
        return self.game_object_owner

    # called before the game_loop object update
    def component_update(self):
        pass

    @abstractmethod
    def get_inspector_debugging_status(self) -> str:
        pass
