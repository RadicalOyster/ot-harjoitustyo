"""
A module for path indicators to display
the path a unit is going to take.
"""
import pygame
from utility_functions import load_image


class PathIndicator(pygame.sprite.Sprite):
    """
    Class for the path indicator.
    """
    def __init__(self, pos_x, pos_y, offset_x=0, offset_y=0):
        """
        Constructor for the path indicator.
            Args:
                pos_x: X position of the indicator
                pos_y: Y position of the indicator
                offset_x: X offset of the indicator
                offset_y: Y offset of the indicator
        """
        super().__init__()
        self.image = pygame.transform.scale(
            load_image("path_indicator.png"), (64, 64))
        self.position_x = pos_x
        self.position_y = pos_y

        self.rect = self.image.get_rect()
        self.rect.x = pos_x * 64 - offset_x * 64
        self.rect.y = pos_y * 64 - offset_y * 64

    def update_offset(self, offset_x, offset_y):
        """
        Method to update the offset of the path indicator.
            Args:
                offset_x: New X offset of the indicator.
                offset_y: New Y offset of the indicator.
        """
        self.rect.x = self.position_x * 64 - offset_x * 64
        self.rect.y = self.position_y * 64 - offset_y * 64
