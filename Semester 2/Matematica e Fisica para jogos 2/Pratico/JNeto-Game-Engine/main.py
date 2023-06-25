from JNeto_Game_Engine.components.circle_collider import CircleCollider
from JNeto_Game_Engine.components.rect_collider import RectCollider
from JNeto_Game_Engine.components.sprite_renderer import SpriteRenderer
from JNeto_Game_Engine.game_data import GameData
from JNeto_Game_Engine.components.rigidbody import Rigidbody
from JNeto_Game_Engine.game_loop import GameLoop
from JNeto_Game_Engine.game_object import GameObject
from JNeto_Game_Engine.scene import Scene
from scripts.movement import Movement
from pygame import Vector2


# MAP
game_map = GameObject("game_map")
game_map.add_component(RectCollider("Floor", 100000, 20, False, Vector2(0, GameData.GAME_SURFACE.get_height() - 10)))
game_map.add_component(RectCollider("Right Wall", 20, 5000, False, Vector2(GameData.GAME_SURFACE.get_width() - 10, 0)))
game_map.add_component(RectCollider("Left Wall", 20, 5000, False, Vector2(0, 0)))
game_map.add_component(RectCollider("Platform", 400, 40, False, Vector2(70, 250)))
game_map.add_component((CircleCollider("Big Circle", 150, False, Vector2(600, 0))))
game_map.add_component(RectCollider("Ceiling", 100000, 20, False, Vector2(0, 0)))

# CHARACTER 1
character = GameObject("character")
character.add_component(SpriteRenderer("ball.png"))
character.add_component(Rigidbody())
character.add_component(CircleCollider("Player Collider", 45, False, Vector2(0, 0)))
# character.add_component(RectCollider("Player Collider", 20, 20))
character.add_component(Movement())

# MAIN SCENE
main_scene = Scene("Main Scene")
main_scene.add_game_object(game_map)
main_scene.add_game_object(character)

# GameData.set_screen_mode(GameData.WindowMode.NO_FRAME)

# GAME LOOP
GameLoop(main_scene).run()
