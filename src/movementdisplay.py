import pygame
import pathfinding
from utility_functions import load_image

class MovementDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super(MovementDisplay, self).__init__()
        self.movement_display = pygame.sprite.Group()
        self.allowed_tiles = []
    
    def UpdateMovementTiles(self, x, y):
        self.movement_display.empty()
        allowed_tiles = pathfinding.GetMovementRange(y, x)
        self.allowed_tiles = allowed_tiles
        for tile in allowed_tiles:
            self.movement_display.add(MoveTile(tile[0], tile[1]))
    
    def ClearMovementRange(self):
        self.movement_display.empty()
    
    def GetMovementRange(self):
        return self.movement_display
    
    def GetAllowedTiles(self):
        return self.allowed_tiles

class MoveTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = load_image("movetile.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * 64
        self.rect.y = y * 64