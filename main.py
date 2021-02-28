import pygame
from random import randint
from copy import deepcopy

# Resolution, size of a single tile and amount of rows and cols
RES = WIDTH, HEIGHT = 1200, 600
TILE = 20
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 6

# Initialize pygame
pygame.init()
pygame.display.set_caption('Simple Game of Life')
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

# Create the current field and fill it with random nums 0 or 1
# and create the next field and fill it with 0's
next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0,1) for i in range(W)] for j in range(H)]

# Function to check the numbers of live cells around the current cell
# it checks the eight sell around and return 0 of too many or 1 if not
def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

# Pygame main loop
while True:

    sc.fill(pygame.Color('#2C3A47'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Draw a grid
    [pygame.draw.line(sc, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(sc, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    # Draw life
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pygame.draw.rect(sc, pygame.Color('#1B9CFC'), (x * TILE + 2 , y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)
    
    current_field = deepcopy(next_field)

    pygame.display.flip()
    clock.tick(FPS)