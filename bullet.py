import pygame

class Bullet():
    def __init__(self, settings, screen, ship):
        # Атрибуты класса
        self.screen = screen.surface
        self.speed_factor = settings.bullet_speed_factor
        # Загрузка изображения и получение прямоугольника
        self.surface = pygame.Surface((settings.bullet_width,settings.bullet_height))
        self.surface.fill(settings.bullet_color)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - settings.bullet_height
        self.start_position = self.rect.top

    def update(self):
        # Обновление координат изображения
        self.rect.y -= self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)