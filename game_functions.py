import sys
import pygame
import random
from time import sleep
from invader import Invader
from eye import Eye
from ball import Ball
from bullet import Bullet
from settings import Settings
from screen import Screen
from ship import Ship
from star import Star
from text import Text
from asteroid import Asteroid
from ammo import Ammo

settings = Settings()
collision = settings.collision
screen = Screen(settings)
ship = Ship(screen, settings)
star = Star(screen, settings)
pause = Text(screen, "PAUSE", screen.rect.centerx - 40, screen.rect.centery)
score = Text(screen, "BOSS ARRIVES: {:,}", screen.rect.left, screen.rect.top + 44)
record = Text(screen, "PREVIOS RECORD: {:,}", screen.rect.left, screen.rect.top + 22)

def collision_test(object, wm, hm):
    # Вывод коллизий на экран.
    screen.surface.blit(pygame.Surface((collision(object.rect, wm, hm).width,collision(object.rect, wm, hm).height)), collision(object.rect, wm, hm))

def check_events(stats):
    # Отслеживание событий клавиатуры и мыши.
    if stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                stats.game_active = False
                score.update_text(settings.update_score_left())
    if not stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                stats.game_active = True

def update_ship(stats):
    # Отслеживание нажатий клавиатуры и мыши.
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == 1 and ship.rect.right < settings.screen_width:
        ship.rect.centerx += settings.ship_sf
    if key[pygame.K_LEFT] == 1 and ship.rect.left > 0:
        ship.rect.centerx -= settings.ship_sf
    if key[pygame.K_UP] == 1 and ship.rect.top > 0:
        ship.rect.centery -= settings.ship_sf
    if key[pygame.K_DOWN] == 1 and ship.rect.bottom < settings.screen_height:
        ship.rect.centery += settings.ship_sf
    if key[pygame.K_SPACE] == 1 and settings.bullet_left > 0:
        settings.bullet_left -= 1
        bullet = Bullet(screen, settings, ship)
        settings.bullets.append(bullet)
    if stats.weapon_active:
        # Флаг перезарядки и фиксация времени начала
        if not settings.reload_bullet and settings.bullet_left == 0:
            settings.reload_bullet = True
            settings.last_bullet_time = pygame.time.get_ticks()
        # Снятие флага перезарядки на основе дельты времени и пополнение боезапаса
        if settings.reload_bullet and pygame.time.get_ticks() - settings.last_bullet_time > settings.reload_bullet_time:
            settings.reload_bullet = False
            settings.bullet_left = settings.bullet_limit

def update_invaders(stats):
    # Обновить расположение объектов на экране.
    for invader in settings.invaders:
        invader.update()
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(invader.rect, 0.8, 0.6)):
            settings.invaders.remove(invader)
            reset_after_collision(stats)

def update_smalls(stats):
    # Обновить расположение объектов на экране.
    for small in settings.smalls:
        small.update()
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(small.rect, 0.8, 0.6)):
            settings.smalls.remove(small)
            reset_after_collision(stats)

def update_balls(stats):
    # Обновить расположение объектов на экране.
    for ball in settings.balls:
        ball.update()
        if not stats.shield_active:
            if collision(ship.rect, 0.6, 0.9).colliderect(collision(ball.rect, 0.7, 0.7)):
                settings.balls.remove(ball)
                reset_after_collision(stats)
        if stats.shield_active:
            if collision(ball.rect, 0.7, 0.7).collidepoint(ship.rect.midtop):
                ball.move_down = False
                ball.surface = settings.alien_ball_surface
            if collision(ball.rect, 0.7, 0.7).collidepoint(ship.rect.midleft):
                ball.move_left = True
                ball.move_right = False
                ball.move_down = False
                ball.surface = settings.alien_ball_surface
            if collision(ball.rect, 0.7, 0.7).collidepoint(ship.rect.midright):
                ball.move_left = False
                ball.move_right = True
                ball.move_down = False
                ball.surface = settings.alien_ball_surface

def update_ammos(stats):
    # Обновить расположение объектов на экране.
    for ammo in settings.ammos:
        ammo.update()
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(ammo.rect, 0.7, 0.7)):
            settings.ammos.remove(ammo)
            if ammo.type == 'weapon':
                stats.weapon_active = True
                settings.invader_sf_min = 1
                settings.invader_sf_max = 8
                settings.bullet_limit = 1
                settings.bullet_left = settings.bullet_limit
                ship.surface = settings.weapon_ship_surface
            if ammo.type == 'shield':
                stats.shield_active = True
                ship.surface = settings.shield_ship_surface
            if ammo.type == 'alien':
                settings.score += 1500

def update_asteroids():
    # Обновить расположение объектов на экране.
    for asteroid in settings.asteroids:
        asteroid.update()
        if collision(asteroid.rect, 0.8, 0.8).collidepoint(ship.rect.midtop):
            asteroid.move_down = False
        if collision(asteroid.rect, 0.8, 0.8).collidepoint(ship.rect.midleft):
            asteroid.move_left = True
            asteroid.move_right = False
            asteroid.move_down = False
        if collision(asteroid.rect, 0.8, 0.8).collidepoint(ship.rect.midright):
            asteroid.move_left = False
            asteroid.move_right = True
            asteroid.move_down = False

def update_eyes():
    # Обновить расположение объектов на экране.
    for eye in settings.eyes:
        eye.update()

def update_bullets():
    # Обновить расположение объектов на экране.
    for bullet in settings.bullets:
        bullet.update()

def update_drop_stars():
    # Обновить расположение объектов на экране.
    for star in settings.drop_stars:
        star.update()

def reset_after_collision(stats):
    # Обновить счет и экран после коллизии
    sleep(0.5)
    if stats.shield_active:
        stats.shield_active = False
        ship.surface = settings.weapon_ship_surface
    else:
        stats.weapon_active = False
        ship.surface = settings.ship_surface
        if len(settings.stars) > 0:
            settings.star_left -= 1
            settings.player_hit()
            drop_star = random.choice(settings.stars)
            settings.stars.remove(drop_star)
            settings.drop_stars.append(drop_star)
        else:
            stats.game_active = False
            if settings.score > settings.record:
                settings.record = settings.score
                record.update_text(settings.record)
            score.update_text(settings.update_score_left())
            ship.rect.centerx = screen.rect.centerx
            ship.rect.bottom = screen.rect.bottom
            settings.new_game()

def append_invader(stats):
    # Создание объектов в списке
    if random.randrange(0,100) < settings.invader_chance and len(settings.invaders) < settings.invader_allowed:
        invader = Invader(screen, settings)
        settings.invaders.append(invader)
        if not stats.weapon_active and settings.invader_sf_min < settings.invader_sf_max - 1:
            settings.invader_sf_min += 0.1

def append_ball():
    # Создание объектов в списке
    if random.randrange(0,5000) < settings.ball_chance:
        ball = Ball(screen, settings)
        settings.balls.append(ball)
        settings.ball_chance = settings.ball_chance / settings.ball_chance_reduction

def append_eye():
    # Создание объектов в списке
    if random.randrange(0,5000) < settings.eye_chance:
        eye = Eye(screen, settings)
        settings.eyes.append(eye)
        settings.eye_chance = settings.eye_chance / settings.eye_chance_reduction

def append_ammo():
    # Создание объектов в списке
    if random.randrange(0,1000) < settings.ammo_chance and len(settings.ammos) < settings.ammo_allowed:
        ammo = Ammo(screen, settings, 'weapon')
        settings.ammos.append(ammo)

def append_asteroid():
    # Создание объектов в списке
    if random.randrange(0,1000) < settings.asteroid_chance and len(settings.asteroids) < settings.asteroid_allowed:
        asteroid = Asteroid(screen, settings)
        settings.asteroids.append(asteroid)

def append_star():
    # Создание объектов в списке
    if len(settings.stars) < settings.star_left:
        star = Star(screen, settings)
        settings.stars.append(star)
    for star in settings.drop_stars:
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(star.rect, 0.6, 0.6)):
            settings.drop_stars.remove(star)
            settings.stars.append(star)

def blit_screen(stats):
    # Вывод изображений на экран.
    screen.blitme()
    for star in settings.stars:
        star.blitme()
    for star in settings.drop_stars:
        star.blitme()
    for asteroid in settings.asteroids:
        asteroid.blitme()
    for ammo in settings.ammos:
        ammo.blitme()
    ship.blitme()
    for bullet in settings.bullets:
        bullet.blitme()
    for invader in settings.invaders:
        invader.blitme()
    for small in settings.smalls:
        small.blitme()
    for eye in settings.eyes:
        eye.blitme()
    for ball in settings.balls:
        ball.blitme()
    if not stats.game_active:
        pause.blitme()
        score.blitme()
        record.blitme()
    pygame.display.update()