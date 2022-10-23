import pygame
pygame.font.init()

class Button():
    def __init__(self, screen, msg, posx, posy):
        # Атрибуты класса
        self.screen = screen.surface
        self.button_color = (150, 150, 255)
        self.text_color = (0, 0, 0)
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.font.SysFont(None, 33).render(msg, True, self.text_color, self.button_color)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = posx
        self.rect.bottom = posy

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)