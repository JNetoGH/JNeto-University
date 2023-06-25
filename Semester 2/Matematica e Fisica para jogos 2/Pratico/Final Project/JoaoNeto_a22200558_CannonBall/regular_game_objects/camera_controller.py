import pygame

from engine_JNeto_Productions.game_object_base_class import GameObject
from engine_JNeto_Productions.scene_camera import SceneCamera
from engine_JNeto_Productions.systems.game_time_system import GameTime
from engine_JNeto_Productions.systems.input_manager_system import InputManager


class CameraController(GameObject):

    def __init__(self, scene, rendering_layer):
        super().__init__("camera_controller", scene, rendering_layer)
        self.remove_default_rect_image()

        # Get the main camera of the scene and store its initial position
        self.main_camera: SceneCamera = self.scene.camera
        self.camera_initial_position: pygame.Vector2 = self.main_camera.world_position_read_only

        # Set the maximum x-coordinate for camera movement and the speed of camera movement
        self.MAX_X = 1000
        self.speed = 300

    # Called once per frame by the Game Loop
    def game_object_update(self) -> None:
        # Update the camera's position based on the user input
        self.move_via_horizontal_axis()

    def move_via_horizontal_axis(self):
        # Move the camera horizontally based on the input and the speed
        position = self.main_camera.world_position_read_only
        position.x += InputManager.Horizontal_Axis * self.speed * GameTime.DeltaTime

        # Check if the camera has reached its initial position or surpassed the maximum x-coordinate,
        # and if so, stop the movement
        if self.camera_initial_position.x > position.x or position.x > self.MAX_X:
            return

        # Focus the camera at the new position in the world
        self.main_camera.focus_camera_at_world_position(position)