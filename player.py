import pygame


class Player:
    def __init__(self, h_game):
        self.screen = h_game.screen
        self.settings = h_game.settings
        self.imagePlayer = ["Pictures/walk/1.png", "Pictures/walk/2.png", "Pictures/walk/3.png", "Pictures/walk/4.png"
                            "Pictures/walk/5.png", "Pictures/walk/6.png"]
        self.screen_rect = h_game.screen.get_rect()             # Access the screen’s rect to place the player in the correct location on the screen.
        self.image = pygame.image.load(self.imagePlayer[h_game.index])        # load the player image and get its rect.
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft            # Set the location of the player on the screen (in the start).
        self.moving_up = False                                  # Movement flags.
        self.moving_down = False
        self.y = float(self.rect.y)                             # Store the player position as a decimal value.



    def moving_player(self):
        if self.moving_up and self.rect.top > 250:              # Moving the player to the top.
            self.y -= self.settings.player_speed

        if self.moving_down and self.rect.bottom < 750:         # Moving the player to the down.
            self.y += self.settings.player_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)                 # Draw the player at its current location.

    def center_player(self):                                    # Center the player on the left side of the screen.
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
