from enum import Enum
import pygame
from utility_functions import load_image


class Alignment(Enum):
    ALLY = 0
    ENEMY = 1


sprite_suffixes = ["", "_e"]


class Unit(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0, alignment=Alignment.ALLY, hp=15,
    name="Fighter", strength=5, speed=2, defense=3, offset_x=0, offset_y=0):
        super().__init__()

        self.unit_class = "fighter"
        self.movement = 3
        self.sprites = []
        self.active_sprite = 0
        self.alignment = alignment
        self.max_hp = hp
        self.current_hp = hp
        self.sprites.append(load_image(
            "fighter_1" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_2" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_3" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_2" + sprite_suffixes[self.alignment.value] + ".png"))
        self.sprites.append(load_image(
            "fighter_1" + sprite_suffixes[self.alignment.value] + ".png"))
        self.image = pygame.transform.scale(
            self.sprites[self.active_sprite], (64, 64))
        self.has_moved = False
        self.name = name
        self.dead = False

        # temporary until weapons are implemented
        self.range = 1
        self.might = 5

        self.strength = strength
        self.speed = speed
        self.defense = defense

        self.items = []

        self.position_x = pos_x
        self.position_y = pos_y
        self.old_position_x = pos_x
        self.old_position_y = pos_y

        self.rect = self.image.get_rect()
        self.rect.x = pos_x * 64 - offset_x * 64
        self.rect.y = pos_y * 64 - offset_y * 64

    def update_position(self, pos_x, pos_y, offset_x=0, offset_y=0):
        self._remember_position(self.position_x, self.position_y)
        self.position_x = pos_x
        self.position_y = pos_y
        self.rect.x = pos_x * 64 - offset_x * 64
        self.rect.y = pos_y * 64 - offset_y * 64

    def revert_position(self, offset_x, offset_y):
        self.position_x = self.old_position_x
        self.position_y = self.old_position_y
        self.update_offset(offset_x, offset_y)

    def _remember_position(self, pos_x, pos_y):
        self.old_position_x = pos_x
        self.old_position_y = pos_y

    def update_animation(self):
        # active frame is still updated even when unit has not moved to keep animations in sync
        self.active_sprite += 0.1
        if self.active_sprite > len(self.sprites):
            self.active_sprite = 0
        if not self.has_moved:
            self.image = pygame.transform.scale(
                self.sprites[int(self.active_sprite)], (64, 64))

    def update_offset(self, offset_x, offset_y):
        self.rect.x = self.position_x * 64 - offset_x * 64
        self.rect.y = self.position_y * 64 - offset_y * 64

    def deactivate(self):
        self.has_moved = True
        self.image = pygame.transform.scale(
            load_image("fighter_inactive.png"), (64, 64))

    def activate(self):
        self.has_moved = False
        self.image = pygame.transform.scale(
            self.sprites[int(self.active_sprite)], (64, 64))

    def update_hp(self, damage):
        self.current_hp -= damage
        if (self.current_hp <= 0):
            self.dead = True

        elif (self.current_hp > self.max_hp):
            self.current_hp = self.max_hp
