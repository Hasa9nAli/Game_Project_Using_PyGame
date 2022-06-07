import pygame
class GameStats:                                                # Track statistics for player invasion.
    def __init__(self, h_game):
        self.settings = h_game.settings
        self.game_active = True
        self.reset_stats()
        self.screen = h_game.screen
        self.main = h_game
        self.screen_rect = h_game.screen.get_rect()

        self.img_heart_1 = pygame.image.load('Pictures/lives img 1.png') # load the hearts images and set their starting positions.
        self.rect_1 = self.img_heart_1.get_rect()
        self.rect_1.topleft = self.screen_rect.topleft

        self.img_heart_2 = pygame.image.load('Pictures/lives img 2.png')
        self.rect_2 = self.img_heart_2.get_rect()
        self.rect_2.topleft = self.screen_rect.topleft

        self.img_heart_3 = pygame.image.load('Pictures/lives img 3.png')
        self.rect_3 = self.img_heart_3.get_rect()
        self.rect_3.topleft = self.screen_rect.topleft


    def reset_stats(self):  # statistics that can change during the game.
        self.score = 0
        self.player_left = self.settings.player_limit

    def draw_hearts(self):                                      # Draws the hearts depending on (player_left) state.
        if self.player_left == 3:
            self.screen.blit(self.img_heart_1, self.rect_1)
        elif self.player_left == 2:
            self.screen.blit(self.img_heart_2, self.rect_2)
        else:
            self.screen.blit(self.img_heart_3, self.rect_3)

    def draw_instructions(self):
        self.img_instructions = pygame.image.load('Pictures/instructions.png')  # Show instruction window.
        self.rect_6 = self.img_instructions.get_rect()
        self.rect_6.center = self.screen_rect.center
        self.screen.blit(self.img_instructions, self.rect_6)

    def game_over(self):
        if not self.game_active:
            self.img_game_over = pygame.image.load('Pictures/GAME OVER.png')  # load (game over) image and set its starting position.
            self.rect_over = self.img_game_over.get_rect()
            self.rect_over.center = self.screen_rect.center
            self.settings.hit_hero.play()
            pygame.mixer.music.stop()
            self.settings.game_over.play()
            self.screen.blit(self.settings.background, (0, 0)) # Draw the background again to hide other elements in the screen.
            self.screen.blit(self.img_game_over, self.rect_over)



    def draw_you_win(self):
        self.img_you_win = pygame.image.load('Pictures/win game img.png')  # load (you win) image and set its starting position.
        self.rect_win = self.img_you_win.get_rect()
        self.rect_win.center = self.screen_rect.center
        self.screen.blit(self.img_you_win, self.rect_win)

    def you_win(self):
        if self.settings.number_columns_x == 7:
            self.screen.blit(self.settings.background, (0, 0))
            pygame.mixer.music.stop()
            self.settings.you_win.play()
            self.draw_you_win()
            self.main._pause()





