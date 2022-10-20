import pygame
import game_functions as gf
from settings import Settings
from screen import Screen
from ship import Ship
from game_stats import GameStats

pygame.init()
pygame.display.set_caption("Alien Invasion")
settings = Settings()
screen = Screen(settings)
stats = GameStats(settings)
ship = Ship(screen)
bullets = []
aliens = []

while True:
    gf.check_events()
    gf.update_bullets(settings, bullets, aliens)
    gf.update_aliens(screen, aliens, ship, stats)
    gf.update_fleet(settings, screen, aliens)
    gf.update_player(settings, screen, ship, bullets)
    gf.update_screen(settings, screen, ship, bullets, aliens)