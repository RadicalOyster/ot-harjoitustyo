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

from logic.ai import Ai
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
    screen_width = 640
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Faux Emblem")

    camera = Camera(0, 0)

    units = []
    units.append(Unit(1, 4, name="Ferdinand", strength=8, speed=6,
                 defense=5, offset_x=camera.offset_x, offset_y=camera.offset_y))
    units[0].items.append(Item(3, 3, 0))
    units[0].items.append(Item(3, 3, 0))
    units[0].items.append(Item(3, 3, 0))
    units.append(Unit(1, 5, name="Sylvain", strength=12, speed=2, defense=8, offset_x=camera.offset_x, offset_y=camera.offset_y))
    units.append(Unit(3, 6, Alignment.ENEMY,
                 offset_x=camera.offset_x, offset_y=camera.offset_y))
    units.append(Unit(6, 6, Alignment.ENEMY,
                 offset_x=camera.offset_x, offset_y=camera.offset_y))
    units.append(Unit(12, 4, Alignment.ENEMY,
                 offset_x=camera.offset_x, offset_y=camera.offset_y))
    units.append(Unit(9, 7, Alignment.ENEMY,
                 offset_x=camera.offset_x, offset_y=camera.offset_y))
    units.append(Unit(2, 5, Alignment.ENEMY,
                 offset_x=camera.offset_x, offset_y=camera.offset_y))

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

    test_level = Level(level, units)
    tile_map = TileMap(level)

    test_level.get_movement_data_with_units(True)


    pathfinding = PathFinding(1, 1, test_level.movement_data)
    target_selector = TargetSelector()

    enemy_ai = Ai(units, pathfinding, test_level)

    game_loop = GameLoop(screen, SpriteRenderer(), Cursor(1, 4, camera.offset_x,
                        camera.offset_y), MenuCursor(),
                         EventQueue(), units, MovementDisplay(pathfinding),
                         font, font2, clock, target_selector, camera, test_level,
                         tile_map, enemy_ai)

    pygame.init()
    game_loop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
