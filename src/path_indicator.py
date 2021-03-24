import pygame
from utility_functions import load_image

class PathIndicator(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(load_image("path_indicator.png"), (64,64))
        self.position_x = x
        self.position_y = y

        self.rect = self.image.get_rect()
        self.rect.x = x * 64
        self.rect.y = y * 64