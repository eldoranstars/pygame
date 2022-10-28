import pygame
import game_functions as gf
from stats import GameStats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Alien Invasion")
stats = GameStats()

while True:
    gf.check_events(stats)
    gf.blit_screen(stats)
    if stats.game_active:
        gf.update_aliens(stats)
        gf.update_player()
        gf.update_bullets()
        gf.update_removed_stars()
        gf.update_asteroids()
        gf.append_star()
        gf.append_alien()
        if stats.asteroid_active:
            gf.append_asteroid()
        if stats.weapon_active:
            gf.reload_bullets()
        if not stats.weapon_active:
            gf.update_ammos(stats)
            gf.append_ammo()