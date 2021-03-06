import unittest
from logic.pathfinding import PathFinding
from entities.level import Level

game_map = [
[1, 80, 1],
[1, 80, 1],
[1, 1, 1]
 ]

level = Level(
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]], []
)

level.movement_data = game_map

class TestPathfinding(unittest.TestCase):
    def setUp(self):
        self.pathfinding = PathFinding(1, 1, game_map)

    def test_pathfinding_returns_correct_distances(self):
        self.pathfinding.calculate_distances(0, 0, level)
        distances = self.pathfinding.distance
        correct_distances = [
            [0, 80, 6],
            [1, 81, 5],
            [2, 3, 4]
        ]
        self.assertEqual(distances, correct_distances)

    def test_return_path_returns_correct_path(self):
        path = self.pathfinding.return_path((0,0), (2,0))
        correct_path = [(2,0), (2,1), (2,2), (1,2), (0,2), (0,1), (0,0)]
        self.assertEqual(path, correct_path)

    def test_return_ranges_returns_correct_tiles(self):
        self.pathfinding.calculate_distances(1, 2, level)
        ranges = self.pathfinding.return_ranges(2)
        self.assertEqual(ranges, [(0, 1), (2, 1), (0, 2), (1, 2), (2, 2)])
