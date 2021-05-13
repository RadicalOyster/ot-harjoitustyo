"""
A module for animated overlay tiles.
"""
import pygame
from utility_functions import load_image


class AnimatedTile(pygame.sprite.Sprite):
    """
    Class representing an animated overlay tile.
    """
    def __init__(self, pos_x=0, pos_y=0, offset_x=0, offset_y=0, sprite_name=""):
        """
        Constructor for the tile
            Args:
                pos_x: X position of the tile
                pos_y: Y position of the tile
                offset_x: X offset of the tile
                offset_y: Y offset of the tile
                sprite_name: the tile's asset name
        """
        super().__init__()

        self.sprites = []
        self.active_sprite = 0
        self.sprites.append(load_image(f"{sprite_name}_1.png"))
        self.sprites.append(load_image(f"{sprite_name}_2.png"))
        self.sprites.append(load_image(f"{sprite_name}_3.png"))
        self.sprites.append(load_image(f"{sprite_name}_4.png"))
        self.sprites.append(load_image(f"{sprite_name}_4.png"))
        self.image = self.sprites[self.active_sprite]
        self.rect = self.image.get_rect()
        self.position_x = pos_x
        self.position_y = pos_y
        self.rect.x = pos_x * 64 - offset_x * 64
        self.rect.y = pos_y * 64 - offset_y * 64
        self.image.set_alpha(168)

    def update_animation(self):
        """
        Method for updating the current animation frame
        """
        self.active_sprite += 0.1
        if self.active_sprite > len(self.sprites):
            self.active_sprite = 0
        self.image = self.sprites[int(self.active_sprite)]
        self.image.set_alpha(168)

    def update_offset(self, offset_x, offset_y):
        """
        Method for updating the offset of the tile.
            Args:
                offset_x: The new X offset of the tile
                offset_y: The new Y offset of the tile
        """
        self.rect.x = self.position_x * 64 - offset_x * 64
        self.rect.y = self.position_y * 64 - offset_y * 64
