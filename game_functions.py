import sys
import pygame
import random
from time import sleep
from bullet import Bullet
from alien import Alien
from settings import Settings
from screen import Screen
from ship import Ship
from text import Text

aliens = []
bullets = []
settings = Settings()
screen = Screen(settings)
ship = Ship(screen)
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

def update_bullets():
    # Вывод изображений на экран.
    for bullet in bullets:
        bullet.update()
        for alien in aliens:
            if alien.rect.contains(bullet.rect):
                aliens.remove(alien)
                settings.score += 1
                score.update_text(settings.score)
                record.update_text(settings.record)
                try:
                    bullets.remove(bullet)
                # если пуля попала сразу в оба объекта
                except ValueError:
                    print('double kill!')
        if bullet.rect.bottom < (bullet.start_position - settings.screen_height):
            bullets.remove(bullet)

def update_aliens(stats):
    # Вывод изображений на экран.
    for alien in aliens:
        alien.update()
        if not screen.rect.colliderect(alien.rect):
            aliens.remove(alien)
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(alien.rect, 0.8, 0.6)):
            sleep(1)
            if settings.ships_left > 0:
                settings.ships_left -= 1
                ship.rect.centerx = screen.rect.centerx
                ship.rect.bottom = screen.rect.bottom
                aliens.clear()
                bullets.clear()
            else:
                stats.game_active = False
                if settings.score > settings.record:
                    settings.record = settings.score
                settings.reset_settings()
                score.update_text(settings.score)
                record.update_text(settings.record)
                ship.rect.centerx = screen.rect.centerx
                ship.rect.bottom = screen.rect.bottom
                aliens.clear()
                bullets.clear()

def update_screen(stats):
    # Вывод изображений на экран.
    screen.blitme()
    ship.blitme()
    for bullet in bullets:
        bullet.blitme()
    for alien in aliens:
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
    if key[pygame.K_SPACE] == 1 and len(bullets) < settings.bullets_allowed:
        bullet = Bullet(settings, screen, ship)
        bullets.append(bullet)

def update_fleet():
    # Создание противника и размещение его в ряду.
    if random.randrange(1,101) < settings.alien_chance and len(aliens) < settings.alien_allowed:
        alien = Alien(settings, screen)
        aliens.append(alien)