import pygame
from pygame import Vector2
from pygame.color import Color
from pygame.surface import Surface

from JNeto_Game_Engine.utilities.abstract.JNeto_abstract_shape import JNetoAbstractShape


class JNetoRect(JNetoAbstractShape):  # my class is required because pygame rects only work with ints

    def __init__(self, center: Vector2, width: float, height: float):
        super().__init__(center)
        self.__width: float = width
        self.__height: float = height
        self.rotation: float = 10
        self.move(center)

    @property
    def center(self) -> Vector2:
        return self._center.copy()

    @property
    def area(self) -> float:
        return self.__width * self.__height

    @property
    def perimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    @property
    def top_left(self) -> Vector2:
        return Vector2(self._center.x - self.__width / 2, self._center.y - self.__height / 2)

    def move(self, new_center) -> None:
        self._center = new_center

    def draw(self, surface: Surface, color: Color, line_width: int):
        top_right = Vector2(self.top_left.x + self.__width, self.top_left.y)
        bottom_left = Vector2(self.top_left.x, self.top_left.y + self.__height)
        bottom_right = Vector2(self.top_left.x + self.__width, self.top_left.y + self.__height)
        pygame.draw.line(surface, color, self.top_left, top_right, line_width)
        pygame.draw.line(surface, color, top_right, bottom_right, line_width)
        pygame.draw.line(surface, color, bottom_right, bottom_left, line_width)
        pygame.draw.line(surface, color, bottom_left, self.top_left, line_width)

    def draw_doted(self, surface: Surface, color: Color, dots_radius: int) -> None:
        pass

    # Swept AABB (Axis-Aligned Bounding Box) or AABB Sweep Test
    def intersects_with_JNetoRect(self, other: 'JNetoRect') -> bool:
        # Calculates the half width and half height of both rectangles
        hw1, hh1 = self.__width / 2, self.__height / 2
        hw2, hh2 = other.get_width() / 2, other.get_height() / 2
        # Calculates the x and y distances between the centers of both rectangles
        dx = self.center.x - other.center.x
        dy = self.center.y - other.center.y
        # Calculates the minimum x and y distances between the centers of both rectangles for intersection
        min_dx = hw1 + hw2 - abs(dx)
        min_dy = hh1 + hh2 - abs(dy)
        # If either the minimum x or y distance is negative, then there is no intersection
        if min_dx < 0 or min_dy < 0:
            return False
        # If both the minimum x and y distances are positive, then there is intersection
        if min_dx > 0 and min_dy > 0:
            return True
        # Otherwise, checks if the intersection occurs at a corner of one of the rectangles
        corner_dx = min(hw1, abs(dx))
        corner_dy = min(hh1, abs(dy))
        return (corner_dx ** 2 + corner_dy ** 2) < (min_dx ** 2 + min_dy ** 2)

    # Separating Axis Theorem (SAT)
    def intersects_with_JNetoCircle(self, jneto_circle: 'JNetoCircle') -> bool:
        # Calculate the half-width and half-height of the rectangle
        half_width = self.__width / 2
        half_height = self.__height / 2
        # Find the distance between the circle center and the rectangle center
        distance_x = abs(jneto_circle.center.x - self.center.x)
        distance_y = abs(jneto_circle.center.y - self.center.y)
        # If the distance on the x-axis is greater than the sum of the half-width of the rectangle and the circle's
        # radius, or the distance on the y-axis is greater than the sum of the half-height of the rectangle and the
        # circle's radius, then there is no intersection
        if distance_x > half_width + jneto_circle.radius or distance_y > half_height + jneto_circle.radius:
            return False
        # If the distance on the x-axis is less than the half-width of the rectangle,
        # or the distance on the y-axis is less than the half-height of the rectangle,
        # then there is intersection
        if distance_x <= half_width or distance_y <= half_height:
            return True
        # Calculate the distance between the circle center and the corners of the rectangle
        corner_distance_sq = (distance_x - half_width) ** 2 + (distance_y - half_height) ** 2
        # If the distance to any corner is less than the square of the circle's radius, then there is intersection
        return corner_distance_sq <= jneto_circle.radius ** 2

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

    def get_projection(self, delta_x, delta_y) -> 'JNetoRect':
        new_center = self._center + Vector2(delta_x, delta_y)
        return JNetoRect(new_center, self.__width, self.__height)

    def copy(self) -> 'JNetoRect':
        return JNetoRect(self._center, self.__width, self.__height)

    def __str__(self) -> str:
        return f"JNetoRect(center={self._center}, width={self.__width}, height={self.__height})"
