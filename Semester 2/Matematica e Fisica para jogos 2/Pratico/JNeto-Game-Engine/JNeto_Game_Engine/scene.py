from JNeto_Game_Engine.game_data import GameData


class Scene:

    def __init__(self, scene_name: str):
        self.scene_name: str = scene_name
        self.game_objects_scene_list = list()

    def add_game_object(self, game_object):
        if game_object in self.game_objects_scene_list:
            raise Exception("A GameObject can't be adde twice in the same scene")
        self.game_objects_scene_list.append(game_object)
        game_object.scene = self
        return game_object

    def start_scene(self) -> None:
        for game_object in self.game_objects_scene_list:
            game_object.start()
            # prints every game object added
            print(f"\nADDED TO SCENE ({self.scene_name})\n" + game_object.overview + "\n")

    def update_scene(self) -> None:
        for game_object in self.game_objects_scene_list:
            game_object.update()

    def render_scene(self) -> None:
        for game_object in self.game_objects_scene_list:
            game_object.render()

    def render_gizmos_scene(self) -> None:
        for game_object in self.game_objects_scene_list:
            # only renders the gizmos of object int the screen to not waste performance
            if GameData.GAME_SURFACE.get_rect().collidepoint(
                    game_object.transform.position.x, game_object.transform.position.y):
                game_object.render_gizmos()
