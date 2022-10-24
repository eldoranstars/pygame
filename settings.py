import pygame

class Settings():
    def __init__(self):
        # Параметры игры
        self.star_limit = 3
        self.star_speedf = 3
        self.record = 0
        # Параметры экрана
        self.screen_width = 480
        self.screen_height = 720
        # Параметры изображений
        self.screen_color = pygame.image.load('images/space.png')
        self.star_color = pygame.image.load('images/star.png')
        self.alien_color = pygame.image.load('images/invader.png')
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_allowed = 1
        self.bullet_speed_factor = 15
        self.bullet_color = (60, 60, 60)
        # Параметры чужих
        self.alien_sf_min = 1
        self.alien_sf_max = 5
        self.alien_allowed = 15
        # Динамические параметры игры
        self.reset_settings()

    def reset_settings(self):
        # Сбросить параметры игры
        self.aliens = []
        self.bullets = []
        self.stars = []
        self.removed_stars = []
        self.star_left = self.star_limit
        self.ship_speed_factor = 5
        self.alien_chance = 5
        self.score = 0