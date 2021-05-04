import unittest, sys
from entities.level import Level

LEVEL_DATA = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_DATA, [])
    
    def test_level_data_converts_to_movement_map_correctly(self):
        correct_data = [
        [1, sys.maxsize, 1],
        [1, sys.maxsize, 1],
        [1, 1, 1]]

        self.assertEqual(self.level.movement_data, correct_data)