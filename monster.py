import pygame
from pygame.sprite import Sprite


class Monster(Sprite):
    def __init__(self, h_game):
        super().__init__()
        self.screen = h_game.screen
        self.settings = h_game.settings
        self.image = pygame.image.load("Pictures/Monster img.png")
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height                     # Start each new alien at the wanted place of the screen.
        self.rect.x = 1250
        self.y = float(self.rect.y)                        # Store tha alien exact vertical position as a decimal value.

    def update(self):
        self.x -= self.settings.monster_speed              # Update decimal position of the monsters.
        self.rect.x = self.x                               # Update the rect position.