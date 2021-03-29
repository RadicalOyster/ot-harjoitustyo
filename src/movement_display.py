import pygame
from attack_tile import AttackTile
from move_tile import MoveTile
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
    
    def UpdateMovementTiles(self, x, y, unit):
        self.movement_display.empty()
        self.pathfinding.CalculateDistances(x, y)
        allowed_tiles = self.pathfinding.ReturnRanges(unit.movement)
        self.allowed_tiles = allowed_tiles
        for tile in allowed_tiles:
            self.movement_display.add(MoveTile(tile[0], tile[1]))

    def UpdateAttackTiles(self, x, y, unit):
        self.attack_display.empty()
        self.pathfinding.CalculateDistances(x, y)
        reachable_tiles = self.pathfinding.ReturnRanges(unit.movement + unit.range)
        attack_tiles = []
        for tile in reachable_tiles:
            if tile not in self.allowed_tiles:
                attack_tiles.append(tile)
        self.attack_tiles = attack_tiles
        for tile in attack_tiles:
            self.attack_display.add(AttackTile(tile[0], tile[1]))
    
    def GetCurrentAttackRanges(self, x, y, range):
        self.pathfinding.CalculateDistances(x, y)
        tiles_in_range = self.pathfinding.ReturnRanges(range)
        for tile in tiles_in_range:
            if (tile[0] == x and tile[1] == y):
                continue
            self.current_ranges.add(AttackTile(tile[0], tile[1]))
        return tiles_in_range
    
    def ClearCurrentAttackRanges(self):
        self.current_ranges = pygame.sprite.Group()
    
    def ClearMovementRange(self):
        self.movement_display.empty()
        self.attack_display.empty()
    
    def GetMovementRange(self):
        if self.hide_movement == True:
            return pygame.sprite.Group()
        return self.movement_display
    
    def GetAttackRange(self):
        if self.hide_attack == True:
            return pygame.sprite.Group()
        return self.attack_display
    
    def GetAllowedTiles(self):
        return self.allowed_tiles
    
    def GetAttackTiles(self):
        return self.attack_tiles