import random

class Asteroid():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen.surface
        self.settings = settings
        self.speed_factor = settings.asteroid_sf
        self.move_left = False
        self.move_right = False
        self.move_down = True
        self.move_direction = random.randrange(0,9)
        if self.move_direction < 4:
            self.move_left = True
        if self.move_direction > 4:
            self.move_right = True
        # Загрузка изображения и получение прямоугольника
        self.surface = random.choice(settings.asteroid_list)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = random.randrange(self.rect.width, settings.screen_width, self.rect.width)
        self.rect.centery = 0

    def update(self):
        # Обновление координат изображения
        if self.move_left:
            self.rect.centerx -= self.speed_factor
        if self.move_right:
            self.rect.centerx += self.speed_factor
        if self.move_down:
            self.rect.centery += self.speed_factor
        else:
            self.rect.centery -= self.speed_factor

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)