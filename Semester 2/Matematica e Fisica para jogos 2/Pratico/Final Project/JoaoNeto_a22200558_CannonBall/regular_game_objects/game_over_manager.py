import pygame
from engine_JNeto_Productions.components.text_render_component import TextRenderComponent
from engine_JNeto_Productions.components.timer_component import TimerComponent
from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen


class GameOverManager(GameObject):

    Count: bool = False
    Score = 0

    def __init__(self, score_scene, game_loop, scene, rendering_layer):
        super().__init__("game_over", scene, rendering_layer)

        # other setting
        self.duration_in_seg = 2.5
        self.remove_default_rect_image()

        # Store the references to the score scene and the game loop
        self.score_scene = score_scene
        self.game_loop = game_loop

        # Load the game over sound
        self.game_over_sound = pygame.mixer.Sound("res/audio/annauncer/Game over 1.wav")

        # Fix the game object in the center of the screen
        self.fix_game_object_on_screen(
            pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfDummyScreenHeight))

        # Create text render components for the header and the score
        self.header = TextRenderComponent("GAME OVER", 70, pygame.Color("white"), 0, 0, self)
        self.score_text = TextRenderComponent("SCORE: 0", 40, pygame.Color("white"), 0, 100, self)

        # Create a timer component to delay the scene transition
        self.timer_comp = TimerComponent(self.duration_in_seg * 1000, self, self.change_scene)

    # Called when the scene is set by the game loop
    def game_object_start(self) -> None:
        # Play the game over sound when the game object starts
        self.game_over_sound.play()

    # called once per frame by the game loop
    def game_object_update(self) -> None:
        # Check if a game over event has occurred
        if GameOverManager.Count:
            GameOverManager.Count = False

            # Update the score text with the current score
            self.score_text.set_text(f"SCORE: {GameOverManager.Score}")

            # Activate the timer component to trigger the scene transition after the specified duration
            self.timer_comp.activate()

    def change_scene(self):
        # Change the current scene in the game loop to the score scene
        self.game_loop.set_current_scene(self.score_scene)

    @staticmethod
    def set_up(score):
        # Set up the game over event with the provided score
        GameOverManager.Count = True
        GameOverManager.Score = score