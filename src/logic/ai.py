import random
from entities.Unit import Alignment

class Ai():
    def __init__(self):
        pass

    def handle_enemy_turn(self, units, pathfinding):
        for unit in units:
            if unit.alignment == Alignment.ENEMY:
                attack_ranges = self._get_attack_tiles(unit, pathfinding)
                movement_ranges = self._get_movement_tiles(unit, pathfinding)

                targets = self._find_enemies(attack_ranges, units)

                



    def _get_attack_tiles(self, unit, pathfinding):
        pathfinding.calculate_distances(unit.position_x, unit.position_y)
        attack_ranges = pathfinding.return_ranges(unit.movement + unit.range)
        return attack_ranges

    def _get_movement_tiles(self, unit, pathfinding):
        movement_ranges = pathfinding.return_ranges(unit.movement)
        return movement_ranges       

    def _find_enemies(self, tiles, units):
        attack_targets = []

        for tile in tiles:
            target = {'unit': None, 'neighbors': []}
            x_coordinate = tile[0]
            y_coordinate = tile[1]

            for unit in units:
                if unit.pos_x == x_coordinate and unit.pos_y == y_coordinate:
                    target['unit'] = unit

                    target['neighbors'].append((x_coordinate + 1, y_coordinate))
                    target['neighbors'].append((x_coordinate, y_coordinate + 1))
                    target['neighbors'].append((x_coordinate - 1, y_coordinate))
                    target['neighbors'].append((x_coordinate, y_coordinate - 1))
                    attack_targets.append(target)
                    break

        return attack_targets
    
    def remove_invalid_targets(self, targets, movement_ranges):
        culled_target_list = []
        for target in targets:
            if not any(tile in target.neighbors for tile in movement_ranges):
                break
            else:
                culled_target_list.append(target)
        return culled_target_list