import sys
from enum import Enum

movement_costs = [1, sys.maxsize]

class Level():
    def __init__(self, level_data, units):
        self.level_data = level_data
        self.movement_data = self._convert_to_movement_data(level_data)
        self.units = units
    

    def _convert_to_movement_data(self, level_data):
        movement_data = [[None for y in range(len(self.level_data[0]))] for x in range(len(self.level_data))]

        for i in range (0, len(self.level_data)):
            for j in range (0, len(self.level_data[0])):
                tile = level_data[i][j]
                movement_data[i][j] = movement_costs[tile]
        
        return movement_data
    
    def get_movement_data(self):
        return self.movement_data