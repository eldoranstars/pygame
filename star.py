import pygame
import random

class Star():
    def __init__(self, settings, screen):
        # Атрибуты класса
        self.screen = screen.surface
        self.speed_factor = settings.star_speedf
        self.move_direction = random.randrange(0,9)
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.star_color
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(self.rect.width, settings.screen_width, self.rect.width)
        self.rect.centery = random.randrange(0, screen.rect.centery, self.rect.height)

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