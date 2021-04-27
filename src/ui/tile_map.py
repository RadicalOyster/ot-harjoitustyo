import pygame
from enum import Enum
from utility_functions import load_image
from ui.map_tile import MapTile

class TileType(Enum):
    PLAIN = 0
    PEAK = 1

class TileMap(pygame.sprite.Sprite):
    def __init__(self, level_data):
        super(TileMap, self).__init__()
        self.tile_map = pygame.sprite.Group()
        self._load_tiles(level_data)

    def _load_tiles(self, level_data):
        for i in range(0, len(level_data)):
            for j in range (0, len(level_data[0])):
                tile_type = level_data[i][j]

                if tile_type == TileType.PEAK.value:
                    tile_image = load_image("peak.png")
                else:
                    tile_image = load_image("plain.png")
                        
                self.tile_map.add(MapTile(tile_image, j, i, 0, 0))
    
    def get_tiles(self):
        return self.tile_map