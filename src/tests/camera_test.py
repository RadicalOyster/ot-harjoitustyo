import unittest
from entities.camera import Camera

class TestCamera(unittest.TestCase):
    def setUp(self):
        self.camera = Camera(1,2)
    
    def test_camera_initialized_correctly(self):
        self.assertEqual(self.camera.offset_x, 1)
        self.assertEqual(self.camera.offset_y, 2)