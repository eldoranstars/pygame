import pygame
pygame.font.init()

class Text():
    def __init__(self, screen, msg, posx, posy):
        # Атрибуты класса
        self.screen = screen.surface
        self.msg = msg
        self.button_color = (150, 150, 255)
        self.text_color = (0, 0, 0)
        self.score = 0
        self.score_msg = msg.format(self.score)
        # Загрузка изображения и получение прямоугольника
        self.font = pygame.font.SysFont(None, 33)
        self.surface = self.font.render(self.score_msg, True, self.text_color, self.button_color)
        self.rect = self.surface.get_rect()
        # Получение изначальных координат изображения
        self.rect.centerx = posx
        self.rect.bottom = posy

    def update_text(self):
        # Обновление изображения
        self.score += 1
        self.score_msg = self.msg.format(self.score)
        self.surface = self.font.render(self.score_msg, True, self.text_color, self.button_color)

    def blitme(self):
        # Вывод изображения на экран
        self.screen.blit(self.surface, self.rect)