import pygame.draw
from pygame.color import Color
from pygame.surface import Surface
from JNeto_Game_Engine.game_data import GameData
from JNeto_Game_Engine.utilities.abstract.JNeto_abstract_shape import JNetoAbstractShape
from pygame.math import Vector2
import math


class JNetoCircle(JNetoAbstractShape):

    def __init__(self, center: Vector2, radius: float):
        super().__init__(center)
        self.__radius: float = radius

    @property
    def center(self) -> Vector2:
        return self._center.copy()

    @property
    def radius(self) -> float:
        return self.__radius

    @property
    def area(self) -> float:
        return math.pi * (self.__radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def move(self, new_center: Vector2) -> None:
        self._center = new_center

    def draw(self, surface: Surface, color: Color, line_width: int) -> None:
        pygame.draw.circle(GameData.GAME_SURFACE, color, self.center, self.radius, line_width)

    def draw_doted(self, surface: Surface, color: Color, dots_radius: int) -> None:
        circumference = self.perimeter
        dot_gap = dots_radius * 4  # the bigger this number the bigger the gaps
        num_dots = int(circumference / dot_gap)
        for i in range(num_dots):
            angle = i * (2 * math.pi / num_dots)
            x = int(self.center[0] + self.radius * math.cos(angle))
            y = int(self.center[1] + self.radius * math.sin(angle))
            pygame.draw.circle(surface, color, (x, y), dots_radius)

    # Intersection checking between two circles based on the Pythagorean theorem
    # to calculate the distance between their centers and the sum of their radii.
    def intersects_with_JNetoCircle(self, other: 'JNetoCircle') -> bool:
        distance_squared = (self._center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2
        radii_sum = self.radius + other.radius
        return distance_squared <= radii_sum ** 2

    def intersects_with_JNetoRect(self, jneto_rect: 'JNetoRect') -> bool:
        return jneto_rect.intersects_with_JNetoCircle(self)

    def get_projection(self, delta_x: float, delta_y: float) -> 'JNetoCircle':
        new_center = self._center + Vector2(delta_x, delta_y)
        return JNetoCircle(new_center, self.__radius)

    def copy(self) -> 'JNetoCircle':
        return JNetoCircle(self._center, self.__radius)

    def __str__(self) -> str:
        return f"JNetoCircle(center={self._center}, radius={self.__radius})"
