class Settings:
    # store all the settings

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # ship setting
        self.ship_speed = 1.5
        self.ship_limit = 3   # stores the initial number of ships that the user has
        self.ship_fire_level = 1

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # aliens settings
        self.alien_speed = 0.7
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means right, = -1 means left
        self.fleet_direction = 1

