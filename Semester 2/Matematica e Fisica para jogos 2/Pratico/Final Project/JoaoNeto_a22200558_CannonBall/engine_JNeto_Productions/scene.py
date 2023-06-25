import pygame

from engine_JNeto_Productions.scene_camera import SceneCamera
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen


class Scene:

    def __init__(self, camera):
        # It holds all game objects of the scene When a game obj is instantiated,
        # it's automatically stored here using the scene passed as parameter in  its constructor
        self.game_object_list = []
        # main camera will render the rendering layers
        self.camera: SceneCamera = camera

    def get_game_object_by_name(self, name: str):
        for game_obj in self.game_object_list:
            if game_obj.name == name:
                return game_obj

    # in order to be garbage collected needs to be removed from both,
    # the scene game obj list and the rendering layer list, believe me, I tested it
    def remove_game_object(self, required_game_object):
        for gm in self.game_object_list:
            if gm == required_game_object:
                self.game_object_list.remove(gm)
                gm.rendering_layer.remove_game_object(gm)

    # called when the scene is set by the game loop
    def scene_start(self):
        for gm in self.game_object_list:
            gm.game_object_start()

    # called once per frame by the game loop
    def scene_update(self):
        # first updates the components then the game object itself
        for gm in self.game_object_list:
            for component in gm.components_list:
                component.component_update()
            gm.game_object_update()

    # called once per frame by the game loop
    def scene_render(self):
        # clears the screen for rendering
        GameScreen.GameScreenDummySurface.fill(pygame.Color(64, 64, 64))
        # renders all rendering layers
        self.camera.render_layers()

    # CALLED BY THE InspectorDebuggingCanvas to show this text at the inspector
    def get_inspector_status(self) -> str:

        MAX_NAMES_PERlINE = 4
        game_obj_names = ""
        count = 0
        for gm_obj in self.game_object_list:
            if count == MAX_NAMES_PERlINE:
                game_obj_names += "\n"
                count = 0
                continue
            game_obj_names += f"{gm_obj.name}, "
            count += 1

        return f"SCENE DEBUGGING STATUS\n" \
               f"total game objects in scene: {len(self.game_object_list)}\n" \
               f"list of game objects: \n{game_obj_names}\n"
