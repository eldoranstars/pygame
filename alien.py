import random

class Alien():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen.surface
        self.settings = settings
        self.speed_factor = random.randrange(settings.alien_sf_min, settings.alien_sf_max)
        self.move_direction = random.randrange(0,9)
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.alien_surface
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(self.rect.width, settings.screen_width, self.rect.width)
        self.rect.centery = 0

    def update(self):
        # Обновление координат изображения
        if self.move_direction < 3:
            self.rect.centerx += self.speed_factor
        if self.move_direction > 5:
            self.rect.centerx -= self.speed_factor
        self.rect.centery += self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)