import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events():
    # Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, ship, bullets, aliens):
    # Вывод изображений на экран.
    screen.blitme()
    ship.blitme()
    for bullet in bullets:
        bullet.blitme()
        bullet.update()
        if bullet.rect.bottom < (bullet.start_position - settings.screen_height):
            bullets.remove(bullet)
    for alien in aliens:
        alien.blitme()
        alien.update()
        if alien.rect.right < 0 or alien.rect.left > settings.screen_width or alien.rect.top > settings.screen_height:
            aliens.remove(alien)
        for bullet in bullets:
            # if alien.rect.collidepoint(bullet.rect.centerx, bullet.rect.centery):
            if alien.rect.contains(bullet.rect):
                aliens.remove(alien)
                bullets.remove(bullet)
    pygame.display.update()

def check_keyboard(settings, screen, ship, bullets):
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

def create_fleet(settings, screen, aliens):
    # Создание пришельца и размещение его в ряду.
    for alien in range(settings.aliens_allowed):
        alien = Alien(settings, screen)
        aliens.append(alien)