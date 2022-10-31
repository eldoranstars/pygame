import random
from ammo import Ammo

class Asteroid():
    def __init__(self, screen, settings):
        # Атрибуты класса
        self.screen = screen
        self.settings = settings
        self.speed_factor = settings.asteroid_sf
        self.move_left = False
        self.move_right = False
        self.move_down = True
        self.move_direction = random.randrange(0,9)
        if self.move_direction < 3:
            self.move_left = True
        if self.move_direction > 5:
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
        if not self.move_down:
            self.rect.centery -= self.speed_factor
        if not self.screen.rect.colliderect(self.rect):
            self.settings.asteroids.remove(self)
        for invader in self.settings.invaders:
            if self.settings.collision(self.rect, 0.8, 0.8).colliderect(self.settings.collision(invader.rect, 0.8, 0.6)):
                self.settings.invaders.remove(invader)
                self.settings.score += 3
        for small in self.settings.smalls:
            if self.settings.collision(self.rect, 0.7, 0.7).colliderect(self.settings.collision(small.rect, 0.8, 0.6)):
                self.settings.smalls.remove(small)
                self.settings.score += 3
        for eye in self.settings.eyes:
            if self.settings.collision(self.rect, 0.7, 0.7).colliderect(self.settings.collision(eye.rect, 0.7, 0.7)):
                ammo = Ammo(self.screen, self.settings, 'alien')
                ammo.rect.center = eye.rect.center
                self.settings.ammos.append(ammo)
                self.settings.eyes.remove(eye)
                self.settings.score += 150
                self.settings.eye_chance = self.settings.eye_chance * self.settings.eye_chance_reduction

    def blitme(self):
        # Вывод изображения на экран
        self.screen.surface.blit(self.surface, self.rect)