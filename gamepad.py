import pygame
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
BLUE = pygame.Color(0, 200, 255)

def tprint(screen, textString):
    x = 10
    y = 10
    line_height = 15
    # This creates a new Surface with the specified text rendered on it. 
    textBitmap = pygame.font.Font(None, 20).render(textString, True, BLACK)
    # pygame provides no way to directly draw text on an existing Surface: 
    # instead you must use Font.render() to create an image (Surface) of the text, then blit this image onto another Surface.
    screen.blit(textBitmap, (x, y))
    y += line_height

# ----------- Main Program Loop -----------
pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((480, 720))
clock = pygame.time.Clock()
# textPrint = TextPrint()
player1 = {'width' : 40, 'height' : 40, 'velocity' : 5, 'color' : BLUE, 'x' : 50, 'y' : 50}
player2 = {'width' : 40, 'height' : 40, 'velocity' : 5, 'color' : BLACK, 'x' : 50, 'y' : 50}
run = True
while run:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            run = False # Flag that we are done so we exit this loop.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False 

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands above this, or they will be erased with this command.
    screen.fill(WHITE)
    # Show count of joysticks
    joystick_count = pygame.joystick.get_count()
    tprint(screen, "Number of joysticks: {}".format(joystick_count))
    tprint(screen, "Numberafaffaff ofafaf joysticks: {}".format(joystick_count))

    if joystick_count >= 1:
        pygame.draw.rect(screen, player1['color'], (player1['x'], player1['y'], player1['width'], player1['height']))
        joystick1 = pygame.joystick.Joystick(0)
        if joystick1.get_axis(0) and joystick1.get_axis(0) < -0.2:
            player1['x'] -= player1['velocity']
        if joystick1.get_axis(0) and joystick1.get_axis(0) > 0.2:
            player1['x'] += player1['velocity']
        if joystick1.get_axis(1) and joystick1.get_axis(1) < -0.2:
            player1['y'] -= player1['velocity']
        if joystick1.get_axis(1) and joystick1.get_axis(1) > 0.2:
            player1['y'] += player1['velocity']
        if joystick1.get_hat(0)[0] == -1:
            player1['x'] -= player1['velocity']
        if joystick1.get_hat(0)[0] == 1:
            player1['x'] += player1['velocity']
        if joystick1.get_hat(0)[1] == 1:
            player1['y'] -= player1['velocity']
        if joystick1.get_hat(0)[1] == -1:
            player1['y'] += player1['velocity']
        if joystick1.get_button(7) == 1:
            event.type = pygame.QUIT


    if joystick_count > 1:
        pygame.draw.rect(screen, player2['color'], (player2['x'], player2['y'], player2['width'], player2['height']))
        joystick2 = pygame.joystick.Joystick(1)
        if joystick2.get_axis(0) and joystick2.get_axis(0) < -0.2:
            player2['x'] -= player2['velocity']
        if joystick2.get_axis(0) and joystick2.get_axis(0) > 0.2:
            player2['x'] += player2['velocity']
        if joystick2.get_axis(1) and joystick2.get_axis(1) < -0.2:
            player2['y'] -= player2['velocity']
        if joystick2.get_axis(1) and joystick2.get_axis(1) > 0.2:
            player2['y'] += player2['velocity']
        if joystick2.get_hat(0)[0] == -1:
            player2['x'] -= player2['velocity']
        if joystick2.get_hat(0)[0] == 1:
            player2['x'] += player2['velocity']
        if joystick2.get_hat(0)[1] == 1:
            player2['y'] -= player2['velocity']
        if joystick2.get_hat(0)[1] == -1:
            player2['y'] += player2['velocity']
        if joystick2.get_button(7) == 1:
            event.type = pygame.QUIT

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # Limit frames per second.
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang' on exit if running from IDLE.
pygame.quit()