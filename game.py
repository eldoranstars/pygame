import pygame

win_width = 500
win_height = 500

pygame.init()
window = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption("Cubes game")
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
clock = pygame.time.Clock()

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

    pygame.display.update()

run = True
while run:
    # задание интервала времени для цикла
    # pygame.time.delay(50)
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < win_width - width:
        x += speed
        left = False
        right = True
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