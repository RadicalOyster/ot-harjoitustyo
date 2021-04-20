import pygame

# Class that contains all sprites to be drawn


class SpriteRenderer(pygame.sprite.Sprite):
    def __init__(self):
        super(SpriteRenderer, self).__init__()
        self.sprites = pygame.sprite.Group()
        self.indicators = pygame.sprite.Group()
        self.overlays = pygame.sprite.Group()
        self.indicators_active = False

    def update(self, cursor, units, indicators, movementranges, attackranges, current_attack_ranges):
        self.sprites.empty()
        self.overlays.empty()
        self.indicators.empty()

        self.overlays.add(movementranges)
        self.overlays.add(attackranges)
        self.overlays.add(current_attack_ranges)
        self.sprites.add(units)
        if self.show_indicators:
            self.indicators.add(indicators)

    def hide_indicators(self):
        self.indicators_active = False

    def show_indicators(self):
        self.indicators_active = True
