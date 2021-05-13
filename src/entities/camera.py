"""Module containing the in-game camera.
"""
class Camera():
    """Class that handles the in-game camera to determine
    how much to offset graphical elements for rendering.
    """
    def __init__(self, offset_x=0, offset_y=0):
        """The camera constructor.

        Args:
            offset_x: determines by how much to offset the position of rendered objects horizontally
            offset_y determines by how much to offset the position of rendered objects vertically
        """
        self.offset_x = offset_x
        self.offset_y = offset_y
