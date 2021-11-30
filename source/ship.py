import pygame
from random import *

class Ship:
    def __init__(self, ai_game):
        self.delay = 0
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # get the image of the ship and make the out rect for it
        self.image = pygame.image.load('resource/images/me1.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.ship_rect = self.image.get_rect()

        self.hit_box_img = pygame.image.load('resource/images/Blue_Square.png')
        self.hit_box_img = pygame.transform.scale(self.hit_box_img, (8, 8))
        self.rect = self.hit_box_img.get_rect()
        self.graze_box = Graze_box()

        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.ship_rect.x)
        self.y = float(self.ship_rect.y)

        self.rect.center = self.ship_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.ship_rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.ship_rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


        self.ship_rect.x = self.x
        self.ship_rect.y = self.y
        self.rect.center = self.ship_rect.center
        self.graze_box.rect.center = self.rect.center


    def bliteme(self):
        self.screen.blit(self.image, self.ship_rect)
        self.screen.blit(self.hit_box_img, self.rect)

    def center_ship(self):
        self.ship_rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.ship_rect.x)
        self.y = float(self.ship_rect.y)
        self.rect.center = self.ship_rect.center

class Graze_box():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 20, 20)