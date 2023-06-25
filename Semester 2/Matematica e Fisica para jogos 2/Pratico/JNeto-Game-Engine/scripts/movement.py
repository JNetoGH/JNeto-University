import pygame
from pygame import Vector2
from JNeto_Game_Engine.components.behaviour import Behaviour
from JNeto_Game_Engine.components.dependencies.collision import Collision
from JNeto_Game_Engine.components.rigidbody import Rigidbody
from JNeto_Game_Engine.components.sprite_renderer import SpriteRenderer
from JNeto_Game_Engine.game_data import GameData


class Movement(Behaviour):


    def start(self) -> None:

        # initial position
        self.transform.position = Vector2(60, 180)

        # rigidbody
        self.rigid_body: Rigidbody = self.get_component(Rigidbody)
        self.rigid_body.use_gravity = True
        self.rigid_body.bounces = True
        self.rigid_body.use_drag = True
        self.rigid_body.add_force(Vector2(1, -0.1), 700)

        # sprite render
        self.spritRenderer: SpriteRenderer = self.get_component(SpriteRenderer)
        self.spritRenderer.scale_image(0.25)

    def update(self) -> None:
        for event in GameData.Game_Events_This_Frame:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rigid_body.add_force(pygame.Vector2(-1, 0), 100)
                elif event.key == pygame.K_RIGHT:
                    self.rigid_body.add_force(pygame.Vector2(1, 0), 100)
                elif event.key == pygame.K_UP:
                    self.rigid_body.add_force(pygame.Vector2(0, -1), 100)
                elif event.key == pygame.K_DOWN:
                    self.rigid_body.add_force(pygame.Vector2(0, 1), 100)
                elif event.key == pygame.K_b:
                    self.rigid_body.bounces = not self.rigid_body.bounces
                elif event.key == pygame.K_p:
                    if GameData.FPS_CAP == 260:
                        GameData.FPS_CAP = 30
                    elif GameData.FPS_CAP == 30:
                        GameData.FPS_CAP = 260

    def on_collision_enter(self, collisions: list[Collision]) -> None:
        pass
        print("COLLIDER ", end="")
        self.print_collision_stuff(collisions)
        for collision in collisions:
            if collision.collided.game_object.name == "Sea":
                self.rigid_body.add_force(Vector2(0, -1), 2)

    def on_trigger_enter(self, collisions: list[Collision]) -> None:
        pass
        print("TRIGGER ", end="")
        self.print_collision_stuff(collisions)

    def print_collision_stuff(self, collisions: list[Collision]):
        txt = "COLLISIONS:"
        for col in collisions:
            txt += f" (name: {col.collided.game_object.name}, col_name: {col.collided.collider_name}, trigger: {col.collided.is_trigger})"
        print(txt)
        