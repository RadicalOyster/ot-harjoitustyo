import pygame
from enum import Enum

class CharMenuCommands(Enum):
    ATTACK = 0
    ITEM = 1
    WAIT = 2

#Handles selection of menu options
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
    
    
    def ScrollMenu(self, menu, pos):
        self.index = pos
        if pos >= len(menu):
            self.index = 0
        elif pos < 0:
            self.index = len(menu) - 1
        
        self.rect.left = 8
        self.rect.top = 5 + self.index * 20
    
    def ResetCursor(self):
        self.index = 0
        self.rect.left = 8
        self.rect.top = 5
    
    def UpdateUnitSelection(unit):
        self.selected_unit = unit
    
    def UnselectUnit():
        self.selected_unit = None
    
    def UpdateState(state):
        self.state = state
    
    def GetCommands(self):
        commands = []
        commands.append(CharMenuCommands.ATTACK.name.capitalize())
        commands.append(CharMenuCommands.ITEM.name.capitalize())
        commands.append(CharMenuCommands.WAIT.name.capitalize())
        return commands