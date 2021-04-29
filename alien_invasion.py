import sys
import pygame


class AlienInvasion:
# GamePlay and Class
    def __init__(self):
    # initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    # background color
        self.bg_color = (230,230,230)

    def run_game(self):
        # main
        while True:
        # keyboard and mouse monitor and feedback
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #
            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()