import pygame
import os

dirname = os.path.dirname(__file__)

def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )

def UnitOnTile(x, y, units):
    for unit in units:
        if unit.position_x == x and unit.position_y == y:
            return unit
    return None