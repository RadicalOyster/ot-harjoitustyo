import pygame
from enum import Enum

class CharMenuCommands(Enum):
    WAIT = 0

class MenuCursor(pygame.sprite.Sprite):
    def __init__(self):
        super(MenuCursor, self).__init__()
        self.surf = pygame.Surface((60, 24))
        self.surf.fill((222,222,222))
        self.surf.set_alpha(98)
        self.rect = self.surf.get_rect()
        self.rect.left = 8
        self.rect.top = 5
        self.index = 0
    
    def UpdatePosition(self, x,y):
        self.position_x = x
        self.position_y = y

        self.rect.left = self.position_x * 64
        self.rect.top = self.position_y * 64
    
    def UpdatePosition(self, menu, pos):
        self.index = pos
        if pos >= len(menu):
            pos = 0
        elif pos < 0:
            pos = len(menu)
    
    def UpdateUnitSelection(unit):
        self.selected_unit = unit
    
    def UnselectUnit():
        self.selected_unit = None
    
    def UpdateState(state):
        self.state = state
    
    def GetCommands(self):
        commands = []
        commands.append(CharMenuCommands.WAIT.name.capitalize())
        return commands