from entities.unit import Unit, Alignment
import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'entities'))


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(1, 2, Alignment.ALLY, 15, 5, 2, 3)

    def test_x_position_set_correctly(self):
        self.assertEqual(self.unit.position_x, 1)

    def test_y_position_set_correctly(self):
        self.assertEqual(self.unit.position_y, 2)

    def test_x_position_updates_correctly_(self):
        self.unit.update_position(3, 4)
        self.assertEqual(self.unit.position_x, 3)

    def test_y_position_updates_correctly_(self):
        self.unit.update_position(3, 4)
        self.assertEqual(self.unit.position_y, 4)

    def test_old_x_position_stored_correctly_on_update(self):
        self.unit.update_position(3, 4)
        self.assertEqual(self.unit.old_position_x, 1)

    def test_old_y_position_stored_correctly_on_update(self):
        self.unit.update_position(3, 4)
        self.assertEqual(self.unit.old_position_y, 2)

    def test_rect_x_set_correctly(self):
        self.assertEqual(self.unit.rect.x, 64)

    def test_rect_y_set_correctly(self):
        self.assertEqual(self.unit.rect.y, 128)

    def test_changing_offset_updates_rect_x_correctly(self):
        self.unit.update_offset(1, 1)
        self.assertEqual(self.unit.rect.x, 0)

    def test_changing_offset_updates_rect_y_correctly(self):
        self.unit.update_offset(1, 1)
        self.assertEqual(self.unit.rect.y, 64)

    def test_revert_position_reverts_x_position(self):
        self.unit.update_position(6, 6)
        self.unit.revert_position(0, 0)
        self.assertEqual(self.unit.position_x, 1)

    def test_revert_position_reverts_y_position(self):
        self.unit.update_position(6, 6)
        self.unit.revert_position(0, 0)
        self.assertEqual(self.unit.position_y, 2)

    def test_revert_position_updates_rect_x(self):
        self.unit.update_position(6, 6)
        self.unit.revert_position(0, 0)
        self.assertEqual(self.unit.rect.x, 64)

    def test_revert_position_updates_rect_y(self):
        self.unit.update_position(6, 6)
        self.unit.revert_position(0, 0)
        self.assertEqual(self.unit.rect.y, 128)

    def test_animation_frame_updates_correctly(self):
        current_frame = self.unit.active_sprite
        self.unit.update_animation()
        self.assertEqual(self.unit.active_sprite, current_frame + 0.1)

    def test_animation_frame_loops_correctly(self):
        self.unit.active_sprite = 15
        self.unit.update_animation()
        self.assertEqual(self.unit.active_sprite, 0)

    def test_damage_changes_remaining_hp(self):
        self.unit.update_hp(10)
        self.assertEqual(self.unit.current_hp, 5)

    def test_lethal_damage_sets_unit_as_dead(self):
        self.unit.update_hp(25)
        self.assertEqual(self.unit.dead, True)

    def test_negative_damage_does_not_set_remaining_hp_above_max(self):
        self.unit.update_hp(-2000)
        self.assertEqual(self.unit.current_hp, 15)

    def test_deactivating_unit_works(self):
        self.unit.deactivate()
        self.assertEqual(self.unit.has_moved, True)

    def test_activating_unit_works(self):
        self.unit.deactivate()
        self.unit.activate()
        self.assertEqual(self.unit.has_moved, False)
