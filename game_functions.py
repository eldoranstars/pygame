from re import S
import sys
import pygame
import random
from time import sleep
from invader import Invader
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
screen = Screen(settings)
ship = Ship(screen, settings)
star = Star(screen, settings)
pause = Text(screen, "PAUSE", screen.rect.centerx, screen.rect.centery - 40)
score = Text(screen, "BOSS ARRIVES: {:,}", screen.rect.centerx, screen.rect.centery)
record = Text(screen, "PREVIOS RECORD: {:,}", screen.rect.centerx, screen.rect.centery - 20)
bullet_left_text = Text(screen, "{:,}", ship.rect.centerx, ship.rect.centery, settings.bullet_left)

def check_events(stats):
    # Отслеживание событий клавиатуры и мыши.
    if stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                stats.game_active = False
    if not stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                stats.game_active = True

def update_player():
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
        bullet_left_text.update_text(settings.bullet_left)
        bullet = Bullet(screen, settings, ship)
        settings.bullets.append(bullet)

def reload_bullets():
    # Флаг перезарядки и фиксация времени начала
    if not settings.reload_bullet and settings.bullet_left == 0:
        settings.reload_bullet = True
        settings.last_bullet_time = pygame.time.get_ticks()
    # Снятие флага перезарядки на основе дельты времени и пополнение боезапаса
    if settings.reload_bullet and pygame.time.get_ticks() - settings.last_bullet_time > settings.reload_bullet_time:
        settings.reload_bullet = False
        settings.bullet_left = settings.bullet_limit
        bullet_left_text.update_text(settings.bullet_left)

def collision(rect, wm, hm):
    # Получаем дополнительный прямоугольник для обработки коллизий.
    collision = pygame.Rect(rect.center, (rect.width * wm, rect.height * hm))
    collision.center = rect.center
    return collision

def collision_test(object, wm, hm):
    # Вывод коллизий на экран.
    screen.surface.blit(pygame.Surface((collision(object.rect, wm, hm).width,collision(object.rect, wm, hm).height)), collision(object.rect, wm, hm))

def update_drop_stars():
    # Обновить расположение объектов на экране.
    for star in settings.drop_stars:
        star.update()
        if not screen.rect.colliderect(star.rect):
            settings.drop_stars.remove(star)

def update_bullets():
    # Обновить расположение объектов на экране.
    for bullet in settings.bullets:
        bullet.update()
        if not screen.rect.colliderect(bullet.rect):
            settings.bullets.remove(bullet)
        for invader in settings.invaders:
            if invader.rect.contains(bullet.rect):
                settings.invaders.remove(invader)
                settings.score += 3
                score.update_text(settings.boss_score - settings.score)
                try:
                    settings.bullets.remove(bullet)
                # если пуля попала сразу в оба объекта
                except: ValueError
        for ball in settings.balls:
            if ball.rect.contains(bullet.rect):
                ball.life_left -= 1
                if ball.life_left == 0:
                    ammo = Ammo(screen, settings, 'shield')
                    ammo.rect.center = ball.rect.center
                    settings.ammos.append(ammo)
                    settings.balls.remove(ball)
                    settings.score += 15
                    score.update_text(settings.boss_score - settings.score)
                    settings.ball_chance = settings.ball_chance * settings.ball_chance_reduction
                try:
                    settings.bullets.remove(bullet)
                # если пуля попала сразу в оба объекта
                except: ValueError

def update_asteroids():
    # Обновить расположение объектов на экране.
    for asteroid in settings.asteroids:
        asteroid.update()
        if not screen.rect.colliderect(asteroid.rect):
            settings.asteroids.remove(asteroid)
        # if collision(asteroid.rect, 0.8, 0.8).collidepoint(ship.rect.midtop):
        #     asteroid.move_down = False
        # if collision(asteroid.rect, 0.8, 0.8).collidepoint(ship.rect.midleft):
        #     asteroid.move_left = True
        #     asteroid.move_right = False
        #     asteroid.move_down = False
        # if collision(asteroid.rect, 0.8, 0.8).collidepoint(ship.rect.midright):
        #     asteroid.move_left = False
        #     asteroid.move_right = True
        #     asteroid.move_down = False
        # for invader in settings.invaders:
        #     if collision(asteroid.rect, 0.8, 0.8).colliderect(collision(invader.rect, 0.8, 0.6)):
        #         settings.invaders.remove(invader)
        #         settings.score += 3
        #         score.update_text(settings.boss_score - settings.score)
        # for ball in settings.balls:
        #     if collision(asteroid.rect, 0.8, 0.8).colliderect(collision(ball.rect, 0.8, 0.8)):
        #         settings.balls.remove(ball)
        #         settings.score += 15
        #         score.update_text(settings.boss_score - settings.score)

def reset_after_collision(stats):
    # Обновить счет и экран после коллизии
    sleep(0.5)
    if not stats.shield_active:
        stats.weapon_active = False
    stats.shield_active = False
    ship.surface = settings.ship_surface
    if len(settings.stars) > 0:
        settings.star_left -= 1
        settings.player_hit()
        bullet_left_text.update_text(settings.bullet_left)
        drop_star = random.choice(settings.stars)
        settings.stars.remove(drop_star)
        settings.drop_stars.append(drop_star)
    else:
        stats.game_active = False
        if settings.score > settings.record:
            settings.record = settings.score
        record.update_text(settings.record)
        ship.rect.centerx = screen.rect.centerx
        ship.rect.bottom = screen.rect.bottom
        settings.new_game()

def update_invaders(stats):
    # Обновить расположение объектов на экране.
    for invader in settings.invaders:
        invader.update()
        if not screen.rect.colliderect(invader.rect):
            settings.invaders.remove(invader)
            settings.score += 1
            score.update_text(settings.boss_score - settings.score)
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(invader.rect, 0.8, 0.6)):
            reset_after_collision(stats)

def update_balls(stats):
    # Обновить расположение объектов на экране.
    for ball in settings.balls:
        ball.update()
        if not screen.rect.collidepoint(ball.rect.midright):
            ball.move_left = False
            ball.move_right = True
        if not screen.rect.collidepoint(ball.rect.midleft):
            ball.move_right = False
            ball.move_left = True
        if not screen.rect.collidepoint(ball.rect.midbottom):
            ball.move_down = False
        if not screen.rect.collidepoint(ball.rect.midtop) and ball.surface == settings.ball_surface:
            ball.move_down = True
        if not screen.rect.colliderect(ball.rect):
            settings.balls.remove(ball)
            settings.score += 15
            settings.ball_chance = settings.ball_chance / settings.ball_chance_reduction
        if not stats.shield_active:
            if collision(ship.rect, 0.6, 0.9).colliderect(collision(ball.rect, 0.8, 0.8)):
                reset_after_collision(stats)
                score.update_text(settings.boss_score - settings.score)
        if stats.shield_active:
            if collision(ball.rect, 0.8, 0.8).collidepoint(ship.rect.midtop):
                ball.move_down = False
                ball.surface = settings.alien_ball_surface
            if collision(ball.rect, 0.8, 0.8).collidepoint(ship.rect.midright):
                ball.move_left = True
                ball.move_right = False
                ball.move_down = False
                ball.surface = settings.alien_ball_surface
            if collision(ball.rect, 0.8, 0.8).collidepoint(ship.rect.midleft):
                ball.move_left = False
                ball.move_right = True
                ball.move_down = False
                ball.surface = settings.alien_ball_surface
        if ball.surface == settings.alien_ball_surface:
            for invader in settings.invaders:
                if collision(ball.rect, 0.8, 0.8).colliderect(collision(invader.rect, 0.8, 0.6)):
                    settings.invaders.remove(invader)
                    settings.score += 3
                    score.update_text(settings.boss_score - settings.score)

def update_ammos(stats):
    # Обновить расположение объектов на экране.
    for ammo in settings.ammos:
        ammo.update()
        if not screen.rect.colliderect(ammo.rect):
            settings.ammos.remove(ammo)
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(ammo.rect, 0.6, 0.6)):
            settings.ammos.remove(ammo)
            if ammo.type == 'weapon':
                stats.weapon_active = True
                settings.invader_sf_min = 1
                settings.invader_sf_max = 8
                settings.bullet_limit = 1
                settings.bullet_left = settings.bullet_limit
                bullet_left_text.update_text(settings.bullet_left)
            if ammo.type == 'shield':
                stats.shield_active = True
                ship.surface = settings.shield_ship_surface

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
    bullet_left_text.blitme()
    for bullet in settings.bullets:
        bullet.blitme()
    for invader in settings.invaders:
        invader.blitme()
    for ball in settings.balls:
        ball.blitme()
    if not stats.game_active:
        pause.blitme()
        score.blitme()
        record.blitme()
    pygame.display.update()