import pygame

from engine_JNeto_Productions.components.text_render_component import TextRenderComponent
from engine_JNeto_Productions.components.timer_component import TimerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.file_manager_system import FileManager
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen
from game_objects_score_scene.score_registration_floating_menu import ScoreRegistrationFloatingMenu


class GameOverManager(GameObject):

    Count: bool = False
    Score = 0
    # The amount on the top shown
    TopLimit = 4

    def __init__(self, score_scene, game_loop, scene, rendering_layer):
        super().__init__("game_over", scene, rendering_layer)

        self.game_loop = game_loop
        self.score_scene = score_scene

        self.game_over_sound = pygame.mixer.Sound("res/audio/annauncer/Game over 1.wav")

        self.remove_default_rect_image()
        self.fix_game_object_on_screen(pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfDummyScreenHeight))
        self.header = TextRenderComponent("GAME OVER", 70, pygame.Color("white"), 0, 0, self)
        self.score_text = TextRenderComponent("SCORE: 0", 40, pygame.Color("white"), 0, 100, self)

        self.duration_in_seg = 4
        self.timer_comp = TimerComponent(self.duration_in_seg * 1000, self, self.change_scene)

    def game_object_scene_set_start(self) -> None:
        self.game_over_sound.play()

    def game_object_update(self) -> None:
        # print(f"timer elapsed time: {self.timer_comp.elapsed_time_read_only} ms")
        # print(f"timer is activate: {self.timer_comp.is_timer_active_read_only}\n")
        if GameOverManager.Count:
            GameOverManager.Count = False
            self.score_text.set_text(f"SCORE: {GameOverManager.Score}")
            self.timer_comp.activate()

    def change_scene(self):
        # registration availability verification
        can_save_score = False
        FileManager.sort_csv_file_by_column_values("score_sheet.csv", 1)
        lines = FileManager.read_from_csv_file("score_sheet.csv")
        if GameOverManager.Score < 0:
            can_save_score = False
        elif len(lines) < GameOverManager.TopLimit:
            can_save_score = True
        elif int(lines[GameOverManager.TopLimit-1][1]) < GameOverManager.Score:
            can_save_score = True

        # syncs and change to score scene to register the score or not
        ScoreRegistrationFloatingMenu.TotalPoints = GameOverManager.Score
        ScoreRegistrationFloatingMenu.Show = can_save_score
        print("game over scene -> score scene")
        self.game_loop.set_current_scene(self.score_scene)

    @staticmethod
    def set_up(score):
        GameOverManager.Count = True
        GameOverManager.Score = score
