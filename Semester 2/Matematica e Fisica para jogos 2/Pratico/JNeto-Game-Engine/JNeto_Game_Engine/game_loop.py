import pygame
import sys
from pygame.color import Color
from pygame.time import Clock
from JNeto_Game_Engine.game_data import GameData
from JNeto_Game_Engine.scene import Scene


class GameLoop:

    """
    Main game loop class responsible for running the game.

    Features:
        - Handles game state updating.
        - Processes events and user input.
        - Renders the scene.
        - Controls the game's frame rate.
    """

    def __init__(self, default_scene: Scene):
        """
        Args:
            default_scene (Scene): The scene to start with.
        """
        pygame.init()
        self.run_current_scene: bool = True
        self.current_scene: Scene = default_scene
        self.__clock: Clock = pygame.time.Clock()

    def run(self):

        """
        Runs the game loop.\n
        This method contains the main game loop that handles updating the game state,
        processing events, rendering the scene, and controlling the game's frame rate.
        """

        is_it_the_first_fame: bool = True

        # Game Loop itself
        while True:

            # Updating Internal stuff
            GameData.set_Delta_Time(self.__clock.tick(GameData.FPS_CAP) / 1000)

            # Makes a safety checking, the engine can get delta times there a too high for the discrete collisions
            # like the ones it's currently using, so, I brute force a 0 to the delta time.
            for event in GameData.Game_Events_This_Frame:
                if event.type == pygame.WINDOWFOCUSLOST:
                    print("focus lost delta time update paused in order to prevent physics errors")
                    GameData.set_Delta_Time(0)
                elif event.type == pygame.WINDOWMOVED:
                    print("Window moved delta time update paused in order to prevent physics errors")
                    GameData.set_Delta_Time(0)
                elif event.type == pygame.WINDOWMINIMIZED:
                    print("Window minimized delta time update paused in order to prevent physics errors")
                    GameData.set_Delta_Time(0)

            GameData.update_Game_Events_This_Frame()
            GameLoop.__clear_game_surface()

            # Updating window's msg
            window_msg = f"FPS {self.__clock.get_fps():.1f} | " f"Frame-time: {GameData.Delta_Time:.3f}"
            pygame.display.set_caption(window_msg)

            # Close Window Event
            for event in GameData.Game_Events_This_Frame:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Game gizmos render
            if GameData.Show_Scene_Gizmos:
                GameLoop.__draw_mouse_track()

            # In case there is no scene set, simply shows an empty screen with "NO SCENE SET"
            if self.current_scene is None:
                GameLoop.__draw_no_scene_set()
                continue

            # Current Scene's starts, updates, renders and render gizmos
            if not (self.run_current_scene and self.current_scene is not None):
                return

            # Scene Start
            if is_it_the_first_fame:
                self.current_scene.start_scene()
                is_it_the_first_fame = False

            # Scene Update and Render
            self.current_scene.update_scene()
            self.current_scene.render_scene()
            if GameData.Show_Scene_Gizmos:
                self.current_scene.render_gizmos_scene()

            # Frame Update
            pygame.display.update()

    @staticmethod
    def __draw_no_scene_set() -> None:
        """ Draws a message on screen indicating that no scene is set on the game surface. """
        txt_surface = GameData.DEFAULT_BIG_FONT.render("NO SCENE SET", True, Color("white"))
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (GameData.GAME_SURFACE.get_width() / 2, GameData.GAME_SURFACE.get_height() / 2)
        GameData.GAME_SURFACE.blit(txt_surface, txt_rect)
        pygame.display.update()

    @staticmethod
    def __draw_mouse_track() -> None:
        """ Draws the mouse position on screen. """
        mouse_pos_surface = GameData.DEFAULT_FONT.render(
            f"x:{pygame.mouse.get_pos()[0]} y:{pygame.mouse.get_pos()[1]}", True, Color("white"))
        mouse_pos_rect = mouse_pos_surface.get_rect()
        mouse_pos_rect.center = (pygame.mouse.get_pos())
        GameData.GAME_SURFACE.blit(mouse_pos_surface, mouse_pos_rect)

    @staticmethod
    def __clear_game_surface():
        """ simply clears teh surface with a solid color for the next render call """
        GameData.GAME_SURFACE.fill(pygame.Color(40, 40, 40))
