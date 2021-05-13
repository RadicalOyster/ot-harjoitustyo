"""
Module containing utility functions
"""
import os
import pygame

dirname = os.path.dirname(__file__)

def load_image(filename):
    """
    Loads an image with the given filename from the assets folder.
        Args:
            filename: the name of the file to load.
    """
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )


def unit_on_tile(pos_x, pos_y, units):
    """
    Iterates through a list of units and returns True if a unit
    with the given x, y coordinates is found. Otherwise returns
    None.
    (Deprecated in favor of a more efficeint solution,
    will be removed once all relevant code has been refactored.)
        Args:
            pos_x: the X position of the tile to search.
            pos_y: the Y position of the tile to search.
        Returns:
            The unit on the given tile or None if there is no unit on that tile.
    """
    for unit in units:
        if unit.position_x == pos_x and unit.position_y == pos_y:
            return unit
    return None
