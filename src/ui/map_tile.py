"""
A module for static map tiles.
"""
import pygame

class MapTile(pygame.sprite.Sprite):
    """
    Class representing static tile representing a spot on the level map.
    """
    def __init__(self, image, pos_x=0, pos_y=0, offset_x=0, offset_y=0):
        """
        Constructor for MapTile.
            Args:
                image: the tile image
                pos_x: X position of the tile
                pos_y: Y position of the tile
                offset_x: X offset of the tile
                offset_y: Y offset of the tile
        """
        super().__init__()
        self.position_x = pos_x
        self.position_y = pos_y
        self.image = image
        self.rect = image.get_rect() 
        self.rect.x = pos_x * 64 - offset_x * 64
        self.rect.y = pos_y * 64 - offset_y * 64

    def update_offset(self, offset_x, offset_y):
        """
        A method for updating the offset of the tile.
            Args:
                offset_x: the new X offset of the tile
                offset_y: the new Y offset of the tile
        """
        self.rect.x = self.position_x * 64 - offset_x * 64
        self.rect.y = self.position_y * 64 - offset_y * 64
