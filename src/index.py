import pygame
from cursor import Cursor, CursorState
from movement_display import MovementDisplay
from sprite_renderer import SpriteRenderer
from menu_cursor import MenuCursor, CharMenuCommands
from unit import Unit, Alignment
import os
from game_loop import GameLoop
from event_queue import EventQueue
from game_clock import GameClock
from pathfinding import PathFinding
from target_selector import TargetSelector
from camera import Camera

#Initializing the game

def main():
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Faux Emblem")

    camera = Camera(0,0)

    units = []
    units.append(Unit(1,1,name="Ferdinand", strength=8, speed=6, defense=5, offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(3,3,Alignment.ENEMY, offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(2,2,Alignment.ENEMY, offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(12,4,Alignment.ENEMY, offset_X=camera.offset_X, offset_Y=camera.offset_Y))
    units.append(Unit(9,7,Alignment.ENEMY, offset_X=camera.offset_X, offset_Y=camera.offset_Y))

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)

    clock = GameClock()

    level = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    pathfinding = PathFinding(1, 1, level)
    target_selector = TargetSelector()

    game_loop = GameLoop(screen, SpriteRenderer(), Cursor(0, 0, camera.offset_X, camera.offset_Y), MenuCursor(),
    EventQueue(), units, MovementDisplay(pathfinding), font, clock, target_selector, camera, level)

    pygame.init()
    game_loop.start()

    pygame.quit()

if __name__ == "__main__":
    main()