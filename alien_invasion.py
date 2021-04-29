import sys
import pygame

from settings import Settings

class AlienInvasion:
# GamePlay and Class
    def __init__(self):
    # initialization
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # main
        while True:
        # keyboard and mouse monitor and feedback
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()