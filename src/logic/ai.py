import random
from entities.Unit import Alignment

class Ai():
    def __init__(self):
        pass

    def handle_enemy_turn(self, units, pathfinding):
        for unit in units:
            if unit.alignment == Alignment.ENEMY:
                attack_ranges = self._getAttackTiles(unit, pathfinding)
                movement_ranges = self._getMovementTiles(unit, pathfinding)
                
                targets = self._findEnemies(attack_ranges, units)



    
    def _getAttackTiles(self, unit, pathfinding):
        pathfinding.calculate_distances(unit.position_x, unit.position_y)
        attack_ranges = pathfinding.return_ranges(unit.movement + unit.range)
        return attack_ranges
    
    def _getMovementTiles(self, unit, pathfinding):
        movement_ranges = pathfinding.return_ranges(unit.movement)
        return movement_ranges       
    
    def _findEnemies(self, tiles, units):
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