import pygame
import os
import time
import random
pygame.font.init()

#LOAD IMAGES
WIDTH, HEIGHT = 1000, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

PLAYER=pygame.transform.scale(pygame.image.load('assets/spaceship.png'), (64, 64))
BLACK_INV=pygame.image.load('assets/black_invader.png')
PURUPLE_INV=pygame.image.load('assets/purple_invader.png')
BULLET=pygame.image.load('assets/bullet_re.png')
BG = pygame.transform.scale(pygame.image.load('assets/spaceBG.jpg'), (WIDTH, HEIGHT))
pygame.init()

class Ship:
    def __init__(self, x, y, health=100):
        self.x=x
        self.y=y
        self.health=health
        self.laser_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    def draw(self, window):
        window.blit(PLAYER, (self.x, self.y)) #what about the self.img stuff?

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = PLAYER
        self.bullet_img = BULLET
        self.mask = pyga
def main():
    FPS = 60
    run = True
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("arial", 50)

    player_vel = 5

    ship = Ship(300, 650)

    def redraw_window():
        WIN.blit(BG, (0,0))
        #draw text
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        WIN.blit(lives_label,(10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width()-10, 10))
        ship.draw(WIN)
        pygame.display.update()
        

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x + player_vel > 0: #left
            ship.x -= player_vel
        if keys[pygame.K_d] and ship.x + player_vel + 45 < WIDTH: #right
            ship.x += player_vel
        if keys[pygame.K_w] and ship.y + player_vel  > 0: #up
            ship.y -= player_vel
        if keys[pygame.K_s] and ship.y + player_vel + 45 < HEIGHT: #down
            ship.y += player_vel
            


main()
