import pygame
from cursor import Cursor
from movementdisplay import MoveTile, MovementDisplay
from utility_functions import UnitOnTile
from movementdisplay import MovementDisplay
from sprite_renderer import SpriteRenderer
from unit import Unit
import os

class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
            self._clock.tick(fps)
        
    def get_ticks(self):
        return pygame.time.get_ticks()

dirname = os.path.dirname(__file__)

running = True

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_z,
    K_x,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((24, 184, 48))

cursor = Cursor()
sprite_renderer = SpriteRenderer()
movementdisplay = MovementDisplay()

units = []
units.append(Unit(1,1))

clock = Clock()

pygame.init()

while running:
    clock.tick(60)
    #print("HEEHO")
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
                running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP:
                if cursor.position_y > 0:
                    cursor.UpdatePosition(cursor.position_x, cursor.position_y - 1)
            elif event.key == pygame.K_DOWN:
                if cursor.position_y < 9:
                    cursor.UpdatePosition(cursor.position_x, cursor.position_y + 1)
            elif event.key == pygame.K_LEFT:
                if cursor.position_x > 0:
                    cursor.UpdatePosition(cursor.position_x - 1, cursor.position_y)
            elif event.key == pygame.K_RIGHT:
                if cursor.position_x < 9:
                    cursor.UpdatePosition(cursor.position_x + 1, cursor.position_y)
            elif event.key == pygame.K_z:
                unit = UnitOnTile(cursor.position_x, cursor.position_y, units)
                if cursor.selectedUnit is not None and unit is None:
                    if (cursor.position_x, cursor.position_y) in movementdisplay.GetAllowedTiles():
                        cursor.selectedUnit.updatePosition(cursor.position_x, cursor.position_y)
                        movementdisplay.ClearMovementRange()
                        cursor.selectedUnit = None
                    else:
                        pass
                else:
                    if unit is not None:
                        movementdisplay.UpdateMovementTiles(cursor.position_x, cursor.position_y)
                        cursor.selectedUnit = unit
                    else:
                        pass
            elif event.key == pygame.K_x:
                movementdisplay.ClearMovementRange()
                cursor.selectedUnit = None
        
    screen.fill((24, 184, 48))
    sprite_renderer.update(cursor, movementdisplay.GetMovementRange(), units)
    sprite_renderer.all_sprites.draw(screen)
    screen.blit(cursor.surf, cursor.rect)
    pygame.display.flip()

    for unit in units:
        unit.updateAnimation()

pygame.quit()