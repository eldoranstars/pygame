import pygame
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(0, 200, 255)
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 720

def tprint(screen, textString, x, y):
    # https://www.pygame.org/docs/ref/font.html#pygame.font.Font
    # Font(filename|object|pathlib.Path, size) -> Font
    # https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
    # render(text, antialias, color, background=None) -> Surface
    # https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit
    # blit(source, dest, area=None, special_flags=0) -> Rect
    textBitmap = pygame.font.Font(None, 20).render(textString, True, BLACK)
    screen.blit(textBitmap, (x, y))

def player_joystick(player, joystick):
        if joystick.get_axis(0) and joystick.get_axis(0) < -0.2:
            player['x'] -= player['velocity']
        if joystick.get_axis(0) and joystick.get_axis(0) > 0.2:
            player['x'] += player['velocity']
        if joystick.get_axis(1) and joystick.get_axis(1) < -0.2:
            player['y'] -= player['velocity']
        if joystick.get_axis(1) and joystick.get_axis(1) > 0.2:
            player['y'] += player['velocity']
        if joystick.get_hat(0)[0] == -1:
            player['x'] -= player['velocity']
        if joystick.get_hat(0)[0] == 1:
            player['x'] += player['velocity']
        if joystick.get_hat(0)[1] == 1:
            player['y'] -= player['velocity']
        if joystick.get_hat(0)[1] == -1:
            player['y'] += player['velocity']

# ----------- Main Program Loop -----------
pygame.init()
pygame.display.set_caption("My Game")
# https://blog.glyph.im/2022/02/a-better-pygame-mainloop.html
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
player1 = {'width' : 40, 'height' : 40, 'velocity' : 5, 'color' : BLUE, 'x' : 50, 'y' : 50}
player2 = {'width' : 40, 'height' : 40, 'velocity' : 5, 'color' : BLACK, 'x' : 50, 'y' : 50}
run = True
while run:
    #
    # EVENT PROCESSING STEP
    #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False 

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    joystick_count = pygame.joystick.get_count()
    tprint(screen, "Number of joysticks : {}".format(joystick_count), SCREEN_WIDTH/2 - 66, 10)

    if joystick_count >= 1:
        pygame.draw.rect(screen, player1['color'], (player1['x'], player1['y'], player1['width'], player1['height']))
        joystick1 = pygame.joystick.Joystick(0)
        player_joystick(player1, joystick1)


    if joystick_count > 1:
        pygame.draw.rect(screen, player2['color'], (player2['x'], player2['y'], player2['width'], player2['height']))
        joystick2 = pygame.joystick.Joystick(1)
        player_joystick(player2, joystick2)

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # Limit frames per second.
    # clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang' on exit if running from IDLE.
pygame.quit()