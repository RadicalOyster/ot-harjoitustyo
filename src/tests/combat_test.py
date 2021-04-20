import unittest
import os, sys, inspect
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'entities'))
from logic.combat import ReturnAttackOrder, Combat
from entities.unit import Unit

class Combat(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(1, 2, name="Testboy")
        self.unit2 = Unit(1, 2, name="Testman")
        self.unit3 = Unit(1, 5, hp=20, strength=1, speed=18, defense=6)
    
    def test_fast_unit_attacks_twice(self):
        attack_order = ReturnAttackOrder(self.unit3, self.unit)

        self.assertEqual(len(attack_order), 3)

        self.assertEqual(attack_order[0][0], self.unit3)
        self.assertEqual(attack_order[0][1], self.unit)

        self.assertEqual(attack_order[1][0], self.unit)
        self.assertEqual(attack_order[1][1], self.unit3)

        self.assertEqual(attack_order[2][0], self.unit3)
        self.assertEqual(attack_order[2][1], self.unit)
    
    def test_equally_fast_units_attack_once_each(self):
        attack_order = ReturnAttackOrder(self.unit, self.unit2)

        self.assertEqual(len(attack_order), 2)
        self.assertEqual(attack_order[0][0], self.unit)
        self.assertEqual(attack_order[0][1], self.unit2)

        self.assertEqual(attack_order[1][0], self.unit2)
        self.assertEqual(attack_order[1][1], self.unit)