import pygame

#Class that contains all sprites to be drawn
class SpriteRenderer(pygame.sprite.Sprite):
    def __init__(self):
        super(SpriteRenderer, self).__init__()
        self.all_sprites = pygame.sprite.Group()

    def update(self, cursor, movementranges, units):   
        self.all_sprites.empty()        
        self.movement_display = movementranges
        for tile in movementranges:
            self.all_sprites.add(movementranges)
        self.all_sprites.add(units)