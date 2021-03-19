import pygame
from utility_functions import load_image
from enum import Enum

class Alignment(Enum):
    ALLY = 0
    ENEMY = 1

sprite_suffixes = ["", "_e"]

class Unit(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, alignment=Alignment.ALLY, hp=15):
        super().__init__()

        self.unit_class = "fighter"
        self.movement = 2
        self.sprites = []
        self.active_sprite = 0
        self.alignment = alignment
        self.hp = hp
        self.sprites.append(load_image("fighter_1" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_2" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_2" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image("fighter_1" + sprite_suffixes[self.alignment.value] + ".png"))
        self.image = pygame.transform.scale(self.sprites[self.active_sprite], (64, 64))
        self.has_moved = False

        #temporary until weapons are implemented
        self.range = 1


        self.position_x = x
        self.position_y = y

        self.rect = self.image.get_rect()
        self.rect.x = x * 64
        self.rect.y = y * 64

    def updatePosition(self, x, y):
        self.position_x = x
        self.position_y = y
        self.rect.x = x * 64
        self.rect.y = y * 64
    
    def updateAnimation(self):
        #active frame is still updated even when unit has not moved to keep animations in sync
        self.active_sprite += 0.1
        if (self.active_sprite > len(self.sprites)):
            self.active_sprite = 0
        if not self.has_moved:            
            self.image = pygame.transform.scale(self.sprites[int(self.active_sprite)], (64,64))
    
    def deactivate(self):
        self.has_moved = True
        self.image = pygame.transform.scale(load_image("fighter_inactive.png"), (64,64))
    
    def activate(self):
        self.has_moved = False
        self.image = pygame.transform.scale(self.sprites[int(self.active_sprite)], (64,64))