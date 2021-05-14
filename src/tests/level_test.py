import unittest, sys
from entities.level import Level
from entities.unit import Unit, Alignment

LEVEL_DATA = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]

correct_data = [
    [1, sys.maxsize, 1],
    [1, sys.maxsize, sys.maxsize],
    [1, sys.maxsize, 1]
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
    
    def test_units_assigned_correct_positions(self):

        unit = Unit(pos_x=1, pos_y=2, alignment=Alignment.ENEMY)
        unit2 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ENEMY)

        level = Level(LEVEL_DATA, [unit, unit2])

        self.assertEqual(level.unit_positions[2][1], unit)
        self.assertEqual(level.unit_positions[1][2], unit2)

    def test_on_player_phase_movement_data_affected_by_enemy_units(self):
        correct_data = [
            [1, sys.maxsize, 1],
            [1, sys.maxsize, sys.maxsize],
            [1, sys.maxsize, 1]
        ]

        unit = Unit(pos_x=1, pos_y=2, alignment=Alignment.ENEMY)
        unit2 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ENEMY)

        level = Level(LEVEL_DATA, [unit, unit2])

        self.assertEqual(level.get_movement_data_with_units(True), correct_data)

    def test_on_player_phase_movement_data_not_affected_by_allied_units(self):
        correct_data = [
            [1, sys.maxsize, 1],
            [1, sys.maxsize, sys.maxsize],
            [1, sys.maxsize, 1]
        ]

        unit = Unit(pos_x=1, pos_y=2, alignment=Alignment.ENEMY)
        unit2 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ENEMY)
        unit3 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ALLY)

        level = Level(LEVEL_DATA, [unit, unit2, unit3])

        self.assertEqual(level.get_movement_data_with_units(True), correct_data)

    def test_on_enemy_phase_movement_data_affected_by_allied_units(self):
        correct_data = [
            [1, sys.maxsize, 1],
            [1, sys.maxsize, sys.maxsize],
            [1, sys.maxsize, 1]
        ]

        unit = Unit(pos_x=1, pos_y=2, alignment=Alignment.ALLY)
        unit2 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ALLY)

        level = Level(LEVEL_DATA, [unit, unit2])

        self.assertEqual(level.get_movement_data_with_units(False), correct_data)

    def test_on_enemy_phase_movement_data_not_affected_by_enemy_units(self):
        correct_data = [
            [1, sys.maxsize, 1],
            [1, sys.maxsize, sys.maxsize],
            [1, sys.maxsize, 1]
        ]

        unit = Unit(pos_x=1, pos_y=2, alignment=Alignment.ALLY)
        unit2 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ALLY)
        unit3 = Unit(pos_x=2, pos_y=1, alignment=Alignment.ENEMY)

        level = Level(LEVEL_DATA, [unit, unit2, unit3])

        self.assertEqual(level.get_movement_data_with_units(False), correct_data)

    def test_updating_unit_position_functions_correctly(self):
        unit = Unit(pos_x=0, pos_y=0)

        correct_positions = [
            [None, None, None],
            [None, None, None],
            [None, None, unit]
        ]

        level = Level(LEVEL_DATA, [unit])
        level.update_unit_position(unit, 2, 2)

        self.assertEqual(level.unit_positions, correct_positions)