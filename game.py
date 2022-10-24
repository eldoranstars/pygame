import pygame
import game_functions as gf
from stats import GameStats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Alien Invasion")
stats = GameStats()

while True:
    gf.check_events(stats)
    gf.update_screen(stats)
    if stats.game_active:
        gf.update_aliens(stats)
        gf.update_bullets()
        gf.update_fleet()
        gf.update_player()