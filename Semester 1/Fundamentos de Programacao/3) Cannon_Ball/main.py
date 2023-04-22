import pygame
from engine_JNeto_Productions.prefabs.game_object_button import Button
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen
from game_objects_game_over_scene.game_over_manager import GameOverManager
from game_objects_main_scene.camera_controller import CameraController
from game_objects_main_scene.map_and_background import Background, Fortress
from game_objects_main_scene.player_stats import HeartsManager, ScoreManager
from game_objects_main_scene.boat_and_boat_manager import BoatsManager
from engine_JNeto_Productions.game_loop import GameLoop
from engine_JNeto_Productions.rendering_layer import RenderingLayer
from engine_JNeto_Productions.scene import Scene
from engine_JNeto_Productions.scene_camera import SceneCamera
from game_objects_main_scene.cannon_and_cannon_ball import Cannon
from game_objects_menu_scene.background import MenuBackground
from game_objects_score_scene.black_filter_game_object import BlackFilter
from game_objects_score_scene.score_registration_floating_menu import ScoreRegistrationFloatingMenu
from game_objects_score_scene.text_holder_game_object import TextHolder

# ======================================================================================================================


# GAMELOOP
GAME_RES = [1000, 380]
game_loop = GameLoop(GAME_RES, GAME_RES, GAME_RES)


# ======================================================================================================================


# GAME OVER SCENE CAMERA AND LAYERS
game_over_layer = RenderingLayer("game_over_layer")
game_over_camera = SceneCamera(game_over_layer)
game_over_scene = Scene(game_over_camera)

# MAIN SCENE CAMERA AND LAYERS
background_layer = RenderingLayer("background_layer ")
layer_1 = RenderingLayer("layer_1")  # boats
layer_2 = RenderingLayer("layer_2")  # particles
layer_3 = RenderingLayer("layer_3")  # ui
main_scene_camera = SceneCamera(background_layer, layer_1, layer_2, layer_3)
main_scene = Scene(main_scene_camera)

# MENU SCENE
menu_layer1 = RenderingLayer("menu_layer1")
menu_layer2 = RenderingLayer("menu_layer2")
camera_menu = SceneCamera(RenderingLayer("map_layer"), menu_layer1, menu_layer2)
menu_scene = Scene(camera_menu)

# SCORE SCENE
score_layer1 = RenderingLayer("score_layer1")
score_layer2 = RenderingLayer("score_layer2")
score_layer3 = RenderingLayer("score_layer3")
score_layer4 = RenderingLayer("score_layer4")
score_scene_camara = SceneCamera(RenderingLayer("map_layer"), score_layer1, score_layer2, score_layer3, score_layer4)
score_scene = Scene(score_scene_camara)


# ======================================================================================================================


# GAME OBJECT USED IN ALL SCENES


# ---------------------------------------------


# MAIN SCENE GAME OBJECTS
background_gmobj = Background(main_scene, background_layer)
camera_controller_gmobj = CameraController(main_scene, background_layer)
fortress = Fortress(main_scene, layer_1)
cannon_gmobj = Cannon(main_scene, layer_2)
boats_manager = BoatsManager(main_scene, background_layer)
score_manager = ScoreManager(main_scene, layer_3)
hearts_manager = HeartsManager(game_loop, game_over_scene, main_scene, background_layer)
def func_setinha_back_to_menu():
    game_loop.set_current_scene(menu_scene)
    print("main scene/score scene => menu")
setinha_main_game_button = Button("res/art/menu/setinha.png", "res/art/menu/setinha_active.png", pygame.Vector2(40, 40),
                                  1.5, func_setinha_back_to_menu, main_scene, layer_3)


# ---------------------------------------------


# GAME OVER SCENE GAME OBJECTS
game_over_manager_obj = GameOverManager(score_scene, game_loop, game_over_scene, game_over_layer)


# ---------------------------------------------


# MENU SCENE GAME OBJECTS
background_gmobj2 = Background(menu_scene, menu_layer1)
def func_start_button():
    game_loop.set_current_scene(main_scene)
    print("menu scene => main scene")
menu_start_button = Button("res/art/menu/start.png", "res/art/menu/start_active.png",
                           pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight-50), 2,
                           func_start_button, menu_scene, menu_layer2)
def func_start_button():
    game_loop.set_current_scene(score_scene)
    print("menu scene => score sence")

menu_score_button = Button("res/art/menu/scores.png", "res/art/menu/scores_active.png",
                           pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight+40), 2,
                           func_start_button, menu_scene, menu_layer2)
menu_background = MenuBackground(menu_scene, menu_layer1)


# ---------------------------------------------


# SCORE SCENE GAME OBJECTS
background_gmobj3 = Background(score_scene, score_layer1)
black_filter = BlackFilter(score_scene, score_layer1)
text_holder = TextHolder(score_scene, score_layer1)
score_registration_menu = ScoreRegistrationFloatingMenu(score_scene, score_layer4)
setinha_scores_button = Button("res/art/menu/setinha.png", "res/art/menu/setinha_active.png", pygame.Vector2(40, 40),
                                  1.5, func_setinha_back_to_menu, score_scene, score_layer4)


# ======================================================================================================================

# GAME LOOP
game_loop.set_current_scene(menu_scene)
game_loop.run_game_loop()
