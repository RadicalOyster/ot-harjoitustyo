import pygame
from utility_functions import load_image
from enum import Enum

itemNames = ["Potion"]


class ItemType(Enum):
    """An Enum that maps item names to a numerical value.
    """
    POTION = 0


class Item(pygame.sprite.Sprite):
    """A class that holds items for units to use and carry.
    """  
    def __init__(self, max_uses, remaining_uses, item_type=ItemType.POTION):
        """Constructor for items.
            Args:
            max_uses: The maximum number of uses
            remaining_uses: The remaining number of uses
            item_type: The type of item (see ItemType).
        """
        super().__init__()

        self.max_uses = max_uses
        self.remaining_uses = remaining_uses
        self.type = item_type

        self.image = load_image("potion.png")

    def use_item(self, user):
        """A method to use items.
            Args:
            user: The unit using the item.
        """
        if self.type == ItemType.POTION.value:
            user.update_hp(-10)
            self.remaining_uses -= 1
            if self.remaining_uses <= 0:
                user.items.remove(self)
