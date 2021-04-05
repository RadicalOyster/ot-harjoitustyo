import pygame
from game_clock import GameClock
from utility_functions import UnitOnTile
from cursor import CursorState
from menu_cursor import CharMenuCommands
from unit import Alignment
from path_indicator import PathIndicator
from combat import Combat

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
    def __init__(self, screen, sprite_renderer, cursor, menu_cursor, event_queue, units, movement_display, font, clock, target_selector, camera, level):
        self.screen = screen
        self.sprite_renderer = sprite_renderer
        self.cursor = cursor
        self.menu_cursor = menu_cursor
        self.event_queue = event_queue
        self.units = units
        self.indicators = pygame.sprite.Group()
        self.movement_display = movement_display
        self.font = font
        self.clock = clock
        self.target_selector = target_selector
        self.camera = camera
        self.level = level
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

                #Handle arrow keys
                    elif event.key == pygame.K_UP:
                        self._move_selection(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self._move_selection(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self._move_selection(-1, 0)    
                    elif event.key == pygame.K_RIGHT:
                        self._move_selection(1, 0)

                #Handle Z key press
                    elif event.key == pygame.K_z:
                        self._handle_confirm(unit)

                #If X is pressed, clear selected unit
                    elif event.key == pygame.K_x:
                        self._handle_cancel()
                
                #For debugging only!
                #If C is pressed, reactivate all units
                    elif event.key == pygame.K_c:
                        for unit_to_activate in self.units:
                            unit_to_activate.activate()

    def _select_unit(self, unit):
        self.movement_display.hide_movement = False
        self.movement_display.hide_attack = False
        self.movement_display.UpdateMovementTiles(self.cursor.position_x, self.cursor.position_y, unit, self.camera.offset_X, self.camera.offset_Y)
        self.movement_display.UpdateAttackTiles(self.cursor.position_x, self.cursor.position_y, unit, self.camera.offset_X, self.camera.offset_Y)
        self.cursor.selected_unit = unit
        self.cursor.selected_unit.old_position_x = self.cursor.selected_unit.position_x
        self.cursor.selected_unit.old_position_y = self.cursor.selected_unit.position_y
        self.cursor.state = CursorState.MOVE
        self.sprite_renderer.showIndicators()
    
    def _get_path(self):
        self.indicators.empty()

        indicator_coordinates = self.movement_display.pathfinding.ReturnPath((self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y), (self.cursor.position_x, self.cursor.position_y))
        for indicator in indicator_coordinates[:-1]:
            if indicator in self.movement_display.allowed_tiles:
                self.indicators.add(PathIndicator(indicator[0], indicator[1], self.camera.offset_X, self.camera.offset_Y))
    
    def _valid_tile(self, x, y):
        if x < 0 or y < 0 or y > (len(self.level) - 1) or x > (len(self.level[0]) - 1):
            return False
        return True
    
    def _deactivate_selected_unit(self):
        self.movement_display.ClearMovementRange()
        self.movement_display.ClearCurrentAttackRanges()
        self.cursor.selected_unit.deactivate()
        self.cursor.UpdatePosition(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
        self.cursor.selected_unit = None
        self.cursor.state = CursorState.MAP
        self.menu_cursor.ResetCursor()
        self.target_selector.ClearTiles()
    
    def _update_offsets(self):
        for unit in self.units:
            unit.updateOffset(self.camera.offset_X, self.camera.offset_Y)
        for tile in self.movement_display.movement_display:
            tile.updateOffset(self.camera.offset_X, self.camera.offset_Y)
        for tile in self.movement_display.attack_display:
            tile.updateOffset(self.camera.offset_X, self.camera.offset_Y)
        for indicator in self.indicators:
            indicator.updateOffset(self.camera.offset_X, self.camera.offset_Y)


    #Moves the camera and cursor
    def _move_selection(self, dx, dy):
        if self.cursor.state != CursorState.ATTACK:
            if dx == 1 and self.cursor.position_x <= len(self.level[0]) - 1 and self.cursor.position_x - self.camera.offset_X >= 7:
                self.camera.offset_X += 1

            if dx == -1 and self.cursor.position_x -self.camera.offset_X > 0 and self.cursor.position_x - self.camera.offset_X < 3 and self.camera.offset_X > 0:
                self.camera.offset_X -= 1

            if dy == 1 and self.cursor.position_y <= len(self.level) - 1 and self.cursor.position_y - self.camera.offset_Y >= 7:
                self.camera.offset_Y += 1
            
            if dy == -1 and self.cursor.position_y > 0 and self.cursor.position_y - self.camera.offset_Y < 3 and self.camera.offset_Y > 0:
                self.camera.offset_Y -= 1

            if self.cursor.state != CursorState.CHARMENU and self.cursor.state != CursorState.ATTACK:
                self._update_offsets()

        if self.cursor.state == CursorState.MAP:
            if self._valid_tile(self.cursor.position_x + dx, self.cursor.position_y + dy):
                self.cursor.UpdatePosition(self.cursor.position_x + dx, self.cursor.position_y + dy, self.camera.offset_X, self.camera.offset_Y)
        elif self.cursor.state == CursorState.MOVE:
            if self._valid_tile(self.cursor.position_x + dx, self.cursor.position_y + dy):
                self.cursor.UpdatePosition(self.cursor.position_x + dx, self.cursor.position_y + dy, self.camera.offset_X, self.camera.offset_Y)
            if self.cursor.selected_unit is not None and (self.cursor.position_x, self.cursor.position_y) in self.movement_display.allowed_tiles:
                self._get_path()
        elif self.cursor.state == CursorState.CHARMENU:
            self.menu_cursor.ScrollMenu(self.menu_cursor.GetCommands(), self.menu_cursor.index + dy)
        elif self.cursor.state == CursorState.ATTACK:
            unit = self.target_selector.ScrollSelection(dx + dy)
            self.cursor.UpdatePosition(self.target_selector.GetSelection()[0], self.target_selector.GetSelection()[1], self.camera.offset_X, self.camera.offset_Y)
            

    def _handle_confirm(self, unit):
        #If player has selected a unit and presses Z on an empty tile in range, move unit
        #If the selected unit is the same as the unit on that tile, change cursor state to CHARMENU
        if self.cursor.selected_unit is not None:

            if unit is None:
                if (self.cursor.position_x, self.cursor.position_y) in self.movement_display.GetAllowedTiles():
                    self.cursor.selected_unit.updatePosition(self.cursor.position_x, self.cursor.position_y, self.camera.offset_X, self.camera.offset_Y)
                    self.movement_display.hide_movement = True
                    self.movement_display.hide_attack = True
                    self.indicators.empty()
                    self.cursor.state = CursorState.CHARMENU

            #If already in CHARMENU, button confirms menu selection
            elif unit == self.cursor.selected_unit:
                if self.cursor.state == CursorState.CHARMENU:

                    if self.menu_cursor.index == CharMenuCommands.WAIT.value:
                        self._deactivate_selected_unit()

                    elif self.menu_cursor.index == CharMenuCommands.ATTACK.value:
                        self.cursor.state = CursorState.ATTACK
                        ranges = self.movement_display.GetCurrentAttackRanges(self.cursor.position_x, self.cursor.position_y, self.cursor.selected_unit.range, self.camera.offset_X, self.camera.offset_Y)
                        self.target_selector.UpdateTiles(ranges, self.units)
                        self.cursor.UpdatePosition(self.target_selector.GetSelection()[0], self.target_selector.GetSelection()[1], self.camera.offset_X, self.camera.offset_Y)
                        self.sprite_renderer.show_indicators = False

                else:
                    self.cursor.state = CursorState.CHARMENU
                    self.movement_display.hide_movement = True
                    self.movement_display.hide_attack = True

            elif self.cursor.state == CursorState.ATTACK:
                dead_unit = Combat(self.cursor.selected_unit, unit)
                if dead_unit is not None:
                    self.units.remove(dead_unit)
                self._deactivate_selected_unit()

            #If player has not selected a unit and there is a unit on the tile, select that unit if it is an active ally and display its movement range
        else:
            if unit is not None and unit.alignment is Alignment.ALLY and unit.has_moved == False:
                self._select_unit(unit)
    
    def _handle_cancel(self):
        self.menu_cursor.ResetCursor()
        self.indicators.empty()
        if self.cursor.state == CursorState.MOVE:
            self.movement_display.ClearMovementRange()
            self.cursor.selected_unit = None
            self.cursor.state = CursorState.MAP
            self.sprite_renderer.hideIndicators()
        elif self.cursor.state == CursorState.CHARMENU:
            self.cursor.state = CursorState.MOVE
            self.cursor.selected_unit.revertPosition(self.camera.offset_X, self.camera.offset_Y)
            self.cursor.UpdatePosition(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
            self.movement_display.hide_movement = False
            self.movement_display.hide_attack = False
        elif self.cursor.state == CursorState.ATTACK:
            self.cursor.state = CursorState.CHARMENU
            self.movement_display.ClearCurrentAttackRanges()
            self.cursor.UpdatePosition(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
            self.target_selector.ClearTiles()
    


    def _render(self, unit):
            self.screen.fill((24, 184, 48))
            self.sprite_renderer.update(self.cursor, self.units, self.indicators, self.movement_display.GetMovementRange(), self.movement_display.GetAttackRange(), self.movement_display.current_ranges)
            self.sprite_renderer.overlays.draw(self.screen)
            if self.sprite_renderer.show_indicators:
                self.sprite_renderer.indicators.draw(self.screen)
            self.sprite_renderer.sprites.draw(self.screen)
            self.screen.blit(self.cursor.surf, self.cursor.rect)

            #If there is a unit on the curently selected tile or a unit is currently selected, display its info
            #To do: refactor
            if unit is not None or self.cursor.selected_unit is not None:
                unit_display = pygame.Surface((100,50))
                unit_display.fill((24, 48, 184))

                if self.cursor.selected_unit is not None:
                    unit_name = self.font.render(str(self.cursor.selected_unit.name), False, (255,255,255))
                    unit_hp = self.font.render("HP: " + str(self.cursor.selected_unit.current_hp) + "/" + str(self.cursor.selected_unit.max_hp), False, (222,222,222))
                
                else:
                    unit_name = self.font.render(str(unit.name), False, (222,222,222))
                    unit_hp = self.font.render("HP: " + str(unit.current_hp) + "/" + str(unit.max_hp), False, (222,222,222))
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

            camera_offset = self.font.render("Offset: (" + str(self.camera.offset_X) + ":" + str(self.camera.offset_Y) + ")", False, (222,222,222))

            self.screen.blit(cursor_pos, (560,4))
            self.screen.blit(cursor_state, (440, 4))
            self.screen.blit(camera_offset, (440, 24))

            pygame.display.flip()
    
    def _update_animations(self):
            for unit in self.units:
                unit.updateAnimation()
            for movetile in self.movement_display.GetMovementRange():
                movetile.updateAnimation()
            for attacktile in self.movement_display.GetAttackRange():
                attacktile.updateAnimation()
            for attacktile in self.movement_display.current_ranges:
                attacktile.updateAnimation()