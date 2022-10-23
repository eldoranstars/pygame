import pygame

class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 480
        self.screen_height = 720
        self.screen_color = pygame.image.load('images/space.png')
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1
        self.bullet_speed_factor = 15
        # Параметры чужих
        self.alien_sf_min = 1
        self.alien_sf_max = 5
        self.alien_allowed = 15
        # Динамические параметры игры
        self.reset_settings()

    def reset_settings(self):
        # Сброс параметров игры
        self.ship_speed_factor = 5
        self.alien_chance = 5
        self.score = 0