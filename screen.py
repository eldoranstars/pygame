import pygame

class Screen():
    def __init__(self, settings):
        # Атрибуты класса
        self.settings = settings
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.SCALED, vsync=1)
        self.rect = self.surface.get_rect()

    def blitme(self):
        # Вывод изображения на экран
        # self.surface.fill(self.settings.screen_color)
        self.surface.blit(self.settings.screen_color, self.rect)