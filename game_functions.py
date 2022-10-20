import sys
import pygame
import random
from bullet import Bullet
from alien import Alien
from text import Text

def check_events():
    # Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def collision(rect, wm, hm):
    # Получаем дополнительный прямоугольник для обработки коллизий.
    collision = pygame.Rect(rect.center, (rect.width * wm, rect.height * hm))
    collision.center = rect.center
    return collision

def collision_test(screen, object, wm, hm):
    # Вывод коллизий на экран.
    screen.surface.blit(pygame.Surface((collision(object.rect, wm, hm).width,collision(object.rect, wm, hm).height)), collision(object.rect, wm, hm))

def update_bullets(settings, bullets):
    # Вывод изображений на экран.
    for bullet in bullets:
        bullet.update()
        if bullet.rect.bottom < (bullet.start_position - settings.screen_height):
            bullets.remove(bullet)

def update_aliens(screen, bullets, aliens):
    # Вывод изображений на экран.
    for alien in aliens:
        alien.update()
        if not screen.rect.colliderect(alien.rect):
            aliens.remove(alien)
        for bullet in bullets:
            if alien.rect.contains(bullet.rect):
                aliens.remove(alien)
                bullets.remove(bullet)

def update_screen(settings, screen, ship, bullets, aliens):
    # Вывод изображений на экран.
    screen.blitme()
    ship.blitme()
    for bullet in bullets:
        bullet.blitme()
    for alien in aliens:
        alien.blitme()
        if collision(ship.rect, 0.6, 0.9).colliderect(collision(alien.rect, 0.8, 0.8)):
            Text(settings, screen, 'Collide with alien').blitme()
    pygame.display.update()

def update_player(settings, screen, ship, bullets):
    # Отслеживание нажатий клавиатуры и мыши.
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] == 1:
        sys.exit()
    if key[pygame.K_RIGHT] == 1 and ship.rect.right < settings.screen_width:
        ship.rect.centerx += settings.ship_speed_factor
    if key[pygame.K_LEFT] == 1 and ship.rect.left > 0:
        ship.rect.centerx -= settings.ship_speed_factor
    if key[pygame.K_UP] == 1 and ship.rect.top > 0:
        ship.rect.centery -= settings.ship_speed_factor
    if key[pygame.K_DOWN] == 1 and ship.rect.bottom < settings.screen_height:
        ship.rect.centery += settings.ship_speed_factor
    if key[pygame.K_SPACE] == 1 and len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.append(new_bullet)

def update_fleet(settings, screen, aliens):
    # Создание противника и размещение его в ряду.
    if random.randrange(1,100) > 57 and len(aliens) < settings.aliens_allowed:
        alien = Alien(settings, screen)
        aliens.append(alien)