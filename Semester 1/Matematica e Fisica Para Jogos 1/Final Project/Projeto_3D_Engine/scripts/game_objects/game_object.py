from abc import abstractmethod


# it's an "abstract class"
class GameObject:
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass