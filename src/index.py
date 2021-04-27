import os
import sys
import inspect
import pygame

from entities.item import Item
from entities.camera import Camera
from entities.target_selector import TargetSelector
from entities.game_clock import GameClock
from entities.unit import Unit, Alignment
from entities.event_queue import EventQueue
from entities.cursor import Cursor
from entities.menu_cursor import MenuCursor
from entities.level import Level

from logic.pathfinding import PathFinding

from game_loop import GameLoop

from ui.sprite_renderer import SpriteRenderer
from ui.movement_display import MovementDisplay
from ui.tile_map import TileMap

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


# Initializing the game


def main():
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Faux Emblem")

    camera = Camera(0, 0)

    units = []
    units.append(Unit(1, 4, name="Ferdinand", strength=8, speed=6,
                 defense=5, offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units[0].items.append(Item(3, 3, 0))
    units[0].items.append(Item(3, 3, 0))
    units[0].items.append(Item(3, 3, 0))
    units.append(Unit(3, 6, Alignment.ENEMY,
                 offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(6, 6, Alignment.ENEMY,
                 offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(12, 4, Alignment.ENEMY,
                 offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(9, 7, Alignment.ENEMY,
                 offset_X=camera.offset_X, offset_Y=camera.offset_Y))

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)
    font2 = pygame.font.SysFont("Arial", 14)

    clock = GameClock()

    level = [
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    ]

    test_map = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    test_level = Level(level, units)
    tile_map = TileMap(level)


    pathfinding = PathFinding(1, 1, test_level.get_movement_data())
    target_selector = TargetSelector()

    game_loop = GameLoop(screen, SpriteRenderer(), Cursor(1, 1, camera.offset_X, camera.offset_Y), MenuCursor(),
                         EventQueue(), units, MovementDisplay(pathfinding), font, font2, clock, target_selector, camera, level,
                         tile_map)

    pygame.init()
    game_loop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
