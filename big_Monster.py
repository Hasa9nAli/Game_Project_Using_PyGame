from random import randint

import pygame
from pygame.sprite import Sprite


class BigMonster(Sprite):
    def __init__(self, m_game):
        super().__init__()
        self.setting = m_game.settings
        self.screen = m_game.screen
        self.rect_screen = m_game.screen.get_rect()
        self.image_big_monster = pygame.image.load("Pictures/player img.png")
        self.rect_big_monster = self.image_big_monster.get_rect()
        self.rect_big_monster.y = self.rect_big_monster.height + 150
        self.rect_big_monster.x = 1380
        self.moveBigMonster = 0                                 # physical control moveing
        self.control = True                                     # control to condition one to logical

    def drawBigMonster(self):
        self.screen.blit(self.image_big_monster, self.rect_big_monster)

    def movingMonster(self):                                    # condition to control physical and limit of monster  and screen and control flag"""
        if 0 <= self.moveBigMonster <= 220 and \
                self.rect_screen.top <= self.rect_big_monster.top and \
                self.rect_screen.left <= self.rect_big_monster.left and \
                self.control:
            self.rect_big_monster.y += 1
            self.rect_big_monster.x -= 1
            self.moveBigMonster += 1

        if 220 <= self.moveBigMonster <= 420 and \
                self.rect_screen.bottom >= self.rect_big_monster.bottom:
            self.control = False
            self.rect_big_monster.y -= 1
            self.rect_big_monster.x -= 1
            self.moveBigMonster += 1
            if self.moveBigMonster == 420:
                self.moveBigMonster = 0
                self.control = True
