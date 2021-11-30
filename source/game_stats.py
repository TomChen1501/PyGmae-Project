class GameStats:
    # status for the game
    def __init__(self, ai_game):
        # initialise the statistics
        self.settings = ai_game.settings
        self.game_score = 0
        self.highest_game_score = 0
        self.game_level = 1
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.game_score = 0


if __name__ == '__main__':
    pass

