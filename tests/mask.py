import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()

class Circle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('circle.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(Player())
circle = pygame.sprite.GroupSingle(Circle())
i = 0

while True:
    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    player.update()
    player.draw(screen)
    circle.draw(screen)

    if pygame.sprite.spritecollide(player.sprite,circle,False, pygame.sprite.collide_mask):
        i += 1
        print('overlap')

    pygame.display.update()
    clock.tick(60)