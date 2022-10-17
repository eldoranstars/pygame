import pygame

class Text():
    def __init__(self, settings, screen, textString):
        # Атрибуты класса
        self.screen = screen.surface
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.font.Font(None, 20).render(textString, True, settings.text_color)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = settings.text_center
        self.rect.bottom = settings.text_bottom

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)