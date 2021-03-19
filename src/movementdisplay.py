import pygame
import pathfinding
from utility_functions import load_image

class MovementDisplay(pygame.sprite.Sprite):
    def __init__(self):
        super(MovementDisplay, self).__init__()
        self.movement_display = pygame.sprite.Group()
        self.attack_display = pygame.sprite.Group()
        self.allowed_tiles = []
        self.attack_tiles = []
    
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
        return self.movement_display
    
    def GetAttackRange(self):
        return self.attack_display
    
    def GetAllowedTiles(self):
        return self.allowed_tiles
    
    def GetAttackTiles(self):
        return self.attack_tiles

class MoveTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.sprites = []
        self.active_sprite = 0
        self.sprites.append(load_image("movetile_1.png"))
        self.sprites.append(load_image("movetile_2.png"))
        self.sprites.append(load_image("movetile_3.png"))
        self.sprites.append(load_image("movetile_4.png"))
        self.sprites.append(load_image("movetile_4.png"))
        self.image = self.sprites[self.active_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x * 64
        self.rect.y = y * 64
        self.image.set_alpha(168)

    def updateAnimation(self):
        self.active_sprite += 0.1
        if (self.active_sprite > len(self.sprites)):
            self.active_sprite = 0
        self.image = self.sprites[int(self.active_sprite)]
        self.image.set_alpha(168)

class AttackTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.sprites = []
        self.active_sprite = 0
        self.sprites.append(load_image("attacktile_1.png"))
        self.sprites.append(load_image("attacktile_2.png"))
        self.sprites.append(load_image("attacktile_3.png"))
        self.sprites.append(load_image("attacktile_4.png"))
        self.sprites.append(load_image("attacktile_4.png"))
        self.image = self.sprites[self.active_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x * 64
        self.rect.y = y * 64
        self.image.set_alpha(168)

    def updateAnimation(self):
        self.active_sprite += 0.1
        if (self.active_sprite > len(self.sprites)):
            self.active_sprite = 0
        self.image = self.sprites[int(self.active_sprite)]
        self.image.set_alpha(168)