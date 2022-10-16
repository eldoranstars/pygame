class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 480
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 5
        # Параметры пули
        self.bullets_allowed = 1
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        # Параметры чужих
        self.aliens_allowed = 5
        self.alien_speed_factor = 1