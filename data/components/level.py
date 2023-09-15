import pygame
from settings import TILE_SIZE, SCREEN_WIDTH
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
            self.world_shift = 8
            player.speed = 0
        elif player_x >= SCREEN_WIDTH / 2 and player_dir_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        # Player tiles
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()
