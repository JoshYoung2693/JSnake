import pygame, sys, time
from pygame.locals import *

# Initialize pygame
pygame.init()

# Make a window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0, 32)
pygame.display.set_caption('Snake')

# Set up direction variables
DOWN = 'down'
UP = 'up'
LEFT = 'left'
RIGHT = 'right'
FOLLOW = 'follow'

MOVE_SPEED = 1

# Snake length starts at 100 pixels
length = 300

# Count (for list purposes)
count = 0

# Colors
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0,0,0)

# Make sprite dictionaries    
# the snake is 50*50                                   
head = {'rect': pygame.Rect(300,80,20,20), 'color': RED, 'dir': DOWN}
tail = {'rect': pygame.Rect(300,80,20,20), 'color': BLACK, 'dir': FOLLOW}
sprite_list = [head, tail]
xposition = []
yposition = []

# Main game loop
while True:
    # If they click the 'x' in the corner
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                head['dir'] = LEFT
            if event.key == K_RIGHT or event.key == K_d:
                head['dir'] = RIGHT
            if event.key == K_UP or event.key == K_w:
                head['dir'] = UP
            if event.key == K_DOWN or event.key == K_s:
                head['dir'] = DOWN



    
    # Everyone clears the screen here, but not me
    # No clear


    # Move the head and tail
    for sprite in sprite_list:
        if sprite['dir'] == DOWN:
            sprite['rect'].top += MOVE_SPEED
        if sprite['dir'] == UP:
            sprite['rect'].top -= MOVE_SPEED
        if sprite['dir'] == LEFT:
            sprite['rect'].left -= MOVE_SPEED
        if sprite['dir'] == RIGHT:
            sprite['rect'].left += MOVE_SPEED
        if sprite['dir'] == FOLLOW and count > (length):
            sprite['rect'].x = xposition[(count-length)]
            sprite['rect'].y = yposition[(count-length)]
        pygame.draw.rect(windowSurface, sprite['color'], sprite['rect'])

    # Add head locations to the list
    xposition.append(head['rect'].x)
    yposition.append(head['rect'].y)
    
    # Keyboard input
    key = pygame.key.get_pressed()
    if key[K_a]:
        head['dir'] == LEFT
    if key[K_d]:
        head['dir'] == RIGHT
    if key[K_w]:
        head['dir'] == UP
    if key[K_s]:
        head['dir'] == DOWN
    # Draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)

    # Count
    count+=1
    
