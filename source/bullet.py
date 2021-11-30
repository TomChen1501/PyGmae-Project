import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # self.color = self.settings.bullet_color

        # set a bullet at point (0,0) then change its position
        self.image = pygame.image.load("resource/images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.ship_rect.midtop # move the bullet to the mid-top of the rect of ship

        self.y = float(self.rect.y) # store the y position of bullet

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
