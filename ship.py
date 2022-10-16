import pygame

class Ship():
    def __init__(self, screen):
        # Атрибуты класса
        self.screen = screen.surface
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.image.load('images/destroyer.png')
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = screen.rect.centerx
        self.rect.bottom = screen.rect.bottom

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)