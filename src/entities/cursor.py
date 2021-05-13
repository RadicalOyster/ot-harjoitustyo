"""
A module for the in-game cursor.
"""
from enum import Enum
import pygame


class CursorState(Enum):
    """An Enum to determine the cursor's state.
    """
    MAP = 0
    MOVE = 1
    CHARMENU = 2
    ATTACK = 3
    ITEM = 4
    INACTIVE = 5


class Cursor(pygame.sprite.Sprite):
    """A class that holds the in-game map cursor with which the player
    interacts with and inspects units.
    """
    def __init__(self, pos_x, pos_y, offset_x=0, offset_y=0):
        """Constructor for the cursor.

            Args:
                x: the X position of the cursor
                y: the Y position of the cursor
                offset_x: the x offset of the cursor for rendering
                offset_y: they offset of the cursor for rendering
        """
        super().__init__()
        self.surf = pygame.Surface((64, 64))
        self.surf.fill((0, 44, 255))
        self.surf.set_alpha(128)
        self.rect = self.surf.get_rect()
        self.position_x = pos_x
        self.position_y = pos_y
        self.rect.left = self.position_x * 64 - offset_x * 64
        self.rect.top = self.position_y * 64 - offset_y * 64
        self.selected_unit = None
        self.state = CursorState.MAP

    def update_position(self, pos_x, pos_y, offset_x=0, offset_y=0):
        """Moves the cursor.

            Args:
                x: the X position of the cursor
                y: the Y position of the cursor
                offset_x: The x offset of the cursor for rendering
                offset_y: The Y offset of the cursor for rendering
        """
        self.position_x = pos_x
        self.position_y = pos_y

        self.rect.left = pos_x * 64 - offset_x * 64
        self.rect.top = pos_y * 64 - offset_y * 64

    def select_unit(self, unit):
        """Marks a unit as selected.

            Args:
                unit: Unit to select
        """
        self.selected_unit = unit

    def unselect_unit(self):
        """Clears selected unit.

            Args:
                unit: Unit to unselect
        """
        self.selected_unit = None

    def update_state(self, state):
        """Updates the cursor's state.

            Args:
                state: New cursor state
        """
        self.state = state
