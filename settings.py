import pygame

class Settings():
    def __init__(self):
        # Параметры экрана
        self.screen_width = 480
        self.screen_height = 720
        self.screen_color = pygame.image.load('images/space.png')
        # Параметры пули
        self.bullets_allowed = 1
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        # Параметры чужих
        self.aliens_allowed = 15
        self.alien_speed_factor = 1
        # Параметры корабля
        self.ship_speed_factor = 5