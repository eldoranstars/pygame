import pygame

win_width = 500
win_height = 500

pygame.init()
pygame.display.set_caption("Cubes game")
window = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

# sprites
walkRight = [pygame.image.load('sprites/pygame_right_1.png'), pygame.image.load('sprites/pygame_right_2.png'), pygame.image.load('sprites/pygame_right_3.png'), pygame.image.load('sprites/pygame_right_4.png'), pygame.image.load('sprites/pygame_right_5.png'), pygame.image.load('sprites/pygame_right_6.png')]
walkLeft = [pygame.image.load('sprites/pygame_left_1.png'), pygame.image.load('sprites/pygame_left_2.png'), pygame.image.load('sprites/pygame_left_3.png'), pygame.image.load('sprites/pygame_left_4.png'), pygame.image.load('sprites/pygame_left_5.png'), pygame.image.load('sprites/pygame_left_6.png')]
playerStand = pygame.image.load('sprites/pygame_idle.png')
bg = pygame.image.load('sprites/pygame_bg.jpg')

width = 60
height = 71
speed = 10
x = 50
y = win_height - height

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = "right"

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.y), self.radius)

def drawWindow():
    global animCount
    window.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        window.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        window.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        window.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < win_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < win_width - width:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()

pygame.quit()