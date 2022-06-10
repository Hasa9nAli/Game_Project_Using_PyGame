import pygame.font
class ScoreBoard:
    def __init__(self, h_game):
        self.screen = h_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = h_game.settings
        self.stats = h_game.stats

        """ Font settings for scrolling information: """
        self.text_color = (255, 245, 110)
        self.font = pygame.font.SysFont(None, 45)
        self.prep_score()                                      # Prepare the initial score image.


        self.coin = pygame.image.load('Pictures/coin img.png') # load coin image and set its starting position.
        self.rect_6 = self.coin.get_rect()
        self.rect_6.left = self.screen_rect.left + 200
        self.rect_6.top = self.screen_rect.top

    def prep_score(self):                                       # method to turn the score into a rendered image.
        score_string = str(self.stats.score)                    # Turn the score into string.
        self.score_image = self.font.render(score_string, True, self.text_color)

        self.score_rect = self.score_image.get_rect()           # Display the score as an image.
        self.score_rect.left = self.screen_rect.left + 250      # Set the location of the score.`
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.coin, self.rect_6)                # Draw the coin image to the screen.
        self.screen.blit(self.score_image, self.score_rect)     # Draw the score to the screen.
