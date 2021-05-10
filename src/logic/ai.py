import random
from entities.unit import Alignment
from logic.combat import Combat

class Ai():
    def __init__(self, units, pathfinding, level):
        self.units = units
        self.pathfinding = pathfinding
        self.level = level    

    def handle_enemy_turn(self, unit, offset_x=0, offset_y=0):
        movement_ranges = self._get_movement_tiles(unit, self.pathfinding, self.level)
        attack_ranges = self._get_attack_tiles(unit, movement_ranges)
        targets = self._find_enemies(attack_ranges, self.level)

        if len(targets) > 0:
            chosen_target = random.choice(targets)
            valid_tiles = self._tiles_to_attack_from(unit, chosen_target)
            for tile in valid_tiles:
                if tile not in movement_ranges:
                    valid_tiles.remove(tile)
            square_to_move_to = self._choose_square_to_move_to(valid_tiles, self.level)
            self.level.update_unit_position(unit, square_to_move_to[0],
            square_to_move_to[1])
            unit.update_position(square_to_move_to[0],
            square_to_move_to[1], offset_x, offset_y)
            dead_unit = Combat(unit, chosen_target)
            if dead_unit is not None:
                self.level.unit_positions[dead_unit.position_y][dead_unit.position_x] = None
                self.units.remove(dead_unit)

        else:
            square_to_move_to = self._choose_square_to_move_to(movement_ranges, self.level)
            self.level.update_unit_position(unit, square_to_move_to[0],
            square_to_move_to[1])
            unit.update_position(square_to_move_to[0],
            square_to_move_to[1], offset_x, offset_y)

    def _choose_square_to_move_to(self, tiles, level):
        square_to_move_to = random.choice(tiles)
        while (level.unit_positions[square_to_move_to[1]][square_to_move_to[0]]
        is not None):
            square_to_move_to = random.choice(tiles)
        return square_to_move_to

    def _get_attack_tiles(self, unit, movement_tiles):
        checked_tiles = []
        attack_range = unit.range
        updated_ranges = []

        for tile in movement_tiles:
            updated_ranges.append(tile)
            for i in range(-attack_range, attack_range + 1):
                for j in range(-attack_range, attack_range + 1):
                    if abs(i) + abs(j) > attack_range or (i == 0 and j == 0):
                        continue
                    new_tile = (tile[0] + i, tile[1] + j)
                    if new_tile not in checked_tiles:
                        updated_ranges.append(new_tile)
                        checked_tiles.append(new_tile)

        return updated_ranges

    def _get_movement_tiles(self, unit, pathfinding, level):
        pathfinding.calculate_distances(unit.position_x, unit.position_y, level, False)
        movement_ranges = pathfinding.return_ranges(unit.movement)
        return movement_ranges

    def _find_enemies(self, tiles, level):
        attack_targets = []

        for tile in tiles:
            if tile[1] >= 0 and tile[1] < len(level.movement_data) and tile[0] >= 0 and tile[0] < len(level.movement_data[0]):
                x_coordinate = tile[0]
                y_coordinate = tile[1]
                unit = level.unit_positions[y_coordinate][x_coordinate]

                if unit is not None and unit.alignment == Alignment.ALLY:
                    attack_targets.append(unit)

        return attack_targets
    
    def _tiles_to_attack_from(self, attacker, target):
        tiles = self._get_attack_tiles(attacker, [(target.position_x, target.position_y)])
        return tiles