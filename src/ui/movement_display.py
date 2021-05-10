import pygame
from .attack_tile import AttackTile
from .move_tile import MoveTile
from utility_functions import load_image


class MovementDisplay(pygame.sprite.Sprite):
    def __init__(self, pathfinding):
        super(MovementDisplay, self).__init__()
        self.movement_display = pygame.sprite.Group()
        self.attack_display = pygame.sprite.Group()
        self.allowed_tiles = []
        self.attack_tiles = []
        self.hide_movement = False
        self.hide_attack = False
        self.pathfinding = pathfinding
        self.current_ranges = pygame.sprite.Group()

    def update_movement_tiles(self, pos_x, pos_y, unit, level, offset_X=0, offset_Y=0):
        self.movement_display.empty()
        self.pathfinding.calculate_distances(pos_x, pos_y, level)
        allowed_tiles = self.pathfinding.return_ranges(unit.movement)
        self.allowed_tiles = allowed_tiles
        for tile in allowed_tiles:
            self.movement_display.add(
            MoveTile(tile[0], tile[1], offset_X, offset_Y))

    def update_attack_tiles(self, unit, offset_x=0, offset_y=0):
        self.attack_display.empty()
        checked_tiles = []
        attack_range = unit.range

        for tile in self.allowed_tiles:
            for i in range(-attack_range, attack_range + 1):
                for j in range(-attack_range, attack_range + 1):
                    if abs(i) + abs(j) > attack_range or (i == 0 and j == 0):
                        continue
                    else:
                        new_tile = (tile[0] + i, tile[1] + j)
                        if new_tile not in self.allowed_tiles and new_tile not in checked_tiles:
                            self.attack_display.add(AttackTile(
                                new_tile[0], new_tile[1], offset_x, offset_y
                            ))
                            checked_tiles.append(new_tile)


    def get_current_attack_ranger(self, pos_x, pos_y, attack_range, offset_x, offset_y):
        self.pathfinding.calculate_distances(pos_x, pos_y)
        tiles_in_range = self.pathfinding.return_ranges(attack_range)
        for tile in tiles_in_range:
            if (tile[0] == pos_x and tile[1] == pos_y):
                continue
            self.current_ranges.add(AttackTile(
                tile[0], tile[1], offset_x, offset_y))
        return tiles_in_range

    def get_current_attack_ranges(self, pos_x, pos_y, attack_range, offset_x, offset_y):
        tile = (pos_x, pos_y)
        tiles = []
        checked_tiles = []
        for i in range(-attack_range, attack_range + 1):
            for j in range(-attack_range, attack_range + 1):
                if abs(i) + abs(j) > attack_range or (i == 0 and j == 0):
                    continue
                new_tile = (tile[0] + i, tile[1] + j)
                if new_tile not in checked_tiles:
                    tiles.append(new_tile)
                    self.current_ranges.add(AttackTile(
                        new_tile[0], new_tile[1], offset_x, offset_y
                    ))
                    checked_tiles.append(new_tile)
        return tiles

    def clear_current_attack_ranges(self):
        self.current_ranges = pygame.sprite.Group()

    def clear_movement_range(self):
        self.movement_display.empty()
        self.attack_display.empty()

    def get_movement_range(self):
        if self.hide_movement == True:
            return pygame.sprite.Group()
        return self.movement_display

    def get_attack_range(self):
        if self.hide_attack == True:
            return pygame.sprite.Group()
        return self.attack_display

    def get_allowed_tiles(self):
        return self.allowed_tiles

    def get_attack_tiles(self):
        return self.attack_tiles
