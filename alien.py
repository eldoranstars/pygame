import pygame
import game_functions as gf
from settings import Settings
from screen import Screen
from ship import Ship

pygame.init()
pygame.display.set_caption("Alien Invasion")
settings = Settings()
screen = Screen(settings)
ship = Ship(screen)
bullets = []

while True:
    gf.check_events()
    gf.check_keyboard(settings, screen, ship, bullets)
    gf.update_screen(settings, screen, ship, bullets)