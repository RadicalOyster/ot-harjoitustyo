from ui.animated_tile import AnimatedTile

class AttackTile(AnimatedTile):
    def __init__(self, x_pos=0, y_pos=0, offset_x=0, offset_y=0):
        super().__init__(x_pos, y_pos, offset_x, offset_y, "attacktile")
