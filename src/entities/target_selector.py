"""
Module for functions relating to selecting a unit
for combat.
"""
from utility_functions import unit_on_tile
from entities.unit import Alignment

# Handles selecting target unit for actions


class TargetSelector():
    """
    Class that handles target selection.
    """
    def __init__(self):
        self.tiles = []
        self.tiles_with_units = []
        self.selection = 0

    def update_tiles(self, tiles, units):
        """
        Updates the currently selectable tiles.
            Args:
                tiles: a list of tuples in the format (x,y) representing tiles within attack range
                units: a list of units
        """
        self.tiles = tiles

        for tile in tiles:
            unit = unit_on_tile(tile[0], tile[1], units)
            if unit is not None and unit.alignment == Alignment.ENEMY:
                self.tiles_with_units.append(tile)

    def clear_tiles(self):
        """
        Clears all tiles and sets the selected index to 0
        """
        self.tiles = []
        self.tiles_with_units = []
        self.selection = 0

    def _scroll_selection(self, direction):
        if self.selection == 0 and direction == -1:
            self.selection = len(self.tiles_with_units) - 1
        elif self.selection == len(self.tiles_with_units) - 1 and direction == 1:
            self.selection = 0
        else:
            self.selection += direction

    def set_selection(self, selection):
        """
        Updates the currently selected index.
            Args:
                selection: the new selected index
        """
        self.selection = selection

    def get_selection(self):
        """
        Returns the currently selected tile.
            Args:
                selection: the new selected index
            Returns:
                The currently selected unit. If none of the given tiles have
                an enemy unit on them, returns (-1, -1).
        """
        if len(self.tiles_with_units) > 0:
            return self.tiles_with_units[self.selection]
        return (-1, -1)
