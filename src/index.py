import pygame
from cursor import Cursor
from movementdisplay import MoveTile, MovementDisplay
from utility_functions import UnitOnTile
from movementdisplay import MovementDisplay
from sprite_renderer import SpriteRenderer
from unit import Unit, Alignment
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
    K_c,
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
units.append(Unit(5,3,Alignment.ENEMY))

clock = Clock()

pygame.init()

while running:
    clock.tick(60)
    events = pygame.event.get()
    for event in events:

        #Close game if window is closed or escape is pressed
        if event.type == pygame.QUIT:
                running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        #Cursor movement
        #Todo: replace hard-coded coordinates with coordinates depending on map size
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

        #When Z is pressed, check if there is a unit on tile
            elif event.key == pygame.K_z:
                unit = UnitOnTile(cursor.position_x, cursor.position_y, units)

        #If player has selected a unit and presses Z on an empty tile in range, move unit to that tile and deactivate and unselect unit
                if cursor.selectedUnit is not None and unit is None:
                    if (cursor.position_x, cursor.position_y) in movementdisplay.GetAllowedTiles():
                        cursor.selectedUnit.updatePosition(cursor.position_x, cursor.position_y)
                        movementdisplay.ClearMovementRange()
                        cursor.selectedUnit.deactivate()
                        cursor.selectedUnit = None

        #If player has not selected a unit and there is a unit on the tile, select that unit if it is an active ally and display its movement range
                else:
                    if unit is not None and unit.alignment is Alignment.ALLY and unit.has_moved == False:
                        movementdisplay.UpdateMovementTiles(cursor.position_x, cursor.position_y)
                        cursor.selectedUnit = unit

        #If X is pressed, clear selected unit
            elif event.key == pygame.K_x:
                movementdisplay.ClearMovementRange()
                cursor.selectedUnit = None
        
        #For debugging only!
        #If C is pressed, reactivate all units
            elif event.key == pygame.K_c:
                for unit in units:
                    unit.activate()
        
    screen.fill((24, 184, 48))
    sprite_renderer.update(cursor, movementdisplay.GetMovementRange(), units)
    sprite_renderer.all_sprites.draw(screen)
    screen.blit(cursor.surf, cursor.rect)
    pygame.display.flip()

    for unit in units:
        unit.updateAnimation()

pygame.quit()