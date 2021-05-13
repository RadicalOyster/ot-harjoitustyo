import unittest
import os
import sys
import inspect
from entities.unit import Unit
from logic.combat import _return_attack_order, combat
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'entities'))


class TestCombat(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(1, 2, name="Testboy")
        self.unit2 = Unit(1, 2, name="Testman")
        self.unit3 = Unit(1, 5, hp=20, strength=1, speed=18, defense=6)
        self.unit4 = Unit(1, 5, hp=20, strength=20, speed=18, defense=6)

    def test_fast_unit_attacks_twice(self):
        attack_order = _return_attack_order(self.unit3, self.unit)

        self.assertEqual(len(attack_order), 3)

        self.assertEqual(attack_order[0][0], self.unit3)
        self.assertEqual(attack_order[0][1], self.unit)

        self.assertEqual(attack_order[1][0], self.unit)
        self.assertEqual(attack_order[1][1], self.unit3)

        self.assertEqual(attack_order[2][0], self.unit3)
        self.assertEqual(attack_order[2][1], self.unit)

    def test_equally_fast_units_attack_once_each(self):
        attack_order = _return_attack_order(self.unit, self.unit2)

        self.assertEqual(len(attack_order), 2)
        self.assertEqual(attack_order[0][0], self.unit)
        self.assertEqual(attack_order[0][1], self.unit2)

        self.assertEqual(attack_order[1][0], self.unit2)
        self.assertEqual(attack_order[1][1], self.unit)
    
    def test_slow_unit_gets_attacked_twice(self):
        attack_order = _return_attack_order(self.unit, self.unit3)

        self.assertEqual(len(attack_order), 3)

        self.assertEqual(attack_order[0][0], self.unit)
        self.assertEqual(attack_order[0][1], self.unit3)

        self.assertEqual(attack_order[1][0], self.unit3)
        self.assertEqual(attack_order[1][1], self.unit)

        self.assertEqual(attack_order[2][0], self.unit3)
        self.assertEqual(attack_order[2][1], self.unit)

    def test_combat_returns_none_if_both_survive(self):
        dead_unit = combat(self.unit, self.unit2)
        self.assertEqual(dead_unit, None)

    def test_combat_returns_dead_unit(self):
        dead_unit = combat(self.unit4, self.unit2)
        self.assertEqual(dead_unit, self.unit2)
