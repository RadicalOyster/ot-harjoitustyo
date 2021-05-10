class Camera():
    """Class that handles the in-game camera to determine
    how much to offset graphical elements for rendering.
    """

    def __init__(self, offset_x=0, offset_y=0):
        """The camera constructor.

        Args:
            offset_X: determines by how much to offset the position of rendered objects horizontally
            offset_Y determines by how much to offset the position of rendered objects vertically
        """
        self.offset_x = offset_y
        self.offset_y = offset_y
