class Settings:
    # store all the settings

    def __init__(self):
        # screen settings
        self.screen_width = 960
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed = 0.7
        self.ship_limit = 3   # stores the initial number of ships that the user has
        self.ship_fire_level = 1

        # bullet settings
        self.bullet_speed = 0.5
        self.alien_bullet_speed = 0.1
        # self.bullet_width = 3
        # self.bullet_height = 15
        # self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # aliens settings
        self.alien_speed = 0.05
        # self.fleet_drop_speed = 10
        # fleet_direction = 1 means right, = -1 means left
        # self.fleet_direction = 1
