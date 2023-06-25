from abc import ABC, abstractmethod
from pygame import Vector2
from pygame.color import Color
from pygame.surface import Surface


class JNetoAbstractShape(ABC):

    def __init__(self, center: Vector2):
        self._center: Vector2 = center

    @property
    def center(self) -> Vector2:
        return self._center.copy()

    @abstractmethod
    def get_projection(self, delta_x, delta_y) -> 'JNetoShapeSubClass':
        pass

    @abstractmethod
    def copy(self) -> 'JNetoShapeSubClass':
        pass

    @abstractmethod
    def move(self, new_center) -> None:
        pass

    @abstractmethod
    def intersects_with_JNetoRect(self, other: 'JNetoRect') -> bool:
        pass

    @abstractmethod
    def intersects_with_JNetoCircle(self, other: 'JNetoCircle') -> bool:
        pass

    @abstractmethod
    def draw(self, surface: Surface, color: Color, line_width: int) -> None:
        pass

    @abstractmethod
    def draw_doted(self, surface: Surface, color: Color, dots_radius: int) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        return f"JNetoAbstractShape(center={self._center}"
