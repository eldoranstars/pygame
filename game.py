import pygame
import game_functions as gf
from settings import Settings
from screen import Screen
from ship import Ship
from stats import GameStats
from button import Button

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Alien Invasion")
settings = Settings()
screen = Screen(settings)
stats = GameStats(settings)
ship = Ship(screen)
buttons = [Button(screen, "start")]
bullets = []
aliens = []

while True:
    gf.check_events(stats)
    if not stats.game_status:
        gf.update_screen(screen, ship, bullets, aliens, stats, buttons)
    if stats.game_status:
        gf.check_events(stats)
        gf.update_aliens(screen, aliens, ship, stats, bullets)
        gf.update_bullets(settings, bullets, aliens)
        gf.update_fleet(settings, screen, aliens)
        gf.update_player(settings, screen, ship, bullets)
        gf.update_screen(screen, ship, bullets, aliens, stats, buttons)