import pygame
import random

class Alien():
    def __init__(self, settings, screen):
        # Атрибуты класса
        self.screen = screen.surface
        self.speed_factor = settings.alien_speed_factor * random.randrange(1,3)
        self.move_direction = random.randrange(0,9)
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.image.load('images/invader.png')
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(self.rect.centerx, settings.screen_width, self.rect.width)
        self.rect.centery = 0

    def update(self):
        # Обновление координат изображения
        if self.move_direction < 3:
            self.rect.centerx += self.speed_factor
        if self.move_direction > 6:
            self.rect.centerx -= self.speed_factor
        self.rect.centery += self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)