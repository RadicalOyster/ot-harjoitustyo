import pygame
from utility_functions import load_image


class PathIndicator(pygame.sprite.Sprite):
    def __init__(self, x, y, offset_X=0, offset_Y=0):
        super().__init__()
        self.image = pygame.transform.scale(
            load_image("path_indicator.png"), (64, 64))
        self.position_x = x
        self.position_y = y

        self.rect = self.image.get_rect()
        self.rect.x = x * 64 - offset_X * 64
        self.rect.y = y * 64 - offset_Y * 64

    def update_offset(self, offset_x, offset_y):
        self.rect.x = self.position_x * 64 - offset_x * 64
        self.rect.y = self.position_y * 64 - offset_y * 64
