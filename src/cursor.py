import pygame
from enum import Enum

class CursorState(Enum):
    MAP = 0
    CHARMENU = 1
    INACTIVE = 2

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super(Cursor, self).__init__()
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((0, 44, 255))
        self.surf.set_alpha(128)
        self.rect = self.surf.get_rect()
        self.position_x = 1
        self.position_y = 1
        self.rect.left = self.position_x * 64
        self.rect.top = self.position_y * 64
        self.selectedUnit = None
        self.state = CursorState.MAP
    
    def UpdatePosition(self, x,y):
        self.position_x = x
        self.position_y = y

        self.rect.left = self.position_x * 64
        self.rect.top = self.position_y * 64
    
    def UpdateUnitSelection(unit):
        self.selectedUnit = unit
    
    def UnselectUnit():
        self.selectedUnit = None
    
    def UpdateState(state):
        self.state = state