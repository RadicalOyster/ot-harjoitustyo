import unittest
import os, sys, inspect
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'entities'))
from entities.unit import Unit, Alignment

class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(1, 2, Alignment.ALLY, 15, 5, 2, 3)
    
    def test_x_position_set_correctly(self):
        self.assertEqual(self.unit.position_x, 1)

    def test_y_position_set_correctly(self):
        self.assertEqual(self.unit.position_y, 2)