import pygame
import os
import time
import random

#LOAD IMAGES
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

PLAYER=pygame.image.load('assets/spaceship.png')
BLACK_INV=pygame.image.load('assets/black_invader.png')
PURUPLE_INV=pygame.image.load('assets/purple_invader.png')
BULLET=pygame.image.load('assets/bullet_re.png')
BG =
pygame.init()

def main():
    FPS = 60
    run = True
    clock = pygame.time.Clock()

    def redraw_window():
        pygame.display.update()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # if event.type == pygame.KEYDOWN:


main()
