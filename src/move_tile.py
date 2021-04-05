import pygame
from utility_functions import load_image

class MoveTile(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, offset_X=0, offset_Y=0):
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
        self.position_x = x
        self.position_y = y
        self.rect.x = x * 64 - offset_X * 64
        self.rect.y = y * 64 - offset_Y * 64
        self.image.set_alpha(168)

    def updateAnimation(self):
        self.active_sprite += 0.1
        if (self.active_sprite > len(self.sprites)):
            self.active_sprite = 0
        self.image = self.sprites[int(self.active_sprite)]
        self.image.set_alpha(168)
    
    def updateOffset(self, offset_x, offset_y):
        self.rect.x = self.position_x * 64 - offset_x * 64
        self.rect.y = self.position_y * 64 - offset_y * 64