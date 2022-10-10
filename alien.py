import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((Settings().screen_width, Settings().screen_height), pygame.SCALED, vsync=1)
    pygame.display.set_caption("Alien Invasion")

    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана.
        screen.fill(Settings().bg_color)
        pygame.display.update()

run_game()