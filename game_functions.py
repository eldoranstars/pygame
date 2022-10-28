from re import S
import sys
import pygame
import random
from time import sleep
from alien import Alien
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
start = Text(screen, "START", screen.rect.centerx, screen.rect.centery - 40)
score = Text(screen, "SCORE: {:,}", screen.rect.centerx, screen.rect.centery)
record = Text(screen, "RECORD: {:,}", screen.rect.centerx, screen.rect.centery - 20)
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
    # Перезарядка
    if settings.bullet_left == 0 and not settings.reload_bullet:
        settings.reload_bullet = True
        settings.last_bullet_time = pygame.time.get_ticks()
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

def update_removed_stars():
    # Обновить расположение объектов на экране.
    for star in settings.removed_stars:
        star.update()
        if not screen.rect.colliderect(star.rect):
            settings.removed_stars.remove(star)

def update_bullets():
    # Обновить расположение объектов на экране.
    for bullet in settings.bullets:
        bullet.update()
        if bullet.rect.bottom < (bullet.start_position - settings.screen_height):
            settings.bullets.remove(bullet)
        for alien in settings.aliens:
            if alien.rect.contains(bullet.rect):
                settings.aliens.remove(alien)
                settings.score += 1
                score.update_text(settings.score)
                try:
                    settings.bullets.remove(bullet)
                # если пуля попала сразу в оба объекта
                except ValueError:
                    print('double kill!')

def update_asteroids():
    # Обновить расположение объектов на экране.
    for asteroid in settings.asteroids:
        asteroid.update()
        if not screen.rect.colliderect(asteroid.rect):
            settings.asteroids.remove(asteroid)
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
        for alien in settings.aliens:
            if collision(asteroid.rect, 0.8, 0.8).colliderect(collision(alien.rect, 0.8, 0.6)):
                settings.aliens.remove(alien)
                settings.score += 1
                score.update_text(settings.score)

def update_aliens(stats):
    # Обновить расположение объектов на экране.
    for alien in settings.aliens:
        alien.update()
        if not screen.rect.colliderect(alien.rect):
            settings.aliens.remove(alien)
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(alien.rect, 0.8, 0.6)):
            sleep(1)
            stats.weapon_active = False
            settings.aliens.clear()
            settings.bullets.clear()
            settings.asteroids.clear()
            settings.ammos.clear()
            settings.bullet_left = 0
            bullet_left_text.update_text(settings.bullet_left)
            if settings.star_left > 0:
                settings.star_left -= 1
                removed_star = random.choice(settings.stars)
                settings.stars.remove(removed_star)
                settings.removed_stars.append(removed_star)
            else:
                stats.game_active = False
                if settings.score > settings.record:
                    settings.record = settings.score
                settings.reset_settings()
                score.update_text(settings.score)
                record.update_text(settings.record)
                ship.rect.centerx = screen.rect.centerx
                ship.rect.bottom = screen.rect.bottom

def update_ammos(stats):
    # Обновить расположение объектов на экране.
    for ammo in settings.ammos:
        ammo.update()
        if not screen.rect.colliderect(ammo.rect):
            settings.ammos.remove(ammo)
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(ammo.rect, 0.6, 0.6)):
            stats.weapon_active = True
            settings.bullet_limit = 1
            settings.bullet_left = settings.bullet_limit
            bullet_left_text.update_text(settings.bullet_left)
            settings.ammos.clear()

def append_alien():
    # Создание объектов в списке
    if random.randrange(0,100) < settings.alien_chance and len(settings.aliens) < settings.alien_allowed:
        alien = Alien(screen, settings)
        settings.aliens.append(alien)

def append_ammo():
    # Создание объектов в списке
    if random.randrange(0,1000) < settings.ammo_chance and len(settings.ammos) < settings.ammo_allowed:
        ammo = Ammo(screen, settings)
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
    for star in settings.removed_stars:
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(star.rect, 0.6, 0.6)):
            settings.star_left += 1
            settings.removed_stars.remove(star)
            settings.stars.append(star)

def blit_screen(stats):
    # Вывод изображений на экран.
    screen.blitme()
    for star in settings.stars:
        star.blitme()
    for star in settings.removed_stars:
        star.blitme()
    for asteroid in settings.asteroids:
        asteroid.blitme()
    for ammo in settings.ammos:
        ammo.blitme()
    ship.blitme()
    bullet_left_text.blitme()
    for bullet in settings.bullets:
        bullet.blitme()
    for alien in settings.aliens:
        alien.blitme()
    if not stats.game_active:
        start.blitme()
        score.blitme()
        record.blitme()
    pygame.display.update()