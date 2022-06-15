import pygame

class Settings:
    def __init__(self, main):
        """"""
        """ Screen settings: """
        self.main = main
        self.background = None
        self.numberBackground = 1
        self.background = pygame.image.load(f'Pictures/bg-{self.numberBackground}.jpg')


        """ Sound settings: """
        self.arrow_sound = pygame.mixer.Sound("Sounds/shoot.ogg")
        self.arrow_wind = pygame.mixer.Sound("Sounds/whoosh (phaser).wav")
        self.hit_hero = pygame.mixer.Sound("Sounds/hit hero.mp3")
        self.game_over = pygame.mixer.Sound("Sounds/Game over .mp3")
        self.you_win = pygame.mixer.Sound("Sounds/Victory.mp3")



        """ player settings: """
        self.player_speed = 1.5
        self.player_limit = 3


        """ Arrow settings: """
        self.arrow_speed = 1.0
        self.arrows_allowed = 10


        """ Monster settings: """
        self.monster_speed = 0.4                                # Speed of the monster in the start of the game.
        self.number_monsters_y = 4                              # The number of monsters in each column.
        self.number_columns_x = 0                               # The number of columns.
        self.monster_points = 10                                # Points for each monster been killed.


        """big monster setting """
        self.big_monster_speed = 0.2


    def increase_speed(self):
        self.arrow_speed += 0.1
        self.monster_speed += 0.05                              # The speed will increase by 0.03 bt each level.
        self.number_columns_x += 1                              # Add a new column by each level.
        print(self.number_columns_x)

    
    def background_image(self):
        if self.main.countNumberEmptyEnemy % 3 == 0:
            if self.numberBackground <= 12:
                self.background = pygame.image.load(f'Pictures/bg-{self.numberBackground}.jpg')
                self.numberBackground += 1
            else:
                self.numberBackground = 0 