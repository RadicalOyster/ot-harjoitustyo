class Camera():
    """Class that handles the in-game camera to determine
    how much to offset graphical elements for rendering.
    """

    def __init__(self, offset_X=0, offset_Y=0):
        """The camera constructor.

        Args:
            offset_X: determines by how much to offset the position of rendered objects horizontally
            offset_Y determines by how much to offset the position of rendered objects vertically
        """
        self.offset_X = offset_X
        self.offset_Y = offset_Y
