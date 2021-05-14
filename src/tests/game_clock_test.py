import unittest
from entities.game_clock import GameClock

class TestGameClock(unittest.TestCase):
    def setUp(self):
        self.clock = GameClock()
    
    def test_camera_initialized_correctly(self):
        self.assertEqual(self.camera.offset_x, 1)
        self.assertEqual(self.camera.offset_y, 2)