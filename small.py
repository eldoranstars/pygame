import random

class Small():
    def __init__(self, screen, settings, center):
        # Атрибуты класса
        self.screen = screen.surface
        self.speed_factor = random.randrange(int(settings.invader_sf_min), int(settings.invader_sf_max))     
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.small_surface
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.center = center

    def update(self):
        # Обновление координат изображения
        self.rect.centery += self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)