from entities.unit import Unit
from entities.cursor import Cursor, CursorState
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'entities'))


class TestCursor(unittest.TestCase):
    def setUp(self):
        self.cursor = Cursor(1, 2)
        self.unit = Unit(1, 2)

    def test_x_position_set_correctly(self):
        self.assertEqual(self.cursor.position_x, 1)

    def test_y_position_set_correctly(self):
        self.assertEqual(self.cursor.position_y, 2)

    def test_rect_x_set_correctly(self):
        self.assertEqual(self.cursor.rect.x, 64)

    def test_rect_y_set_correctly(self):
        self.assertEqual(self.cursor.rect.y, 128)

    def test_state_initializes_as_MAP(self):
        self.assertEqual(self.cursor.state, CursorState.MAP)

    def test_selecting_unit_works(self):
        self.cursor.select_unit(self.unit)
        self.assertEqual(self.cursor.selected_unit, self.unit)

    def test_unselecting_unit_works(self):
        self.cursor.select_unit(self.unit)
        self.assertEqual(self.cursor.selected_unit, self.unit)
        self.cursor.unselect_unit()
        self.assertEqual(self.cursor.selected_unit, None)

    def test_update_state_works(self):
        self.cursor.update_state(CursorState.MOVE)
        self.assertEqual(self.cursor.state, CursorState.MOVE)

        self.cursor.update_state(CursorState.CHARMENU)
        self.assertEqual(self.cursor.state, CursorState.CHARMENU)

        self.cursor.update_state(CursorState.ATTACK)
        self.assertEqual(self.cursor.state, CursorState.ATTACK)

        self.cursor.update_state(CursorState.ITEM)
        self.assertEqual(self.cursor.state, CursorState.ITEM)

        self.cursor.update_state(CursorState.INACTIVE)
        self.assertEqual(self.cursor.state, CursorState.INACTIVE)

    def test_update_position_x_works(self):
        self.cursor.update_position(2, 4)
        self.assertEqual(self.cursor.position_x, 2)

    def test_update_position_x_works(self):
        self.cursor.update_position(2, 4)
        self.assertEqual(self.cursor.position_y, 4)

    def test_rect_x_updates_with_offset(self):
        self.cursor.update_position(1, 1, 1, 1)
        self.assertEqual(self.cursor.rect.x, 0)

    def test_rect_y_updates_with_offset(self):
        self.cursor.update_position(1, 1, 1, 1)
        self.assertEqual(self.cursor.rect.y, 0)
