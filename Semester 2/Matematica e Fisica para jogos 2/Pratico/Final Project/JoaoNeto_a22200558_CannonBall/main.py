import sys
import pygame
from engine_JNeto_Productions.prefabs.game_object_button import Button
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen
from physics_game_objects.dolphin import Dolphin
from regular_game_objects.game_over_manager import GameOverManager
from regular_game_objects.camera_controller import CameraController
from regular_game_objects.map_and_background import Background, Fortress, Sea
from regular_game_objects.player_stats import HeartsManager, ScoreManager
from physics_game_objects.boat_and_boat_manager import BoatsManager
from engine_JNeto_Productions.game_loop import GameLoop
from engine_JNeto_Productions.rendering_layer import RenderingLayer
from engine_JNeto_Productions.scene import Scene
from engine_JNeto_Productions.scene_camera import SceneCamera
from regular_game_objects.cannon import Cannon
from regular_game_objects.menu_background import MenuBackground


# This is the main.py, it's only purpose is to set the Game Loop, the Scenes and instantiate the GameObjects.
# The scenes required game objects and a camera (which require rendering layer).
# Once the game loop is set, the camera and the rendering layer are created, and then the game objects are instantiated.
# Once it's all done, the game loop runs the current scene.


# ======================================================================================================================
# GAME LOOP (SET)
# ======================================================================================================================


GAME_RES = [1200, 700]
game_loop = GameLoop(GAME_RES, GAME_RES, GAME_RES)


# ======================================================================================================================
# SCENES AND CAMERA / RENDERING LAYERS
# ======================================================================================================================


# MENU SCENE AND CAMERA / RENDERING LAYERS
menu_layer1 = RenderingLayer("menu_layer1")
menu_layer2 = RenderingLayer("menu_layer2")
camera_menu = SceneCamera(RenderingLayer("map_layer"), menu_layer1, menu_layer2)
menu_scene = Scene(camera_menu)

# GAME SCENE AND CAMERA / RENDERING LAYERS
background_layer = RenderingLayer("background_layer")
layer_1 = RenderingLayer("layer_1")  # boats
sea_layer = RenderingLayer("sea_layer")
layer_2 = RenderingLayer("layer_2")  # particles
layer_3 = RenderingLayer("layer_3")  # ui
game_scene_camera = SceneCamera(background_layer, layer_1, sea_layer, layer_2, layer_3)
game_scene = Scene(game_scene_camera)

# GAME OVER AND CAMERA / RENDERING LAYERS
game_over_layer = RenderingLayer("game_over_layer")
game_over_camera = SceneCamera(game_over_layer)
game_over_scene = Scene(game_over_camera)


# ======================================================================================================================
# SCENES' GAME OBJECTS
# ======================================================================================================================


# MENU SCENE GAME OBJECTS
background_gmobj2 = Background(menu_scene, menu_layer1)
sea_gmobj2 = Sea(menu_scene, menu_layer1)
menu_background = MenuBackground(menu_scene, menu_layer1)

# GAME SCENE GAME OBJECTS
sea_gmobj = Sea(game_scene, sea_layer)
background_gmobj = Background(game_scene, background_layer)
camera_controller_gmobj = CameraController(game_scene, background_layer)
fortress = Fortress(game_scene, layer_1)
cannon_gmobj = Cannon(game_scene, layer_2)
boats_manager = BoatsManager(game_scene, background_layer)
dolphin1 = Dolphin(pygame.Vector2(350, 650), game_scene, layer_2)
dolphin2 = Dolphin(pygame.Vector2(600, 610), game_scene, layer_2)
dolphin3 = Dolphin(pygame.Vector2(850, 620), game_scene, layer_2)
dolphin4 = Dolphin(pygame.Vector2(1100, 650), game_scene, layer_2)
dolphin5 = Dolphin(pygame.Vector2(1300, 610), game_scene, layer_2)
score_manager = ScoreManager(game_scene, layer_3)

# GAME OVER SCENE GAME OBJECTS
game_over_manager_obj = GameOverManager(menu_scene, game_loop, game_over_scene, game_over_layer)
hearts_manager = HeartsManager(game_loop, game_over_scene, game_scene, background_layer)


# ======================================================================================================================
# BUTTONS AND FUNCTIONS
# ======================================================================================================================


def func_setinha_back_to_menu():
    game_loop.set_current_scene(menu_scene)
    print("game scene => menu scene")


def func_start_button():
    game_loop.set_current_scene(game_scene)
    print("menu scene => main scene")


# setinha button settings
img_path1 = "res/art/menu/setinha.png"
img_path2 = "res/art/menu/setinha_active.png"
setinha_main_game_button = \
    Button(img_path1, img_path2, pygame.Vector2(60, 70), 1.5, func_setinha_back_to_menu, game_scene, layer_3)

# start button settings
img_path3 = "res/art/menu/start.png"
img_path4 = "res/art/menu/start_active.png"
menu_start_button = \
    Button(img_path3, img_path4, pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight - 50), 2,
           func_start_button, menu_scene, menu_layer2)

# exit button settings
img_path5 = "res/art/menu/exit.png"
img_path6 = "res/art/menu/exit_active.png"
menu_exit_button = \
    Button(img_path5, img_path6, pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight + 40), 2,
           sys.exit, menu_scene, menu_layer2)


# ======================================================================================================================
# GAME LOOP (RUN)
# ======================================================================================================================


game_loop.set_current_scene(menu_scene)
game_loop.run_game_loop()
