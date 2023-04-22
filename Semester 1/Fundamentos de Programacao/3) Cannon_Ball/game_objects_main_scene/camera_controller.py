import pygame

from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.scene_camera import SceneCamera
from engine_JNeto_Productions.systems.game_time_system import GameTime
from engine_JNeto_Productions.systems.input_manager_system import InputManager


class CameraController(GameObject):

    def __init__(self, scene, rendering_layer):
        super().__init__("camera_controller", scene, rendering_layer)
        self.remove_default_rect_image()
        self.main_camera: SceneCamera = self.scene.camera
        self.camera_initial_position: pygame.Vector2 = self.main_camera.world_position_read_only
        self.MAX_X = 800  # 800
        self.speed = 300

    def game_object_update(self) -> None:
        self.move_via_horizontal_axis()

    def move_via_horizontal_axis(self):
        position = self.main_camera.world_position_read_only
        position.x += InputManager.Horizontal_Axis * self.speed * GameTime.DeltaTime
        if self.camera_initial_position.x > position.x or position.x > self.MAX_X:
            return
        self.main_camera.focus_camera_at_world_position(position)
