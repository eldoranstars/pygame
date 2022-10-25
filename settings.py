import pygame

class Settings():
    def __init__(self):
        # Параметры игры
        self.star_limit = 5
        self.record = 0
        self.star_speedf = 3
        # Параметры экрана
        self.screen_width = 480
        self.screen_height = 720
        self.screen_color = (100, 100, 100)
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_limit = 1
        self.bullet_sf = 15
        self.reload_bullet_time = 1000
        self.bullet_color = (60, 60, 60)
        # Параметры изображений
        self.screen_bg = pygame.image.load('images/space.png')
        self.star_color = pygame.image.load('images/star.png')
        self.ship_surface = pygame.image.load('images/destroyer.png')
        self.alien_surface = pygame.image.load('images/invader.png')
        self.asteroid_pink = pygame.image.load('images/asteroid-pink.png')
        self.asteroid_grey = pygame.image.load('images/asteroid-grey.png')
        self.asteroid_blue = pygame.image.load('images/asteroid-blue.png')
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED, vsync=1)
        self.bullet_surface = pygame.Surface((self.bullet_width, self.bullet_height))
        self.asteroid_list = [self.asteroid_pink, self.asteroid_grey, self.asteroid_blue]
        # Параметры чужих
        self.alien_sf_min = 1
        self.alien_sf_max = 5
        self.alien_chance = 10
        self.alien_allowed = 15
        # Параметры среды
        self.asteroid_chance = 10
        self.asteroid_allowed = 15
        # Динамические параметры игры
        self.reset_settings()

    def reset_settings(self):
        # Сбросить параметры игры
        self.aliens = []
        self.asteroids = []
        self.bullets = []
        self.stars = []
        self.removed_stars = []
        self.score = 0
        self.ship_sf = 4
        self.last_bullet_time = 0
        self.reload_bullet = False
        self.asteroid_sf = self.ship_sf + 1
        self.star_left = self.star_limit
        self.bullet_left = self.bullet_limit