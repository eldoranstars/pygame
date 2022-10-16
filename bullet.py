import pygame

class Bullet():
    """Класс для управления пулями, выпущенными кораблем."""
    def __init__(self, ai_settings, screen, ship):
        """Создает объект пули в текущей позиции корабля."""
        self.screen = screen
        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.Surface((ai_settings.bullet_width,ai_settings.bullet_height))
        self.image.fill(ai_settings.bullet_color)
        self.rect = self.image.get_rect()
        # Каждая новая пуля появляется у верхнего края корабля.
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - ai_settings.bullet_height * 2
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает пулю вверх по экрану."""
        self.rect.y -= self.speed_factor

    def blitme(self):
        """Вывод пули на экран."""
        self.screen.blit(self.image, self.rect)