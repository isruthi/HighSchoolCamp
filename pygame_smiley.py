"""
title: pygame_smiley
author: isruthi
date: 2019-06-14 10:54
"""

import pygame

pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

pi = 3.141592653

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, [200, 200], 150)
    pygame.draw.ellipse(screen, BLACK, [125, 125, 30, 50])
    pygame.draw.ellipse(screen, BLACK, [225, 125, 30, 50])
    pygame.draw.arc(screen, BLACK, [130, 160, 125, 125], pi, 0, 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()