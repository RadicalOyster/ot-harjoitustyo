import pygame


class GameClock:
    """Class that handles the in-game clock.
    """
    def __init__(self):
        self._clock = pygame.time.Clock()
    
    """Progress game time.

        Args:
            fps: the desired framerate for the game.
    """  
    def tick(self, fps):
        self._clock.tick(fps)

    """Return the number of clock ticks.
    """  
    def get_ticks(self):
        return pygame.time.get_ticks()
