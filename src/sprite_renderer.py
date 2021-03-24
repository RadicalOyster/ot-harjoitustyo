import pygame

#Class that contains all sprites to be drawn
class SpriteRenderer(pygame.sprite.Sprite):
    def __init__(self):
        super(SpriteRenderer, self).__init__()
        self.sprites = pygame.sprite.Group()
        self.indicators = pygame.sprite.Group()
        self.overlays = pygame.sprite.Group()
        self.show_indicators = False

    def update(self, cursor, units, indicators, movementranges, attackranges):
        self.sprites.empty()
        self.overlays.empty()
        self.indicators.empty()

        self.overlays.add(movementranges)
        self.overlays.add(attackranges)
        self.sprites.add(units)
        if self.show_indicators:
            self.indicators.add(indicators)
    
    def hideIndicators(self):
        self.show_indicators = False
    
    def showIndicators(self):
        self.show_indicators = True