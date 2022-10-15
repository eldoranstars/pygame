import sys
import pygame
from bullet import Bullet

def check_events():
    # Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship, bullets):
    # Отображение последнего прорисованного экрана.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    bullets.update()
    pygame.display.update()

def check_keyboard(ai_settings, screen, ship, bullets):
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == 1 and ship.rect.centerx < ai_settings.screen_width:
        ship.rect.centerx += ai_settings.ship_speed_factor
    if key[pygame.K_LEFT] == 1 and ship.rect.centerx > 0:
        ship.rect.centerx -= ai_settings.ship_speed_factor
    if key[pygame.K_UP] == 1 and ship.rect.centery > 0:
        ship.rect.centery -= ai_settings.ship_speed_factor
    if key[pygame.K_DOWN] == 1 and ship.rect.centery < ai_settings.screen_height:
        ship.rect.centery += ai_settings.ship_speed_factor
    if key[pygame.K_ESCAPE] == 1:
        sys.exit()
    if key[pygame.K_SPACE] == 1 and len(bullets) < 100:
       new_bullet = Bullet(ai_settings, screen, ship)
       bullets.add(new_bullet)