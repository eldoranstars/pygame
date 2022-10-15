import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.SCALED, vsync=1)
    ship = Ship(screen)
    bullets = Group()

    while True:
        gf.check_events()
        gf.check_keyboard(ai_settings, screen, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()