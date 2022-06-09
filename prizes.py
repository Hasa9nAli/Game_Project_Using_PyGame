import pygame

class Prize:
    def __init__(self, h_game):
        self.screen = h_game.screen
        self.settings = h_game.settings
        self.screen_rect = h_game.screen.get_rect()
        self.image = pygame.image.load('Pictures/coin img.png')
        self.rect = self.image.get_rect()
        self.rect.y = 350
        self.rect.x = 1380
        self.x = float(self.rect.x)

    def moving_coin(self):
        self.x -= self.settings.monster_speed
        self.rect.x = self.x

    def draw_coin(self):
        self.screen.blit(self.image, self.rect)









