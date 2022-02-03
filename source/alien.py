import pygame
from pygame.sprite import Sprite
from math import *

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.image = pygame.image.load('resource/images/enemy1.png')
        self.rect = self.image.get_rect()
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("resource/images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("resource/images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("resource/images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("resource/images/enemy1_down4.png").convert_alpha(),
        ])
        # self.rect.left, self.rect.top = \
        #     randint(0, self.settings.screen_width - self.rect.width), \
        #     randint(-5 * self.settings.screen_height, 0)
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        self.rect.y = -50
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # def check_edges(self):
    #     screen_rect = self.screen.get_rect()
    #     if self.rect.right >= screen_rect.right or self.rect.left <= 0:
    #         return True

    def update(self):
        self.y += self.settings.alien_speed
        self.rect.y = self.y

        # self.x += self.settings.alien_speed * self.settings.fleet_direction
        # self.rect.x = self.x


class Alien_Bullet(Sprite):
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # self.color = self.settings.bullet_color

        # set a bullet at point (0,0) then change its position
        self.image = pygame.image.load("resource/images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = alien.rect.midbottom

        self.y = float(self.rect.y)  # store the y position of bullet
        self.grazed = False

    def update(self):
        self.y += self.settings.alien_bullet_speed * 3
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

class Alien_sniper_bullet(Sprite):
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("resource/images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = alien.rect.midbottom

        self.y = float(self.rect.y)  # store the y position of bullet
        self.x = float(self.rect.x)
        self.grazed = False
        self.target = ai_game.ship
        distance = sqrt(pow(self.rect.x - self.target.rect.x, 2) + pow(self.rect.y - self.target.rect.y, 2))
        self.y_speed = (self.settings.alien_bullet_speed / distance) * (self.target.rect.y - self.rect.y) * 3
        self.x_speed = (self.settings.alien_bullet_speed / distance) * (self.target.rect.x - self.rect.x) * 2

        # self.sina = (self.rect.y - self.target.rect.y) / distance
        # self.cosa = (self.target.rect.x - self.rect.x) / distance
        # angle = atan2(self.target.rect.y - self.rect.y, self.target.rect.x - self.rect.x)

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

class Alien_Boss(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.image = pygame.image.load('resource/images/enemy2.png')
        self.rect = self.image.get_rect()

        self.rect.y = -120
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # def __int__(self, ai_game, alien):
    #     super().__init__(ai_game)
    #     self.image = pygame.image.load('resource/images/enemy2.png').convert_alpha()
    #     self.rect = self.image.get_rect()

    def update(self):
        if self.y <= 100:
            self.y += self.settings.alien_speed
            self.rect.y = self.y
        else:
            pass
