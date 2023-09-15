import pygame
from settings import TILE_SIZE, SCREEN_WIDTH, PLAYER_SPEED
from .tiles import Tile
from .player import Player


class Level:
    def __init__(self, level_data, surface) -> None:
        """Level setup

        Args:
            level_data (_type_): _description_
            surface (_type_): _description_
        """
        self.display_surface = surface
        self.setup(level_data)
        self.world_shift = 0

    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == "X":
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                if col == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_dir_x = player.direction.x

        if player_x <= SCREEN_WIDTH / 4 and player_dir_x < 0:
            self.world_shift = PLAYER_SPEED
            player.speed = 0
        elif player_x >= SCREEN_WIDTH / 2 and player_dir_x > 0:
            self.world_shift = -PLAYER_SPEED
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = PLAYER_SPEED

    def horzontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        # Player tiles
        self.player.update()
        self.horzontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
