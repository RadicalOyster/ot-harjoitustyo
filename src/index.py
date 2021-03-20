import pygame
from cursor import Cursor, CursorState
from movementdisplay import MoveTile, MovementDisplay
from utility_functions import UnitOnTile
from movementdisplay import MovementDisplay
from sprite_renderer import SpriteRenderer
from menu_cursor import MenuCursor, CharMenuCommands
from unit import Unit, Alignment
import os

class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
            self._clock.tick(fps)
        
    def get_ticks(self):
        return pygame.time.get_ticks()

pygame.init()

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
menu_cursor = MenuCursor()
sprite_renderer = SpriteRenderer()
movementdisplay = MovementDisplay()

units = []
units.append(Unit(1,1,name="Ferdinand"))
units.append(Unit(5,3,Alignment.ENEMY))

clock = Clock()

testFont = pygame.font.SysFont("Arial", 20)
#testText = testFont.render("TEST",0,(255,255,255))
pygame.font.init()

while running:
    clock.tick(60)

    #Check if the currently selected tile has a unit on it
    unit = UnitOnTile(cursor.position_x, cursor.position_y, units)

    #Handle events
    #Todo: separate into its own file
    events = pygame.event.get()
    for event in events:

        #Close game if window is closed or escape is pressed
        if event.type == pygame.QUIT:
                running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        #Cursor movement, movement is disabled while in menu
        #To do: replace hard-coded coordinates with coordinates depending on map size
            elif event.key == pygame.K_UP:
                if cursor.position_y > 0 and cursor.state is not CursorState.CHARMENU:
                    cursor.UpdatePosition(cursor.position_x, cursor.position_y - 1)
            elif event.key == pygame.K_DOWN:
                if cursor.position_y < 9 and cursor.state is not CursorState.CHARMENU:
                    cursor.UpdatePosition(cursor.position_x, cursor.position_y + 1)
            elif event.key == pygame.K_LEFT:
                if cursor.position_x > 0 and cursor.state is not CursorState.CHARMENU:
                    cursor.UpdatePosition(cursor.position_x - 1, cursor.position_y)
            elif event.key == pygame.K_RIGHT:
                if cursor.position_x < 9 and cursor.state is not CursorState.CHARMENU:
                    cursor.UpdatePosition(cursor.position_x + 1, cursor.position_y)

        #When Z is pressed, check if there is a unit on tile
            elif event.key == pygame.K_z:

        #If player has selected a unit and presses Z on an empty tile in range, move unit
                if cursor.selected_unit is not None:
                    if unit is None:
                        if (cursor.position_x, cursor.position_y) in movementdisplay.GetAllowedTiles():
                            cursor.selected_unit.updatePosition(cursor.position_x, cursor.position_y)
                            #movementdisplay.ClearMovementRange()
                            movementdisplay.hide_movement = True
                            movementdisplay.hide_attack = True
                            cursor.state = CursorState.CHARMENU
        #If the selected unit is the same as the unit on that tile, change cursor state to CHARMENU
        #If already in CHARMENU, button confirms menu selection
                    elif unit == cursor.selected_unit:
                        if cursor.state == CursorState.CHARMENU:
                            if (menu_cursor.index == CharMenuCommands.WAIT.value):
                                movementdisplay.ClearMovementRange()
                                cursor.selected_unit.deactivate()
                                cursor.selected_unit = None
                                cursor.state = CursorState.MAP
                            else:
                                pass
                        else:
                            cursor.state = CursorState.CHARMENU
                            movementdisplay.hide_movement = True
                            movementdisplay.hide_attack = True
                        

        #If player has not selected a unit and there is a unit on the tile, select that unit if it is an active ally and display its movement range
                else:
                    if unit is not None and unit.alignment is Alignment.ALLY and unit.has_moved == False:
                        movementdisplay.hide_movement = False
                        movementdisplay.hide_attack = False
                        movementdisplay.UpdateMovementTiles(cursor.position_x, cursor.position_y, unit)
                        movementdisplay.UpdateAttackTiles(cursor.position_x, cursor.position_y, unit)
                        cursor.selected_unit = unit
                        cursor.selected_unit.old_position_x = cursor.selected_unit.position_x
                        cursor.selected_unit.old_position_y = cursor.selected_unit.position_y
                        cursor.state = CursorState.MOVE

        #If X is pressed, clear selected unit
            elif event.key == pygame.K_x:
                if cursor.state == CursorState.MOVE:
                    movementdisplay.ClearMovementRange()
                    cursor.selected_unit = None
                    cursor.state = CursorState.MAP
                elif cursor.state == CursorState.CHARMENU:
                    cursor.state = CursorState.MOVE
                    cursor.selected_unit.updatePosition(cursor.selected_unit.old_position_x, cursor.selected_unit.old_position_y)
                    cursor.UpdatePosition(cursor.selected_unit.position_x, cursor.selected_unit.position_y)
                    movementdisplay.hide_movement = False
                    movementdisplay.hide_attack = False
        
        #For debugging only!
        #If C is pressed, reactivate all units
            elif event.key == pygame.K_c:
                for unit in units:
                    unit.activate()
    
    screen.fill((24, 184, 48))
    sprite_renderer.update(cursor, units, movementdisplay.GetMovementRange(), movementdisplay.GetAttackRange())
    sprite_renderer.overlays.draw(screen)
    sprite_renderer.sprites.draw(screen)
    screen.blit(cursor.surf, cursor.rect)

    #If there is a unit on the curently selected tile or a unit is currently selected, display its info
    #To do: refactor
    if unit is not None or cursor.selected_unit is not None:
        unit_display = pygame.Surface((100,50))
        unit_display.fill((24, 48, 184))

        if cursor.selected_unit is not None:
            unit_name = testFont.render(str(cursor.selected_unit.name), False, (255,255,255))
            unit_hp = testFont.render("HP: " + str(cursor.selected_unit.max_hp) + "/" + str(cursor.selected_unit.current_hp), False, (222,222,222))
        
        else:
            unit_name = testFont.render(str(unit.name), False, (222,222,222))
            unit_hp = testFont.render("HP: " + str(unit.max_hp) + "/" + str(unit.current_hp), False, (222,222,222))
        unit_display.blit(unit_name, (10,4))
        unit_display.blit(unit_hp,(10,24))
        screen.blit(unit_display, (10,5))
    
    #If in character menu, draw menu
    #Refactor
    if cursor.state == CursorState.CHARMENU:
        available_commands = menu_cursor.GetCommands()

        #Additional menu commands for testing purposes
        #available_commands.append("Attack")
        #available_commands.append("Item")

        character_menu_height = 16 + 20 * len(available_commands)
        character_menu = pygame.Surface((70,character_menu_height))
        character_menu.fill((24, 48, 184))

        i = 0
        for command in available_commands:
            command_to_draw = testFont.render(command, False, (222,222,222))
            command_y_pos = 6 + i * 20
            character_menu.blit(command_to_draw, (11, command_y_pos))
            i += 1

        character_menu.blit(menu_cursor.surf, menu_cursor.rect)
        screen.blit(character_menu, (10,80))
        


    

    #Display cursor debug information
    #Add env variable to toggle this
    cursor_pos = testFont.render("x: " + str(cursor.position_x) + " y: " + str(cursor.position_y), False, (222,222,222))
    cursor_state = testFont.render(cursor.state.name, False, (222,222,222))
    screen.blit(cursor_pos, (560,4))
    screen.blit(cursor_state, (440, 4))

    pygame.display.flip()

    for unit in units:
        unit.updateAnimation()
    for tile in movementdisplay.GetMovementRange():
        tile.updateAnimation()
    for tile in movementdisplay.GetAttackRange():
        tile.updateAnimation()

pygame.quit()