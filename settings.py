import pygame

class Settings():
    def __init__(self):
        # Параметры игры
        self.star_limit = 3
        self.record = 0
        self.boss_score = 4444
        self.ship_sf = 4
        self.star_speedf = self.ship_sf - 1
        # Параметры экрана
        self.screen_width = 480
        self.screen_height = 720
        self.screen_color = (100, 100, 100)
        # Параметры пули
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_sf = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 1
        self.reload_bullet_time_limit = 900
        # Параметры изображений
        self.screen_bg = pygame.image.load('images/space.png')
        self.star_surface = pygame.image.load('images/star.png')
        self.ship_surface = pygame.image.load('images/ship.png')
        self.weapon_ship_surface = pygame.image.load('images/weapon-ship.png')
        self.shield_ship_surface = pygame.image.load('images/shield-ship.png')
        self.alien_ball_surface = pygame.image.load('images/alien-ball.png')
        self.invader_surface = pygame.image.load('images/invader.png')
        self.small_surface = pygame.image.load('images/small.png')
        self.tusk_surface = pygame.image.load('images/tusk.png')
        self.ball_surface = pygame.image.load('images/ball.png')
        self.boss_surface = pygame.image.load('images/boss.png')
        self.boss75_surface = pygame.image.load('images/boss75.png')
        self.boss50_surface = pygame.image.load('images/boss50.png')
        self.boss25_surface = pygame.image.load('images/boss25.png')
        self.eye_surface = pygame.image.load('images/eye.png')
        self.ammo_surface = pygame.image.load('images/laser-gun.png')
        self.alien_surface = pygame.image.load('images/alien.png')
        self.brain_surface = pygame.image.load('images/brain.png')
        self.shield_surface = pygame.image.load('images/space-gun.png')
        self.asteroid_pink = pygame.image.load('images/asteroid-pink.png')
        self.asteroid_grey = pygame.image.load('images/asteroid-grey.png')
        self.asteroid_blue = pygame.image.load('images/asteroid-blue.png')
        self.screen_surface = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.SCALED, vsync=1)
        self.bullet_surface = pygame.Surface((self.bullet_width, self.bullet_height))
        # Параметры чужих
        self.boss_sf = self.ship_sf - 2
        self.tusk_sf = 5
        self.small_sf_min = 1
        self.small_sf_max = 8
        self.invader_chance = 10
        self.invader_allowed = 15
        self.ball_sf_min = 2
        self.ball_sf_max = 5
        self.ball_chance_reduction = 2
        self.eye_sf_min = 2
        self.eye_sf_max = 5
        self.eye_chance_reduction = 2
        self.asteroid_sf = 4
        self.asteroid_surfaces = [self.asteroid_pink, self.asteroid_grey, self.asteroid_blue]
        # Параметры аммуниции
        self.ammo_sf_min = 1
        self.ammo_sf_max = 2
        self.ammo_chance = 1
        self.ammo_allowed = 1
        # Титры
        self.messages = ['Producer:', 'eldoranstars', '', 'Quality Assurance:', 'eldoranstars', '', 'Gameplay Developer:', 'eldoranstars', '', \
            'Tools Developer:', 'eldoranstars', '', 'UI Developer:', 'eldoranstars', '', 'Audio Developer:', 'eldoranstars', '', 'Lead DevOps:', 'eldoranstars']
        # Динамические параметры игры
        self.new_game()

    def player_hit(self):
        # Сбросить параметры при столкновении
        self.smalls.clear()
        self.tusks.clear()
        self.invaders.clear()
        self.eyes.clear()
        self.balls.clear()
        self.bullets.clear()
        self.asteroids.clear()
        self.ammos.clear()
        self.invader_sf_min = 1
        self.invader_sf_max = 9
        self.eye_chance = 8
        self.ball_chance = 16
        self.bullet_left = self.bullet_limit - self.bullet_limit

    def new_game(self):
        # Сбросить параметры для новой игры
        self.final_text = []
        self.smalls = []
        self.tusks = []
        self.invaders = []
        self.eyes = []
        self.balls = []
        self.bullets = []
        self.asteroids = []
        self.ammos = []
        self.stars = []
        self.drop_stars = []
        self.bosses = []
        self.star_left = self.star_limit
        self.score = 0
        self.first_line = 0
        self.reload_power_time = 3300
        self.reload_bullet = False
        self.reload_bullet_time = self.reload_bullet_time_limit
        self.player_hit()

    def collision(self, rect, wm, hm):
        # Получаем дополнительный прямоугольник для обработки коллизий.
        collision = pygame.Rect(rect.center, (rect.width * wm, rect.height * hm))
        collision.center = rect.center
        return collision

    def mask_from_surface(self, object):
        # Получаем пиксельную маску для обработки коллизий.
        return pygame.mask.from_surface(object)

    def overlap(self, small_obj, big_obj, area = 0.05):
        # Вычисляем пересечение масок для обработки коллизий.
        return small_obj.mask.overlap_area(big_obj.mask, (big_obj.rect.left - small_obj.rect.left, big_obj.rect.top - small_obj.rect.top)) > small_obj.mask.count() * area