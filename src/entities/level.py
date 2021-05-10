import sys
from enum import Enum
from entities.unit import Alignment

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
        self.movement_data = self._convert_to_movement_data()
        self.units = units
        self.unit_positions = ([[None for j in range(0,len(self.movement_data[0]))]
        for i in range (0,len(self.movement_data))])
        for unit in units:
            self.unit_positions[unit.position_y][unit.position_x] = unit


    def _convert_to_movement_data(self):
        """A method to convert tile data into movement data.
            Args:
            level_data: The level data to convert.
        """
        movement_data = [[None for y in range(len(self.level_data[0]))]
        for x in range(len(self.level_data))]

        for i in range (0, len(self.level_data)):
            for j in range (0, len(self.level_data[0])):
                tile = self.level_data[i][j]
                movement_data[i][j] = movement_costs[tile]

        return movement_data

    def get_movement_data_with_units(self, is_player_phase):
        movement_data_with_units = ([[self.movement_data[i][j]
        for j in range(0,len(self.movement_data[0]))]
        for i in range (0,len(self.movement_data))])
        if is_player_phase:
            for unit in self.units:
                if unit.alignment == Alignment.ENEMY:
                    movement_data_with_units[unit.position_y][unit.position_x] = sys.maxsize
        return movement_data_with_units
        