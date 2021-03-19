import pygame
from utility_functions import load_image

class Unit(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.unit_class = "fighter"
        self.movement = 3
        self.sprites = []
        self.sprites.append(load_image("fighter_1.png"))
        self.sprites.append(load_image("fighter_2.png"))
        self.sprites.append(load_image("fighter_3.png"))
        self.sprites.append(load_image("fighter_3.png"))
        self.sprites.append(load_image("fighter_3.png"))
        self.sprites.append(load_image("fighter_3.png"))
        self.sprites.append(load_image("fighter_2.png"))
        self.sprites.append(load_image("fighter_1.png"))
        self.active_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.active_sprite], (64, 64))


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
        self.active_sprite += 0.1

        if (self.active_sprite > len(self.sprites)):
            self.active_sprite = 0
        
        self.image = pygame.transform.scale(self.sprites[int(self.active_sprite)], (64,64))