import random

class Ammo():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen.surface
        self.speed_factor = random.randrange(settings.ammo_sf_min, settings.ammo_sf_max)   
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.ammo_surface
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(self.rect.width, settings.screen_width, self.rect.width)
        self.rect.centery = 0

    def update(self):
        # Обновление координат изображения
        self.rect.centery += self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)