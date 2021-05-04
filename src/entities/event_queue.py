import pygame


class EventQueue:
    """A class that holds the event queue.
    """
    def get(self):
        """Returns the event queue.
        """
        return pygame.event.get()
