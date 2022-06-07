import pygame
from pygame.sprite import Sprite                                # Inherit an arrow class from sprite.

class Arrow(Sprite):
    def __init__(self, h_game):
        super().__init__()                                      # Create an arrow object at the ship current location.
        self.screen = h_game.screen
        self.settings = h_game.settings
        self.player = h_game.player
        self.image_arrow = pygame.image.load('Pictures/arrow.png')       # load the arrow image and get list rect.
        self.rect = self.image_arrow.get_rect()
        self.rect.midleft = h_game.player.rect.midright         # Put the arrow location in the middle-top of the player image.
        self.x = float(self.rect.x)                             # Store the arrow position as a decimal value.

    def update(self):
        self.x += self.settings.arrow_speed                     # Update decimal position of the arrow.
        self.rect.x = self.x                                    # Update the rect position.

    def draw_arrow(self):                                       # Draw the arrow in the screen.
        self.screen.blit(self.image_arrow, self.rect)
