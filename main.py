import pygame


# initialize pygame, like starting the engine
pygame.init()

# set up the screen
screen = pygame.display.set_mode((800, 600))


# adding a title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('pictures/spaceship.png')
pygame.display.set_icon(icon)

#adding a player
playerIMG = pygame.image.load('pictures/spaceship.png')
playerIMG = pygame.transform.scale(playerIMG, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
#making a function so that this loads on our screen
def player(x, y):
    screen.blit(playerIMG, (x, y))

# Game loop so that it runs

running = True
while running:
    screen.fill((49, 49, 49)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # if function for if we have a keystroke (which in itself is an event) is pressed
        if event.type == pygame.KEYDOWN:
            #checking if its the a (left)
            if event.key == pygame.K_a:
                playerX_change = -0.1
            if event.key == pygame.K_d:
                playerX_change = 0.1
            if event.key == pygame.K_w:
                playerY_change = -0.1
            if event.key == pygame.K_s:
                playerY_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
    
    playerX+=playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    playerY+=playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
        
    player(playerX, playerY)
    
    pygame.display.update()
        