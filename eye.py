import random

class Eye():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen.surface
        self.speed_factor = random.randrange(int(settings.eye_sf_min), int(settings.eye_sf_max))
        # Загрузка изображения и получение прямоугольника
        self.surface = settings.eye_surface
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(0, screen.rect.right, screen.rect.right)
        self.rect.centery = random.randrange(0, screen.rect.centery / 2, self.rect.height)
        if self.rect.centerx == 0:
            self.move_left = False
        if self.rect.centerx == screen.rect.right:
            self.move_left = True

    def update(self):
        # Обновление координат изображения
        if self.move_left:
            self.rect.centerx -= self.speed_factor
        if not self.move_left:
            self.rect.centerx += self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)