import pygame

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

pygame.init()
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((480, 720))
clock = pygame.time.Clock()
# Get ready to print.
textPrint = TextPrint()

# Define player position
left = False
right = False
width = 40
height = 40
speed = 10
x = 50
y = 480 - height 

# ----------- Main Program Loop -----------
done = False
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # # For each joystick:
    # Left Stick:
    #     Left -> Right   - Axis 0
    #     Up   -> Down    - Axis 1
    # Right Stick:
    #     Left -> Right   - Axis 3
    #     Up   -> Down    - Axis 4
    # Left Trigger:
    #     Out -> In       - Axis 2
    # Right Trigger:
    #     Out -> In       - Axis 5
    # Buttons:
    #     A Button        - Button 0
    #     B Button        - Button 1
    #     X Button        - Button 2
    #     Y Button        - Button 3
    #     Left Bumper     - Button 4
    #     Right Bumper    - Button 5
    #     Back Button     - Button 6
    #     Start Button    - Button 7
    #     L. Stick In     - Button 8
    #     R. Stick In     - Button 9
    #     Guide Button    - Button 10
    # Hat/D-pad:
    #     Down -> Up      - get_hat()[1]
    #     Left -> Right   - get_hat()[0]

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()
    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    if joystick_count == 1:
        joystick = pygame.joystick.Joystick(0)
        if joystick.get_axis(0) and joystick.get_axis(0) < -0.2:
            x -= speed
        if joystick.get_axis(0) and joystick.get_axis(0) > 0.2:
            x += speed
        if joystick.get_axis(1) and joystick.get_axis(1) < -0.2:
            y -= speed
        if joystick.get_axis(1) and joystick.get_axis(1) > 0.2:
            y += speed
        if joystick.get_hat(0)[0] == -1:
            x -= speed
        if joystick.get_hat(0)[0] == 1:
            x += speed
        if joystick.get_hat(0)[1] == 1:
            y -= speed
        if joystick.get_hat(0)[1] == -1:
            y += speed

    pygame.draw.rect(screen, (0,150,255), (x, y, width, height))

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
    # Limit frames per second.
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()