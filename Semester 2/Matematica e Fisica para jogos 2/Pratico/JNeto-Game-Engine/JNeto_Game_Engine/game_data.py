from enum import Enum
import pygame
from pygame import font, Vector2, display
from pygame.event import Event
from pygame.surface import Surface
pygame.init()


class __GameEngineRefreshableData:

    """
    When the FPS (frames per second) is too high, meaning that your game is running very quickly and smoothly,
    the time elapsed between calls to tick() can become very small. If the time between calls is less than 1
    millisecond, the result of clock.tick() will be 0, which means that delta_time will also be 0.
    """

    # Controller
    FPS_CAP: int = 260  # max should be 300 but for safety 260 is gold, 0 means no cap
    __Delta_Time: float = 0.0
    __Gravity: Vector2 = Vector2(0, 9.8 * 20 * 2)
    __Kinetic_Friction: float = 4
    __Game_Events_This_Frame: list[Event] = pygame.event.get()

    # Rendering
    Show_Scene_Gizmos: bool = True
    __GAME_SURFACE: Surface = display.set_mode((1400, 1000))
    __DEFAULT_FONT_NAME: str = 'freesansbold.ttf'
    __DEFAULT_FONT_SIZE: int = 14
    __DEFAULT_BIG_FONT_SIZE: int = 22
    __DEFAULT_FONT = font.Font(__DEFAULT_FONT_NAME, __DEFAULT_FONT_SIZE)
    __DEFAULT_BIG_FONT = font.Font(__DEFAULT_FONT_NAME, __DEFAULT_BIG_FONT_SIZE)

    class WindowMode(Enum):
        FULLSCREEN = pygame.FULLSCREEN
        RESIZABLE = pygame.RESIZABLE
        NO_FRAME = pygame.NOFRAME
        SCALED = pygame.SCALED

    @property
    def GAME_SURFACE(self) -> Surface:
        return GameData.__GAME_SURFACE

    @property
    def KINETIC_FRICTION(self) -> float:
        return GameData.__Kinetic_Friction

    @property
    def DEFAULT_FONT(self) -> font.Font:
        return GameData.__DEFAULT_FONT

    @property
    def DEFAULT_BIG_FONT(self) -> font.Font:
        return GameData.__DEFAULT_BIG_FONT

    @property
    def Gravity(self) -> Vector2:
        return GameData.__Gravity.copy()

    @property
    def Delta_Time(self) -> float:
        return GameData.__Delta_Time

    @property
    def Game_Events_This_Frame(self) -> list[Event]:
        return GameData.__Game_Events_This_Frame.copy()

    @staticmethod
    def set_Gravity(value: Vector2) -> None:
        GameData.__Gravity = value

    @staticmethod
    def set_Delta_Time(value: float) -> None:
        GameData.__Delta_Time = value

    @staticmethod
    def update_Game_Events_This_Frame() -> None:
        GameData.__Game_Events_This_Frame = pygame.event.get()

    def set_screen_mode(self, window_mode: WindowMode):
        size = (self.__GAME_SURFACE.get_width(), self.__GAME_SURFACE.get_height())
        __GAME_SURFACE: Surface = display.set_mode(size, window_mode.value)


GameData: __GameEngineRefreshableData = __GameEngineRefreshableData()
