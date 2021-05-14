import unittest
from entities.camera import Camera
from entities.level import Level
from entities.unit import Unit, Alignment
from logic.pathfinding import PathFinding
from logic.ai import Ai

LEVEL_DATA = [
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 0]
]

class TestAi(unittest.TestCase):
    def setUp(self):
        self.units = []
        unit = Unit(pos_x=0, pos_y=2, alignment=Alignment.ENEMY)
        unit2 = Unit(pos_x=2, pos_y=3)

        self.units.append(unit)
        self.units.append(unit2)

        self.level = Level(LEVEL_DATA, self.units)
        self.pathfinding = PathFinding(1, 1, self.level.movement_data)

        self.ai = Ai(self.units, self.pathfinding, self.level)
    
    def test_ai_initialized_correclty(self):
        self.assertEqual(self.ai.units, self.units)
        self.assertEqual(self.ai.pathfinding, self.pathfinding)
        self.assertEqual(self.ai.level, self.level)
    
    def test_when_no_player_unit_in_range_moves_to_random_valid_tile(self):
        unit = self.units[0]
        self.ai.handle_enemy_turn(unit)
        unit_position = (unit.position_x, unit.position_y)
        unit_on_allowed_tiles = unit_position in [(0,2), (1,2), (1,1), (2,1)]
        assert unit_on_allowed_tiles is True
    
    def test_when_player_unit_in_range_attacks_that_unit(self):
        unit = self.units[0]
        unit.update_position(3, 3)
        self.ai.handle_enemy_turn(unit, offset_x=0, offset_y=0)
        self.assertEqual(unit.current_hp, 8)
        self.assertEqual(self.units[1].current_hp, 8)