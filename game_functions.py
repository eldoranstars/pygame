import sys
import pygame

def check_events():
    # Отслеживание событий клавиатуры и мыши.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # Отображение последнего прорисованного экрана.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.update()

def check_keyboard(ship, ai_settings):
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] == 1 and ship.rect.centerx < ai_settings.screen_width:
        ship.rect.centerx += ai_settings.ship_speed_factor
    if key[pygame.K_LEFT] == 1 and ship.rect.centerx > 0:
        ship.rect.centerx -= ai_settings.ship_speed_factor
    if key[pygame.K_UP] == 1 and ship.rect.centery > 0:
        ship.rect.centery -= ai_settings.ship_speed_factor
    if key[pygame.K_DOWN] == 1 and ship.rect.centery < ai_settings.screen_height:
        ship.rect.centery += ai_settings.ship_speed_factor