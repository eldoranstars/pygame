import pygame
import game_functions as gf
from stats import GameStats

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Invader Invasion")
stats = GameStats()
bullet_sound = pygame.mixer.Sound('images/bullet.mp3')
intro_sound = pygame.mixer.Sound('images/intro.mp3')
intro_sound.play(-1)
joystick = 0
if pygame.joystick.get_count():
    joystick = pygame.joystick.Joystick(0)

while True:
    gf.check_events(stats, joystick, intro_sound)
    gf.blit_screen(stats)
    if stats.final_active and not stats.game_active:
        gf.update_final_text()
        gf.append_messages()
    if stats.game_active:
        gf.update_ship(stats, joystick, bullet_sound)
        gf.update_bosses(stats)
        gf.update_invaders(stats)
        gf.update_smalls(stats)
        gf.update_asteroids(stats)
        gf.update_tusks(stats)
        gf.update_balls(stats)
        gf.update_ammos(stats)
        gf.update_eyes(stats)
        gf.update_bullets()
        gf.update_drop_stars()
        gf.append_star()
        if stats.shield_active:
            gf.append_eye()
        if stats.weapon_active:
            gf.append_ball()
        if not stats.boss_active:
            gf.append_invader()
        if not stats.weapon_active:
            gf.append_ammo()