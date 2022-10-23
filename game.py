import pygame
import game_functions as gf
from stats import GameStats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Alien Invasion")
stats = GameStats()
aliens = []
bullets = []

while True:
    gf.check_events(stats)
    gf.update_screen(aliens, bullets, stats)
    if stats.game_active:
        gf.update_aliens(aliens, bullets, stats)
        gf.update_bullets(aliens, bullets)
        gf.update_fleet(aliens)
        gf.update_player(bullets)