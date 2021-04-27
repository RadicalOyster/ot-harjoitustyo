import unittest
from entities.unit import Unit
from utility_functions import UnitOnTile

class TestUnitOnTile(unittest.TestCase):
    def setUp(self):
        self.unit1 = Unit(2,2)
        self.unit2 = Unit(3,4)
        self.units = [self.unit1, self.unit2]
    
    def test_returns_unit_on_given_tile(self):
        unit = UnitOnTile(3, 4, self.units)
        self.assertEqual(unit, self.unit2)
    
    def test_returns_none_if_no_unit_on_tile(self):
        unit = UnitOnTile(5, 4, self.units)
        self.assertEqual(unit, None)