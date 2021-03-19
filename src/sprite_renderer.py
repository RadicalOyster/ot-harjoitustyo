import pygame

#Class that contains all sprites to be drawn
class SpriteRenderer(pygame.sprite.Sprite):
    def __init__(self):
        super(SpriteRenderer, self).__init__()
        self.sprites = pygame.sprite.Group()
        self.overlays = pygame.sprite.Group()

    def update(self, cursor, units, movementranges, attackranges):   
        self.sprites.empty()
        self.overlays.empty()    
        self.movement_display = movementranges
        for tile in movementranges:
            self.overlays.add(movementranges)
            self.overlays.add(attackranges)
        self.sprites.add(units)