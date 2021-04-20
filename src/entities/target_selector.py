from utility_functions import UnitOnTile
from .unit import Alignment

#Handles selecting target unit for actions
class TargetSelector():
    def __init__(self):
        self.tiles = []
        self.tiles_with_units = []
        self.selection = 0
    
    def UpdateTiles(self, tiles, units):
        self.tiles = tiles

        for tile in tiles:
            unit = UnitOnTile(tile[0], tile[1], units)
            if unit is not None and unit.alignment == Alignment.ENEMY:
                self.tiles_with_units.append(tile)
    
    def ClearTiles(self):
        self.tiles = []
        self.tiles_with_units = []
        self.selection = 0
    
    def ScrollSelection(self, direction):
        if self.selection == 0 and direction == -1:
            self.selection = len(self.tiles_with_units) - 1
        elif self.selection == len(self.tiles_with_units) - 1 and direction == 1:
            self.selection = 0
        else:
            self.selection += direction
    
    def SetSelection(self, selection):
        self.selection = selection
    
    def GetSelection(self):
        if len(self.tiles_with_units) > 0:
            return self.tiles_with_units[self.selection]
        return (-1,-1)