import sys
import pygame
from ship import Ship
from settings import Settings


class AlienInvasion:
    # GamePlay and Class
    def __init__(self):
        # initialization
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        # main
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # keyboard and mouse monitor and feedback
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # draw stuff
        self.screen.fill(self.settings.bg_color)
        self.ship.bliteme()

        # make drawn stuff visible
        pygame.display.flip()


if __name__ == '__main__':
    # test and run
    ai = AlienInvasion()
    ai.run_game()
