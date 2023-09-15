import pygame
from settings import PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)
        # Player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.gravity = 0.5
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            print("x")
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_SPACE]:
            self.jump()
        else:
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        self.apply_gravity()
