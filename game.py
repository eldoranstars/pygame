import pygame
import game_functions as gf
from settings import Settings
from screen import Screen
from ship import Ship
from game_stats import GameStats
from button import Button

pygame.init()
pygame.display.set_caption("Alien Invasion")
settings = Settings()
screen = Screen(settings)
play_button = Button(settings, screen, "Play")
stats = GameStats(settings)
ship = Ship(screen)
bullets = []
aliens = []

while True:
    gf.check_events(stats)
    if not stats.game_active:
        gf.update_screen(screen, ship, bullets, aliens, stats, play_button)
    if stats.game_active:
        gf.update_aliens(screen, aliens, ship, stats)
        gf.update_bullets(settings, bullets, aliens)
        gf.update_fleet(settings, screen, aliens)
        gf.update_player(settings, screen, ship, bullets)
        gf.update_screen(screen, ship, bullets, aliens, stats, play_button)