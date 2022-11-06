import pygame, sys

class Player():
    def __init__(self):
        # super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = pygame.mouse.get_pos()

class Circle():
    def __init__(self):
        # super().__init__()
        self.image = pygame.image.load('circle.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400,400)
        self.mask = pygame.mask.from_surface(self.image)

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
player = Player()
circle = Circle()
# player = pygame.sprite.GroupSingle(Player())
# circle = pygame.sprite.GroupSingle(Circle())
i = 0

while True:
    for event in pygame.event.get():
         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    screen.fill('white')

    player.update()
    screen.blit(player.image, player.rect)
    screen.blit(circle.image, circle.rect)
    # screen.blit(player.mask_surface, player.rect)
    # screen.blit(circle.mask_surface, circle.rect)
    # player.draw(screen)
    # circle.draw(screen)

    offset_x = circle.rect.left - player.rect.left
    offset_y = circle.rect.top - player.rect.top
    if player.mask.overlap(circle.mask, (offset_x, offset_y)):
        i += 1
        print('overlap' + str(i))

    pygame.display.update()
    clock.tick(60)