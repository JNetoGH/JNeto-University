import pygame
from abc import ABC
from pygame import Rect, Surface
from JNeto_Game_Engine.components.abstract.abstract_component import AbstractComponent
from JNeto_Game_Engine.game_data import GameData
from JNeto_Game_Engine.utilities.color_list import PASTEL_RED


class SpriteRenderer(AbstractComponent, ABC):

    """
    Component for rendering a sprite image on a game object.

    Description:
        The SpriteRenderer class is a derived component class that allows rendering of a sprite image on a game object.
        It provides methods for changing the image, scaling the image, and rotating the image.
        The sprite image is displayed using the pygame library.

    Note:
        - The SpriteRenderer class is designed to be used in conjunction with a game object that has a Transform component.
        - The pygame library is required for loading, scaling, and rotating the sprite image.

    Attributes:
        __image_path: The file path to the sprite image.
        __image: The loaded sprite image as a pygame surface.
        __original_img: A copy of the original sprite image for rotating purposes.
        __scale: The scale factor to be applied to the sprite image.
        __angle: The rotation angle to be applied to the sprite image.
        image_rect: The rectangle representing the dimensions and position of the sprite image.
        __color: The color used for rendering gizmos related to the sprite renderer.
        label_text_render: The rendered text label for the sprite renderer gizmos.

    Methods:
        change_image: Changes the sprite image to a new image specified by the given file path.
        scale_image: Scales the sprite image by the given scale factor.
        rotate_image: Rotates the sprite image by the given angle.

    """

    def __init__(self, image_path):

        """
        - This constructor initializes the SpriteRenderer with the provided image path.
        - It loads the sprite image using pygame and initializes other attributes for rendering and manipulation.

        Args:
            image_path: The file path to the sprite image.
        """

        super().__init__()

        # image
        self.__image_path = pygame.image.load(image_path).convert_alpha()
        self.__image = pygame.image.load(image_path).convert_alpha()
        self.__original_img: Surface = self.__image.copy()
        self.__scale = 1
        self.__angle = 0

        # image rect
        self.image_rect: Rect = self.__image.get_rect()

        # gizmos
        self.__color = PASTEL_RED
        self.label_text_render = GameData.DEFAULT_FONT.render("sprite", True, self.__color, None)

    # ================================================================================================================
    #  PUBLIC METHODS
    # ================================================================================================================

    def change_image(self, image_path: str) -> None:
        """
        Changes the sprite image to a new image specified by the given file path.

        Args:
            image_path: The file path to the new sprite image.
        """
        self.__image = pygame.image.load(image_path).convert_alpha()

    def scale_image(self, scale) -> None:
        """
        - Scales the sprite image by the given scale factor.
        - This method scales the sprite image by the provided scale factor using pygame's transform.scale function.
        - The scaled image replaces the existing sprite image for rendering.
        - The __original_img attribute is also scaled to maintain the original image's aspect ratio for rotation purposes.

        Args:
            scale: The scale factor to be applied to the sprite image.
        """
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * scale, self.__image.get_height() * scale)).convert_alpha()
        self.__original_img = pygame.transform.scale(self.__original_img, (self.__original_img.get_width() * scale, self.__original_img.get_height() * scale)).convert_alpha()
        self.__scale = scale

    def rotate_image(self, angle) -> None:
        """
        -Rotates the sprite image by the given angle.
        -Only a copy of the stored is rotated in order to preserve the original one from sequential rotation distortions.

        Args:
            angle: The rotation angle in degrees.
        """
        # check for performance
        if self.__angle == angle:
            return
        self.__angle = angle
        self.__image = pygame.transform.rotate(self.__original_img, self.__angle)

    # ================================================================================================================
    #  METHODS FROM AbstractComponent SUPER CLASS
    # ================================================================================================================

    def start_component(self) -> None:
        pass

    def update_component(self) -> None:
        self.image_rect: Rect = self.__image.get_rect()
        self.image_rect.centerx = self.transform.position.x
        self.image_rect.centery = self.transform.position.y

    def render_component(self) -> None:
        GameData.GAME_SURFACE.blit(self.__image, self.image_rect)

    def render_gizmos_component(self) -> None:
        pygame.draw.rect(GameData.GAME_SURFACE, PASTEL_RED, self.image_rect, 2)
        pos = (self.image_rect.x, self.image_rect.y - 20)
        GameData.GAME_SURFACE.blit(self.label_text_render, pos)
