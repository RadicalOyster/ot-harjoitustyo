import pygame
import pathfinding
from attack_tile import AttackTile
from move_tile import MoveTile
from utility_functions import load_image

class MovementDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super(MovementDisplay, self).__init__()
        self.movement_display = pygame.sprite.Group()
        self.attack_display = pygame.sprite.Group()
        self.allowed_tiles = []
        self.attack_tiles = []
        self.hide_movement = False
        self.hide_attack = False
    
    def UpdateMovementTiles(self, x, y, unit):
        self.movement_display.empty()
        allowed_tiles = pathfinding.GetMovementRange(y, x, unit.movement)
        self.allowed_tiles = allowed_tiles
        for tile in allowed_tiles:
            self.movement_display.add(MoveTile(tile[0], tile[1]))

    def UpdateAttackTiles(self, x, y, unit):
        self.attack_display.empty()
        reachable_tiles = pathfinding.GetMovementRange(y, x, unit.movement+unit.range)
        attack_tiles = []
        for tile in reachable_tiles:
            if tile not in self.allowed_tiles:
                attack_tiles.append(tile)
        self.attack_tiles = attack_tiles
        for tile in attack_tiles:
            self.attack_display.add(AttackTile(tile[0], tile[1]))
    
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