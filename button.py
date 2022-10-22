import pygame

class Button():
    def __init__(self, settings, screen, msg):
        # Атрибуты класса
        self.screen = screen.surface
        self.button_color = (150, 150, 255)
        self.text_color = (0, 0, 0)
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.font.SysFont(None, 33).render(msg, True, self.text_color, self.button_color)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = settings.screen_width / 2
        self.rect.bottom = settings.screen_height - 20

    def blitme(self):
        # Вывод изображения на экран
        # self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.surface, self.rect)