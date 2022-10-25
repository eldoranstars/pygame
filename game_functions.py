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

settings = Settings()
screen = Screen(settings)
ship = Ship(screen, settings)
star = Star(screen, settings)
start = Text(screen, "START", screen.rect.centerx, screen.rect.centery - 40)
score = Text(screen, "SCORE: {:,}", screen.rect.centerx, screen.rect.centery)
record = Text(screen, "RECORD: {:,}", screen.rect.centerx, screen.rect.centery - 20)

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

def collision(rect, wm, hm):
    # Получаем дополнительный прямоугольник для обработки коллизий.
    collision = pygame.Rect(rect.center, (rect.width * wm, rect.height * hm))
    collision.center = rect.center
    return collision

def collision_test(object, wm, hm):
    # Вывод коллизий на экран.
    screen.surface.blit(pygame.Surface((collision(object.rect, wm, hm).width,collision(object.rect, wm, hm).height)), collision(object.rect, wm, hm))

def update_removed_stars():
    # Вывод изображений на экран.
    for star in settings.removed_stars:
        star.update()
        if not screen.rect.colliderect(star.rect):
            settings.removed_stars.remove(star)

def update_bullets():
    # Вывод изображений на экран.
    for bullet in settings.bullets:
        bullet.update()
        for alien in settings.aliens:
            if alien.rect.contains(bullet.rect):
                settings.aliens.remove(alien)
                settings.score += 1
                score.update_text(settings.score)
                record.update_text(settings.record)
                try:
                    settings.bullets.remove(bullet)
                # если пуля попала сразу в оба объекта
                except ValueError:
                    print('double kill!')
        if bullet.rect.bottom < (bullet.start_position - settings.screen_height):
            settings.bullets.remove(bullet)

def update_aliens(stats):
    # Вывод изображений на экран.
    for alien in settings.aliens:
        alien.update()
        if not screen.rect.colliderect(alien.rect):
            settings.aliens.remove(alien)
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(alien.rect, 0.8, 0.6)):
            sleep(1)
            if settings.star_left > 0:
                settings.star_left -= 1
                removed_star = settings.stars.pop(-1)
                settings.removed_stars.append(removed_star)
                ship.rect.centerx = screen.rect.centerx
                ship.rect.bottom = screen.rect.bottom
                settings.aliens.clear()
                settings.bullets.clear()
            else:
                stats.game_active = False
                if settings.score > settings.record:
                    settings.record = settings.score
                settings.reset_settings()
                score.update_text(settings.score)
                record.update_text(settings.record)
                ship.rect.centerx = screen.rect.centerx
                ship.rect.bottom = screen.rect.bottom
                settings.aliens.clear()
                settings.bullets.clear()

def update_screen(stats):
    # Вывод изображений на экран.
    screen.blitme()
    for star in settings.stars:
        star.blitme()
    for star in settings.removed_stars:
        star.blitme()
    ship.blitme()
    for bullet in settings.bullets:
        bullet.blitme()
    for alien in settings.aliens:
        alien.blitme()
    if not stats.game_active:
        start.blitme()
        score.blitme()
        record.blitme()
    pygame.display.update()

def update_player():
    # Отслеживание нажатий клавиатуры и мыши.
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == 1 and ship.rect.right < settings.screen_width:
        ship.rect.centerx += settings.ship_speed_factor
    if key[pygame.K_LEFT] == 1 and ship.rect.left > 0:
        ship.rect.centerx -= settings.ship_speed_factor
    if key[pygame.K_UP] == 1 and ship.rect.top > 0:
        ship.rect.centery -= settings.ship_speed_factor
    if key[pygame.K_DOWN] == 1 and ship.rect.bottom < settings.screen_height:
        ship.rect.centery += settings.ship_speed_factor
    if key[pygame.K_SPACE] == 1 and len(settings.bullets) < settings.bullet_allowed:
        bullet = Bullet(screen, settings, ship)
        settings.bullets.append(bullet)

def update_fleet():
    # Создание объектов в списке
    if random.randrange(1,101) < settings.alien_chance and len(settings.aliens) < settings.alien_allowed:
        alien = Alien(screen, settings)
        settings.aliens.append(alien)

def update_stars():
    # Создание объектов в списке
    if len(settings.stars) < settings.star_left:
        star = Star(screen, settings)
        settings.stars.append(star)
    for star in settings.removed_stars:
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(star.rect, 0.6, 0.6)):
            settings.star_left += 1
            settings.removed_stars.remove(star)
            settings.stars.append(star)