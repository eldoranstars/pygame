import pygame

class Screen():
    def __init__(self, settings):
        # Атрибуты класса
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.SCALED, vsync=1)
        self.surface.fill(settings.bg_color)
        self.rect = self.surface.get_rect()

    def blitme(self):
        # Вывод изображения на экран
        self.surface.fill(self.settings.bg_color)