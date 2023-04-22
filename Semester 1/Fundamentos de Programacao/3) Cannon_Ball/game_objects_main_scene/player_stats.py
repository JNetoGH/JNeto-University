import pygame
from engine_JNeto_Productions.components.sprite_component import SpriteComponent
from engine_JNeto_Productions.components.text_render_component import TextRenderComponent
from engine_JNeto_Productions.components.timer_component import TimerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from game_objects_game_over_scene.game_over_manager import GameOverManager
from game_objects_main_scene.boat_and_boat_manager import Rank


# ======================================================================================================================


class ScoreManager(GameObject):

    Score = 0
    TotalBoatsSunk = 0
    Multiplier = 1
    TotalSeconds = 0

    def __init__(self, scene, rendering_layer):
        super().__init__("score_manager", scene, rendering_layer)

        self.remove_default_rect_image()
        self.transform.move_world_position(pygame.Vector2(900, 60))
        self.fix_game_object_on_screen(self.transform.world_position_read_only)

        self.points_text_render = TextRenderComponent(f"score: {ScoreManager.Score}", 15, pygame.Color(255, 255, 255), 0, 0, self)
        self.sunk_boats_text_render = TextRenderComponent(f"sunk boats: {ScoreManager.TotalBoatsSunk}", 13, pygame.Color(255, 255, 255), 0, 20, self)
        self.multiplier_text_render = TextRenderComponent(f"multiplier: {ScoreManager.Multiplier}x", 13, pygame.Color(255, 255, 255), 0, 40, self)
        self.total_seconds_text_render = TextRenderComponent(f"seconds: {ScoreManager.TotalSeconds}s", 13, pygame.Color(255, 255, 255), 0, 60, self)

        # Por cada segundo que passa no jogo, incrementamos o score por 1
        self.timer = TimerComponent(1000, self, self.__add_one_point_timer_only)

    def game_object_scene_set_start(self) -> None:
        # resets whenever the scene is set as the default one
        ScoreManager.reset_score()
        self.points_text_render.set_text(f"points: {ScoreManager.Score}")
        self.sunk_boats_text_render.set_text(f"sunk boats: {ScoreManager.TotalBoatsSunk}")
        self.multiplier_text_render.set_text(f"multiplier: {ScoreManager.Multiplier}x")

    def game_object_update(self) -> None:
        if not self.timer.is_timer_active_read_only:
            self.timer.activate()

    def __add_one_point_timer_only(self):
        ScoreManager.Score += 1
        ScoreManager.TotalSeconds += 1

        self.points_text_render.set_text(f"points: {ScoreManager.Score}")
        self.total_seconds_text_render.set_text(f"seconds: {ScoreManager.TotalSeconds}s")

    @staticmethod
    def reset_score():
        ScoreManager.Score = 0
        ScoreManager.TotalBoatsSunk = 0
        ScoreManager.Multiplier = 1
        ScoreManager.TotalSeconds = 0

    # called by the CannonBall
    def add_points_according_to_boat_rank(self, rank: Rank):
        if rank == Rank.HUGE:
            ScoreManager.Score += 1
        elif rank == Rank.LARGE:
            ScoreManager.Score += 2
        elif rank == Rank.MEDIUM:
            ScoreManager.Score += 3
        elif rank == Rank.SMALL:
            ScoreManager.Score += 4
        elif rank == Rank.TINY:
            ScoreManager.Score += 5

        ScoreManager.TotalBoatsSunk += 1
        ScoreManager.Multiplier = ScoreManager.TotalBoatsSunk // 10 + 1

        self.points_text_render.set_text(f"points: {ScoreManager.Score}")
        self.sunk_boats_text_render.set_text(f"sunk boats: {ScoreManager.TotalBoatsSunk}")
        self.multiplier_text_render.set_text(f"multiplier: {ScoreManager.Multiplier}x")


# ======================================================================================================================


class Heart(GameObject):

    PathOn = "res/art/hearts/on.png"
    PathOff = "res/art/hearts/off.png"
    ImgScale = 0.25

    def __init__(self, name: str, scene, rendering_layer):
        super().__init__(name, scene, rendering_layer)
        self.sprite = SpriteComponent(Heart.PathOn, self)

# ======================================================================================================================


class HeartsManager(GameObject):

    Hearts: list[Heart] = []
    MaxHealthPoints = 3
    HealthPoints = MaxHealthPoints

    def __init__(self, game_loop, game_over_scene, scene, rendering_layer):
        super().__init__("hearts_manager", scene, rendering_layer)

        self.game_loop = game_loop
        self.game_over_scene = game_over_scene

        self.remove_default_rect_image()
        self.transform.move_world_position(pygame.Vector2(870, 30))
        self.fix_game_object_on_screen(self.transform.world_position_read_only)

        # instantiation
        x = self.transform.world_position_read_only.x
        spacing = 30
        for i in range(0, HeartsManager.MaxHealthPoints):
            heart = Heart(f"heart{i}", self.scene, self.scene.camera.get_rendering_layer_by_name("layer_3"))
            heart.transform.move_world_position(pygame.Vector2(x, self.transform.world_position_read_only.y))
            heart.fix_game_object_on_screen(pygame.Vector2(x, self.transform.world_position_read_only.y))
            x += spacing
            heart.sprite.scale_sprite(Heart.ImgScale)
            HeartsManager.Hearts.append(heart)

    @property
    def is_player_dead(self):
        return HeartsManager.HealthPoints <= 0

    def game_object_scene_set_start(self) -> None:
        # resets whenever the scene is set as the default one
        HeartsManager.reset_health()

    def game_object_update(self) -> None:
        # print(f"HP: {HeartsManager.HealthPoints}")
        if self.is_player_dead:
            GameOverManager.set_up(ScoreManager.Score)
            self.game_loop.set_current_scene(self.game_over_scene)

    # called by fortress
    @staticmethod
    def update_hearts():
        tot_dmg = HeartsManager.MaxHealthPoints - HeartsManager.HealthPoints
        count = tot_dmg
        for heart in reversed(HeartsManager.Hearts):
            if count > 0:
                heart.sprite.change_image(Heart.PathOff)
                heart.sprite.scale_sprite(Heart.ImgScale)
            count -= 1

    @staticmethod
    def reset_health():
        HeartsManager.HealthPoints = HeartsManager.MaxHealthPoints
        for heart in reversed(HeartsManager.Hearts):
            heart.sprite.change_image(Heart.PathOn)
            heart.sprite.scale_sprite(Heart.ImgScale)
