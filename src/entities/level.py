import sys
from enum import Enum

movement_costs = [1, sys.maxsize]

class Level():
    """A class containing level data.
    """
    def __init__(self, level_data, units):
        """Constructor for level.
            Args:
            level_data: A 2D array containing the type of tile at each coordinate.
            units: A list of units in the level.
        """
        self.level_data = level_data
        self.movement_data = self._convert_to_movement_data(level_data)
        self.units = units
    

    def _convert_to_movement_data(self, level_data):
        """A method to convert tile data into movement data.
            Args:
            level_data: The level data to convert.
        """
        movement_data = [[None for y in range(len(self.level_data[0]))] for x in range(len(self.level_data))]

        for i in range (0, len(self.level_data)):
            for j in range (0, len(self.level_data[0])):
                tile = level_data[i][j]
                movement_data[i][j] = movement_costs[tile]
        
        return movement_data