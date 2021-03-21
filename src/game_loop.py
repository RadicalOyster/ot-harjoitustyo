import pygame
from game_clock import GameClock
from utility_functions import UnitOnTile
from cursor import CursorState
from menu_cursor import CharMenuCommands
from unit import Alignment

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

class GameLoop():
    def __init__(self, screen, sprite_renderer, cursor, menu_cursor, event_queue, units, movement_display, font, clock):
        self.screen = screen
        self.sprite_renderer = sprite_renderer
        self.cursor = cursor
        self.menu_cursor = menu_cursor
        self.event_queue = event_queue
        self.units = units
        self.movement_display = movement_display
        self.font = font
        self.clock = clock
        self.running = True
        self.disable_input = False

    def start(self):
        while self.running:
            self.clock.tick(60)
            #Check if the currently selected tile has a unit on it
            unit = UnitOnTile(self.cursor.position_x, self.cursor.position_y, self.units)
            self._handle_events(unit)
            self._render(unit)
            self._update_animations()

    def _handle_events(self, unit):
            events = self.event_queue.get()

            for event in events:
                if self.disable_input:
                    pass
                #Close game if window is closed or escape is pressed
                elif event.type == pygame.QUIT:
                        self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                
                #Cursor movement, movement is disabled while in menu
                #To do: replace hard-coded coordinates with coordinates depending on map size
                    elif event.key == pygame.K_UP:
                        if self.cursor.position_y > 0 and self.cursor.state is not CursorState.CHARMENU:
                            self.cursor.UpdatePosition(self.cursor.position_x, self.cursor.position_y - 1)
                        elif self.cursor.state == CursorState.CHARMENU:
                            self.menu_cursor.ScrollMenu(self.menu_cursor.GetCommands(), self.menu_cursor.index - 1)
                    elif event.key == pygame.K_DOWN:
                        if self.cursor.position_y < 9 and self.cursor.state is not CursorState.CHARMENU:
                            self.cursor.UpdatePosition(self.cursor.position_x, self.cursor.position_y + 1)
                        elif self.cursor.state == CursorState.CHARMENU:
                            self.menu_cursor.ScrollMenu(self.menu_cursor.GetCommands(), self.menu_cursor.index + 1)
                    elif event.key == pygame.K_LEFT:
                        if self.cursor.position_x > 0 and self.cursor.state is not CursorState.CHARMENU:
                            self.cursor.UpdatePosition(self.cursor.position_x - 1, self.cursor.position_y)
                    elif event.key == pygame.K_RIGHT:
                        if self.cursor.position_x < 9 and self.cursor.state is not CursorState.CHARMENU:
                            self.cursor.UpdatePosition(self.cursor.position_x + 1, self.cursor.position_y)

                #When Z is pressed, check if there is a unit on tile
                    elif event.key == pygame.K_z:

                #If player has selected a unit and presses Z on an empty tile in range, move unit
                #If the selected unit is the same as the unit on that tile, change cursor state to CHARMENU
                        if self.cursor.selected_unit is not None:
                            if unit is None:
                                if (self.cursor.position_x, self.cursor.position_y) in self.movement_display.GetAllowedTiles():
                                    self.cursor.selected_unit.updatePosition(self.cursor.position_x, self.cursor.position_y)
                                    self.movement_display.hide_movement = True
                                    self.movement_display.hide_attack = True
                                    self.cursor.state = CursorState.CHARMENU
                #If already in CHARMENU, button confirms menu selection
                            elif unit == self.cursor.selected_unit:
                                if self.cursor.state == CursorState.CHARMENU:
                                    if (self.menu_cursor.index == CharMenuCommands.WAIT.value):
                                        self.movement_display.ClearMovementRange()
                                        self.cursor.selected_unit.deactivate()
                                        self.cursor.selected_unit = None
                                        self.cursor.state = CursorState.MAP
                                        self.menu_cursor.ResetCursor()
                                    else:
                                        pass
                                else:
                                    self.cursor.state = CursorState.CHARMENU
                                    self.movement_display.hide_movement = True
                                    self.movement_display.hide_attack = True
                                

                #If player has not selected a unit and there is a unit on the tile, select that unit if it is an active ally and display its movement range
                        else:
                            if unit is not None and unit.alignment is Alignment.ALLY and unit.has_moved == False:
                                self.movement_display.hide_movement = False
                                self.movement_display.hide_attack = False
                                self.movement_display.UpdateMovementTiles(self.cursor.position_x, self.cursor.position_y, unit)
                                self.movement_display.UpdateAttackTiles(self.cursor.position_x, self.cursor.position_y, unit)
                                self.cursor.selected_unit = unit
                                self.cursor.selected_unit.old_position_x = self.cursor.selected_unit.position_x
                                self.cursor.selected_unit.old_position_y = self.cursor.selected_unit.position_y
                                self.cursor.state = CursorState.MOVE

                #If X is pressed, clear selected unit
                    elif event.key == pygame.K_x:
                        self.menu_cursor.ResetCursor()
                        if self.cursor.state == CursorState.MOVE:
                            self.movement_display.ClearMovementRange()
                            self.cursor.selected_unit = None
                            self.cursor.state = CursorState.MAP
                        elif self.cursor.state == CursorState.CHARMENU:
                            self.cursor.state = CursorState.MOVE
                            self.cursor.selected_unit.revertPosition()
                            self.cursor.UpdatePosition(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y)
                            self.movement_display.hide_movement = False
                            self.movement_display.hide_attack = False
                
                #For debugging only!
                #If C is pressed, reactivate all units
                    elif event.key == pygame.K_c:
                        for unit_to_activate in self.units:
                            unit_to_activate.activate()
    
    def _render(self, unit):
            self.screen.fill((24, 184, 48))
            self.sprite_renderer.update(self.cursor, self.units, self.movement_display.GetMovementRange(), self.movement_display.GetAttackRange())
            self.sprite_renderer.overlays.draw(self.screen)
            self.sprite_renderer.sprites.draw(self.screen)
            self.screen.blit(self.cursor.surf, self.cursor.rect)

            #If there is a unit on the curently selected tile or a unit is currently selected, display its info
            #To do: refactor
            if unit is not None or self.cursor.selected_unit is not None:
                unit_display = pygame.Surface((100,50))
                unit_display.fill((24, 48, 184))

                if self.cursor.selected_unit is not None:
                    unit_name = self.font.render(str(self.cursor.selected_unit.name), False, (255,255,255))
                    unit_hp = self.font.render("HP: " + str(self.cursor.selected_unit.max_hp) + "/" + str(self.cursor.selected_unit.current_hp), False, (222,222,222))
                
                else:
                    unit_name = self.font.render(str(unit.name), False, (222,222,222))
                    unit_hp = self.font.render("HP: " + str(unit.max_hp) + "/" + str(unit.current_hp), False, (222,222,222))
                unit_display.blit(unit_name, (10,4))
                unit_display.blit(unit_hp,(10,24))
                self.screen.blit(unit_display, (10,5))
            
            #If in character menu, draw menu
            #Refactor
            if self.cursor.state == CursorState.CHARMENU:
                available_commands = self.menu_cursor.GetCommands()

                #Additional menu commands for testing purposes
                #available_commands.append("Attack")
                #available_commands.append("Item")

                character_menu_height = 16 + 20 * len(available_commands)
                character_menu = pygame.Surface((70,character_menu_height))
                character_menu.fill((24, 48, 184))

                i = 0
                for command in available_commands:
                    command_to_draw = self.font.render(command, False, (222,222,222))
                    command_y_pos = 6 + i * 20
                    character_menu.blit(command_to_draw, (11, command_y_pos))
                    i += 1

                character_menu.blit(self.menu_cursor.surf, self.menu_cursor.rect)
                self.screen.blit(character_menu, (10,80))
                
            #Display cursor debug information
            #Add env variable to toggle this
            cursor_pos = self.font.render("x: " + str(self.cursor.position_x) + " y: " + str(self.cursor.position_y), False, (222,222,222))
            cursor_state = self.font.render(self.cursor.state.name, False, (222,222,222))
            self.screen.blit(cursor_pos, (560,4))
            self.screen.blit(cursor_state, (440, 4))

            pygame.display.flip()
    
    def _update_animations(self):
            for unit in self.units:
                unit.updateAnimation()
            for movetile in self.movement_display.GetMovementRange():
                movetile.updateAnimation()
            for attacktile in self.movement_display.GetAttackRange():
                attacktile.updateAnimation()    