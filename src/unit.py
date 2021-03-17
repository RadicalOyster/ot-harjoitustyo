import pygame
from utility_functions import load_image

class Unit(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.unit_class = "fighter"
        self.movement = 4
        self.image = load_image("fighter.png")

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