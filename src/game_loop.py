import pygame
from entities.game_clock import GameClock
from utility_functions import UnitOnTile
from entities.cursor import CursorState
from entities.menu_cursor import CharMenuCommands
from entities.unit import Alignment
from ui.path_indicator import PathIndicator
from logic.combat import Combat
from entities.item import itemNames

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
    def __init__(self, screen, sprite_renderer, cursor, menu_cursor, event_queue, units, movement_display, font, font2, clock, target_selector, camera, level):
        self.screen = screen
        self.sprite_renderer = sprite_renderer
        self.cursor = cursor
        self.menu_cursor = menu_cursor
        self.event_queue = event_queue
        self.units = units
        self.indicators = pygame.sprite.Group()
        self.movement_display = movement_display
        self.font = font
        self.font2 = font2
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
        self.cursor.select_unit(unit)
        self.cursor.selected_unit.old_position_x = self.cursor.selected_unit.position_x
        self.cursor.selected_unit.old_position_y = self.cursor.selected_unit.position_y
        self.cursor.state = CursorState.MOVE
        self.sprite_renderer.showIndicators()
    
    def _get_path(self):
        self.indicators.empty()

        indicator_coordinates = self.movement_display.pathfinding.return_path((self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y), (self.cursor.position_x, self.cursor.position_y))
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
        self.cursor.update_position(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
        self.cursor.selected_unit = None
        self.cursor.state = CursorState.MAP
        self.menu_cursor.SetCharState()
        self.target_selector.ClearTiles()
    
    def _update_offsets(self):
        for unit in self.units:
            unit.update_offset(self.camera.offset_X, self.camera.offset_Y)
        for tile in self.movement_display.movement_display:
            tile.update_offset(self.camera.offset_X, self.camera.offset_Y)
        for tile in self.movement_display.attack_display:
            tile.update_offset(self.camera.offset_X, self.camera.offset_Y)
        for indicator in self.indicators:
            indicator.update_offset(self.camera.offset_X, self.camera.offset_Y)


    #Moves the camera and cursor
    def _move_selection(self, dx, dy):
        if self.cursor.state == CursorState.MAP or self.cursor.state == CursorState.MOVE:
            if dx == 1 and self.cursor.position_x <= len(self.level[0]) - 1 and self.cursor.position_x - self.camera.offset_X >= 7:
                self.camera.offset_X += 1

            if dx == -1 and self.cursor.position_x -self.camera.offset_X > 0 and self.cursor.position_x - self.camera.offset_X < 3 and self.camera.offset_X > 0:
                self.camera.offset_X -= 1

            if dy == 1 and self.cursor.position_y <= len(self.level) - 1 and self.cursor.position_y - self.camera.offset_Y >= 7:
                self.camera.offset_Y += 1
            
            if dy == -1 and self.cursor.position_y > 0 and self.cursor.position_y - self.camera.offset_Y < 3 and self.camera.offset_Y > 0:
                self.camera.offset_Y -= 1

            if self.cursor.state != CursorState.CHARMENU and self.cursor.state != CursorState.ATTACK and self.cursor.state != CursorState.ITEM:
                self._update_offsets()

        if self.cursor.state == CursorState.MAP:
            if self._valid_tile(self.cursor.position_x + dx, self.cursor.position_y + dy):
                self.cursor.update_position(self.cursor.position_x + dx, self.cursor.position_y + dy, self.camera.offset_X, self.camera.offset_Y)

        elif self.cursor.state == CursorState.MOVE:
            if self._valid_tile(self.cursor.position_x + dx, self.cursor.position_y + dy):
                self.cursor.update_position(self.cursor.position_x + dx, self.cursor.position_y + dy, self.camera.offset_X, self.camera.offset_Y)
            if self.cursor.selected_unit is not None and (self.cursor.position_x, self.cursor.position_y) in self.movement_display.allowed_tiles:
                self._get_path()

        elif self.cursor.state == CursorState.CHARMENU:
            self.menu_cursor.ScrollCharMenu(self.menu_cursor.GetCommands(), self.menu_cursor.index + dy)

        elif self.cursor.state == CursorState.ATTACK:
            unit = self.target_selector.ScrollSelection(dx + dy)
            self.cursor.update_position(self.target_selector.GetSelection()[0], self.target_selector.GetSelection()[1], self.camera.offset_X, self.camera.offset_Y)
        
        elif self.cursor.state == CursorState.ITEM:
            self.menu_cursor.ScrollItemMenu(self.cursor.selected_unit.items, self.menu_cursor.index + dy)
            

    def _handle_confirm(self, unit):
        #If player has selected a unit and presses Z on an empty tile in range, move unit
        #If the selected unit is the same as the unit on that tile, change cursor state to CHARMENU
        if self.cursor.selected_unit is not None:

            if unit is None:
                if (self.cursor.position_x, self.cursor.position_y) in self.movement_display.GetAllowedTiles():
                    self.cursor.selected_unit.update_position(self.cursor.position_x, self.cursor.position_y, self.camera.offset_X, self.camera.offset_Y)
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
                        self.cursor.update_position(self.target_selector.GetSelection()[0], self.target_selector.GetSelection()[1], self.camera.offset_X, self.camera.offset_Y)
                        self.sprite_renderer.show_indicators = False
                    
                    elif self.menu_cursor.index == CharMenuCommands.ITEM.value:
                        self.cursor.state = CursorState.ITEM
                        self.menu_cursor.SetItemState()
                
                elif self.cursor.state == CursorState.ITEM:
                    if len(self.cursor.selected_unit.items) > 0:
                        selected_item = self.cursor.selected_unit.items[self.menu_cursor.index]
                        selected_item.use_item(self.cursor.selected_unit)
                        self._deactivate_selected_unit()

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
        self.menu_cursor.SetCharState()
        self.indicators.empty()
        if self.cursor.state == CursorState.MOVE:
            self.movement_display.ClearMovementRange()
            self.cursor.unselect_unit()
            self.cursor.state = CursorState.MAP
            self.sprite_renderer.hideIndicators()
        elif self.cursor.state == CursorState.CHARMENU:
            self.cursor.state = CursorState.MOVE
            self.cursor.selected_unit.revert_position(self.camera.offset_X, self.camera.offset_Y)
            self.cursor.update_position(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
            self.movement_display.hide_movement = False
            self.movement_display.hide_attack = False
        elif self.cursor.state == CursorState.ATTACK:
            self.cursor.state = CursorState.CHARMENU
            self.movement_display.ClearCurrentAttackRanges()
            self.cursor.update_position(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
            self.target_selector.ClearTiles()
        elif self.cursor.state == CursorState.ITEM:
            self.cursor.state = CursorState.CHARMENU
            self.menu_cursor.SetCharState()
            self.cursor.update_position(self.cursor.selected_unit.position_x, self.cursor.selected_unit.position_y, self.camera.offset_X, self.camera.offset_Y)
    


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
                unit_display = pygame.Surface((164,64))
                if (unit is not None and unit.alignment == Alignment.ENEMY):
                    unit_display.fill((154, 18, 4))
                else:
                    unit_display.fill((24, 48, 184))

                if self.cursor.selected_unit is not None and self.cursor.state is not CursorState.ATTACK:
                    unit_name = self.font.render(str(self.cursor.selected_unit.name), False, (255,255,255))
                    unit_hp = self.font.render("HP: " + str(self.cursor.selected_unit.current_hp) + "/" + str(self.cursor.selected_unit.max_hp), False, (222,222,222))
                    unit_attack = self.font2.render("STR: " + str(self.cursor.selected_unit.strength), False, (222,222,222))
                    unit_defense = self.font2.render("DEF: " + str(self.cursor.selected_unit.defense), False, (222,222,222))
                    unit_speed = self.font2.render("SPD: " + str(self.cursor.selected_unit.speed), False, (222,222,222))
                
                elif unit is not None:
                    unit_name = self.font.render(str(unit.name), False, (222,222,222))
                    unit_hp = self.font.render("HP: " + str(unit.current_hp) + "/" + str(unit.max_hp), False, (222,222,222))
                    unit_attack = self.font2.render("STR: " + str(unit.strength), False, (222,222,222))
                    unit_defense = self.font2.render("DEF: " + str(unit.defense), False, (222,222,222))
                    unit_speed = self.font2.render("SPD: " + str(unit.speed), False, (222,222,222))

                try:
                    unit_display.blit(unit_name, (10, 4))
                    unit_display.blit(unit_hp,(10, 24))
                    unit_display.blit(unit_attack, (10, 44))
                    unit_display.blit(unit_defense, (60, 44))
                    unit_display.blit(unit_speed, (110, 44))
                    self.screen.blit(unit_display, (10,5))
                except:
                    pass
                
            
            #If in character menu, draw menu
            #Refactor
            if self.cursor.state == CursorState.CHARMENU:
                available_commands = self.menu_cursor.GetCommands()

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
                self.screen.blit(character_menu, (10,100))
            
            elif self.cursor.state == CursorState.ITEM:
                items = self.cursor.selected_unit.items

                item_menu = pygame.Surface((100,100))
                item_menu.fill((24, 48, 184))

                i = 0
                for item in items:
                    item_menu.blit(item.image, (4, 6 + (i * 20)))
                    name_to_draw = self.font.render(itemNames[item.type.value] + "  " + str(item.remaining_uses), False, (222,222,222))
                    item_menu.blit(name_to_draw, (24, 2 + (i * 20)))
                    item_menu.blit(self.menu_cursor.surf, self.menu_cursor.rect)
                    self.screen.blit(item_menu, (10,80))
                    i += 1
                    
                
            #Display cursor debug information
            #TO DO: Add env variable to toggle this
            cursor_pos = self.font.render("x: " + str(self.cursor.position_x) + " y: " + str(self.cursor.position_y), False, (222,222,222))
            cursor_state = self.font.render(self.cursor.state.name, False, (222,222,222))

            camera_offset = self.font.render("Offset: (" + str(self.camera.offset_X) + ":" + str(self.camera.offset_Y) + ")", False, (222,222,222))

            self.screen.blit(cursor_pos, (560,4))
            self.screen.blit(cursor_state, (440, 4))
            self.screen.blit(camera_offset, (440, 24))

            pygame.display.flip()
    
    def _update_animations(self):
            for unit in self.units:
                unit.update_animation()
            for movetile in self.movement_display.GetMovementRange():
                movetile.update_animation()
            for attacktile in self.movement_display.GetAttackRange():
                attacktile.update_animation()
            for attacktile in self.movement_display.current_ranges:
                attacktile.update_animation()