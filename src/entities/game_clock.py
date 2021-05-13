"""
Module for the game clock.
"""
import pygame


class GameClock:
    """Class that handles the in-game clock.
    """
    def __init__(self):
        """
        Constructor for the game clock.
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """
        Progress game time.

            Args:
                fps: the desired framerate for the game.
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """
        Return the number of clock ticks.

            Returns:
                The number of ticks.
        """
        return pygame.time.get_ticks()
