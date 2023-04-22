from game_loop import Game
from scripts.game_objects.game_object_animated_sprite import GameObjectAnimatedSprite
from scripts.game_objects.game_object_static_sprite import GameObjectStaticSprite
from scripts.game_objects.game_object_animated_fixed_on_screen_sprite import GameObjectAnimatedFixedOnScreen


class Tree(GameObjectStaticSprite):
    def __init__(self, game, pos):
        super().__init__(game, "resources/sprites/static_sprites/tree.png", initial_pos_tile_matrix=pos, scale=2, height_shift=-0.25)

class Grass(GameObjectStaticSprite):
    def __init__(self, game, pos):
        super().__init__(game, "resources/sprites/static_sprites/grass.png", initial_pos_tile_matrix=pos, scale=0.25, height_shift=1.5)

class Weapon(GameObjectAnimatedFixedOnScreen):
        pass

if __name__ == "__main__":
    game = Game()

    static_sprite_gmObj = GameObjectStaticSprite(game)
    animeted_sprite_gmObj = GameObjectAnimatedSprite(game)
    weapon = GameObjectAnimatedFixedOnScreen(game)
    tree1 = Tree(game, [11, 5])
    tree2 = Tree(game, [11, 5.5])
    tree3 = Tree(game, [11, 6])
    grass1 = Grass(game, [11, 7])
    grass2 = Grass(game, [12, 6])
    grass3 = Grass(game, [12, 7])
    grass4 = Grass(game, [13, 6])

    gmObjs = [static_sprite_gmObj, animeted_sprite_gmObj, weapon, tree1, tree2, tree3, grass1, grass2, grass3, grass4]
    game.load_game_objects(gmObjs)

    game.run()
