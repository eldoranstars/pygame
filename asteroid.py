import random

class Asteroid():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen.surface
        self.settings = settings
        self.speed_factor = settings.asteroid_sf
        self.move_direction = random.randrange(0,9)
        self.down = True
        # Загрузка изображения и получение прямоугольника
        self.surface = random.choice(settings.asteroid_list)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(self.rect.width, settings.screen_width, self.rect.width)
        self.rect.centery = 0

    def update(self):
        # Обновление координат изображения
        if self.move_direction < 3:
            self.rect.centerx += self.speed_factor
        if self.move_direction > 5:
            self.rect.centerx -= self.speed_factor
        if self.down:
            self.rect.centery += self.speed_factor
        else:
            self.rect.centery -= self.speed_factor

    def change_direction(self):
        # Обновление координат изображения
        self.down = False

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)