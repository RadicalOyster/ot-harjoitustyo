import pygame
from utility_functions import load_image
from enum import Enum

itemNames = ["Potion"]


class ItemType(Enum):
    POTION = 0


class Item(pygame.sprite.Sprite):
    def __init__(self, max_uses, remaining_uses, item_type=ItemType.POTION):
        super().__init__()

        self.max_uses = max_uses
        self.remaining_uses = remaining_uses
        self.type = item_type

        self.image = load_image("potion.png")

    def use_item(self, user):
        if self.type == ItemType.POTION.value:
            user.update_hp(-10)
            self.remaining_uses -= 1
            if (self.remaining_uses <= 0):
                user.items.remove(self)
