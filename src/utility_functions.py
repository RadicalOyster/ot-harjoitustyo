import pygame
import os

dirname = os.path.dirname(__file__)

# Loads an image for use in pygame


def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )

# Checks if there is a unit in the coordinates (X,Y) and returns the unit if true


def UnitOnTile(x, y, units):
    for unit in units:
        if unit.position_x == x and unit.position_y == y:
            return unit
    return None
