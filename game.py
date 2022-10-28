import pygame
import game_functions as gf
from stats import GameStats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("invader Invasion")
stats = GameStats()

while True:
    gf.check_events(stats)
    gf.blit_screen(stats)
    if stats.game_active:
        gf.update_invaders(stats)
        gf.update_balls(stats)
        gf.update_player()
        gf.update_bullets()
        gf.update_drop_stars()
        gf.update_asteroids()
        gf.append_star()
        gf.append_invader(stats)
        if stats.asteroid_active:
            gf.append_asteroid()
        if stats.weapon_active:
            gf.reload_bullets()
            gf.append_ball()
        if not stats.weapon_active:
            gf.update_ammos(stats)
            gf.append_ammo()