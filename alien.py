import pygame
import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.SCALED, vsync=1)
    ship = Ship(screen)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()