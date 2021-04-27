import unittest
from entities.unit import Unit
from entities.item import Item, ItemType


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item = Item(3, 2, ItemType.POTION.value)
        self.unit = Unit(1, 2)
        self.unit.items.append(self.item)

    def test_max_uses_set_correctly(self):
        self.assertEqual(self.item.max_uses, 3)

    def test_remaining_uses_set_correctly(self):
        self.assertEqual(self.item.remaining_uses, 2)

    def test_item_type_set_correctly(self):
        self.assertEqual(self.item.type, ItemType.POTION.value)

    def test_use_item_deducts_remaining_uses(self):
        self.item.use_item(self.unit)
        self.assertEqual(self.item.remaining_uses, 1)

    def test_consuming_item_removes_it_from_unit_inventory(self):
        self.assertEqual(len(self.unit.items), 1)
        self.item.use_item(self.unit)
        self.item.use_item(self.unit)
        self.assertEqual(len(self.unit.items), 0)

    def test_consuming_potion_heals_user(self):
        self.unit.current_hp = 5
        self.item.use_item(self.unit)
        self.assertEqual(self.unit.current_hp, 15)

    def test_other_item_type_does_not_trigger_potion(self):
        item = Item(3, 3, 2)
        self.unit.current_hp = 2
        item.use_item(self.unit)
        self.assertEqual(self.unit.current_hp, 2)
