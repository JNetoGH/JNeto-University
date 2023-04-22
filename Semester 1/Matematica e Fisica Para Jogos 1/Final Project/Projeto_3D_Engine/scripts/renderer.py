import pygame as pg
from settings import settings


# RENDERS ALL OBJS AND THEIR TEXTURES, IT DOESN'T MAKE AND 2D TO 3D CONVERSION LIKE THE RAY CASTER, ONLY RENDERS
# It renders the sky, floor, walls and sprite objects, if there are more things they will be rendered by the Renderer as well
class Renderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        # holds a dictionary with all wall_textures
        self.wall_textures = self.load_wall_textures()
        #sky
        self.sky_image = self.get_texture("resources/wall_textures/sky.png", (settings.SCREEN_WIDTH, settings.SCREEN_HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_back_ground()
        self.render_game_objects()

    def draw_back_ground(self):
        # sky: draw 2 images and connects them using the player mouse relative pos
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % settings.SCREEN_WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + settings.SCREEN_WIDTH, 0))
        # floor: just a rectangle
        pg.draw.rect(self.screen, settings.FLOOR_COLOR, (0, settings.SCREEN_HALF_HEIGHT, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

    # draws the resulting texture of the objects to render list
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    # loads a texture from the path and return a scaled img
    @staticmethod
    def get_texture(path, res=(settings.TEXTURE_SIZE, settings.TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    # returns a dictionary in which the texture number is the key and the texture is value
    # at map.py, the numbers refers to what texture might be applied to the walls
    # it gets just the paths and converts it to loaded textures
    def load_wall_textures(self):
        textures_path_dic = self.game.map.wall_textures_path_dictionary
        textures_dic = {}
        for key in textures_path_dic:
            textures_dic[key] = Renderer.get_texture(textures_path_dic[key])
        return textures_dic
