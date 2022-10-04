import pygame
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(0, 200, 255)
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 720

def screen_text(screen, textString, x, y):
    # pygame provides no way to directly draw text on an existing Surface: 
    # instead you must use Font.render() to create an image (Surface) of the text, then blit this image onto another Surface.
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
        if joystick.get_button(7) == 1:
            game_pause(joystick)

def game_pause(joystick):
    if joystick_count >= 1:
        pygame.draw.rect(screen, player1['color'], (player1['x'], player1['y'], player1['width'], player1['height']))
    if joystick_count > 1:
        pygame.draw.rect(screen, player2['color'], (player2['x'], player2['y'], player2['width'], player2['height']))
    pygame.display.update(screen_text(screen, "BACK to RESUME", SCREEN_WIDTH/2 - 52, 25))
    pygame.display.update(screen_text(screen, "START to QUIT", SCREEN_WIDTH/2 - 45, 40))
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN and joystick.get_button(6) == 1:
                pause = False
            if event.type == pygame.JOYBUTTONDOWN and joystick.get_button(7) == 1:
                pygame.quit()

# ----------- Main Program Loop -----------
pygame.init()
pygame.display.set_caption("My Game")
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
    screen_text(screen, "Number of joysticks : {}".format(joystick_count), SCREEN_WIDTH/2 - 66, 10)

    if joystick_count >= 1:
        joystick1 = pygame.joystick.Joystick(0)
        player_joystick(player1, joystick1)
        pygame.draw.rect(screen, player1['color'], (player1['x'], player1['y'], player1['width'], player1['height']))



    if joystick_count > 1:
        joystick2 = pygame.joystick.Joystick(1)
        player_joystick(player2, joystick2)
        pygame.draw.rect(screen, player2['color'], (player2['x'], player2['y'], player2['width'], player2['height']))

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    pygame.display.update()
    # Limit frames per second.
    # clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang' on exit if running from IDLE.
pygame.quit()