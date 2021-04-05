import pygame
from enum import Enum

class CursorState(Enum):
    MAP = 0
    MOVE = 1
    CHARMENU = 2
    ATTACK = 3
    INACTIVE = 4

class Cursor(pygame.sprite.Sprite):
    def __init__(self, x, y, offset_x=0, offset_y=0):
        super(Cursor, self).__init__()
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((0, 44, 255))
        self.surf.set_alpha(128)
        self.rect = self.surf.get_rect()
        self.position_x = x
        self.position_y = y
        self.rect.left = self.position_x * 64 - offset_x * 64
        self.rect.top = self.position_y * 64 - offset_y * 64
        self.selected_unit = None
        self.state = CursorState.MAP
    
    def UpdatePosition(self, x, y, offset_x=0, offset_y=0):
        self.position_x = x
        self.position_y = y

        self.rect.left = x * 64 - offset_x * 64
        self.rect.top = y * 64 - offset_y * 64
    
    def UpdateMenuPosition(self, index):
        self.selected_item = index
    
    def UpdateUnitSelection(unit):
        self.selected_unit = unit
    
    def UnselectUnit(self):
        self.selected_unit = None
    
    def UpdateState(state):
        self.state = state